import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data (replace with your actual dataset)
sales_data = pd.DataFrame({
    'CustomerID': [1, 2, 3, 1, 4, 2, 3, 5, 1, 2],
    'PurchaseAmount': [100, 150, 200, 120, 80, 170, 190, 220, 130, 160],
    'PurchaseDate': ['2024-01-01', '2024-01-05', '2024-01-10', '2024-02-02', '2024-02-05', '2024-03-01', '2024-03-10', '2024-04-02', '2024-04-05', '2024-04-10']
})

# Convert PurchaseDate to datetime
sales_data['PurchaseDate'] = pd.to_datetime(sales_data['PurchaseDate'])

# Sidebar title
st.sidebar.title('Sales Dashboard')

# Sidebar options
analysis_option = st.sidebar.selectbox('Select Analysis', ('Sales Trend', 'Customer Loyalty', 'Repeat Purchase Analysis'))

if analysis_option == 'Sales Trend':
    # Sales trend over time
    sales_data['MonthYear'] = sales_data['PurchaseDate'].dt.to_period('M')
    monthly_sales = sales_data.groupby('MonthYear')['PurchaseAmount'].sum()

    # Plotting sales trend
    st.header('Sales Trend Over Time')
    st.line_chart(monthly_sales)

elif analysis_option == 'Customer Loyalty':
    # Customer loyalty
    loyalty_data = sales_data.drop_duplicates(subset='CustomerID')
    loyalty_data['JoinMonth'] = loyalty_data['PurchaseDate'].dt.to_period('M')
    loyalty_counts = loyalty_data.groupby('JoinMonth')['CustomerID'].count()

    # Plotting customer loyalty
    st.header('Customer Loyalty Over Time')
    st.line_chart(loyalty_counts)

elif analysis_option == 'Repeat Purchase Analysis':
    # Repeat purchase analysis
    repeat_purchase_intervals = sales_data.sort_values(by=['CustomerID', 'PurchaseDate']).groupby('CustomerID')['PurchaseDate'].diff()
    repeat_purchase_intervals = repeat_purchase_intervals.dropna().dt.days

    # Plotting repeat purchase intervals
    st.header('Repeat Purchase Analysis')
    st.pyplot(plt.hist(repeat_purchase_intervals, bins=20, color='r', edgecolor='k', alpha=0.7))
