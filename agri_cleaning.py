import pandas as pd
import numpy as np

# 💾 Read the CSV that sits in the SAME folder as this script
file_path = ".\\ICRISAT-District Data.csv"


print("📂 Reading the dataset, please wait...")
data = pd.read_csv(file_path)

print("\n✅ File loaded successfully!")
print("Total Rows:", len(data))
print("Total Columns:", len(data.columns))

# 👀 Peek at the data
print("\n--- First 5 Rows ---")
print(data.head())

print("\n--- Column Names ---")
for i, col in enumerate(data.columns, start=1):
    print(f"{i}. {col}")

# 🧼 Handle missing values (simple & safe)
num_cols = data.select_dtypes(include=[np.number]).columns
data[num_cols] = data[num_cols].fillna(0)

if "Year" in data.columns:
    data["Year"] = data["Year"].ffill()

print("\n🧹 Missing values handled!")

# 📏 Convert units: “(1000 ha)” → “(ha)”, “(1000 tons)” → “(tons)”
for col in data.columns:
    if "(1000 ha)" in col:
        new_col = col.replace("(1000 ha)", "(ha)").strip()
        data[new_col] = data[col] * 1000
    elif "(1000 tons)" in col:
        new_col = col.replace("(1000 tons)", "(tons)").strip()
        data[new_col] = data[col] * 1000

print("\n📐 Added new columns with corrected units!")

# 💾 Save cleaned copy in the SAME folder
out_path = ".\\AgriData.csv"
data.to_csv(out_path, index=False)
print(f"\n✅ Cleaned file saved successfully as: {out_path}")

print("\n--- Sample After Cleaning ---")
print(data.head())
