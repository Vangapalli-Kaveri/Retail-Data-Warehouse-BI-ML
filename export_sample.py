import pandas as pd
import psycopg

# Connect to your PostgreSQL database
conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="retail_bi",
    user="postgres",
    password=input("Enter your PostgreSQL password: ")
)

query = """
SELECT *
FROM analytics.sales_prediction_sample;
"""

output_file = r"D:\BI Project\sales_prediction_sample.csv"

try:
    df = pd.read_sql_query(query, conn)
    df.to_csv(output_file, index=False)

    print("Export completed successfully.")
    print("Rows exported:", len(df))
    print("Saved to:", output_file)

finally:
    conn.close()