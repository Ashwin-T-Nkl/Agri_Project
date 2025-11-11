
# 🌾Top 5 Wheat Producing States
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../AgriData.csv")

if "WHEAT PRODUCTION (tons)" not in data.columns:
    print(" The column 'WHEAT PRODUCTION (tons)' was not found in the dataset.")
else:
    # Group by 'State Name' & Sum wheat production for each state
    wheat_statewise = (
        data.groupby("State Name")["WHEAT PRODUCTION (tons)"]
        .sum()                            
        .sort_values(ascending=False)
    )

    # Top 5 states
    top5_wheat = wheat_statewise.head(5)

    print("\n🌾 Top 5 Wheat Producing States in India:")
    print(top5_wheat)

    # Bar Chart
    plt.figure(figsize=(8, 5))              
    top5_wheat.plot(kind='bar', color='#de425b')
    plt.title("Top 5 Wheat Producing States in India", fontsize=14)
    plt.xlabel("State Name")
    plt.ylabel("Total Wheat Production (tons)")
    plt.tight_layout()
    plt.show()

    # Pie Chart (percentage share)
    plt.figure(figsize=(6, 6))
    top5_wheat.plot(

        kind='pie',
        autopct='%1.1f%%',
        startangle=90,                        
        colors=['gold', 'lightgreen', 'skyblue', 'salmon', 'violet']

    )

    plt.title("Wheat Production Share of Top 5 States", fontsize=14)
    plt.ylabel("")     
    plt.tight_layout()
    plt.show()

