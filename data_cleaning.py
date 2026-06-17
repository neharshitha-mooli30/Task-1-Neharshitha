import pandas as pd
# Load dataset
df = pd.read_excel("Dataset for Data Analytics.xlsx")
print("Dataset loaded successfully")
# Show first rows
print(df.head())
# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Remove missing values
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")
# Check duplicates
print("\nDuplicate rows:")
print(df.duplicated().sum())
# Remove duplicates
df.drop_duplicates(inplace=True)
# Clean text columns
for col in df.select_dtypes(include="str").columns:
    df[col] = df[col].str.strip()
    df[col] = df[col].str.title()
# Convert date columns
for col in df.columns:
    if "date" in col.lower():
        df[col] = pd.to_datetime(df[col], errors="coerce")
# Save cleaned file
df.to_excel("Cleaned_Dataset.xlsx", index=False)
print("\nCleaning Completed Successfully")