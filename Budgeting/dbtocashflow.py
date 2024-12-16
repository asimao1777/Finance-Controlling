# Description: the code takes an Excel workbook with the budget database, creates a new column and
# #              converts the cash value column into its accrual value, placing the value converted
# #              into the newly created column. The conversion is based on the days of payable,
# #              which the user shall define in the code.
#

import pandas as pd

# Load the data
file_path = r"C:\Users\asimao\OneDrive\Desktop\Base_Forecast.xlsx"
workbook = pd.ExcelFile(file_path)

# Parse the "DB" sheet
df = workbook.parse("DB")
print("Columns in the dataset:", df.columns)

# Ensure necessary columns exist and fix column names if required
required_columns = ['unit', 'cost_account', 'cost_center', 'short_description', 'month', 'USD']
for col in required_columns:
    if col not in df.columns:
        raise KeyError(f"Required column '{col}' is missing from the data!")

# Preprocessing: fill missing currency values
df['USD'] = df['USD'].fillna(0)

# Group by and pivot the data
pivot_data = (
    df.groupby(['unit', 'cost_center', 'cost_account', 'short_description', 'month'])['USD']
    .sum()
    .unstack(fill_value=0)
)

# Rename columns to make them more readable
pivot_data.columns = [f"Month_{col}" for col in pivot_data.columns]

# Sort the index
pivot_data = pivot_data.sort_index(level=['unit','cost_account', 'short_description'])

# Identify month columns
month_columns = [col for col in pivot_data.columns if col.startswith('Month_')]

# Calculate column totals (sum of each month)
column_totals = pivot_data[month_columns].sum()

# Add total row safely
pivot_data.loc[('Total', 'Total', 'Total', 'Total')] = 0  # Add a total row with placeholder levels
for col in month_columns:
    pivot_data.loc[('Total', 'Total', 'Total', 'Total'), col] = column_totals[col]

# Add a total column (sum of rows)
pivot_data['Total'] = pivot_data[month_columns].sum(axis=1)

# Print the final table
print(pivot_data)

# Export to Excel
out_file = "cashflow_forecast.xlsx"
pivot_data.to_excel(out_file, sheet_name="Recon Forecast")
