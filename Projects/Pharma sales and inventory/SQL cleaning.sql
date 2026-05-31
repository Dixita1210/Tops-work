use dk
-- ── 1. dim_products ──────────────────────────────────────────
CREATE TABLE dbo.dim_products (
    product_id       NVARCHAR(10)   NOT NULL,
    product_name     NVARCHAR(100)  NULL,
    category         NVARCHAR(50)   NULL,
    manufacturer     NVARCHAR(100)  NULL,
    unit_cost        NVARCHAR(20)   NULL,   -- kept as NVARCHAR intentionally (dirty data)
    unit_price       NVARCHAR(20)   NULL,   -- kept as NVARCHAR intentionally (dirty data)
    shelf_life_days  NVARCHAR(10)   NULL,
    hsn_code         NVARCHAR(20)   NULL
);
 
-- ── 2. dim_customers ─────────────────────────────────────────
CREATE TABLE dbo.dim_customers (
    customer_id      NVARCHAR(10)   NOT NULL,
    customer_name    NVARCHAR(150)  NULL,
    customer_type    NVARCHAR(50)   NULL,
    city             NVARCHAR(100)  NULL,
    state            NVARCHAR(100)  NULL,
    region           NVARCHAR(50)   NULL,
    contact_email    NVARCHAR(200)  NULL,
    credit_limit     NVARCHAR(20)   NULL
);
 
-- ── 3. dim_suppliers ─────────────────────────────────────────
CREATE TABLE dbo.dim_suppliers (
    supplier_id          NVARCHAR(10)   NOT NULL,
    supplier_name        NVARCHAR(150)  NULL,
    lead_time_days       NVARCHAR(20)   NULL,   -- dirty: some rows have "10 days"
    reliability_score    NVARCHAR(10)   NULL,   -- dirty: some rows have "70%"
    payment_terms_days   NVARCHAR(10)   NULL,
    state                NVARCHAR(100)  NULL
);
 
-- ── 4. fact_sales ─────────────────────────────────────────────
CREATE TABLE dbo.fact_sales (
    sale_id          NVARCHAR(15)   NOT NULL,
    sale_date        NVARCHAR(20)   NULL,   -- dirty: some invalid dates like "2024-13-45"
    product_id       NVARCHAR(10)   NULL,
    customer_id      NVARCHAR(10)   NULL,
    quantity_sold    NVARCHAR(20)   NULL,   -- dirty: some negative values
    unit_price       NVARCHAR(20)   NULL,
    discount_pct     NVARCHAR(10)   NULL,   -- dirty: some values = 110
    total_revenue    NVARCHAR(20)   NULL,   -- dirty: some negative values, some NULL
    payment_mode     NVARCHAR(50)   NULL,
    sales_rep        NVARCHAR(100)  NULL
);
 
-- ── 5. fact_inventory ────────────────────────────────────────
CREATE TABLE dbo.fact_inventory (
    inventory_id     NVARCHAR(15)   NOT NULL,
    record_date      NVARCHAR(20)   NULL,
    product_id       NVARCHAR(10)   NULL,
    supplier_id      NVARCHAR(10)   NULL,
    opening_stock    NVARCHAR(20)   NULL,   -- dirty: some rows have "N/A"
    received_qty     NVARCHAR(20)   NULL,
    closing_stock    NVARCHAR(20)   NULL,   -- dirty: some negative values
    expiry_date      NVARCHAR(20)   NULL,
    warehouse_loc    NVARCHAR(20)   NULL,
    batch_number     NVARCHAR(20)   NULL
);
 
-- ── 6. fact_purchases ────────────────────────────────────────
CREATE TABLE dbo.fact_purchases (
    purchase_id      NVARCHAR(15)   NOT NULL,
    purchase_date    NVARCHAR(20)   NULL,
    product_id       NVARCHAR(10)   NULL,
    supplier_id      NVARCHAR(10)   NULL,
    qty_ordered      NVARCHAR(20)   NULL,   -- dirty: some rows have "PENDING"
    qty_received     NVARCHAR(20)   NULL,
    expected_date    NVARCHAR(20)   NULL,
    actual_date      NVARCHAR(20)   NULL,   -- dirty: some rows have "TBD"
    unit_cost        NVARCHAR(20)   NULL,
    total_cost       NVARCHAR(20)   NULL,
    invoice_number   NVARCHAR(20)   NULL
);
ALTER TABLE dim_suppliers
ALTER COLUMN reliability_score VARCHAR(20);

select * from dbo.dim_customers
select * from dbo.dim_products
select * from dbo.dim_suppliers
select * from dbo.fact_inventory
select * from dbo.fact_purchases
select * from dbo.fact_sales

------------------------------------- fact_sales------------------------------

--- checking null values ----

SELECT
    COUNT(*) AS total_rows,
    SUM(CASE WHEN sale_date IS NULL THEN 1 ELSE 0 END)      AS null_dates,
    SUM(CASE WHEN quantity_sold IS NULL THEN 1 ELSE 0 END)   AS null_qty,
    SUM(CASE WHEN total_revenue IS NULL THEN 1 ELSE 0 END)   AS null_revenue,
    SUM(CASE WHEN payment_mode IS NULL THEN 1 ELSE 0 END)    AS null_payment,
    SUM(CASE WHEN sales_rep IS NULL THEN 1 ELSE 0 END)       AS null_rep
FROM dbo.fact_sales;

--- replacing / deleteing null values 

update dbo.fact_sales
set payment_mode='Unknown' where payment_mode is null

--- filling null values --- 
UPDATE dbo.fact_sales
SET total_revenue = TRY_CAST(quantity_sold AS FLOAT)
                  * TRY_CAST(unit_price AS FLOAT)
                  * (1 - TRY_CAST(discount_pct AS FLOAT)/100)
WHERE total_revenue IS NULL
  AND quantity_sold IS NOT NULL
  AND unit_price IS NOT NULL;


--- standarlize payment_mode casing---
UPDATE dbo.fact_sales
SET payment_mode = UPPER(LEFT(TRIM(payment_mode),1))
                 + LOWER(SUBSTRING(TRIM(payment_mode),2,50));


-- checking duplicate-----

SELECT sale_id, sale_date, product_id, customer_id,
       quantity_sold, total_revenue, COUNT(*) AS occurrences
FROM dbo.fact_sales
GROUP BY sale_id, sale_date, product_id, customer_id,
         quantity_sold, total_revenue
HAVING COUNT(*) > 1
ORDER BY occurrences DESC;

--- deleting duplicate ---

WITH cte AS (
    SELECT *, ROW_NUMBER() OVER (
        PARTITION BY sale_id, sale_date, product_id,
                     customer_id, quantity_sold, total_revenue
        ORDER BY (SELECT NULL)
    ) AS rn
    FROM dbo.fact_sales
)
DELETE FROM cte WHERE rn > 1;


--- checking negative values ---
select quantity_sold , unit_price, total_revenue from dbo.fact_sales where 
try_cast (quantity_sold as float) <0 or try_cast(unit_price as float) <0 or try_cast(total_revenue as float)<0 


--- remove nehgative values----
delete  from dbo.fact_sales where 
try_cast (quantity_sold as float) <0 or try_cast(unit_price as float) <0 or try_cast(total_revenue as float)<0 

--- invalid dates---
SELECT sale_date FROM dbo.fact_sales
WHERE TRY_CONVERT(DATE, sale_date) IS NULL
  AND sale_date IS NOT NULL;

  --- deleteing invalid dates----
  DELETE FROM dbo.fact_sales
WHERE TRY_CONVERT(DATE, sale_date) IS NULL
  AND sale_date IS NOT NULL;
 

--- impossible discounts--- 
SELECT * FROM dbo.fact_sales
WHERE TRY_CAST(discount_pct AS FLOAT) > 100;

--- update discounts to 0 ---
update dbo.fact_sales
set discount_pct= 0 where try_cast (discount_pct as float) > 100 ;


---------------------purchases----------------


-- Step 1: NULL out 'PENDING' qty and 'TBD' dates----

UPDATE dbo.fact_purchases
SET qty_ordered = NULL
WHERE TRIM(CAST(qty_ordered AS NVARCHAR)) = 'PENDING';
 
UPDATE dbo.fact_purchases
SET actual_date = NULL
WHERE TRIM(CAST(actual_date AS NVARCHAR)) = 'TBD';


------Fix NULL total_cost------- 

UPDATE dbo.fact_purchases
SET total_cost = TRY_CAST(qty_received AS FLOAT)
              * TRY_CAST(unit_cost AS FLOAT)
WHERE total_cost IS NULL
  AND qty_received IS NOT NULL;


  -----------------------------inventory------------------

  -- Step 1: Remove rows where opening_stock is 'N/A'
DELETE FROM dbo.fact_inventory
WHERE TRIM(CAST(opening_stock AS NVARCHAR)) = 'N/A';
 
-- Step 2: Fix negative closing_stock (set to 0)
UPDATE dbo.fact_inventory
SET closing_stock = 0
WHERE TRY_CAST(closing_stock AS FLOAT) < 0;
 
-- Step 3: Fill NULL warehouse_loc
UPDATE dbo.fact_inventory
SET warehouse_loc = 'Unassigned'
WHERE warehouse_loc IS NULL;

-------------------suppliers--------

-- Add clean integer column for lead time
ALTER TABLE dbo.dim_suppliers ADD lead_time_clean INT;
 
UPDATE dbo.dim_suppliers
SET lead_time_clean = TRY_CAST(
    TRIM(REPLACE(REPLACE(LOWER(CAST(lead_time_days AS NVARCHAR)),
         'days',''), ' ', ''))
    AS INT);
 
-- Add clean decimal column for reliability score
ALTER TABLE dbo.dim_suppliers ADD reliability_clean FLOAT;
 
UPDATE dbo.dim_suppliers
SET reliability_clean =
    CASE
        WHEN CAST(reliability_score AS NVARCHAR) LIKE '%[%]%'
        THEN TRY_CAST(REPLACE(CAST(reliability_score AS NVARCHAR),'%','') AS FLOAT) / 100
        ELSE TRY_CAST(reliability_score AS FLOAT)
    END;


--------------products -------------------------------

-- Step 1: Trim & standardize product names
UPDATE dbo.dim_products
SET product_name =UPPER(LEFT(TRIM(product_name),1))
                + LOWER(SUBSTRING(TRIM(product_name),2,200));


-- Step 2: Standardize category casing
UPDATE dbo.dim_products
SET category = TRIM(UPPER(LEFT(TRIM(category),1)))
             + LOWER(SUBSTRING(TRIM(category),2,100));



-- Step 3: Delete duplicate 


select product_id , product_name, category, manufacturer, unit_cost, unit_price, shelf_life_days, hsn_code , 
count(*) as duplicate_count from dim_products group by product_id , product_name, category, manufacturer, unit_cost, unit_price, shelf_life_days, hsn_code
having count(*) >1

WITH cte AS (

    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY product_name, manufacturer
               ORDER BY product_id
           ) AS rn

    FROM dbo.dim_products
)

DELETE FROM cte
WHERE rn > 1;


-----------------------customers---------------------

UPDATE dbo.dim_customers
SET region = UPPER(LEFT(TRIM(region),1))
           + LOWER(SUBSTRING(TRIM(region),2,50));

-- Fix customer_type casing
UPDATE dbo.dim_customers
SET customer_type = TRIM(UPPER(LEFT(TRIM(customer_type),1)))
                  + LOWER(SUBSTRING(TRIM(customer_type),2,50));


-- Fix city trailing spaces
UPDATE dbo.dim_customers
SET city = TRIM(city);


-- Fill missing customer_type with 'Unknown'
UPDATE dbo.dim_customers
SET customer_type = 'Unknown'
WHERE customer_type IS NULL OR TRIM(customer_type) = '';











