import getpass
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import psycopg2

from sqlalchemy import create_engine, URL, text

# Enter the same password used in pgAdmin
password = getpass.getpass("PostgreSQL password: ")
print("password length:",len(password))

# First test a direct PostgreSQL connection
try:
    test_conn = psycopg2.connect(
        host="127.0.0.1",
        port=5432,
        dbname="retail_bi",
        user="postgres",
        password=password,
        connect_timeout=5
    )

    print("Direct PostgreSQL connection successful!")
    test_conn.close()

except psycopg2.Error as error:
    print("PostgreSQL connection failed.")
    print("Error:", error)
    raise SystemExit(1)

# Create the SQLAlchemy connection
connection_url = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password=password,
    host="127.0.0.1",
    port=5432,
    database="retail_bi"
)

engine = create_engine(connection_url)

# Verify the imported transaction data
with engine.connect() as connection:
    total_rows = connection.execute(
        text("SELECT COUNT(*) FROM staging.transaction_data")
    ).scalar_one()

    print("SQLAlchemy connection successful!")
    print("Transaction rows:", total_rows)

from sqlalchemy import create_engine, URL, text

connection_url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password=password,
    host="127.0.0.1",
    port=5432,
    database="retail_bi"
)

engine = create_engine(connection_url)

with engine.connect() as connection:
    total_rows = connection.execute(
        text("SELECT COUNT(*) FROM staging.transaction_data")
    ).scalar_one()

    print("SQLAlchemy connection successful!")
    print("Transaction rows:", total_rows)

#seven tables
from pathlib import Path
import pandas as pd
from sqlalchemy import text

output_dir = Path("03_EDA_Results")
output_dir.mkdir(exist_ok=True)

tables = [
    "transaction_data",
    "product",
    "hh_demographic",
    "coupon",
    "coupon_redempt",
    "campaign_table",
    "campaign_desc"
]

row_results = []
missing_results = []
type_results = []

with engine.connect() as connection:
    for table in tables:
        print(f"Profiling {table}...")

        total = connection.execute(
            text(f"SELECT COUNT(*) FROM staging.{table}")
        ).scalar_one()

        row_results.append({
            "table_name": table,
            "row_count": total
        })

        columns = connection.execute(
            text("""
                SELECT column_name, data_type
                FROM information_schema.columns
                WHERE table_schema = 'staging'
                  AND table_name = :table
                ORDER BY ordinal_position
            """),
            {"table": table}
        ).fetchall()

        for column, data_type in columns:
            quoted_column = '"' + column.replace('"', '""') + '"'

            null_count = connection.execute(
                text(
                    f"SELECT COUNT(*) FROM staging.{table} "
                    f"WHERE {quoted_column} IS NULL"
                )
            ).scalar_one()

            missing_results.append({
                "table_name": table,
                "column_name": column,
                "missing_count": null_count,
                "missing_percent": round(
                    null_count * 100 / total, 2
                ) if total else 0
            })

            type_results.append({
                "table_name": table,
                "column_name": column,
                "data_type": data_type
            })

pd.DataFrame(row_results).to_csv(
    output_dir / "table_row_counts.csv", index=False
)

pd.DataFrame(missing_results).to_csv(
    output_dir / "missing_value_profile.csv", index=False
)

pd.DataFrame(type_results).to_csv(
    output_dir / "column_data_types.csv", index=False
)

print("\nProfiling reports saved in:", output_dir.resolve())

#customer level features
customer_features = pd.read_sql(
    text("""
        SELECT
            household_key,
            COUNT(DISTINCT basket_id) AS basket_count,
            COUNT(DISTINCT day) AS active_days,
            COUNT(DISTINCT product_id) AS unique_products,
            SUM(quantity) AS total_quantity,
            SUM(sales_value) AS total_spend,
            AVG(sales_value) AS average_line_sales,
            SUM(ABS(coupon_disc))
                + SUM(ABS(coupon_match_disc))
                AS recorded_coupon_discount
        FROM staging.transaction_data
        GROUP BY household_key
        ORDER BY household_key
    """),
    engine
)

customer_features.to_csv(
    output_dir / "household_purchase_features.csv",
    index=False
)

print("\nHousehold feature dataset created.")
print("Number of households:", len(customer_features))
print(customer_features.head(10))
print("\nSummary statistics:")
print(customer_features.describe().round(2))

engine.dispose()

