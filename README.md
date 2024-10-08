# Data Analysis and Visualization Projects

## Overview

This repository contains multiple data analysis and visualization projects. The projects involve working with medical examination data, demographic data, time series data, and sea level change data. The tasks include data cleaning, transformation, visualization, and statistical analysis.

## Project 1: Medical Examination Data Analysis

### Description

This project focuses on visualizing and performing calculations on medical examination data. The dataset contains information about patients, including body measurements, blood test results, and lifestyle choices.

### Dataset

- **File Name:** `medical_examination.csv`
- **Description:** Contains patient data collected during medical examinations.

### Features

| Feature | Variable Type | Value Type |
|---------|---------------|------------|
| Age | Objective Feature | int (days) |
| Height | Objective Feature | int (cm) |
| Weight | Objective Feature | float (kg) |
| Gender | Objective Feature | categorical code |
| Systolic blood pressure | Examination Feature | int |
| Diastolic blood pressure | Examination Feature | int |
| Cholesterol | Examination Feature | 1: normal, 2: above normal, 3: well above normal |
| Glucose | Examination Feature | 1: normal, 2: above normal, 3: well above normal |
| Smoking | Subjective Feature | binary |
| Alcohol intake | Subjective Feature | binary |
| Physical activity | Subjective Feature | binary |
| Presence or absence of cardiovascular disease | Target Variable | binary |

### Tasks

1. **Visualization:**
   - Create a chart showing the counts of good and bad outcomes for cholesterol, gluc, alco, active, and smoke variables for patients with cardio=1 and cardio=0 in different panels.

2. **Data Processing:**
   - Add an `overweight` column based on BMI.
   - Normalize the data for cholesterol and glucose.
   - Convert data into long format and create a chart using seaborn's `catplot()`.
   - Clean the data by filtering out incorrect entries.
   - Create and plot a correlation matrix using seaborn's `heatmap()`.

## Project 2: Demographic Data Analysis

### Description

Analyze demographic data extracted from the 1994 Census database using Pandas. The goal is to answer various questions about the dataset.

### Dataset

- **Description:** Contains demographic data with features like age, workclass, education, and salary.

### Tasks

1. **Data Analysis:**
   - Determine the number of people of each race.
   - Calculate the average age of men.
   - Find the percentage of people with a Bachelor's degree.
   - Calculate the percentage of people with advanced education making more than 50K.
   - Calculate the percentage of people without advanced education making more than 50K.
   - Determine the minimum number of hours worked per week.
   - Find the percentage of people working the minimum number of hours who earn more than 50K.
   - Identify the country with the highest percentage of people earning >50K.
   - Determine the most popular occupation for those earning >50K in India.

## Project 3: Time Series Data Visualization

### Description

Visualize time series data to understand visit patterns and identify growth trends on the freeCodeCamp.org forum.

### Dataset

- **File Name:** `fcc-forum-pageviews.csv`
- **Description:** Contains daily page views data from 2016-05-09 to 2019-12-03.

### Tasks

1. **Data Cleaning:**
   - Import the data and filter out outliers in page views.

2. **Visualization:**
   - Create a line chart of daily page views.
   - Draw a bar chart showing average daily page views for each month, grouped by year.
   - Create box plots to show the distribution of page views by year and month.

## Project 4: Sea Level Change Analysis

### Description

Analyze and predict sea level changes using historical data. The goal is to visualize sea level changes and make predictions up to the year 2050.

### Dataset

- **File Name:** `epa-sea-level.csv`
- **Description:** Contains data on global average sea level changes since 1880.

### Tasks

1. **Data Analysis:**
   - Import the data and create a scatter plot of sea level vs. year.
   - Fit and plot a line of best fit for the entire dataset and for the period from 2000 to the most recent year.
   - Predict sea level changes up to the year 2050.

## Files

- `medical_data_visualizer.py`: Contains code for analyzing and visualizing medical examination data.
- `demographic_data_analyzer.py`: Contains code for analyzing demographic data.
- `fcc_forum_pageviews_visualizer.py`: Contains code for visualizing time series data.
- `sea_level_predictor.py`: Contains code for predicting sea level changes.

## Dependencies

- pandas
- matplotlib
- seaborn
- scipy

## Usage

1. Clone the repository:
   ```bash
   git clone <https://github.com/Sou7ai1/Python>

2. Navigate to the project directory:
    ```bash
    cd <Python>

3. Install dependencies:
    ```bash
    pip install pandas matplotlib seaborn scipy

4. Run The Scripts.
