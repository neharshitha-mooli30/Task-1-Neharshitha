# Data Analytics Project 1 - Data Cleaning & Preparation

## Project Overview

This project focuses on cleaning and preparing a raw e-commerce dataset using Python and Pandas.

## Objectives

* Identify missing values
* Handle missing data
* Check and remove duplicate records
* Standardize text formatting
* Validate date formats
* Generate a clean dataset for further analysis

## Tools Used

* Python
* Pandas
* OpenPyXL
* VS Code

## Dataset Information

The dataset contains e-commerce order information including:

* Order ID
* Customer ID
* Product Details
* Quantity
* Unit Price
* Payment Method
* Order Status
* Coupon Code
* Referral Source
* Total Price

## Data Cleaning Steps Performed

### 1. Missing Value Analysis

Checked all columns for missing values using:

```python
df.isnull().sum()
```

Result:

* CouponCode column contained 309 missing values.

### 2. Missing Value Handling

Replaced missing CouponCode values with "No Coupon".

### 3. Duplicate Record Check

Checked for duplicate records using:

```python
df.duplicated().sum()
```

Result:

* No duplicate rows found.

### 4. Text Cleaning

* Removed extra spaces
* Standardized text formatting

### 5. Date Validation

Converted date columns into proper datetime format.

### 6. Export Cleaned Dataset

Saved the cleaned dataset as:

Cleaned_Dataset.xlsx

## Project Outcome

Successfully cleaned the dataset and prepared it for further analysis while maintaining data integrity.

## Author

Neharshitha Mooli
B.Tech ECE Student
Aspiring Data Analyst
