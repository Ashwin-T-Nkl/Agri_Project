# 🍬India's Sugarcane Production from Last 50 Years (Line Plot)

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../AgriData.csv")

if "SUGARCANE PRODUCTION (tons)" not in data.columns:
    print("Column not found! Please check the dataset.")
else:
    # Group data by year and sum up total sugarcane production across India
    sugarcane_yearwise = data.groupby("Year")["SUGARCANE PRODUCTION (tons)"].sum()

    print("\n🍬 India's Sugarcane Production (First 10 Years):")
    print(sugarcane_yearwise.head(10))

    # Line chart
    plt.figure(figsize=(10,5))
    plt.plot(sugarcane_yearwise.index, sugarcane_yearwise.values, color='brown', marker='o', linewidth=2)

    start_year = int(sugarcane_yearwise.index.min())
    end_year = int(sugarcane_yearwise.index.max())
    plt.xticks(range(start_year, end_year + 1, 5))
    
    plt.title("India's Sugarcane Production (Last 50 Years)")
    plt.xlabel("Year")
    plt.ylabel("Total Sugarcane Production (tons)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
