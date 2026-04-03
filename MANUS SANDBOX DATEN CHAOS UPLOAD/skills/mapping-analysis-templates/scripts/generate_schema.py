#!/usr/bin/env python3
"""
Schema Generator für strukturierte Datenerfassung

Dieses Skript generiert JSON-Schemas für verschiedene Mapping- und Analyse-Szenarien.
"""

import json
import sys
from typing import Dict, List, Any


def generate_data_mapping_schema() -> Dict[str, Any]:
    """Generiert ein JSON-Schema für Daten-Mapping"""
    return {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Data Mapping Schema",
        "type": "object",
        "required": ["mapping_overview", "field_mappings"],
        "properties": {
            "mapping_overview": {
                "type": "object",
                "required": ["source", "target", "mapping_type", "date"],
                "properties": {
                    "source": {"type": "string", "description": "Quellsystem/Datenbank/API"},
                    "target": {"type": "string", "description": "Zielsystem/Datenbank/API"},
                    "mapping_type": {
                        "type": "string",
                        "enum": ["1:1", "1:N", "N:M", "Transformation"],
                        "description": "Art des Mappings"
                    },
                    "date": {"type": "string", "format": "date"}
                }
            },
            "field_mappings": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["source_field", "source_type", "target_field", "target_type"],
                    "properties": {
                        "source_field": {"type": "string"},
                        "source_type": {"type": "string"},
                        "target_field": {"type": "string"},
                        "target_type": {"type": "string"},
                        "transformation": {"type": "string"},
                        "validation": {"type": "string"},
                        "notes": {"type": "string"}
                    }
                }
            },
            "transformation_rules": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "rule_name": {"type": "string"},
                        "condition": {"type": "string"},
                        "action": {"type": "string"},
                        "alternative": {"type": "string"}
                    }
                }
            },
            "data_quality": {
                "type": "object",
                "properties": {
                    "required_fields": {"type": "array", "items": {"type": "string"}},
                    "value_ranges": {"type": "object"},
                    "format_patterns": {"type": "object"},
                    "referential_integrity": {"type": "array", "items": {"type": "string"}}
                }
            }
        }
    }


def generate_process_mapping_schema() -> Dict[str, Any]:
    """Generiert ein JSON-Schema für Prozess-Mapping"""
    return {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Process Mapping Schema",
        "type": "object",
        "required": ["process_overview", "process_steps"],
        "properties": {
            "process_overview": {
                "type": "object",
                "required": ["process_name", "owner", "process_type", "date"],
                "properties": {
                    "process_name": {"type": "string"},
                    "owner": {"type": "string"},
                    "process_type": {
                        "type": "string",
                        "enum": ["Kernprozess", "Unterstützungsprozess", "Managementprozess"]
                    },
                    "scope": {"type": "string"},
                    "date": {"type": "string", "format": "date"}
                }
            },
            "process_steps": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["step_number", "activity", "responsible"],
                    "properties": {
                        "step_number": {"type": "integer"},
                        "activity": {"type": "string"},
                        "responsible": {"type": "string"},
                        "input": {"type": "string"},
                        "output": {"type": "string"},
                        "system": {"type": "string"},
                        "duration": {"type": "string"},
                        "notes": {"type": "string"}
                    }
                }
            },
            "decision_points": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "decision_name": {"type": "string"},
                        "criterion": {"type": "string"},
                        "options": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "option": {"type": "string"},
                                    "condition": {"type": "string"},
                                    "next_step": {"type": "string"}
                                }
                            }
                        },
                        "escalation": {"type": "string"}
                    }
                }
            },
            "kpis": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "kpi_name": {"type": "string"},
                        "target_value": {"type": "string"},
                        "measurement_frequency": {"type": "string"},
                        "responsible": {"type": "string"},
                        "data_source": {"type": "string"}
                    }
                }
            }
        }
    }


def generate_system_mapping_schema() -> Dict[str, Any]:
    """Generiert ein JSON-Schema für System-Mapping"""
    return {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "System Mapping Schema",
        "type": "object",
        "required": ["system_overview", "components"],
        "properties": {
            "system_overview": {
                "type": "object",
                "required": ["system_name", "system_type", "owner", "criticality"],
                "properties": {
                    "system_name": {"type": "string"},
                    "system_type": {
                        "type": "string",
                        "enum": ["Application", "Database", "API", "Infrastructure", "Integration"]
                    },
                    "owner": {"type": "string"},
                    "criticality": {
                        "type": "string",
                        "enum": ["Kritisch", "Hoch", "Mittel", "Niedrig"]
                    },
                    "date": {"type": "string", "format": "date"}
                }
            },
            "components": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["component_name", "technology", "version"],
                    "properties": {
                        "component_name": {"type": "string"},
                        "technology": {"type": "string"},
                        "version": {"type": "string"},
                        "hosting": {"type": "string"},
                        "responsible": {"type": "string"},
                        "status": {
                            "type": "string",
                            "enum": ["Aktiv", "Deprecated", "Planned", "Retired"]
                        }
                    }
                }
            },
            "interfaces": {
                "type": "object",
                "properties": {
                    "inbound": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "source_system": {"type": "string"},
                                "protocol": {"type": "string"},
                                "data_format": {"type": "string"},
                                "frequency": {"type": "string"},
                                "authentication": {"type": "string"},
                                "endpoint": {"type": "string"}
                            }
                        }
                    },
                    "outbound": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "target_system": {"type": "string"},
                                "protocol": {"type": "string"},
                                "data_format": {"type": "string"},
                                "frequency": {"type": "string"},
                                "authentication": {"type": "string"},
                                "endpoint": {"type": "string"}
                            }
                        }
                    }
                }
            },
            "dependencies": {
                "type": "object",
                "properties": {
                    "upstream": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "system": {"type": "string"},
                                "dependency_type": {
                                    "type": "string",
                                    "enum": ["Synchron", "Asynchron"]
                                },
                                "criticality": {
                                    "type": "string",
                                    "enum": ["Hoch", "Mittel", "Niedrig"]
                                },
                                "failover_strategy": {"type": "string"}
                            }
                        }
                    },
                    "downstream": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "system": {"type": "string"},
                                "dependency_type": {
                                    "type": "string",
                                    "enum": ["Synchron", "Asynchron"]
                                },
                                "criticality": {
                                    "type": "string",
                                    "enum": ["Hoch", "Mittel", "Niedrig"]
                                },
                                "impact_on_failure": {"type": "string"}
                            }
                        }
                    }
                }
            }
        }
    }


def generate_analysis_output_schema() -> Dict[str, Any]:
    """Generiert ein JSON-Schema für strukturierte Analyse-Outputs"""
    return {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Analysis Output Schema",
        "type": "object",
        "required": ["analysis_type", "summary", "findings"],
        "properties": {
            "analysis_type": {
                "type": "string",
                "enum": [
                    "Explorative Datenanalyse",
                    "Zeitreihenanalyse",
                    "Segmentierungsanalyse",
                    "Prozesseffizienz-Analyse",
                    "Root-Cause-Analyse",
                    "Compliance-Analyse",
                    "Architektur-Review",
                    "Dependency-Analyse",
                    "Integration-Analyse",
                    "Stakeholder-Analyse",
                    "Gap-Analyse",
                    "Kosten-Nutzen-Analyse"
                ]
            },
            "metadata": {
                "type": "object",
                "properties": {
                    "analyst": {"type": "string"},
                    "date": {"type": "string", "format": "date"},
                    "version": {"type": "string"},
                    "data_sources": {"type": "array", "items": {"type": "string"}}
                }
            },
            "summary": {
                "type": "object",
                "required": ["executive_summary", "key_insights"],
                "properties": {
                    "executive_summary": {"type": "string"},
                    "key_insights": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "recommendations": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                }
            },
            "findings": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["finding_id", "category", "description", "severity"],
                    "properties": {
                        "finding_id": {"type": "string"},
                        "category": {"type": "string"},
                        "description": {"type": "string"},
                        "severity": {
                            "type": "string",
                            "enum": ["Kritisch", "Hoch", "Mittel", "Niedrig", "Info"]
                        },
                        "evidence": {"type": "string"},
                        "impact": {"type": "string"},
                        "recommendation": {"type": "string"},
                        "priority": {
                            "type": "string",
                            "enum": ["Hoch", "Mittel", "Niedrig"]
                        }
                    }
                }
            },
            "metrics": {
                "type": "object",
                "description": "Quantitative Metriken aus der Analyse"
            },
            "visualizations": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "type": {"type": "string"},
                        "file_path": {"type": "string"},
                        "description": {"type": "string"}
                    }
                }
            },
            "next_steps": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string"},
                        "responsible": {"type": "string"},
                        "deadline": {"type": "string", "format": "date"},
                        "dependencies": {"type": "array", "items": {"type": "string"}}
                    }
                }
            }
        }
    }


def main():
    """Hauptfunktion"""
    if len(sys.argv) < 2:
        print("Usage: python generate_schema.py <schema_type> [output_file]")
        print("\nAvailable schema types:")
        print("  - data_mapping")
        print("  - process_mapping")
        print("  - system_mapping")
        print("  - analysis_output")
        sys.exit(1)

    schema_type = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    schema_generators = {
        "data_mapping": generate_data_mapping_schema,
        "process_mapping": generate_process_mapping_schema,
        "system_mapping": generate_system_mapping_schema,
        "analysis_output": generate_analysis_output_schema
    }

    if schema_type not in schema_generators:
        print(f"Error: Unknown schema type '{schema_type}'")
        print(f"Available types: {', '.join(schema_generators.keys())}")
        sys.exit(1)

    schema = schema_generators[schema_type]()

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
        print(f"Schema written to {output_file}")
    else:
        print(json.dumps(schema, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
