-- Product dimension
CREATE TABLE IF NOT EXISTS warehouse.dim_product (
    product_id BIGINT PRIMARY KEY,
    manufacturer BIGINT,
    department TEXT,
    brand TEXT,
    commodity_desc TEXT,
    sub_commodity_desc TEXT,
    curr_size_of_product TEXT
);

-- Household dimension
CREATE TABLE IF NOT EXISTS warehouse.dim_household (
    household_key BIGINT PRIMARY KEY,
    classification_1 TEXT,
    classification_2 TEXT,
    classification_3 TEXT,
    homeowner_desc TEXT,
    classification_5 TEXT,
    classification_4 TEXT,
    kid_category_desc TEXT
);

-- Store dimension
CREATE TABLE IF NOT EXISTS warehouse.dim_store (
    store_id BIGINT PRIMARY KEY
);

-- Day dimension
CREATE TABLE IF NOT EXISTS warehouse.dim_day (
    day_key INTEGER PRIMARY KEY,
    week_no INTEGER
);

-- Transaction fact table
CREATE TABLE IF NOT EXISTS warehouse.fact_transactions (
    transaction_key BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    household_key BIGINT,
    basket_id BIGINT,
    product_id BIGINT,
    store_id BIGINT,
    day_key INTEGER,
    quantity BIGINT,
    sales_value NUMERIC(12,2),
    retail_disc NUMERIC(12,2),
    coupon_disc NUMERIC(12,2),
    coupon_match_disc NUMERIC(12,2)
);