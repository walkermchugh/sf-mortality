import pandas as pd
from datetime import datetime

# Step 1: Read in the CSV file
csv_file_path = 'legislators.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_file_path)

# Step 2: Convert date columns to datetime objects
date_columns = ['DOB', 'Term_start', 'Term_end']

for column in date_columns:
    df[column] = pd.to_datetime(df[column])


# Step 3: Calculate the number of years if 'Term_start' is before March 3, 1791 and 'Type' is 'sen'
def calculate_years(row):
    cutoff_date = datetime(1791, 3, 3)
    if row['Term_start'] < cutoff_date and row['Type'] == 'sen':
        years_difference = (cutoff_date - row['DOB']).days / 365.25  # Consider leap years
        return years_difference
    else:
        return None

df['Years_from_DOB_to_1791'] = df.apply(calculate_years, axis=1)

#Print def
print(df)
