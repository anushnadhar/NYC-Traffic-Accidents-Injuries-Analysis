import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import STL
import numpy as np

# --- Configuration ---
# Name of the column to analyze
DATA_COLUMN = 'accidents'
PERIOD = 12 # Monthly data has a period of 12 for yearly seasonality
OUTPUT_CSV_FILE = 'nyc_accidents_seasonally_adjusted.csv' # File to save for Tableau

def load_and_prepare_data(file_path):
    """Loads the CSV, sets the datetime index, and handles potential issues."""
    print(f"Loading data from {file_path}...")
    
    # 1. Load data
    df = pd.read_csv(file_path)
    
    # 2. Convert to datetime and set as index
    df['month'] = pd.to_datetime(df['month'])
    df.set_index('month', inplace=True)
    df.sort_index(inplace=True)
    df = df.asfreq('MS')
    df.fillna(method='ffill', inplace=True) 
    
    return df

def remove_seasonality(df, column_name, period):
    """
    Performs STL decomposition to remove seasonal component.
    """
    print(f"Performing Seasonal Adjustment on '{column_name}'...")
    
    # Drop any leading NaNs resulting from asfreq
    series_to_analyze = df[column_name].dropna() 
  
    stl = STL(series_to_analyze, period=period, seasonal=13)
    result = stl.fit()
    
    # Calculate the Seasonally Adjusted Series (Trend + Residual)
    df[f'{column_name}_adjusted'] = result.trend + result.resid
    
    return df

def plot_comparison(df, raw_col, adjusted_col):
    """Generates the comparison plot: Raw vs. Seasonally Adjusted."""
    print("Plotting comparison chart...")
    
    # Only plot where adjusted data is available
    df_plot = df.dropna(subset=[adjusted_col])
    
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(14, 8))

    # --- Plot Raw Data (Unadjusted/With Seasonality) ---
    ax.plot(df_plot.index, df_plot[raw_col], 
            color='#1f77b4', linewidth=1.5, alpha=0.6, 
            label=f'Raw {raw_col.title()} (With Seasonality)')

    # --- Plot Seasonally Adjusted Data (Clean Trend) ---
    ax.plot(df_plot.index, df_plot[adjusted_col], 
            color='#d62728', linewidth=3.0, 
            label=f'Seasonally Adjusted {raw_col.title()} (Underlying Trend)')

    ax.set_title(f'NYC Car Accidents: Raw vs. Seasonally Adjusted', 
                 fontsize=18, weight='bold', loc='left')
    ax.set_ylabel('Total Accidents', fontsize=14)
    ax.set_xlabel('Year', fontsize=14)
    
    # Add comma formatting to Y axis
    ax.get_yaxis().set_major_formatter(
        plt.FuncFormatter(lambda x, p: format(int(x), ',')))

    ax.legend(loc='upper right', fontsize=12)
    
    plt.tight_layout()
    plt.savefig('nyc_accidents_seasonal_adjustment.png')
    plt.show()

if __name__ == "__main__":
    file_path = 'monthly_metrics.csv'
  
    data_df = load_and_prepare_data(file_path)
   
    data_df = remove_seasonality(data_df, DATA_COLUMN, PERIOD)
   
    adjusted_col_name = f'{DATA_COLUMN}_adjusted'
    plot_comparison(data_df, DATA_COLUMN, adjusted_col_name)
  
    data_df_output = data_df.reset_index()[['month', DATA_COLUMN, adjusted_col_name]]
    data_df_output.to_csv(OUTPUT_CSV_FILE, index=False)
    print(f"\nSUCCESS: Data saved to {OUTPUT_CSV_FILE}")

    print("\nData Snapshot (Head):")
    print(data_df[[DATA_COLUMN, adjusted_col_name]].head())
    print("\nData Snapshot (Tail):")
    print(data_df[[DATA_COLUMN, adjusted_col_name]].tail())