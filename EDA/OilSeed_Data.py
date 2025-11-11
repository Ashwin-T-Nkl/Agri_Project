# 🌻 Top 5 Oilseed Producing States in India

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../AgriData.csv")

# Logic
if "OILSEEDS PRODUCTION (tons)" not in data.columns:
    print("Column not found! Please check the dataset.")
else:
    oilseed_statewise = data.groupby("State Name")["OILSEEDS PRODUCTION (tons)"].sum()
    oilseed_statewise = oilseed_statewise.sort_values(ascending=False)
    top5_oilseed = oilseed_statewise.head(5)

    # Output
    print("\nTop 5 Oilseed Producing States in India:")
    print(top5_oilseed)

    # Bar chart
    plt.bar(top5_oilseed.index, top5_oilseed.values, color='#C5A5CF')
    plt.title("Top 5 Oilseed Producing States in India")
    plt.xlabel("State Name")
    plt.ylabel("Oilseed Production (tons)")
    plt.xticks(rotation=30)
    plt.show()
