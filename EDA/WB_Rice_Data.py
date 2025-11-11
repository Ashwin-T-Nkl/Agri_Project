# 🍚 Rice Production by Districts in West Bengal

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../AgriData.csv")

#Logic
if ("State Name" not in data.columns) or ("Dist Name" not in data.columns) or ("RICE PRODUCTION (tons)" not in data.columns):
    print("Column missing! Please check the dataset.")
else:
    # Filter only West Bengal rows
    wb_data = data[data["State Name"] == "West Bengal"]

    # Group by district and add up rice production
    wb_rice = wb_data.groupby("Dist Name")["RICE PRODUCTION (tons)"].sum()

    # Sort from highest to lowest
    wb_rice = wb_rice.sort_values(ascending=False)

    # Take top 10 districts
    top10_wb = wb_rice.head(10)

    # Output
    print("\n🍚 Top 10 Rice Producing Districts in West Bengal:")
    print(top10_wb)

    # Bar chart
    plt.bar(top10_wb.index, top10_wb.values, color="#6f2495")
    plt.title("Top 10 Rice Producing Districts in West Bengal")
    plt.xlabel("District Name")
    plt.ylabel("Rice Production (tons)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()
