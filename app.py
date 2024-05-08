from flask import Flask, render_template, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

app = Flask(__name__)

# Load data
cosr_data = pd.read_csv("cosr_dataframe.csv")
cov_data = pd.read_csv("cov_dataframe.csv")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cosr_data')
def get_cosr_data():
    # Process CoSR data
    salesman_data = cosr_data.groupby("Sales emp_id")["CoSR_weekly"].mean()
    cosr_plot_data = {
        "x": salesman_data.index.tolist(),
        "y": salesman_data.values.tolist()
    }
    return jsonify(cosr_plot_data)

@app.route('/cov_data')
def get_cov_data():
    # Process CoV data
    df = cov_data.dropna(subset=['CoV'])  # Drop NaN values
    df['CoV'] = pd.to_numeric(df['CoV'], errors='coerce')  # Convert 'CoV' column to numeric
    # Plotly scatter plot
    fig = px.scatter(df, x='week', y='CoV', color='color', hover_data=['week'])
    cov_plot_div = fig.to_html(full_html=False, include_plotlyjs='cdn')
    return cov_plot_div

if __name__ == '__main__':
    app.run(debug=True)
