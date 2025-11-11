# 🌾 Sorghum Production (Kharif & Rabi) by Top States
#kharif - Monsoon
#Rabi - Winter

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("../AgriData.csv")

# Group by state and take sum
sorghum = data.groupby("State Name")[["KHARIF SORGHUM PRODUCTION (1000 tons)",
                                      "RABI SORGHUM PRODUCTION (1000 tons)"]].sum()

# Pick top 8 states (for clear view)
sorghum["TOTAL"] = sorghum.sum(axis=1)
top8 = sorghum.sort_values("TOTAL", ascending=False).head(8)

# Create positions for bars
x = np.arange(len(top8))
w = 0.4

# Plot both bars
plt.bar(x - w/2, top8["KHARIF SORGHUM PRODUCTION (1000 tons)"], width=w, color="#d3a24c", label="Kharif")
plt.bar(x + w/2, top8["RABI SORGHUM PRODUCTION (1000 tons)"], width=w, color="#8b5e3c", label="Rabi")

# Add chart labels
plt.title("Sorghum Production (Kharif & Rabi) by Top States")
plt.xlabel("State Name")
plt.ylabel("Production (1000 tons)")
plt.xticks(x, top8.index, rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
