# 🌾 India's Millet Production (Last 50 Years)

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../AgriData.csv")


if ("Year" not in data.columns) or ("FINGER MILLET PRODUCTION (1000 tons)" not in data.columns):
    print("Column missing! Please check the dataset.")
else:
    millet_yearwise = data.groupby("Year")["FINGER MILLET PRODUCTION (1000 tons)"].sum()
    print("\n🌾 India's Millet Production (First 10 Years):")
    print(millet_yearwise.head(10))

    # line chart
    plt.figure(figsize=(10,5))
    plt.plot(millet_yearwise.index, millet_yearwise.values, color="#0d7e80", marker='o', linewidth=2)

    plt.title("India's Millet Production (Last 50 Years)")
    plt.xlabel("Year")
    plt.ylabel("Total Millet Production (1000 tons)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
