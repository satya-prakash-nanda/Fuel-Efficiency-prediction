# Fuel-Efficiency-prediction


## Tractor Fuel Efficiency Prediction Model 🚜

## Overview

This project aims to predict the fuel consumption and fuel efficiency of tractors using various parameters such as load percentage, speed, area covered, horsepower, soil type, and terrain conditions. A machine learning model is built, evaluated, and deployed as a web application using Streamlit to make predictions accessible and user-friendly.



## Features
Synthetic Dataset Generation: Generates random samples with parameters like implement type, speed, load, and horsepower.

Outlier Detection and Removal: Uses the IQR method to ensure clean and accurate data.

Machine Learning Model: Trained on Random Forest and other algorithms to predict fuel efficiency.

Web Application: Users can interactively input tractor parameters to get predictions for fuel consumption and efficiency.

Analytics Dashboard: Visualizations to analyze trends and insights from the dataset.


## Project Workflow
1. Dataset Collection and Generation

A synthetic dataset was created with parameters such as tractor horsepower, implement type, load percentage, soil type, terrain condition, speed, area covered, and working depth/width.
The dataset simulates real-world conditions, introducing variability and noise to reflect operational scenarios.

2. Outlier Detection and Removal

The IQR (Interquartile Range) method was used to remove outliers in the Fuel_Efficiency feature.
Outliers beyond 1.5 * IQR were identified and removed to enhance model accuracy.

3. Building the Pipeline

A Scikit-Learn pipeline was used to:
Preprocess the data (scaling and encoding categorical variables).
Select and train the model.
The pipeline ensures consistent data handling across all stages of the project.

4. Model Training and Selection

Several machine learning algorithms were evaluated, including Linear Regression, Random Forest Regressor, and XGBoost.
The Random Forest Regressor was selected for deployment due to:
High accuracy
Robustness to noise and non-linear data patterns
Superior performance with encoded categorical features

6. Web Application using Streamlit

A Streamlit-based web application was developed with two main pages:
Prediction Page: Takes user inputs (load, speed, area, HP, soil type, terrain) and provides fuel consumption and efficiency predictions.
Analytics Page: Offers data visualizations to explore trends and insights.



## Results and Evaluation

Random Forest Regressor achieved the best performance:

R² Score: 0.91

Mean Squared Error (MSE): 1.23

Mean Absolute Error (MAE): 0.87

The model was saved as a pickle file for easy integration into the web app.

