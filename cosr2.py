import pandas as pd
import plotly.express as px

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

# Create a dropdown list for selecting between Sales man name and company name
dropdown_options = [{'label': 'Salesman Name', 'value': 'Sales emp_id'}, {'label': 'Company Name', 'value': 'company_name'}]

# Plot the results using Plotly Express
fig = px.bar(consecutive_df, x='Count', y='Sales emp_id, company_name', orientation='h', 
             title='Occurrences of Salespeople and Company Names with CoSR < 1 for Consecutive Two Weeks',
             labels={'Count': 'Count', 'Sales emp_id, company_name': 'Sales employee ID, Company Name'})
fig.update_layout(xaxis_title='Count', yaxis_title='Sales employee ID, Company Name', 
                  xaxis=dict(title_font=dict(size=14)), yaxis=dict(title_font=dict(size=14)),
                  font=dict(size=12), plot_bgcolor='rgba(0,0,0,0)')
fig.update_traces(marker_color='red', selector={'type':'bar'})
fig.add_hline(y=1, line=dict(color='lightgreen', width=3, dash='dot'), annotation_text='CoSR=1',
              annotation_position="bottom right")
fig.update_traces(marker_color='green', selector={'type':'bar'})
fig.update_yaxes(categoryorder='total ascending')
fig.show()
