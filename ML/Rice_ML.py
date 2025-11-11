import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error


df = pd.read_csv("C:\\Users\\Ashwin\\Downloads\\AgriProject\\AgriData.csv")

# Features / target
X = df[['RICE AREA (1000 ha)', 'RICE YIELD (Kg per ha)', 'Year']]
y = df['RICE PRODUCTION (1000 tons)']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LinearRegression().fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)

# prediction
new_data = pd.DataFrame({
    'RICE AREA (1000 ha)': [600],
    'RICE YIELD (Kg per ha)': [3200],
    'Year': [2025]
})
pred = model.predict(new_data)[0]

# Output
print("📊 Simple ML — Rice Production")
print("R²:", round(r2, 3))
print("Predicted Rice Production (1000 tons):", round(pred, 2))


