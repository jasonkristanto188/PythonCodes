import pandas as pd

# Load the Excel file
df = pd.read_excel("file.xlsx")

# Pivot the DataFrame
pivot_df = df.pivot_table(index=['a', 'b'], columns=['c', 'd'], values='e', aggfunc='sum')

# Print the pivoted DataFrame
print(pivot_df)

