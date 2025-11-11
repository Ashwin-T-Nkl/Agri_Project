# 🌾 Top 10 Wheat Production Years from Uttar Pradesh

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../AgriData.csv")

# Logic
if ("State Name" not in data.columns) or ("Year" not in data.columns) or ("WHEAT PRODUCTION (tons)" not in data.columns):
    print("Column missing! Please check the dataset.")
else:
    #  Uttar Pradesh 
    up_data = data[data["State Name"] == "Uttar Pradesh"]

    # Group by year and sum total wheat production
    up_wheat = up_data.groupby("Year")["WHEAT PRODUCTION (tons)"].sum()

    # Sort from highest to lowest
    up_wheat = up_wheat.sort_values(ascending=False)

    # Top 10 years
    top10_years = up_wheat.head(10)

    print("\n🌾 Top 10 Wheat Production Years from Uttar Pradesh:")
    print(top10_years)

    # Bar chart
    plt.bar(top10_years.index, top10_years.values, color="#8e6528")
    plt.title("Top 10 Wheat Production Years - Uttar Pradesh")
    plt.xlabel("Year")
    plt.ylabel("Wheat Production (tons)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()
