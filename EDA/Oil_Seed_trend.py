import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../AgriData.csv")

if "OILSEEDS PRODUCTION (1000 tons)" not in data.columns:
    print("Column not found! Please check the dataset.")
else:
    # Group by state name and sum the oilseed production
    OS_statewise = (
        data.groupby("State Name")["OILSEEDS PRODUCTION (1000 tons)"]
        .sum()
        .sort_values(ascending=False)
    )

    # Select top 8 oilseed states
    top8_OS = OS_statewise.head(8)


    print("\n🌻 Oilseed Production in Major States (Top 8):")
    print(top8_OS)

    # Pie Chart (percentage)
    plt.figure(figsize=(6, 6))
    top8_OS.plot(
        kind='pie',
        autopct='%1.1f%%',  
        startangle=90,     
        colors=['gold', 'lightgreen', 'skyblue', 'salmon',
                'violet', 'khaki', 'orchid', 'lightcoral']
    )
    plt.title("Oilseed Production Share by Major States in India", fontsize=13)
    plt.ylabel("") 
    plt.tight_layout()
    plt.show()
