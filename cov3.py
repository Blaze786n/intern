import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data
data = {
    'company_name': ['Company A'] * 10 + ['Company B'] * 10,
    'week': list(range(1, 11)) * 2,
    'CoV': [20, 60, 80, 110, 130, 40, 30, 20, 50, 90] * 2
}

# Create DataFrame
df = pd.DataFrame(data)

# Function to assign color based on CoV values
def assign_color(cov_prev, cov_current):
    # Check if either cov_prev or cov_current is NaN
    if pd.isna(cov_prev) or pd.isna(cov_current):
        return 'blue'  # default color
    
    # Check conditions for assigning colors
    conditions = [
        ((cov_prev < 50) & (50 <= cov_current) & (cov_current < 100)),
        ((cov_prev < 50) & (cov_current >= 100)),
        ((cov_prev < 50) & (cov_current >= 150)),
        ((cov_prev < 50) & (cov_current <= 100)),
        ((cov_prev < 50) & (cov_current <= 100)),
    ]
    colors = ['red', 'lightgreen', 'darkgreen', 'pink', 'darkred']
    
    # Apply conditions to assign colors
    return np.select(conditions, colors, default='blue')

# Apply color assignment to DataFrame
df['color'] = df.groupby('company_name').apply(lambda x: assign_color(x['CoV'].shift(1), x['CoV'])).reset_index(drop=True)

# Plotting function
def plot_company(company):
    company_df = df[df['company_name'] == company]
    
    plt.figure(figsize=(10, 6))
    plt.scatter(company_df['week'], company_df['CoV'], c=company_df['color'], alpha=0.7)
    plt.title(f'Coefficient of Variation (CoV) for {company}')
    plt.xlabel('Week')
    plt.ylabel('CoV')
    plt.grid(True)
    plt.show()

# Interactive dropdown menu for selecting company
def dropdown_event_handler(change):
    plot_company(change.new)

dropdown = widgets.Dropdown(options=df['company_name'].unique(), description='Company:')
dropdown.observe(dropdown_event_handler, names='value')

display(dropdown)
