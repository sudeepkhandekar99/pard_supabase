import json
import pandas as pd

# === File paths ===
input_json_path = "project_updated_with_uuid_refs.json"
output_csv_path = "project_supabase_ready.csv"

# === Step 1: Load the updated project JSON ===
with open(input_json_path, "r", encoding="utf-8") as f:
    project_data = json.load(f)

# === Step 2: Flatten 'fields' dicts into a list of rows ===
records = [entry["fields"] for entry in project_data]

# === Step 3: Convert to DataFrame ===
df = pd.DataFrame(records)

# === Step 4: Drop 'id' column (let Supabase auto-generate) ===
df.drop(columns=["id"], errors="ignore", inplace=True)

# === Step 5: Save as CSV ===
df.to_csv(output_csv_path, index=False)

print(f"✅ Supabase-compatible CSV saved to: {output_csv_path}")
