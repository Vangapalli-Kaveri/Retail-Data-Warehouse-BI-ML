-- Sales prediction sample validation

SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT (store_id, product_id, week_no))
        AS unique_store_product_weeks
FROM analytics.sales_prediction_sample;


-- Inspect sample data

SELECT *
FROM analytics.sales_prediction_sample
LIMIT 5;


-- Highest quantity observations

SELECT *
FROM analytics.sales_prediction_sample
ORDER BY total_quantity DESC
LIMIT 20;


-- Quantity distribution

SELECT
    MIN(total_quantity) AS min_quantity,
    MAX(total_quantity) AS max_quantity,
    AVG(total_quantity) AS avg_quantity,
    PERCENTILE_CONT(0.50)
        WITHIN GROUP (ORDER BY total_quantity) AS median_quantity,
    PERCENTILE_CONT(0.95)
        WITHIN GROUP (ORDER BY total_quantity) AS p95_quantity,
    PERCENTILE_CONT(0.99)
        WITHIN GROUP (ORDER BY total_quantity) AS p99_quantity
FROM analytics.sales_prediction_sample;


-- Promotion information

SELECT
    display,
    COUNT(*) AS records
FROM staging.causal_data
GROUP BY display
ORDER BY records DESC;


SELECT
    mailer,
    COUNT(*) AS records
FROM staging.causal_data
GROUP BY mailer
ORDER BY records DESC;