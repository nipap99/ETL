# ETL
# ETL Data Pipeline with Supabase & Python

Modern, lightweight **ETL** (Extract → Transform → Load) pipeline that pulls data from various sources, cleans & transforms it using Python + SQL, and loads it into **Supabase** (PostgreSQL) — creating a simple but powerful **data warehouse** for business analytics and decision making.

![ETL Pipeline Overview](https://img.shields.io/badge/ETL-Pipeline-blue?style=for-the-badge&logo=apachespark)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Powerful%20Queries-4479A1?style=for-the-badge&logo=postgresql)

## ✨ What this project does

- **Extracts** data from APIs, CSV files, web scraping, databases, etc.
- **Transforms** data using Python (pandas, cleaning, enrichment, aggregations) + powerful **SQL** inside Supabase
- **Loads** clean, structured data into Supabase tables (your personal cloud data warehouse)
- Enables fast **business-oriented SQL queries** for reports, dashboards & decisions

→ From raw messy data → clean, queryable tables ready for BI tools / analysts / managers



## 🚀 Tech Stack

| Layer              | Technology                          | Purpose                              |
|--------------------|-------------------------------------|--------------------------------------|
| Language           | Python 3.10+                        | Core scripting & transformation      |
| Data Processing    | pandas, numpy                       | Cleaning, calculations, joins        |
| Database           | Supabase (PostgreSQL)               | Storage + Data Warehouse             |
| Connection         | SQLAlchemy + psycopg2               | Reliable & safe database interaction |
| SQL Transformations| PostgreSQL window functions, CTEs   | Advanced analytics directly in DB    |
| Orchestration      |   Apache Airflow / cron             | Scheduling & monitoring              |

## 📊  Business Queries that I run

```sql
-- Monthly revenue by customer segment
SELECT 
    DATE_TRUNC('month', order_date) AS month,
    customer_segment,
    COUNT(DISTINCT order_id) AS orders,
    ROUND(SUM(total_amount)::numeric, 2) AS revenue
FROM fact_orders
JOIN dim_customers USING (customer_id)
GROUP BY 1, 2
ORDER BY 1 DESC;

-- Top 5 products by margin last 90 days
SELECT 
    p.product_name,
    SUM(o.quantity * (o.unit_price - p.cost_price)) AS total_margin
FROM fact_order_items o
JOIN dim_products p ON o.product_id = p.product_id
WHERE o.order_date >= CURRENT_DATE - INTERVAL '90 days'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5;
