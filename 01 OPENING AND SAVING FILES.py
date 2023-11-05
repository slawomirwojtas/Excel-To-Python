# import necessary libraries
import pandas as pd

# OPENING FILES

# open file with specific columns and narrow down to the first two rows only
df = pd.read_csv('employee_data.csv', usecols=['first_name', 'last_name'], nrows=2)
print(df.head().to_string())

# open file with no column labels and add them
df = pd.read_csv('employee_data - no headers.csv', header=None)
df.columns = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8']
print(df.head().to_string())

# open excel file, skip the first and last rows
df = pd.read_excel('employee_data.xlsx', sheet_name='dummy_data', skiprows=1, skipfooter=1)
print(df.head(10).to_string())


# SAVING FILES

# save part of the file and then add another part to it
df[:1].to_csv('output_file1.csv', index=False, mode='w')
df[1:2].to_csv('output_file1.csv', index=False, mode='a', header=False)


# save two tables in separate sheets of the same spreadsheet
with pd.ExcelWriter('output_file2.xlsx', engine='openpyxl', mode='w') as writer:
    df[:1].to_excel(writer, sheet_name='row1', index=False)
with pd.ExcelWriter('output_file2.xlsx', engine='openpyxl', mode='a') as writer:
    df[1:2].to_excel(writer, sheet_name='row2', index=False)