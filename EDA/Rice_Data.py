import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("../AgriData.csv")

print("✅ File loaded successfully!")
print("Total rows in the file:", len(data))
print("Total columns in the file:", len(data.columns))


if "RICE PRODUCTION (tons)" not in data.columns:
    print("The column 'RICE PRODUCTION (tons)' was not found in the dataset.")
else:
    # Group by state name and sum the rice production
    rice_statewise = (
        data.groupby("State Name")["RICE PRODUCTION (tons)"]
        .sum()
        .sort_values(ascending=False)
    )

    #Select top 7 
    top7_rice = rice_statewise.head(7)

    print("\n🌾 Top 7 Rice Producing States in India:")
    print(top7_rice)

    # Step 5: Plot bar chart
    plt.figure(figsize=(8, 5))
    top7_rice.plot(kind='bar', color='skyblue')
    plt.title("Top 7 Rice Producing States in India", fontsize=14)
    plt.xlabel("States Of India")
    plt.ylabel("Total Rice Production (tons)")
    plt.xticks(rotation=25)
    plt.tight_layout()
    plt.show()
