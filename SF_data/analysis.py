import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file from the URL
url = "https://github.com/walkermchugh/giantkiller/raw/main/SF_data/raw_dat.csv"
df = pd.read_csv(url)

# Step 2: Convert the first row from DD/MM/YYYY to YYYY-MM-DD datetime
df.iloc[0] = pd.to_datetime(df.iloc[0], format='%d/%m/%Y')

# Step 3: Calculate 'Cumulative Drug Overdose Deaths'
df.iloc[1] = df.iloc[1].cumsum()

# Step 4: Calculate 'Cumulative CoV-19 Deaths'
df.iloc[2] = df.iloc[2].cumsum()

# Step 5: Plot lineplot of 'Cumulative Drug Overdose Deaths' and 'Cumulative CoV-19 Deaths'
plt.figure(figsize=(10, 6))
plt.plot(df.columns, df.iloc[1], label='Cumulative Drug Overdose Deaths', marker='o')
plt.plot(df.columns, df.iloc[2], label='Cumulative CoV-19 Deaths', marker='o')
plt.xlabel('Date')
plt.ylabel('Cumulative Deaths')
plt.title('Cumulative Drug Overdose Deaths vs. Cumulative CoV-19 Deaths')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Display the plot (optional)
plt.show()
