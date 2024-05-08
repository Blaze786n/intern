import matplotlib.pyplot as plt
import pandas as pd
import ipywidgets as widgets

# Load data from CSV
df = pd.read_csv('cov_dataframe.csv')

# Function to update scatter plot based on selected company name
def update_plot(company_name):
    plt.cla()
    plt.xlabel('Week Number')
    plt.ylabel('Coefficient of Variation (CoV)')
    plt.title(f'CoV Over Time for {company_name}')

    # Filter data for the selected company name
    selected_data = df[df['company_name'] == company_name]

    # Plot scatter plot
    plt.scatter(selected_data['week'], selected_data['CoV'], label=company_name)
    plt.legend()

# Get unique company names
unique_company_names = df['company_name'].unique().tolist()

# Create dropdown menu
dropdown = widgets.Dropdown(options=unique_company_names, description='Select Company')

# Define dropdown menu callback function
def dropdown_callback(change):
    update_plot(change.new)

dropdown.observe(dropdown_callback, names='value')

# Text input for custom company name
text_input = widgets.Text(description='Enter Company:', value=unique_company_names[0])

# Define text input callback function
def text_input_callback(change):
    update_plot(change.new)

text_input.observe(text_input_callback, names='value')

# Display widgets
widgets.VBox([dropdown, text_input])

# Initial plot with the first company
update_plot(unique_company_names[0])

plt.show()
