import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("../AgriData.csv")

needed_cols = ["State Name", "RICE YIELD (Kg per ha)", "WHEAT YIELD (Kg per ha)"]

if not all(col in data.columns for col in needed_cols):
    print("Column not found! Please check the dataset.")
else:
    # Group by state and find average yield for Rice and Wheat
    yield_by_state = data.groupby("State Name")[["RICE YIELD (Kg per ha)", "WHEAT YIELD (Kg per ha)"]].mean()

    # Sort states by Rice yield
    yield_by_state = yield_by_state.sort_values("RICE YIELD (Kg per ha)", ascending=False)

    top10_yield = yield_by_state.head(10)

    # Bar chart 
    x = np.arange(len(top10_yield))
    w = 0.35

    plt.figure(figsize=(9, 5))
    plt.bar(x - w/2, top10_yield["RICE YIELD (Kg per ha)"], width=w, label="Rice Yield", color="goldenrod")
    plt.bar(x + w/2, top10_yield["WHEAT YIELD (Kg per ha)"], width=w, label="Wheat Yield", color="lightgreen")

    # Chart labels
    plt.title("Rice vs Wheat Yield Across States", fontsize=13)
    plt.xlabel("State Name")
    plt.ylabel("Yield (Kg per ha)")
    plt.xticks(x, top10_yield.index, rotation=30)
    plt.legend()
    plt.tight_layout()
    plt.show()


