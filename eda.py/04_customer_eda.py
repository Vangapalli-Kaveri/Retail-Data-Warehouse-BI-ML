from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

output_dir = Path("03_EDA_Results")
data = pd.read_csv(
    output_dir / "household_purchase_features.csv"
)

sns.histplot(data=data, x="total_spend", bins=30)
plt.title("Distribution of Household Spending")
plt.xlabel("Total spend")
plt.ylabel("Number of households")
plt.tight_layout()
plt.savefig(
    output_dir / "household_spending_distribution.png",
    dpi=150
)
plt.show()

sns.histplot(data=data, x="basket_count", bins=30)
plt.title("Distribution of Household Purchase Frequency")
plt.xlabel("Distinct baskets")
plt.ylabel("Number of households")
plt.tight_layout()
plt.savefig(
    output_dir / "household_purchase_frequency.png",
    dpi=150
)
plt.show()

sns.scatterplot(
    data=data,
    x="basket_count",
    y="total_spend"
)
plt.title("Household Spending vs Purchase Frequency")
plt.xlabel("Distinct baskets")
plt.ylabel("Total spend")
plt.tight_layout()
plt.savefig(
    output_dir / "spending_vs_frequency.png",
    dpi=150
)
plt.show()

print("EDA visualizations saved in:", output_dir.resolve())