from ner_app.ner_model import extract_entities

# Load sample text
with open("ner_app/sample_text.txt", "r") as f:
    text = f.read()

# Extract entities
entities = extract_entities(text)

# Print result
print("Named Entities found:\n")
for ent, label in entities:
    print(f"{ent} --> {label}")
