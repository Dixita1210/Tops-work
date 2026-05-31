create database churn_analysis
use churn_analysis

CREATE TABLE Telco_customer_churn (

    CustomerID VARCHAR(50),

    Count INT,

    Country VARCHAR(100),
    State VARCHAR(100),
    City VARCHAR(100),
    Zip_Code INT,

    Lat_Long VARCHAR(100),
    Latitude FLOAT,
    Longitude FLOAT,

    Gender VARCHAR(20),
    Senior_Citizen VARCHAR(10),
    Partner VARCHAR(10),
    Dependents VARCHAR(10),

    Tenure_Months INT,

    Phone_Service VARCHAR(20),
    Multiple_Lines VARCHAR(30),

    Internet_Service VARCHAR(30),
    Online_Security VARCHAR(30),
    Online_Backup VARCHAR(30),
    Device_Protection VARCHAR(30),
    Tech_Support VARCHAR(30),

    Streaming_TV VARCHAR(30),
    Streaming_Movies VARCHAR(30),

    Contract VARCHAR(50),
    Paperless_Billing VARCHAR(10),
    Payment_Method VARCHAR(100),

    Monthly_Charge FLOAT,
    Total_Charges FLOAT,

    Customer_Status VARCHAR(20),

    Churn_Label VARCHAR(10),
    Churn_Value INT,
    Churn_Score INT,

    CLTV FLOAT,

    Churn_Category VARCHAR(100),
    Churn_Reason VARCHAR(500),

    Satisfaction_Score INT
);

select * from Telco_customer_churn

-- check the datatype 

SELECT
COLUMN_NAME,
DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME='Telco_customer_churn';


-- total rows
SELECT COUNT(*)
FROM Telco_customer_churn


--check duplicates
SELECT
CustomerID,
COUNT(*)
FROM Telco_customer_churn
GROUP BY CustomerID
HAVING COUNT(*) > 1;


--check null 
SELECT
    SUM(CASE WHEN CustomerID IS NULL THEN 1 ELSE 0 END) AS CustomerID_Nulls,
    SUM(CASE WHEN Country IS NULL THEN 1 ELSE 0 END) AS Country_Nulls,
    SUM(CASE WHEN State IS NULL THEN 1 ELSE 0 END) AS State_Nulls,
    SUM(CASE WHEN City IS NULL THEN 1 ELSE 0 END) AS City_Nulls,
    SUM(CASE WHEN Zip_Code IS NULL THEN 1 ELSE 0 END) AS ZipCode_Nulls,
    SUM(CASE WHEN Lat_Long IS NULL THEN 1 ELSE 0 END) AS LatLong_Nulls,
    SUM(CASE WHEN Latitude IS NULL THEN 1 ELSE 0 END) AS Latitude_Nulls,
    SUM(CASE WHEN Longitude IS NULL THEN 1 ELSE 0 END) AS Longitude_Nulls,
    SUM(CASE WHEN Gender IS NULL THEN 1 ELSE 0 END) AS Gender_Nulls,
    SUM(CASE WHEN Senior_Citizen IS NULL THEN 1 ELSE 0 END) AS SeniorCitizen_Nulls,
    SUM(CASE WHEN Partner IS NULL THEN 1 ELSE 0 END) AS Partner_Nulls,
    SUM(CASE WHEN Dependents IS NULL THEN 1 ELSE 0 END) AS Dependents_Nulls,
    SUM(CASE WHEN Tenure_Months IS NULL THEN 1 ELSE 0 END) AS Tenure_Nulls,
    SUM(CASE WHEN Phone_Service IS NULL THEN 1 ELSE 0 END) AS PhoneService_Nulls,
    SUM(CASE WHEN Multiple_Lines IS NULL THEN 1 ELSE 0 END) AS MultipleLines_Nulls,
    SUM(CASE WHEN Internet_Service IS NULL THEN 1 ELSE 0 END) AS InternetService_Nulls,
    SUM(CASE WHEN Online_Security IS NULL THEN 1 ELSE 0 END) AS OnlineSecurity_Nulls,
    SUM(CASE WHEN Online_Backup IS NULL THEN 1 ELSE 0 END) AS OnlineBackup_Nulls,
    SUM(CASE WHEN Device_Protection IS NULL THEN 1 ELSE 0 END) AS DeviceProtection_Nulls,
    SUM(CASE WHEN Tech_Support IS NULL THEN 1 ELSE 0 END) AS TechSupport_Nulls,
    SUM(CASE WHEN Streaming_TV IS NULL THEN 1 ELSE 0 END) AS StreamingTV_Nulls,
    SUM(CASE WHEN Streaming_Movies IS NULL THEN 1 ELSE 0 END) AS StreamingMovies_Nulls,
    SUM(CASE WHEN Contract IS NULL THEN 1 ELSE 0 END) AS Contract_Nulls,
    SUM(CASE WHEN Paperless_Billing IS NULL THEN 1 ELSE 0 END) AS PaperlessBilling_Nulls,
    SUM(CASE WHEN Payment_Method IS NULL THEN 1 ELSE 0 END) AS PaymentMethod_Nulls,
    SUM(CASE WHEN Monthly_Charges IS NULL THEN 1 ELSE 0 END) AS MonthlyCharges_Nulls,
    SUM(CASE WHEN Total_Charges IS NULL THEN 1 ELSE 0 END) AS TotalCharges_Nulls,
    SUM(CASE WHEN Churn_Label IS NULL THEN 1 ELSE 0 END) AS ChurnLabel_Nulls,
    SUM(CASE WHEN Churn_Value IS NULL THEN 1 ELSE 0 END) AS ChurnValue_Nulls,
    SUM(CASE WHEN Churn_Score IS NULL THEN 1 ELSE 0 END) AS ChurnScore_Nulls,
    SUM(CASE WHEN CLTV IS NULL THEN 1 ELSE 0 END) AS CLTV_Nulls,
    SUM(CASE WHEN Churn_Reason IS NULL THEN 1 ELSE 0 END) AS ChurnReason_Nulls
FROM Telco_customer_churn;

SELECT
    COUNT(*) AS Blank_ChurnReason
FROM Telco_customer_churn
WHERE Churn_Reason IS NULL
   OR Churn_Reason = '';


SELECT Churn_Label, COUNT(*) AS Count
FROM Telco_customer_churn
WHERE Churn_Reason IS NULL
GROUP BY Churn_Label;


SELECT DISTINCT Contract
FROM Telco_customer_churn;

SELECT DISTINCT Tech_Support
FROM Telco_customer_churn;


SELECT
MIN(Monthly_Charges),
MAX(Monthly_Charges),
AVG(Monthly_Charges)
FROM Telco_customer_churn;

SELECT *
FROM Telco_customer_churn
WHERE Monthly_Charges < 0;

---- feature Engineering 
ALTER TABLE Telco_customer_churn
ADD churn_flag INT;

UPDATE Telco_customer_churn
SET churn_flag=
CASE
WHEN Churn_Label='Yes' THEN 1
ELSE 0
END;

ALTER TABLE  Telco_customer_churn
ADD tenure_group VARCHAR(20);

UPDATE Telco_customer_churn
SET tenure_group=
CASE
WHEN Tenure_Months <=12 THEN '0-12'
WHEN Tenure_Months <=24 THEN '13-24'
WHEN Tenure_Months <=48 THEN '25-48'
ELSE '48+'
END;

ALTER TABLE Telco_customer_churn
ADD revenue_segment VARCHAR(20);

UPDATE Telco_customer_churn
SET revenue_segment=
CASE
WHEN Monthly_Charges <50 THEN 'Low'
WHEN Monthly_Charges <100 THEN 'Medium'
ELSE 'High'
END;


--overall churn rate 
SELECT
COUNT(*) AS total_customers,
SUM(churn_flag) AS churned_customers,
ROUND(
SUM(churn_flag)*100.0/COUNT(*),
2
) AS churn_rate
FROM Telco_customer_churn

ALTER TABLE Telco_customer_churn
ADD risk_category VARCHAR(20);

UPDATE Telco_customer_churn
SET risk_category =
CASE
    WHEN Churn_Score >= 80 THEN 'High'
    WHEN Churn_Score >= 50 THEN 'Medium'
    ELSE 'Low'
END;


ALTER TABLE Telco_customer_churn
ADD cltv_segment VARCHAR(20);

UPDATE Telco_customer_churn
SET cltv_segment =
CASE
    WHEN CLTV >= 5000 THEN 'High Value'
    WHEN CLTV >= 2500 THEN 'Medium Value'
    ELSE 'Low Value'
END;