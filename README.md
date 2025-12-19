
# Tableau Dashboard for NYC Traffic Accidents Analysis (2013–2025)

## Overview

This project analyzes New York City traffic accidents, injuries, and fatalities from 2013 to 2025 to uncover long-term trends, geographic disparities, and the impact of major policy and behavioral changes such as COVID-19 lockdowns and congestion pricing.
Using SQL, Python, and Tableau, the project focuses on monthly trend analysis, borough-level comparisons, and seasonally adjusted time-series insights to support data-driven road safety and Vision Zero initiatives.

## Objectives

1. Identify long-term trends in traffic accidents, injuries, and fatalities
2. Compare accident patterns across NYC boroughs
3. Assess the impact of traffic reduction policies (COVID-19, congestion pricing)
4. Remove seasonal noise to reveal underlying accident trends
5. Build intuitive dashboards for policymakers and urban planners

## Dataset

Source: NYC Open Data
Time Period: 2013 – 2025
Granularity: Monthly aggregated data

## Tools & Technologies

- SQL (DuckDB) – data ingestion, cleaning, transformations, and aggregations
- Python (Pandas, Statsmodels) – time-series analysis and seasonal adjustment (STL decomposition)
- Tableau – interactive dashboards and visual storytelling

## Data Processing & Methodology

1. Data Cleaning & Transformation

- Raw datasets ingested into DuckDB
- Monthly aggregation of accidents, injuries, and fatalities
- Consistent date handling and borough standardization

2. Time-Series Analysis

- Seasonal adjustment applied using STL decomposition
- Isolation of long-term trends from recurring seasonal patterns
- Year-over-year comparisons to highlight structural changes

3. Visualization & Analysis

- Monthly trend lines
- Borough ranking analysis (bump charts)
- Pre- vs post-policy comparisons
- Heatmaps and KPI summaries

## Overview

# Dashboard 1: NYC Traffic Accidents & Injuries Analysis (2013–2025)

<img width="1638" height="777" alt="image" src="https://github.com/user-attachments/assets/2ae5e5b0-8450-4568-92c0-f24816188b70" />

This first dashboard focuses on understanding the big picture: how NYC traffic accidents, injuries, and fatalities have evolved over the last decade, and whether those changes reflect long-term trends or seasonal effects.
Key insights:
- The monthly trend line from 2013 to 2025 shows a gradual long-term decline in accidents, reasons for which we will see subsequently.
-	To separate real trends from recurring patterns, I applied seasonal adjustment here. This removes predictable seasonal spikes like summer travel or winter driving, and lets us focus on underlying movement.
-	The year-over-year % change chart helps quantify this impact. Instead of just seeing ‘up or down,’ we see how strong each change was, the strongest decline in 2020 and then in 2025.
-	As we select any bar on the YoY% change chart, each bar represents the year from 2013 to 2025 and hence other charts and KPIs dynamically change as per the year selected.

# Dashboard 2: Understanding the Impact: NYC Traffic Injury Trends by User Group

<img width="1633" height="762" alt="image" src="https://github.com/user-attachments/assets/3534d67e-ffc1-4e19-af5c-e5d3a1a5c512" />

The second dashboard shifts focus from how many accidents occur to who is most affected.
Key insights:
- Motorists account for the largest number of injuries, followed by pedestrians and then cyclists
- Same thing depicted by the pie chart showing the percentage of different types of users who got injured that can be filtered by year
- The injury trend lines show that while total injuries declined post-COVID, vulnerable user injuries did not fall at the same rate
- The YoY change chart for vulnerable users is especially important as it shows greater volatility, suggesting these groups are more sensitive to infrastructure and policy changes.
- As we select any year on the line chart, the proportion on the pie chart changes dynamocally showing what percentage of each user groups were injured in that year thus giving a better insights regarding the most vulnerable users.

# Dashboard 3: NYC Traffic Safety Insights: Impact of Weather, Traffic Volume & Congestion Pricing (2013–2025)

<img width="1648" height="781" alt="image" src="https://github.com/user-attachments/assets/ff987610-a251-4881-b113-865dea598f9e" />

This dashboard evaluates what actually drives accidents—behavioral, environmental, and policy factors.
Key insights:
- The strongest relationship we see is between traffic volume and accidents. When volume drops, accidents consistently drop.
- This is clearly visible during COVID-19 lockdowns and again after the introduction of congestion pricing, where reduced traffic coincides with sustained accident reduction.
- In contrast, weather variables like snowfall and precipitation show weak correlation with accident counts.” That can be due to:
   * behavioral adaptation: NYC residents tend to reduce unessetial travel, work from home, or shift to public transportation during severe weather. 
   * Or other reason could be that advance weather warnings, city preparedness (salting, plowing), and cautious driving behavior may mitigate the impact of harsh weather on crash frequency. 
- This challenges common assumptions that weather is a primary driver—data shows traffic exposure matters far more.
- By marking key events directly on the timeline, the dashboard makes causality easier to interpret rather than just correlation.

# Dashboard 4: How NYC Boroughs Compare: Rank Shifts & Geographic Accident Density

<img width="1647" height="777" alt="image" src="https://github.com/user-attachments/assets/8ae94530-f9c9-4ad6-8117-492d424f3ca3" />

The final dashboard answers where accidents are concentrated and how that has changed over time.”
Key insights:
- The bump chart shows ranking shifts across boroughs
- Brooklyn and Queens consistently rank highest, reflecting population density and roadway usage.
- Manhattan shows notable improvement over time, likely influenced by transit usage, and pedestrian-friendly design.
- The geospatial map complements the ranking by showing spatial concentration, helping identify hotspots
- This dashboard supports targeted, borough-specific interventions. Safety solutions shouldn’t be one-size-fits-all—each borough faces different structural challenges.
- A year-wise filter enables deeper drill-down to analyze accident patterns across boroughs and identify major variations in borough rankings. All KPIs update dynamically based on the selected year.

## Conclusion:

This project demonstrates how multi-year traffic data, combined with policy and contextual factors, can provide actionable insights into urban road safety. The findings strongly support traffic reduction strategies as an effective mechanism to reduce accidents and protect vulnerable road users. Continued data-driven monitoring will be essential for achieving NYC’s long-term Vision Zero goals.
