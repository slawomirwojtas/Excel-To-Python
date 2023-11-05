# IMPORT NECESSARY LIBRARIES
import pandas as pd


# LOADING DATAFRAMES

df_ee = pd.read_csv('vlookup_employee.csv')
print(df_ee.head().to_string())
print(df_ee.shape)

df_dep = pd.read_csv('vlookup_departments.csv')
df_dep.drop_duplicates(keep='first', inplace=True) # REMOVE DUPLICATE RECORDS
#df_dep = df_dep.drop_duplicates(keep='first', inplace=False) # THE ALTERNATE WAY
print(df_dep.to_string())
print(df_dep.shape)

df_ins = pd.read_csv('vlookup_insurance.csv')
print(df_ins.head().to_string())
print(df_ins.shape)


# FIRST VLOOKUP: DEPARTMENT CITY

#df = df_ee.merge(df_dep, how='left', left_on='department_id', right_on='department_id').drop(columns=['department_name', 'department_address']) # JOIN THE WHOLE TABLEs AND THEN REMOVE EXTRA COLUMNS
df = df_ee.merge(df_dep[['department_id', 'city']], how='left', left_on='department_id', right_on='department_id') # SELECT PROPER COLUMNS BEFORE JOINING TABLES
print(df.head().to_string())
print(df.shape)


# SECOND VLOOKUP: INSURANCE NUMBER

#df = df.merge(df_ins, how='left', left_on=['first_name', 'last_name'], right_on=['First Name', 'Last Name']).drop(columns=['First Name', 'Last Name']) # JOIN THE WHOLE TABLEs AND THEN REMOVE EXTRA COLUMNS
df_ins.rename(columns={'First Name': 'first_name', 'Last Name': 'last_name', 'Insurance Number': 'insurance_number'}, inplace=True) # CHANGE THE COLUMN LABELS BEFORE JOINING
df = df.merge(df_ins, how='left', left_on=['first_name', 'last_name'], right_on=['first_name', 'last_name'])
print(df.head().to_string())
print(df.shape)

df.to_clipboard()