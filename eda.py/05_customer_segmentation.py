
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Existing EDA output folder
output_dir = Path(r"D:\BI Project\03_EDA_Results")
output_dir.mkdir(parents=True, exist_ok=True)

input_file = output_dir / "household_purchase_features.csv"

# Load the household-level dataset
df = pd.read_csv(input_file)

print("Dataset shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

# Features available for the first model
candidate_features = [
    "basket_count",
    "active_days",
    "unique_products",
    "total_spend",
    "average_line_sales",
]

# Keep only features present in the CSV
features = [c for c in candidate_features if c in df.columns]

if len(features) < 2:
    raise ValueError(
        "Required household features are missing. "
        "Check household_purchase_features.csv."
    )

# Prepare numeric values
X = df[features].apply(pd.to_numeric, errors="coerce")
X = X.replace([float("inf"), float("-inf")], float("nan"))

valid_rows = X.notna().all(axis=1)
X = X.loc[valid_rows].copy()
df_model = df.loc[valid_rows].copy()

# Reduce skew using log1p, then standardize features
X_log = X.clip(lower=0)
X_log = X_log.apply(lambda col: __import__("numpy").log1p(col))

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_log)

# Compare K-means models with 2 to 6 clusters
results = []

for k in range(2, 7):
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )
    labels = model.fit_predict(X_scaled)

    score = silhouette_score(
        X_scaled,
        labels,
        sample_size=min(2000, len(X_scaled)),
        random_state=42
    )

    results.append({
        "k": k,
        "silhouette_score": score,
        "inertia": model.inertia_
    })

scores = pd.DataFrame(results)
scores.to_csv(output_dir / "kmeans_model_comparison.csv", index=False)

print("\nModel comparison:")
print(scores.round(4).to_string(index=False))

# Select the k with the highest silhouette score
best_k = int(scores.loc[scores["silhouette_score"].idxmax(), "k"])

best_model = KMeans(
    n_clusters=best_k,
    random_state=42,
    n_init=10
)

df_model["cluster"] = best_model.fit_predict(X_scaled)

# Save household assignments
df_model.to_csv(
    output_dir / "household_cluster_assignments.csv",
    index=False
)

# Summarize clusters using original feature units
profile = df_model.groupby("cluster")[features].mean().round(2)
profile["households"] = df_model.groupby("cluster").size()

profile.to_csv(output_dir / "customer_cluster_profile.csv")

print(f"\nSelected cluster count: {best_k}")
print("\nCluster profile:")
print(profile)

# Save model-comparison chart
plt.figure(figsize=(8, 5))
plt.plot(
    scores["k"],
    scores["silhouette_score"],
    marker="o"
)
plt.xlabel("Number of clusters (k)")
plt.ylabel("Silhouette score")
plt.title("K-means Customer Segmentation Evaluation")
plt.xticks(scores["k"])
plt.tight_layout()
plt.savefig(
    output_dir / "kmeans_silhouette_comparison.png",
    dpi=150
)
plt.show()

print(f"\nResults saved in: {output_dir}")
