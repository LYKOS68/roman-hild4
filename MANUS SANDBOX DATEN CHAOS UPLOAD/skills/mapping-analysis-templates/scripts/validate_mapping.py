#!/usr/bin/env python3
"""
Mapping Validator

Validiert Mapping-Definitionen gegen definierte Schemas und prüft auf häufige Fehler.
"""

import json
import sys
from typing import Dict, List, Tuple, Any


class MappingValidator:
    """Validator für verschiedene Mapping-Typen"""

    def __init__(self):
        self.errors = []
        self.warnings = []
        self.info = []

    def validate_data_mapping(self, mapping: Dict[str, Any]) -> bool:
        """Validiert ein Daten-Mapping"""
        is_valid = True

        # Prüfe Pflichtfelder
        if "mapping_overview" not in mapping:
            self.errors.append("Fehlendes Pflichtfeld: mapping_overview")
            is_valid = False

        if "field_mappings" not in mapping:
            self.errors.append("Fehlendes Pflichtfeld: field_mappings")
            is_valid = False
        elif not mapping["field_mappings"]:
            self.warnings.append("Keine Feld-Mappings definiert")

        # Prüfe Feld-Mappings
        if "field_mappings" in mapping:
            source_fields = set()
            target_fields = set()

            for idx, field_mapping in enumerate(mapping["field_mappings"]):
                # Prüfe auf Duplikate
                source = field_mapping.get("source_field")
                target = field_mapping.get("target_field")

                if source in source_fields:
                    self.warnings.append(
                        f"Duplikat: Quellfeld '{source}' wird mehrfach gemappt (Index {idx})"
                    )
                source_fields.add(source)

                if target in target_fields:
                    self.warnings.append(
                        f"Duplikat: Zielfeld '{target}' wird mehrfach beschrieben (Index {idx})"
                    )
                target_fields.add(target)

                # Prüfe Typ-Kompatibilität
                source_type = field_mapping.get("source_type", "").upper()
                target_type = field_mapping.get("target_type", "").upper()

                if source_type and target_type:
                    if not self._are_types_compatible(source_type, target_type):
                        if not field_mapping.get("transformation"):
                            self.warnings.append(
                                f"Inkompatible Typen bei '{source}' -> '{target}': "
                                f"{source_type} -> {target_type} ohne Transformation"
                            )

        # Prüfe Transformationsregeln
        if "transformation_rules" in mapping:
            for idx, rule in enumerate(mapping["transformation_rules"]):
                if not rule.get("rule_name"):
                    self.warnings.append(f"Transformationsregel {idx} hat keinen Namen")
                if not rule.get("condition") and not rule.get("action"):
                    self.warnings.append(
                        f"Transformationsregel '{rule.get('rule_name', idx)}' "
                        "hat weder Bedingung noch Aktion"
                    )

        return is_valid

    def validate_process_mapping(self, mapping: Dict[str, Any]) -> bool:
        """Validiert ein Prozess-Mapping"""
        is_valid = True

        # Prüfe Pflichtfelder
        if "process_overview" not in mapping:
            self.errors.append("Fehlendes Pflichtfeld: process_overview")
            is_valid = False

        if "process_steps" not in mapping:
            self.errors.append("Fehlendes Pflichtfeld: process_steps")
            is_valid = False
        elif not mapping["process_steps"]:
            self.errors.append("Keine Prozessschritte definiert")
            is_valid = False

        # Prüfe Prozessschritte
        if "process_steps" in mapping and mapping["process_steps"]:
            step_numbers = []
            for step in mapping["process_steps"]:
                step_num = step.get("step_number")
                if step_num is not None:
                    step_numbers.append(step_num)

                if not step.get("activity"):
                    self.warnings.append(
                        f"Schritt {step_num}: Keine Aktivität definiert"
                    )
                if not step.get("responsible"):
                    self.warnings.append(
                        f"Schritt {step_num}: Kein Verantwortlicher definiert"
                    )

            # Prüfe auf Lücken in der Nummerierung
            if step_numbers:
                step_numbers.sort()
                expected = list(range(1, len(step_numbers) + 1))
                if step_numbers != expected:
                    self.warnings.append(
                        f"Lücken oder Duplikate in der Schritt-Nummerierung: {step_numbers}"
                    )

        # Prüfe Entscheidungspunkte
        if "decision_points" in mapping:
            for decision in mapping["decision_points"]:
                if not decision.get("decision_name"):
                    self.warnings.append("Entscheidungspunkt ohne Namen gefunden")
                if not decision.get("options") or len(decision.get("options", [])) < 2:
                    self.warnings.append(
                        f"Entscheidungspunkt '{decision.get('decision_name')}' "
                        "hat weniger als 2 Optionen"
                    )

        # Prüfe KPIs
        if "kpis" in mapping and mapping["kpis"]:
            for kpi in mapping["kpis"]:
                if not kpi.get("kpi_name"):
                    self.warnings.append("KPI ohne Namen gefunden")
                if not kpi.get("target_value"):
                    self.warnings.append(
                        f"KPI '{kpi.get('kpi_name')}' hat keinen Zielwert"
                    )

        return is_valid

    def validate_system_mapping(self, mapping: Dict[str, Any]) -> bool:
        """Validiert ein System-Mapping"""
        is_valid = True

        # Prüfe Pflichtfelder
        if "system_overview" not in mapping:
            self.errors.append("Fehlendes Pflichtfeld: system_overview")
            is_valid = False

        if "components" not in mapping:
            self.errors.append("Fehlendes Pflichtfeld: components")
            is_valid = False
        elif not mapping["components"]:
            self.warnings.append("Keine Komponenten definiert")

        # Prüfe Komponenten
        if "components" in mapping:
            component_names = set()
            for component in mapping["components"]:
                name = component.get("component_name")
                if name in component_names:
                    self.warnings.append(f"Duplikat: Komponente '{name}' mehrfach definiert")
                component_names.add(name)

                if component.get("status") == "Deprecated":
                    self.info.append(
                        f"Komponente '{name}' ist als 'Deprecated' markiert"
                    )

        # Prüfe Schnittstellen
        if "interfaces" in mapping:
            inbound = mapping["interfaces"].get("inbound", [])
            outbound = mapping["interfaces"].get("outbound", [])

            if not inbound and not outbound:
                self.warnings.append("Keine Schnittstellen (inbound/outbound) definiert")

            # Prüfe auf fehlende Authentifizierung
            for interface in inbound + outbound:
                if not interface.get("authentication"):
                    system = interface.get("source_system") or interface.get("target_system")
                    self.warnings.append(
                        f"Schnittstelle zu '{system}': Keine Authentifizierung definiert"
                    )

        # Prüfe Abhängigkeiten
        if "dependencies" in mapping:
            upstream = mapping["dependencies"].get("upstream", [])
            downstream = mapping["dependencies"].get("downstream", [])

            critical_upstream = [
                d for d in upstream if d.get("criticality") == "Hoch"
            ]
            if critical_upstream:
                for dep in critical_upstream:
                    if not dep.get("failover_strategy"):
                        self.warnings.append(
                            f"Kritische Upstream-Abhängigkeit '{dep.get('system')}' "
                            "hat keine Failover-Strategie"
                        )

        return is_valid

    def _are_types_compatible(self, source_type: str, target_type: str) -> bool:
        """Prüft, ob zwei Datentypen kompatibel sind"""
        # Vereinfachte Typ-Kompatibilitätsprüfung
        numeric_types = {"INT", "INTEGER", "BIGINT", "SMALLINT", "DECIMAL", "NUMERIC", "FLOAT", "DOUBLE"}
        string_types = {"VARCHAR", "CHAR", "TEXT", "STRING"}
        date_types = {"DATE", "DATETIME", "TIMESTAMP"}

        # Exakte Übereinstimmung
        if source_type == target_type:
            return True

        # Numerische Typen untereinander
        if source_type in numeric_types and target_type in numeric_types:
            return True

        # String-Typen untereinander
        if source_type in string_types and target_type in string_types:
            return True

        # Datum-Typen untereinander
        if source_type in date_types and target_type in date_types:
            return True

        return False

    def print_report(self):
        """Gibt einen Validierungsbericht aus"""
        print("\n" + "=" * 60)
        print("VALIDIERUNGSBERICHT")
        print("=" * 60)

        if self.errors:
            print(f"\n❌ FEHLER ({len(self.errors)}):")
            for error in self.errors:
                print(f"  • {error}")

        if self.warnings:
            print(f"\n⚠️  WARNUNGEN ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  • {warning}")

        if self.info:
            print(f"\nℹ️  INFORMATIONEN ({len(self.info)}):")
            for info_msg in self.info:
                print(f"  • {info_msg}")

        if not self.errors and not self.warnings:
            print("\n✅ Keine Probleme gefunden!")

        print("\n" + "=" * 60)
        print(f"Zusammenfassung: {len(self.errors)} Fehler, {len(self.warnings)} Warnungen")
        print("=" * 60 + "\n")

        return len(self.errors) == 0


def main():
    """Hauptfunktion"""
    if len(sys.argv) < 3:
        print("Usage: python validate_mapping.py <mapping_type> <mapping_file>")
        print("\nMapping types:")
        print("  - data")
        print("  - process")
        print("  - system")
        sys.exit(1)

    mapping_type = sys.argv[1]
    mapping_file = sys.argv[2]

    try:
        with open(mapping_file, 'r', encoding='utf-8') as f:
            mapping = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{mapping_file}' not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{mapping_file}': {e}")
        sys.exit(1)

    validator = MappingValidator()

    if mapping_type == "data":
        is_valid = validator.validate_data_mapping(mapping)
    elif mapping_type == "process":
        is_valid = validator.validate_process_mapping(mapping)
    elif mapping_type == "system":
        is_valid = validator.validate_system_mapping(mapping)
    else:
        print(f"Error: Unknown mapping type '{mapping_type}'")
        print("Available types: data, process, system")
        sys.exit(1)

    success = validator.print_report()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
