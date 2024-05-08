import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

# Load the data
data = {
    'company_name': ['8a80815e8bb379c3018bb3c6a0870001', '8a8081908c2eefef018c587620500116', '8a80875a8d18d498018d1b2b82be0016', 
                     '8a8089b48d31f3ea018d693c3ff60231', '8a80973f8a9cb965018aa2f795720009', '8a80973f8a9cb965018aa3173466005d', 
                     '8a809b238df5d3a0018dfe18fca00053', '8a809b238df5d3a0018e3cd1fbfb03de', '8a809b238df5d3a0018e5fe356bf05da'],
    'Year': [2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024],
    'Month': [1, 2, 3, 4, 1, 2, 3, 4, 1],
    'Proportion_New_Customers': [1.0, 1.0, 1.0, 1.0, 0.904762, 0.857143, 1.0, 1.0, 1.0]
}

df = pd.DataFrame(data)

# Convert Month and Year to datetime format
df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(day=1))

# Filter data for the last observed month
last_month_data = df[df['Date'] == df['Date'].max()]

# Fit exponential smoothing model
model = SimpleExpSmoothing(last_month_data['Proportion_New_Customers'])
fit_model = model.fit()

# Forecast for the next month
forecast_next_month = fit_model.forecast(1)

print("Forecast for next month's proportion of repeat customers:", forecast_next_month.iloc[0])

# Salesperson's performance across locations
locations = ['Location A', 'Location B', 'Location C']  # Assuming there are 3 locations
performance_ratios = [0.33, 0.45, 0.28]  # Performance ratios for each location

# Calculate the harmonic mean
harmonic_mean = len(locations) / sum(1 / ratio for ratio in performance_ratios)

print("Harmonic mean of salesperson's performance across locations:", harmonic_mean)

# Plot the time series
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(last_month_data['Date'], last_month_data['Proportion_New_Customers'], marker='o')
plt.title('Proportion of New Customers Over Time')
plt.xlabel('Date')
plt.ylabel('Proportion of New Customers')
plt.xticks(rotation=45)

# Salesperson's performance
plt.subplot(1, 2, 2)
plt.bar(locations, performance_ratios, color='skyblue')
plt.axhline(y=harmonic_mean, color='red', linestyle='--', label='Salesperson Performance')
plt.title("Salesperson's Performance Across Locations")
plt.xlabel('Location')
plt.ylabel('Performance Ratio')
plt.legend()
plt.tight_layout()
plt.show()
