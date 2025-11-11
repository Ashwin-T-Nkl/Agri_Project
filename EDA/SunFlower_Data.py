# 🌻 Top 7 Sunflower Producing States in India

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../AgriData.csv")

# Logic
if "SUNFLOWER PRODUCTION (tons)" not in data.columns:
    print("Column not found! Please check the dataset.")
else:
    sunflower_statewise = data.groupby("State Name")["SUNFLOWER PRODUCTION (tons)"].sum()
    sunflower_statewise = sunflower_statewise.sort_values(ascending=False)
    top7_sunflower = sunflower_statewise.head(7)

    # Output
    print("\nTop 7 Sunflower Producing States in India:")
    print(top7_sunflower)

    # Bar chart
    plt.bar(top7_sunflower.index, top7_sunflower.values, color='gold')
    plt.title("Top 7 Sunflower Producing States in India")
    plt.xlabel("State Name")
    plt.ylabel("Sunflower Production (tons)")
    plt.xticks(rotation=30)
    plt.show()
