import pandas as pd
import matplotlib.pyplot as plt

# Example data
data = {
    'Customer_Type': ['New Customers', 'Repeat Customers', 'Loyal Customers', 'Churned Customers', 
                      'High-Value Customers', 'Low-Value Customers', 'Segmented Customers', 
                      'Corporate Customers vs. Individual Customers'],
    'Average_Count': [100, 150, 200, 50, 80, 30, 120, 90]
}

# Creating DataFrame
customer_data = pd.DataFrame(data)

# Visualizing the data
plt.figure(figsize=(10, 6))
plt.barh(customer_data['Customer_Type'], customer_data['Average_Count'], color='skyblue')
plt.xlabel('Average Count')
plt.ylabel('Customer Type')
plt.title('Average Number of Customers by Type')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
