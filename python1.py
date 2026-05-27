import pandas as pd

# Read dataset
df = pd.read_csv("employee_data.csv")

print("ORIGINAL DATA")
print(df)

# Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Fill missing Age
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Remove duplicate rows
df = df.drop_duplicates()

# Find duplicate IDs
duplicate_ids = df[df.duplicated('ID')]

print("\nDUPLICATE IDs")
print(duplicate_ids)

# Remove duplicate IDs
df = df.drop_duplicates(subset='ID')

# Fix date format
df['Joining_Date'] = pd.to_datetime(
    df['Joining_Date'],
    dayfirst=True,
    errors='coerce'
)

# Find wrong dates
invalid_dates = df[df['Joining_Date'].isnull()]

print("\nINVALID DATES")
print(invalid_dates)

# Remove wrong dates
df = df.dropna(subset=['Joining_Date'])

# Convert date format
df['Joining_Date'] = df['Joining_Date'].dt.strftime('%Y-%m-%d')

print("\nCLEANED DATA")
print(df)

# Save cleaned data
df.to_csv("cleaned_employee_data.csv", index=False)

print("\nPROJECT COMPLETED")