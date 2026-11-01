-- Customer-level features for segmentation
DROP TABLE IF EXISTS analytics.customer_features;

CREATE TABLE analytics.customer_features AS
SELECT
    f.household_key,
    COUNT(DISTINCT f.basket_id) AS total_baskets,
    COUNT(*) AS total_transaction_lines,
    COUNT(DISTINCT f.day_key) AS shopping_days,
    SUM(f.sales_value) AS total_spend,
    AVG(f.sales_value) AS avg_line_spend,
    SUM(f.quantity) AS total_quantity,
    SUM(ABS(COALESCE(f.retail_disc, 0))) AS retail_discount_amount,
    SUM(ABS(COALESCE(f.coupon_disc, 0))) AS coupon_discount_amount,
    SUM(ABS(COALESCE(f.coupon_match_disc, 0))) AS coupon_match_discount_amount,
    COUNT(DISTINCT p.department) AS departments_shopped,
    COUNT(DISTINCT f.product_id) AS distinct_products
FROM warehouse.fact_transactions f
LEFT JOIN warehouse.dim_product p
    ON f.product_id = p.product_id
GROUP BY f.household_key;

ALTER TABLE analytics.customer_features
ADD PRIMARY KEY (household_key);


-- Input table for customer segmentation
DROP TABLE IF EXISTS analytics.customer_segmentation_input;

CREATE TABLE analytics.customer_segmentation_input AS
SELECT
    household_key,
    total_baskets,
    shopping_days,
    total_spend,
    avg_line_spend,
    total_quantity,
    retail_discount_amount,
    coupon_discount_amount,
    coupon_match_discount_amount,
    departments_shopped,
    distinct_products
FROM analytics.customer_features
WHERE total_baskets > 0;

ALTER TABLE analytics.customer_segmentation_input
ADD PRIMARY KEY (household_key);


-- Store-product-week aggregation for sales prediction
DROP TABLE IF EXISTS analytics.store_product_week;

CREATE TABLE analytics.store_product_week AS
SELECT
    f.store_id,
    f.product_id,
    d.week_no,
    SUM(f.quantity) AS total_quantity,
    SUM(f.sales_value) AS total_sales,
    SUM(ABS(COALESCE(f.retail_disc, 0))) AS retail_discount,
    SUM(ABS(COALESCE(f.coupon_disc, 0))) AS coupon_discount,
    SUM(ABS(COALESCE(f.coupon_match_disc, 0)))
        AS coupon_match_discount
FROM warehouse.fact_transactions f
JOIN warehouse.dim_day d
    ON f.day_key = d.day_key
GROUP BY f.store_id, f.product_id, d.week_no;