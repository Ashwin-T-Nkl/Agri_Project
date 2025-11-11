import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../AgriData.csv")

if "SOYABEAN PRODUCTION (1000 tons)" not in data.columns or "SOYABEAN AREA (1000 ha)" not in data.columns:
    print("Column not found! Please check the dataset.")
else:
    # Group by State and get total Production + Area
    SB_byState = data.groupby("State Name")[["SOYABEAN PRODUCTION (1000 tons)", "SOYABEAN AREA (1000 ha)"]].sum()

    # Calculate Yield = Production ÷ Area
    SB_byState["SB_YIELD (tons per ha)"] = SB_byState["SOYABEAN PRODUCTION (1000 tons)"] / SB_byState["SOYABEAN AREA (1000 ha)"]

    # Sort states by total Soybean production (highest first)
    SB_sorted = SB_byState.sort_values("SOYABEAN PRODUCTION (1000 tons)", ascending=False)

    # Top 5 Soybean 
    SB_Top5 = SB_sorted.head(5)

    print("\n🌱 Top 5 Soybean (SB) Producing States in India with Yield Efficiency:")
    print(SB_Top5)

    plt.figure(figsize=(8, 5))
    SB_Top5["SOYABEAN PRODUCTION (1000 tons)"].plot(kind='bar', color='#4e52a4')
    plt.title("Top 5 Soybean (SB) Producing States in India")
    plt.xlabel("State Name")
    plt.ylabel("Soybean Production (1000 tons)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    SB_Top5["SB_YIELD (tons per ha)"].plot(kind='bar', color='#ff8d43')
    plt.title("Soybean (SB) Yield Efficiency by Top 5 States")
    plt.xlabel("State Name")
    plt.ylabel("Yield (tons per ha)")
    plt.xticks(rotation=43)
    plt.tight_layout()
    plt.show()
