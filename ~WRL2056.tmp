      # Retail Data Warehouse & Predictive Analytics

      ## Project Overview

      This project implements an end-to-end **Retail Data Warehouse and
      Predictive Analytics pipeline** for analyzing customer purchasing
      behaviour and predicting sales quantity under promotion-driven retail
      conditions.

      The solution integrates **relational data warehousing, ETL, exploratory
      data analysis, feature engineering, machine learning, statistical
      analysis, and business intelligence** into a single analytical workflow.

      The project uses retail transaction, product, household, coupon,
      campaign, and coupon-redemption data to transform raw operational data
      into analytical datasets and actionable business insights.

      ------------------------------------------------------------------------

      ## Domain

      **Domain:** Retail / Retail Analytics / Customer & Promotion Analytics

      The project focuses on two promotion-oriented analytical use cases:

      ### Use Case 1 --- Promotion-Aware Store/Product Sales Prediction

      Predict future **sales quantity** using historical sales behaviour
      together with product, store, temporal, and promotional attributes.

      **Business objective:** - Support demand forecasting. - Improve
      promotion planning. - Assist inventory allocation. - Identify expected
      sales response under promotional conditions. - Support store-level and
      product-level decision making.

      ### Use Case 2 --- Customer Purchase Behaviour & Promotion-Response Segmentation

      Segment households based on purchasing behaviour and promotion-related
      characteristics.

      **Business objective:** - Identify customer behaviour groups. -
      Understand purchasing frequency and spending patterns. - Identify
      promotion-sensitive customer groups. - Support targeted marketing and
      coupon strategies. - Improve customer engagement and promotional
      effectiveness.

      ------------------------------------------------------------------------

      ## Objectives

      -   Design and implement a retail-oriented data warehouse.
      -   Perform ETL from source retail datasets into an analytical database.
      -   Profile transaction and master datasets.
      -   Analyse data quality and missing-value patterns.
      -   Transform transaction-level records into household-level analytical
      features.
      -   Perform exploratory data analysis and visualization.
      -   Engineer customer, product, store, temporal, and promotion-related
      features.
      -   Perform customer segmentation using unsupervised machine learning.
      -   Develop a promotion-aware sales quantity prediction workflow.
      -   Validate the predictive model using appropriate validation
      procedures.
      -   Build Power BI dashboards for analytical reporting.
      -   Convert technical outputs into interpretable business insights.

      ------------------------------------------------------------------------

      ## Technology Stack

      Layer                     Technology
      ------------------------- ---------------------------------------------
      Programming Language      Python
      Database                  PostgreSQL
      Data Processing           Pandas, NumPy
      Statistical Analysis      Python statistical libraries
      Machine Learning          Scikit-learn
      Unsupervised Learning     K-Means Clustering
      Data Visualization        Matplotlib / Python visualization libraries
      Business Intelligence     Microsoft Power BI
      Query Language            SQL
      Development Environment   VS Code / Jupyter Notebook
      Version Control           Git / GitHub

      ------------------------------------------------------------------------

      ## Data Sources

      The analytical workflow uses the following retail datasets:

      -   Transaction data
      -   Product information
      -   Household demographic information
      -   Coupon information
      -   Coupon redemption information
      -   Campaign information
      -   Campaign description information

      The transaction dataset contains approximately **2.6 million records**
      and was used as the primary transactional source for downstream
      analysis.

      ------------------------------------------------------------------------

      ## System Architecture

      ``` text
                        ┌──────────────────────────┐
                        │     Raw Retail Data      │
                        │ Transactions / Products  │
                        │ Households / Coupons     │
                        │ Campaigns / Redemptions  │
                        └────────────┬─────────────┘
                                    │
                                    ▼
                        ┌──────────────────────────┐
                        │     PostgreSQL Database   │
                        │      Staging / Source     │
                        └────────────┬─────────────┘
                                    │
                                    ▼
                        ┌──────────────────────────┐
                        │          ETL Layer       │
                        │ Extract → Transform →    │
                        │ Load                     │
                        └────────────┬─────────────┘
                                    │
                                    ▼
                        ┌──────────────────────────┐
                        │   Analytical Data Model  │
                        │ Customer / Product /     │
                        │ Store / Promotion / Time │
                        └────────────┬─────────────┘
                                    │
                        ┌──────────────┴──────────────┐
                        ▼                             ▼
            ┌─────────────────────┐       ┌─────────────────────┐
            │ Customer Analytics  │       │ Sales Prediction    │
            │ & Segmentation      │       │ Pipeline            │
            └──────────┬──────────┘       └──────────┬──────────┘
                        │                             │
                        ▼                             ▼
            ┌─────────────────────┐       ┌─────────────────────┐
            │ K-Means Clustering  │       │ Supervised ML       │
            └──────────┬──────────┘       └──────────┬──────────┘
                        │                             │
                        └──────────────┬──────────────┘
                                    ▼
                        ┌──────────────────────────┐
                        │     Power BI Layer       │
                        │ Dashboards / KPIs /      │
                        │ Business Insights        │
                        └──────────────────────────┘
      ```

      ------------------------------------------------------------------------

      ## End-to-End Workflow

      ``` text
      Data Acquisition
            ↓
      Data Profiling
            ↓
      PostgreSQL Data Loading
            ↓
      ETL / Data Transformation
            ↓
      Data Quality Assessment
            ↓
      Exploratory Data Analysis
            ↓
      Feature Engineering
            ↓
      Analytical Dataset Creation
            ↓
      Customer Segmentation
            ↓
      Sales Quantity Prediction
            ↓
      Model Validation
            ↓
      Power BI Visualization
            ↓
      Business Interpretation
      ```

      ------------------------------------------------------------------------

      # 1. Data Warehousing

      The raw retail datasets were integrated into **PostgreSQL** to provide a
      centralized analytical data environment.

      The database layer enables:

      -   Structured data storage
      -   Relational joins
      -   Referential analysis
      -   SQL-based transformation
      -   Aggregation
      -   Data quality checks
      -   Analytical querying
      -   Integration with downstream Python workflows

      The warehouse-oriented design separates source data from transformed
      analytical datasets and supports repeatable data processing.

      ------------------------------------------------------------------------

      # 2. ETL Pipeline

      The project follows an **Extract--Transform--Load (ETL)** architecture.

      ### Extract

      Source retail datasets were collected and loaded for processing.

      ### Transform

      Transformation activities included:

      -   Data type handling
      -   Data profiling
      -   Missing-value assessment
      -   Dataset integration
      -   Record aggregation
      -   Household-level feature construction
      -   Promotion-related feature preparation
      -   Sales prediction feature preparation

      ### Load

      The transformed datasets were loaded/stored in the PostgreSQL analytical
      environment and subsequently consumed by Python-based machine-learning
      workflows and Power BI.

      ------------------------------------------------------------------------

      # 3. Data Profiling & Quality Assessment

      Initial profiling was performed to understand:

      -   Dataset dimensions
      -   Row counts
      -   Attribute structure
      -   Missing-value patterns
      -   Numerical distributions
      -   Data completeness

      Profiling outputs included:

      ``` text
      table_row_counts.csv
      missing_value_profile.csv
      ```

      These outputs provide a reproducible data-quality baseline before
      modelling.

      ------------------------------------------------------------------------

      # 4. Exploratory Data Analysis

      EDA was performed before machine learning to understand the underlying
      customer and transaction behaviour.

      The analysis included:

      -   Dataset profiling
      -   Descriptive statistics
      -   Distribution analysis
      -   Household-level aggregation
      -   Spending analysis
      -   Purchase-frequency analysis
      -   Relationship analysis
      -   Visualization

      The household analytical dataset contained **2,500 households** and was
      used for customer behaviour analysis.

      Key analytical attributes included:

      -   Basket count
      -   Active days
      -   Total spending
      -   Average line sales
      -   Recorded coupon discount
      -   Total quantity purchased
      -   Departments shopped
      -   Distinct products purchased
      -   Promotion-related attributes

      ------------------------------------------------------------------------

      # 5. Feature Engineering

      Feature engineering transformed raw transactional records into
      machine-learning-ready analytical features.

      ## Customer-level features

      Examples include:

      -   Total baskets
      -   Shopping days
      -   Total spending
      -   Average line spending
      -   Total quantity purchased
      -   Retail discount amount
      -   Coupon discount amount
      -   Number of departments visited
      -   Number of distinct products purchased

      These features represent different dimensions of customer behaviour:

      ``` text
      Frequency  → How often the customer purchases
      Monetary   → How much the customer spends
      Quantity   → How much product is purchased
      Variety    → Product/category diversity
      Promotion  → Discount and coupon interaction
      ```

      ## Sales prediction features

      The sales prediction dataset incorporated relevant:

      -   Product attributes
      -   Store attributes
      -   Week/time information
      -   Promotional attributes
      -   Historical sales information

      These variables were prepared to support promotion-aware sales quantity
      prediction.

      ------------------------------------------------------------------------

      # 6. Customer Segmentation

      Customer segmentation was implemented as an **unsupervised learning**
      task.

      ### Algorithm

      **K-Means Clustering**

      K-Means groups observations into clusters based on feature-space
      similarity.

      The workflow includes:

      ``` text
      Household Feature Dataset
            ↓
      Feature Preparation
            ↓
      Feature Scaling / Preparation
            ↓
      Cluster Analysis
            ↓
      K-Means Model
            ↓
      Customer Clusters
            ↓
      Cluster Profiling
            ↓
      Business Interpretation
      ```

      The resulting clusters were analysed to identify differences in:

      -   Spending behaviour
      -   Purchase frequency
      -   Shopping activity
      -   Product diversity
      -   Promotion-related behaviour

      ### K-Means Model Selection

      Different values of K were evaluated using the silhouette score:

      | K | Silhouette Score |
      |---:|---:|
      | 3 | 0.336 |
      | 4 | 0.336 |
      | 5 | 0.243 |

      Based on the evaluation and business interpretability, **K=4** was selected as the final clustering solution.

      ### Final Customer Segment Results

      | Segment | Households | Household % | Avg Spend | Avg Baskets | Avg Shopping Days | Avg Departments | Avg Products |
      |---:|---:|---:|---:|---:|---:|---:|---:|
      | 0 | 64 | 2.56% | 8,171.57 | 216.23 | 169.56 | 17.23 | 1,172.05 |
      | 1 | 1,387 | 55.48% | 1,196.08 | 48.94 | 43.67 | 10.48 | 270.62 |
      | 2 | 869 | 34.76% | 4,462.57 | 147.52 | 124.30 | 15.49 | 791.35 |
      | 3 | 180 | 7.20% | 11,097.51 | 369.87 | 256.06 | 18.49 | 1,463.45 |


      ------------------------------------------------------------------------

      # 7. Sales Quantity Prediction

      Sales prediction was implemented as a **supervised machine-learning**
      use case.

      ### Prediction Target

      **Sales Quantity**

      ### Predictors

      The modelling dataset incorporates relevant:

      -   Product-level variables
      -   Store-level variables
      -   Temporal variables
      -   Promotion-related variables
      -   Historical sales information

      The objective is to learn the relationship between explanatory variables
      and sales quantity and then estimate expected sales for unseen
      observations.

      ------------------------------------------------------------------------

      # 8. Model Validation

      The final prediction stage included validation of the trained sales
      prediction model.

      Validation is important to determine whether the model generalizes
      beyond the training data.

      The validation workflow follows:

      ``` text
      Prepared Dataset
            ↓
      Train/Test Data
            ↓
      Model Training
            ↓
      Prediction
            ↓
      Validation Metrics
            ↓
      Actual vs Predicted Analysis
            ↓
      Final Model Assessment
      ```

      The final validation outputs are used to assess prediction quality and
      identify whether the model is suitable for the intended retail
      forecasting use case.

      ### Final Model Results

      | Metric | Result |
      |---|---:|
      | MAE | 24.278 |
      | RMSE | 719.870 |
      | R² | 0.946 |

      The Power BI report also includes an **Actual vs Predicted Quantity** visual for model validation.

      ------------------------------------------------------------------------

      # 9. Power BI Business Intelligence Layer

      The final analytical datasets were connected to **Power BI** to create
      business-oriented dashboards.

      The dashboards convert analytical results into interactive visual
      information.

      The visualization layer supports analysis of:

      -   Sales performance
      -   Customer behaviour
      -   Promotion-related patterns
      -   Product/store performance
      -   Customer segments
      -   Prediction-oriented insights

      The Power BI layer acts as the **business consumption layer** of the
      analytical pipeline.

      ### Dashboard Pages

      The Power BI report contains three analytical pages:

      1. **Business Performance** — sales KPIs, weekly sales trends, department performance, promotion analysis, and product/category analysis.
      2. **ML Prediction & Validation** — actual vs predicted quantity and model validation metrics.
      3. **Customer Segmentation** — customer segment distribution, average spend by segment, and customer segment profiles.

      The Power BI report is stored in:

      ```text
      ── Dashboard.pbix
      ```

      ------------------------------------------------------------------------

      # 10. Project Outputs

      The project produces multiple analytical outputs, including:

      ``` text
      ├── Data Quality Reports
      │   ├── table_row_counts.csv
      │   └── missing_value_profile.csv
      │
      ├── EDA Outputs
      │   ├── household_spending_distribution.png
      │   ├── household_purchase_frequency.png
      │   └── spending_vs_frequency.png
      │
      ├── Analytical Datasets
      │   └── Household-level feature dataset
      │
      ├── Machine Learning
      │   ├── Customer segmentation
      │   └── Sales quantity prediction
      │
      └── Business Intelligence
      └── Power BI dashboards
      ```

      ------------------------------------------------------------------------

      # 11. Repository Structure

      The project repository is organized as follows:

      ```text
      BI Project/
      │
      ├── README.md
      ├── requirements.txt
      ├── 03_EDA_Results/
      ├── ML_Customer_Segmentation/
      ├── ML_Sales_Prediction/
      ├  
      ├── SQL/
      │   ├── 01_database_and_staging.sql
      │   ├── 02_data_quality_and_eda.sql
      │   ├── 03_data_warehouse.sql
      │   ├── 04_analytics_and_customer_segmentation.sql
      │   └── 05_sales_prediction_and_promotion.sql
      ├──── Dashboard.pbix
      ├────── eda.py/
      │   ├── 03_customer_eda.py
      │   ├── 04_customer_eda.py
      │   └── 05_customer_segmentation.py
      ├── check.py
      └── export_sample.py
      ```

      The repository contains the SQL scripts, Python workflows, analytical outputs,and Power BI dashboard used in the project.

      Large raw datasets, database credentials, and other sensitive or unnecessary generated files should not be committed to GitHub. The `.gitignore` file is used to exclude local and sensitive files.

      # 12. Installation

      Clone the repository:

      ``` bash
      git clone <repository-url>
      cd Retail-Data-Warehouse-BI-ML
      ```

      Create a virtual environment:

      ``` bash
      python -m venv venv
      ```

      Activate the environment on Windows:

      ``` bash
      venv\Scripts\activate
      ```

      Install dependencies:

      ``` bash
      pip install -r requirements.txt
      ```

      ------------------------------------------------------------------------

      # 13. PostgreSQL Configuration

      The project was developed using a local PostgreSQL database. The connection parameters
      shown below are provided for local reproduction when required.

      Example environment variables:

      ``` text
      DB_HOST=
      DB_PORT=
      DB_NAME=
      DB_USER=
      DB_PASSWORD=
      ```

      Credentials should be stored in a local `.env` file and must **not** be
      committed to GitHub.

      Example:

      ``` text
      .env
      ```

      Add the following to `.gitignore`:

      ``` text
      .env
      venv/
      __pycache__/
      *.pyc
      data/raw/
      ```

      ------------------------------------------------------------------------

      # 14. Reproducibility

      The project is structured to support analytical review and reproduction of the main workflows:

      1.  Review the project documentation and repository structure.
      2.  Review the SQL scripts for staging, data quality, warehouse, and analytical processing.
      3.  Review the Python machine-learning workflows and analytical outputs.
      4.  Review the customer segmentation and sales prediction results.
      5.  Open the Power BI report to review the final business dashboards.

      PostgreSQL was used as the local development and analytical database. The GitHub repository contains the SQL scripts, Python workflows, analytical outputs, and Power BI report. 

      ------------------------------------------------------------------------

      # 15. Business Value

      The project demonstrates how a retail organization can move from **raw
      transactional data to decision-support analytics**.

      ### Customer Analytics

      Customer segmentation enables differentiated treatment of customer
      groups instead of applying the same marketing strategy to every
      household.

      ### Promotion Analytics

      Promotion-related variables enable the analysis of customer response to
      discounts and coupons.

      ### Sales Forecasting

      Sales quantity prediction can support:

      -   Inventory planning
      -   Demand estimation
      -   Store-level planning
      -   Product-level planning
      -   Promotion planning

      ### Decision Support

      Power BI converts analytical outputs into dashboards that can be
      consumed by business users without directly interacting with the
      underlying machine-learning pipeline.

      ------------------------------------------------------------------------

      # 16. Key Technical Concepts

      This project demonstrates practical implementation of:

      -   Data Warehousing
      -   ETL
      -   Relational Database Management
      -   SQL
      -   PostgreSQL
      -   Data Profiling
      -   Exploratory Data Analysis
      -   Descriptive Statistics
      -   Feature Engineering
      -   Unsupervised Learning
      -   K-Means Clustering
      -   Supervised Learning
      -   Regression-based Prediction
      -   Model Validation
      -   Promotion Analytics
      -   Customer Segmentation
      -   Business Intelligence
      -   Power BI
      -   Data Visualization
      -   End-to-End Analytics Pipeline

      ------------------------------------------------------------------------

      # 17. Limitations

      -   Prediction quality depends on the availability and quality of
      historical retail data.
      -   Promotion effects may vary across products, stores and customer
      groups.
      -   Customer segmentation is dependent on the selected behavioural
      features.
      -   Historical patterns may not fully represent future market
      conditions.
      -   The project focuses on analytical prediction rather than real-time
      production deployment.

      ------------------------------------------------------------------------

      # 18. Future Enhancements

      Potential extensions include:

      -   Automated ETL orchestration.
      -   Real-time transaction ingestion.
      -   Advanced time-series forecasting.
      -   Hyperparameter optimization.
      -   Model explainability using SHAP or similar techniques.
      -   Automated model monitoring.
      -   Promotion uplift modelling.
      -   Customer-level recommendation systems.
      -   Cloud-based data warehousing.
      -   API-based model deployment.
      -   Automated Power BI refresh pipelines.

      ------------------------------------------------------------------------

      # 19. Conclusion

      This project demonstrates an end-to-end **Retail Data Warehouse and
      Predictive Analytics architecture** that integrates PostgreSQL, Python,
      machine learning and Power BI.

      The pipeline transforms raw retail transaction and promotion data into
      structured analytical datasets, derives customer and sales-related
      features, performs customer segmentation and sales quantity prediction,
      validates the predictive workflow, and presents the resulting insights
      through business intelligence dashboards.

      The project therefore demonstrates the complete progression:

      **Raw Data → Data Warehouse → ETL → EDA → Feature Engineering → Machine
      Learning → Validation → Business Intelligence → Decision Support**

      ------------------------------------------------------------------------

      ## Author

      **Retail Data Warehouse & Predictive Analytics Project**

      Built using Python, PostgreSQL, Machine Learning and Power BI.
