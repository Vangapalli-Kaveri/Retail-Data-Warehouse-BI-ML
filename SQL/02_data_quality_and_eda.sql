-- Row counts
SELECT 'transaction_data' AS table_name, COUNT(*) AS row_count
FROM staging.transaction_data
UNION ALL
SELECT 'product', COUNT(*)
FROM staging.product
UNION ALL
SELECT 'hh_demographic', COUNT(*)
FROM staging.hh_demographic
UNION ALL
SELECT 'coupon', COUNT(*)
FROM staging.coupon
UNION ALL
SELECT 'coupon_redempt', COUNT(*)
FROM staging.coupon_redempt
UNION ALL
SELECT 'campaign_table', COUNT(*)
FROM staging.campaign_table
UNION ALL
SELECT 'campaign_desc', COUNT(*)
FROM staging.campaign_desc
UNION ALL
SELECT 'causal_data', COUNT(*)
FROM staging.causal_data;


-- Missing values in transaction data
SELECT
    COUNT(*) AS total_rows,
    COUNT(*) FILTER (WHERE household_key IS NULL) AS missing_household_key,
    COUNT(*) FILTER (WHERE basket_id IS NULL) AS missing_basket_id,
    COUNT(*) FILTER (WHERE product_id IS NULL) AS missing_product_id,
    COUNT(*) FILTER (WHERE quantity IS NULL) AS missing_quantity,
    COUNT(*) FILTER (WHERE sales_value IS NULL) AS missing_sales_value,
    COUNT(*) FILTER (WHERE store_id IS NULL) AS missing_store_id
FROM staging.transaction_data;


-- Duplicate transaction records
SELECT
    household_key,
    basket_id,
    product_id,
    day,
    COUNT(*) AS duplicate_count
FROM staging.transaction_data
GROUP BY household_key, basket_id, product_id, day
HAVING COUNT(*) > 1;


-- Basic quantity and sales checks
SELECT
    MIN(quantity) AS min_quantity,
    MAX(quantity) AS max_quantity,
    MIN(sales_value) AS min_sales_value,
    MAX(sales_value) AS max_sales_value,
    AVG(quantity) AS avg_quantity,
    AVG(sales_value) AS avg_sales_value
FROM staging.transaction_data;


-- Unique counts
SELECT
    COUNT(DISTINCT household_key) AS households,
    COUNT(DISTINCT basket_id) AS baskets,
    COUNT(DISTINCT product_id) AS products,
    COUNT(DISTINCT store_id) AS stores
FROM staging.transaction_data;