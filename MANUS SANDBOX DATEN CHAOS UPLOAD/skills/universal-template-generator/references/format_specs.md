# Format Specifications

Detaillierte Spezifikationen für Template-Formate.

---

## YAML Format

### Grundstruktur

```yaml
key: "value"
nested:
  key: "value"
list:
  - "item1"
  - "item2"
```

### Validierung

**Tools:**
- `yamllint` - YAML Linter
- `pyyaml` - Python YAML Parser

**Common Errors:**
- Inkonsistente Einrückung (2 Spaces verwenden)
- Fehlende Quotes bei Special Characters
- Trailing Whitespace

---

## Markdown Format

### Strukturierter Text

```markdown
# Heading 1
## Heading 2

**Bold Text**
*Italic Text*

- List Item 1
- List Item 2

1. Numbered Item 1
2. Numbered Item 2
```

### Code Blocks

```markdown
\`\`\`yaml
key: value
\`\`\`

\`\`\`python
def function():
    pass
\`\`\`
```

---

## JSON Format

### Grundstruktur

```json
{
  "key": "value",
  "nested": {
    "key": "value"
  },
  "list": ["item1", "item2"]
}
```

### Validierung

**Tools:**
- `jq` - JSON Processor
- `json.loads()` - Python JSON Parser

---

## Platzhalter-Konvention

### Format

```
[PLACEHOLDER_NAME]
```

### Regeln

1. Nur Großbuchstaben
2. Unterstriche für Trennung
3. Beschreibend (nicht zu kurz, nicht zu lang)

### Beispiele

**Gut:**
- `[AGENT_NAME]`
- `[PIPELINE_TYPE]`
- `[SYSTEM_ZWECK]`

**Schlecht:**
- `[name]` (nicht Großbuchstaben)
- `[N]` (zu kurz)
- `[THE_VERY_LONG_NAME_OF_THE_AGENT]` (zu lang)

---

## Validierungsregeln

### YAML Templates

1. Valid YAML Syntax
2. Required Fields vorhanden
3. Platzhalter im richtigen Format
4. Konsistente Einrückung

### Markdown Templates

1. Valid Markdown Syntax
2. Überschriften-Hierarchie korrekt
3. Code Blocks geschlossen
4. Platzhalter markiert

### JSON Templates

1. Valid JSON Syntax
2. Alle Strings quoted
3. Trailing Commas entfernt
4. Platzhalter in Strings

---

## Best Practices

### YAML

- 2 Spaces für Einrückung
- Quotes für Strings mit Special Characters
- Kommentare mit `#`
- Multiline Strings mit `|` oder `>`

### Markdown

- Eine Leerzeile zwischen Sections
- Code Blocks mit Sprache annotieren
- Listen konsistent (entweder `-` oder `*`)

### JSON

- 2 Spaces für Einrückung
- Keine Trailing Commas
- Alle Keys quoted
- Strings escaped
