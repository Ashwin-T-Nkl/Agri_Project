import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("../AgriData.csv")

if "GROUNDNUT PRODUCTION (1000 tons)" not in data.columns:
    print("Column not found! Please check the dataset.")
else:
    # Group by state and sum groundnut production
    GroundNut_statewise = (
        data.groupby("State Name")["GROUNDNUT PRODUCTION (1000 tons)"]
        .sum()
        .sort_values(ascending=False)
    )

   
    top7_GroundNut = GroundNut_statewise.head(7)

    # Display
    print("\n🥜 Top 7 Groundnut Producing States in India:")
    print(top7_GroundNut)

    # Bar chart
    plt.figure(figsize=(8, 5))
    top7_GroundNut.plot(kind='bar', color='Gold')
    plt.title("Top 7 Groundnut Producing States in India")
    plt.xlabel("State Name")
    plt.ylabel("Groundnut Production (1000 tons)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()
