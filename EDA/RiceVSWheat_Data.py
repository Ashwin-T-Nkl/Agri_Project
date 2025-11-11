# 🌾 Rice Production vs Wheat Production (Last 50 Years)

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../AgriData.csv")

if ("RICE PRODUCTION (tons)" not in data.columns) or ("WHEAT PRODUCTION (tons)" not in data.columns):
    print(" Required columns not found! Please check the dataset.")
else:
    rice_yearwise = data.groupby("Year")["RICE PRODUCTION (tons)"].sum()
    wheat_yearwise = data.groupby("Year")["WHEAT PRODUCTION (tons)"].sum()

    print("\n🌾 Rice Production (First 5 Years):")
    print(rice_yearwise.head())
    print("\n🌾 Wheat Production (First 5 Years):")
    print(wheat_yearwise.head())

    # Line chart
    plt.figure(figsize=(10,5))

    # Rice line
    plt.plot(rice_yearwise.index, rice_yearwise.values, color='#6996b3', marker='o', linewidth=2, label='Rice')

    # Wheat line
    plt.plot(wheat_yearwise.index, wheat_yearwise.values, color='#488f31', marker='s', linewidth=2, label='Wheat')

 
    plt.title("Rice vs Wheat Production in India (Last 50 Years)")
    plt.xlabel("Year")
    plt.ylabel("Total Production (tons)")
    plt.legend()
    plt.grid(True)

    # X-axis every 5 years
    start_year = int(rice_yearwise.index.min())
    end_year = int(rice_yearwise.index.max())
    plt.xticks(range(start_year, end_year + 1, 5))
    plt.tight_layout()
    plt.show()
