import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("cosr_dataframe.csv")  # Replace "your_data.csv" with the actual filename

# Assuming CoSR_weekly column contains CoSR values

# Function to plot CoSR
def plot_CoSR(selection):
    plt.figure(figsize=(10, 6))
    
    # Plot CoSR for the selected option
    if selection == "Salesman":
        # Plot CoSR for each salesman
        # Replace "Sales emp_id" with the actual column name for Salesman ID
        # Replace "CoSR_weekly" with the actual column name for CoSR
        salesman_data = data.groupby("Sales emp_id")["CoSR_weekly"].mean()
        plt.bar(salesman_data.index, salesman_data.values, color="skyblue")
        plt.xticks(rotation=45, ha='right')
        plt.xlabel("Salesman ID")
        plt.ylabel("CoSR")
    elif selection == "Company":
        # Plot CoSR for each company
        # Replace "company_name" with the actual column name for Company Name
        company_data = data.groupby("company_name")["CoSR_weekly"].mean()
        plt.bar(company_data.index, company_data.values, color="skyblue")
        plt.xticks(rotation=45, ha='right')
        plt.xlabel("Company Name")
        plt.ylabel("CoSR")
    
    # Add a horizontal line at CoSR = 1
    plt.axhline(y=1, color="lightgreen", linestyle="--", linewidth=2)
    
    # Color bars based on CoSR value
    bars = plt.gca().patches
    for bar in bars:
        if bar.get_height() > 1:
            bar.set_color('green')
        else:
            bar.set_color('red')
    
    plt.title("CoSR Plot")
    plt.tight_layout()
    plt.show()

# Plot CoSR for Salesman or Company
plot_CoSR("Company")  # Replace "Company" with "Salesman" to plot for Salesman
