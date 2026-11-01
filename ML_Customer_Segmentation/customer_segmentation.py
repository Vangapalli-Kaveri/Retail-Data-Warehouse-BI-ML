import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# 1. Load customer data
df = pd.read_csv("customer_segmentation_input.csv")
print("Loaded households:", len(df))

# 2. Prepare features
household_ids = df["household_key"].copy()
features = df.drop(columns=["household_key"]).copy()

features = features.replace([float("inf"), float("-inf")], float("nan"))
features = features.fillna(features.median())

# 3. Scale features
scaler = StandardScaler()
X = scaler.fit_transform(features)

# 4. Compare cluster counts
print("\nSILHOUETTE SCORES")
for k in [3, 4, 5]:
    test_model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = test_model.fit_predict(X)
    score = silhouette_score(
        X, labels,
        sample_size=min(1000, len(X)),
        random_state=42
    )
    print(f"K={k}: {score:.3f}")

# 5. Train the four-cluster model
model = KMeans(n_clusters=4, random_state=42, n_init=10)
df["segment"] = model.fit_predict(X)

# 6. Save household-level segment assignments
df.to_csv("customer_segments.csv", index=False)

# 7. Summarize each segment
summary = df.groupby("segment").agg(
    households=("household_key", "count"),
    avg_baskets=("total_baskets", "mean"),
    avg_shopping_days=("shopping_days", "mean"),
    avg_spend=("total_spend", "mean"),
    avg_departments=("departments_shopped", "mean"),
    avg_products=("distinct_products", "mean"),
    avg_coupon_discount=("coupon_discount_amount", "mean"),
    avg_retail_discount=("retail_discount_amount", "mean")
).round(2)

summary["household_percentage"] = (
    summary["households"] / len(df) * 100
).round(2)

print("\nFINAL CUSTOMER SEGMENT SUMMARY")
print(summary.to_string())

summary.to_csv("customer_segment_summary.csv")

print("\nSUCCESS!")
print("Created: customer_segments.csv")
print("Created: customer_segment_summary.csv")

import matplotlib.pyplot as plt

plt.figure(figsize=(9, 5))

bars = plt.bar(
    summary.index.astype(str),
    summary["households"]
)

plt.title("Households by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Households")

plt.bar_label(bars)
plt.tight_layout()

plt.savefig("customer_segment_chart.png", dpi=200)
plt.show()