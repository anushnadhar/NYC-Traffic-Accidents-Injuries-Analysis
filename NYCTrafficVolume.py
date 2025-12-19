# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 13:00:42 2025

@author: anush
"""

import pandas as pd

df = pd.read_csv('Automated_Traffic_Volume_Counts.csv', low_memory=False)

# Clean volume
df['Vol_clean'] = (
    df['Vol']
    .astype(str)
    .str.replace(',', '', regex=False)
)
df['Vol_clean'] = pd.to_numeric(df['Vol_clean'], errors='coerce')

# Build datetime
df['datetime'] = pd.to_datetime(
    df[['Yr', 'M', 'D', 'HH', 'MM']].rename(
        columns={'Yr':'year','M':'month','D':'day','HH':'hour','MM':'minute'}
    ),
    errors='coerce'
)

df = df.dropna(subset=['datetime'])

# Monthly aggregation
monthly = (
    df
    .groupby(df['datetime'].dt.to_period('M'))['Vol_clean']
    .sum()
    .reset_index()
)

monthly['month'] = monthly['datetime'].dt.to_timestamp()
monthly = monthly[['month', 'Vol_clean']].rename(columns={'Vol_clean':'total_volume'})

monthly.to_csv('NYC_monthly_traffic_volume.csv', index=False)
