# Description: the code takes an Excel workbook with the budget database, creates a new column and
# #              converts the cash value column into its accrual value, placing the value converted
# #              into the newly created column. The conversion is based on the days of payable,
# #              which the user shall define in the code.
#

import openpyxl
import pandas as pd
import numpy as np
import matplotlib
from pandas import pivot_table
import pandas as pd
import numpy as np

# Load the data
file_path = r"C:\Users\asimao\OneDrive\Desktop\Base_Forecast.xlsx"
df = pd.read_excel(file_path)

# Set the currency
currency = "USD"

# Preprocessing
df[currency] = df[currency].fillna(0)

# Group by managing_area and short_description, and pivot the months
pivot_table = df.groupby(['managing_area', 'short_description', 'month'])[currency].sum().unstack(fill_value=0)

# Rename columns to make them more readable
pivot_table.columns = [f"Month_{col}" for col in pivot_table.columns]

# Sort the index
pivot_table = pivot_table.sort_index(level=['managing_area', 'short_description'])

# Identify month columns
month_columns = [col for col in pivot_table.columns if col.startswith('Month_')]

# Calculate column totals (sum of each month)
column_totals = pivot_table[month_columns].sum()

# Correct way to add total row
pivot_table.loc[('Total', 'Total')] = 0  # Initialize with zeros
for col in month_columns:
    pivot_table.loc[('Total', 'Total'), col] = column_totals[col]

# Add a total column (sum of rows)
pivot_table['Total'] = pivot_table[month_columns].sum(axis=1)

# Print the final table
print(pivot_table)

# Export to Excel
out_file = "reconciliacao.xlsx"
pivot_table.to_excel(out_file, sheet_name="Recon Forecast")