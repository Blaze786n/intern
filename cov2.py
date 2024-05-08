import pandas as pd
import plotly.express as px

# Load data from CSV
df = pd.read_csv('cov_dataframe.csv')

# Convert 'CoV' column to numeric (if it's not already)
df['CoV'] = pd.to_numeric(df['CoV'], errors='coerce')

# Drop rows with missing values in 'CoV' column
df = df.dropna(subset=['CoV'])

# Define color codes based on CoV values and changes over time
def assign_color(cov_prev, cov_current):
    if cov_prev < 50 and 50 <= cov_current < 100:
        return 'red'
    elif cov_prev < 50 and cov_current >= 100:
        return 'lightgreen'
    elif cov_prev < 50 and cov_current >= 150:
        return 'darkgreen'
    elif cov_prev < 50 and cov_current <= 100:
        return 'pink'
    elif cov_prev < 50 and cov_current <= 100:
        return 'darkred'
    else:
        return 'blue'  # default color

# Apply color codes
df['color'] = df.apply(lambda row: assign_color(row['CoV'], row['CoV']), axis=1)

# Create scatter plot
fig = px.scatter(df, x='week', y='CoV', color='color', hover_data=['week'])

# Update layout with title and axis labels
fig.update_layout(title='CoV Over Time',
                  xaxis_title='Week Number',
                  yaxis_title='Coefficient of Variation (CoV)')

# Show plot
fig.show()
