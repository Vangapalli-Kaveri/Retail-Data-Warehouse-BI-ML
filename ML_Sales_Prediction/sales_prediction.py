import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# 1. Load the sample data
df = pd.read_csv("sales_prediction_sample.csv")
print("CSV file path:", __import__("os").path.abspath("sales_prediction_sample.csv"))
print("CSV rows read:", len(df))
print("Rows immediately after reading CSV:", len(df))
print("Duplicate rows:", df.duplicated().sum())
print("Rows loaded:", len(df))

features = [
    "store_id",
    "product_id",
    "week_no",
    "retail_discount",
    "coupon_discount",
    "coupon_match_discount",
    "has_display",
    "has_mailer"
]
target = "total_quantity"

print("\nMissing values by column:")
print(df[features + [target]].isna().sum())

print("\nRows with any missing model values:")
print(df[features + [target]].isna().any(axis=1).sum())
print("Rows loaded:", len(df))

# 2. Select features and prediction target
features = [
    "store_id",
    "product_id",
    "week_no",
    "retail_discount",
    "coupon_discount",
    "coupon_match_discount",
    "has_display",
    "has_mailer"
]
target = "total_quantity"

df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna(subset=features + [target])

X = df[features]
y = df[target]

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train the regression model
model = RandomForestRegressor(
    n_estimators=100,
    max_depth=15,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

# 5. Make predictions and evaluate
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

print("\nMODEL EVALUATION")
print(f"MAE:  {mae:.3f}")
print(f"RMSE: {rmse:.3f}")
print(f"R-squared: {r2:.3f}")

# 6. Save product-level actual and predicted values

# Retrieve the original product, store and week information
results = df.loc[
    X_test.index,
    ["product_id", "store_id", "week_no"]
].copy().reset_index(drop=True)

# Add actual and predicted quantities
results["Actual_Quantity"] = y_test.to_numpy()
results["Predicted_Quantity"] = predictions

# Save the expanded prediction results
results.to_csv("sales_prediction_results.csv", index=False)

print("\nProduct-level prediction results saved successfully!")
print(results.head())

# 7. Create an actual-versus-predicted chart
plt.figure(figsize=(8, 6))
plt.scatter(
    results["Actual_Quantity"],
    results["Predicted_Quantity"],
    alpha=0.35
)
plt.xlabel("Actual Quantity")
plt.ylabel("Predicted Quantity")
plt.title("Actual vs Predicted Weekly Sales Quantity")
plt.tight_layout()
plt.savefig("sales_prediction_chart.png", dpi=200)
plt.show()

# 8. Save feature importance
importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
}).sort_values("Importance", ascending=False)

importance.to_csv("sales_feature_importance.csv", index=False)
print("\nSaved prediction results, chart, and feature importance.")