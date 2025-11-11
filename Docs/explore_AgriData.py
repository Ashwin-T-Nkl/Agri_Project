import pandas as pd

# Step 1: Read the cleaned data file
data = pd.read_csv("../AgriData.csv")

print("File loaded successfully!")
print("Total rows in the file:", len(data))
print("Total columns in the file:", len(data.columns))

# Step 2: Show first few rows
print("\nFirst 5 rows of the data:")
print(data.head())

# Step 3: Show column names (simple)
print("\nThese are the column names present in the file:")
print(data.columns)

# Step 4: Basic info about numbers
print("\nSome basic details about the data (average, min, max etc.):")
print(data.describe())

# Step 5: Total production of some important crops
print("\nTotal Production of Major Crops (in tons):")

if "RICE PRODUCTION (tons)" in data.columns:
    print("Total Rice Production:", data["RICE PRODUCTION (tons)"].sum())

if "WHEAT PRODUCTION (tons)" in data.columns:
    print("Total Wheat Production:", data["WHEAT PRODUCTION (tons)"].sum())

if "SUGARCANE PRODUCTION (tons)" in data.columns:
    print("Total Sugarcane Production:", data["SUGARCANE PRODUCTION (tons)"].sum())

if "MAIZE PRODUCTION (tons)" in data.columns:
    print("Total Maize Production:", data["MAIZE PRODUCTION (tons)"].sum())
