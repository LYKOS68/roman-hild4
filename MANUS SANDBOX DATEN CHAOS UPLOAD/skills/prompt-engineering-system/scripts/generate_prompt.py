import json
import argparse

# This is a placeholder script to demonstrate the skill's structure.
# In a real implementation, this script would be much more complex, 
# interacting with the PROMPT_PACKs and the Kalibrierungs-Generator.

def generate_prompt(method_id, input_data):
    # In a real scenario, this would load the corresponding PROMPT_PACK,
    # find the method, and use the template to generate a prompt.
    print(f"--- Generating Prompt for Method: {method_id} ---")
    print(f"Input Data: {input_data}")
    
    # Placeholder for the generated prompt
    generated_prompt = f"""### ROLLE
Du bist ein spezialisiertes KI-Modell.

### ZIEL
Führe die Methode '{method_id}' mit den folgenden Daten aus: {input_data}

### ANWEISUNGEN
1. Analysiere die Daten.
2. Führe die Methode aus.
3. Validiere das Ergebnis, bevor du es zurückgibst.

### VALIDIERUNG
- Ist das Ergebnis im korrekten Format?
- Entspricht das Ergebnis den Qualitätsstandards?

### AUSGABEFORMAT
JSON mit dem Feld 'result'.
"""
    
    print("\n--- Generated Prompt ---")
    print(generated_prompt)
    print("------------------------")
    
    return generated_prompt

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a calibrated prompt.')
    parser.add_argument('method_id', type=str, help='The ID of the method to use.')
    parser.add_argument('input_data', type=str, help='The input data for the prompt as a JSON string.')
    
    args = parser.parse_args()
    
    try:
        input_data_json = json.loads(args.input_data)
    except json.JSONDecodeError:
        print("Error: Invalid JSON string for input_data.")
        exit(1)
        
    generate_prompt(args.method_id, input_data_json)
