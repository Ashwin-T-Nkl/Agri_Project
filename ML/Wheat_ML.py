import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

df = pd.read_csv("C:\\Users\\Ashwin\\Downloads\\AgriProject\\AgriData.csv")

# Features and Target
X = df[['WHEAT AREA (1000 ha)', 'WHEAT YIELD (Kg per ha)', 'Year']]
y = df['WHEAT PRODUCTION (1000 tons)']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
r2 = r2_score(y_test, y_pred)

# Prediction
new_data = pd.DataFrame({
    'WHEAT AREA (1000 ha)': [500],
    'WHEAT YIELD (Kg per ha)': [3000],
    'Year': [2025]
})
predicted_production = model.predict(new_data)[0]

# Summary
print("📊 Simple ML Model — Wheat Production Prediction\n")
print("R² Score:", round(r2, 2))
print("Predicted Wheat Production (1000 tons):", round(predicted_production, 2))


