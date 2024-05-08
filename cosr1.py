import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data into a pandas DataFrame
df = pd.read_csv('cosr_dataframe.csv')

# Sort dataframe by time if it's not already sorted
df = df.sort_values(by='Unnamed: 0')

# Initialize variables to keep track of consecutive weeks
prev_sales_emp = None
prev_company = None
consecutive_weeks = 0

# Dictionary to store counts of occurrences for each salesperson and company
consecutive_counts = {}

# Iterate through the dataframe
for index, row in df.iterrows():
    if row['CoSR_weekly'] < 1:
        # Check if it's consecutive weeks
        if row['Sales emp_id'] == prev_sales_emp and row['company_name'] == prev_company:
            consecutive_weeks += 1
        else:
            consecutive_weeks = 1

        # Check if consecutive weeks is 2
        if consecutive_weeks == 2:
            sales_emp_id = row['Sales emp_id']
            company_name = row['company_name']
            if (sales_emp_id, company_name) in consecutive_counts:
                consecutive_counts[(sales_emp_id, company_name)] += 1
            else:
                consecutive_counts[(sales_emp_id, company_name)] = 1

    else:
        consecutive_weeks = 0

    # Update previous sales employee and company
    prev_sales_emp = row['Sales emp_id']
    prev_company = row['company_name']

# Convert the counts dictionary into a DataFrame
consecutive_df = pd.DataFrame(list(consecutive_counts.items()), columns=['Sales emp_id, company_name', 'Count'])

# Convert tuples into strings for x-values
consecutive_df['Sales emp_id, company_name'] = consecutive_df['Sales emp_id, company_name'].apply(lambda x: f"{x[0]}, {x[1]}")

# Set style using seaborn
sns.set_style("whitegrid")

# Plot the results
plt.figure(figsize=(12, 8))
sns.barplot(x='Count', y='Sales emp_id, company_name', data=consecutive_df, palette='viridis')
plt.title('Occurrences of Salespeople and Company Names with CoSR < 1 for Consecutive Two Weeks', fontsize=16)
plt.xlabel('Count', fontsize=14)
plt.ylabel('Sales employee ID, Company Name', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
