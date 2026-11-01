CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS analytics;
CREATE SCHEMA IF NOT EXISTS warehouse;

CREATE TABLE staging.transaction_data (
    household_key BIGINT,
    basket_id BIGINT,
    day INTEGER,
    product_id BIGINT,
    quantity BIGINT,
    sales_value NUMERIC(12,2),
    store_id BIGINT,
    retail_disc NUMERIC(12,2),
    trans_time INTEGER,
    week_no INTEGER,
    coupon_disc NUMERIC(12,2),
    coupon_match_disc NUMERIC(12,2)
);

CREATE TABLE staging.product (
    product_id BIGINT,
    manufacturer BIGINT,
    department TEXT,
    brand TEXT,
    commodity_desc TEXT,
    sub_commodity_desc TEXT,
    curr_size_of_product TEXT
);

CREATE TABLE staging.hh_demographic (
    classification_1 TEXT,
    classification_2 TEXT,
    classification_3 TEXT,
    homeowner_desc TEXT,
    classification_5 TEXT,
    classification_4 TEXT,
    kid_category_desc TEXT,
    household_key BIGINT
);

CREATE TABLE staging.coupon (
    coupon_upc TEXT,
    product_id BIGINT,
    campaign INTEGER
);

CREATE TABLE staging.coupon_redempt (
    household_key BIGINT,
    day INTEGER,
    coupon_upc TEXT,
    campaign INTEGER
);

CREATE TABLE staging.campaign_table (
    description TEXT,
    household_key BIGINT,
    campaign INTEGER
);

CREATE TABLE staging.campaign_desc (
    description TEXT,
    campaign INTEGER,
    start_day INTEGER,
    end_day INTEGER
);

CREATE TABLE staging.causal_data (
    product_id BIGINT,
    store_id BIGINT,
    week_no INTEGER,
    display TEXT,
    mailer TEXT
);