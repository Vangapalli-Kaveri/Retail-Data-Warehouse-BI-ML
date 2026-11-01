import pandas as pd
import os

file_path = r"D:\BI Project\sales_prediction_sample.csv"

print("File exists:", os.path.exists(file_path))
print("File size (MB):", round(os.path.getsize(file_path) / (1024 * 1024), 2))

df = pd.read_csv(file_path)

print("Rows excluding header:", len(df))
print("Columns:", df.columns.tolist())
print("Last 5 rows:")
print(df.tail())