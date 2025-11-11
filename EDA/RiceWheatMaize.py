import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("../AgriData.csv")
cols_needed = [
    "RICE AREA (1000 ha)", "RICE PRODUCTION (1000 tons)",
    "WHEAT AREA (1000 ha)", "WHEAT PRODUCTION (1000 tons)",
    "MAIZE AREA (1000 ha)", "MAIZE PRODUCTION (1000 tons)"
]

if not all(col in data.columns for col in cols_needed):
    print("Column not found! Please check the dataset.")
else:
    # Calculate average values for each crop
    rice_area = data["RICE AREA (1000 ha)"].mean()
    rice_prod = data["RICE PRODUCTION (1000 tons)"].mean()
    wheat_area = data["WHEAT AREA (1000 ha)"].mean()
    wheat_prod = data["WHEAT PRODUCTION (1000 tons)"].mean()
    maize_area = data["MAIZE AREA (1000 ha)"].mean()
    maize_prod = data["MAIZE PRODUCTION (1000 tons)"].mean()

    # Create data for plotting
    crops = ["Rice", "Wheat", "Maize"]
    avg_area = [rice_area, wheat_area, maize_area]
    avg_prod = [rice_prod, wheat_prod, maize_prod]

    # Bar chart
    x = np.arange(len(crops))
    w = 0.35

    plt.figure(figsize=(8,5))
    plt.bar(x - w/2, avg_area, width=w, label='Area (1000 ha)', color='lightgreen')
    plt.bar(x + w/2, avg_prod, width=w, label='Production (1000 tons)', color='goldenrod')

    # Labels and design
    plt.title("Impact of Area Cultivated on Production (Rice, Wheat, Maize)", fontsize=13)
    plt.xlabel("Crop Type")
    plt.ylabel("Average Values")
    plt.xticks(x, crops)
    plt.legend()
    plt.tight_layout()
    plt.show()
