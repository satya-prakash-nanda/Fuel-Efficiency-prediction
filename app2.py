import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the saved model pipeline
with open('fuel_efficiency_pipeline.pkl', 'rb') as f:
    model_pipeline = pickle.load(f)

# Create the main app
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a page:", ["Prediction", "Analytics"])

if page == "Prediction":
    st.title("Tractor Fuel and Fuel Efficiency Prediction App")

    implement = st.selectbox("Select Implement", ["Plow", "Harrow", "Rotavator", "Seeder", "Sprayer"])
    load_percentage = st.slider("Load Percentage (%)", 0.0, 100.0, step=0.1)
    speed = st.slider("Speed (km/h)", 2.0, 10.0, step=0.1)
    area_covered = st.number_input("Area Covered (hectares)", 0.5, 5.0, step=0.1)
    hp_of_tractor = st.number_input("Horsepower of Tractor", 30, 100, step=1)
    soil_type = st.selectbox("Soil Type", ["Loamy", "Clay", "Sandy", "Silty"])
    terrain_condition = st.selectbox("Terrain Condition", ["Flat", "Slightly Hilly", "Hilly", "Very Hilly"])

    if implement in ["Plow", "Harrow", "Rotavator"]:
        working_depth = st.slider("Working Depth (cm)", 5.0, 30.0, step=0.1)
        working_width = 0.0
    else:
        working_depth = 0.0
        working_width = st.slider("Working Width (m)", 1.0, 4.0, step=0.1)

    input_data = pd.DataFrame(
        [[implement, load_percentage, speed, area_covered, hp_of_tractor, working_depth, working_width, soil_type,
          terrain_condition]],
        columns=["Implement", "Load_Percentage", "Speed", "Area_Covered", "HP_of_Tractor", "Working_Depth",
                 "Working_Width", "Soil_Type", "Terrain_Condition"]
    )

    if st.button("Predict Fuel Consumption and Efficiency"):
        predicted_fuel_consumed = model_pipeline.predict(input_data)[0]
        fuel_efficiency = predicted_fuel_consumed / input_data["Area_Covered"].values[0]
        st.success(f"Fuel Consumption: {predicted_fuel_consumed:.2f} liters")
        st.success(f"Fuel Efficiency: {fuel_efficiency:.2f} liters per hectare")

elif page == "Analytics":

    # Load the synthetic dataset
    df = pd.read_csv("dataset.csv")  # Update with the correct path to your dataset

    st.title("Tractor Fuel Analytics Dashboard")

    # Sidebar to choose analysis type
    st.header("Fuel Efficiency Analysis")

    # Select an implement
    implement = st.selectbox("Select Implement", ["Plow", "Harrow", "Rotavator", "Seeder", "Sprayer"])

    # Select X-axis feature
    x_axis_feature = st.selectbox("Select X-axis feature", ["Speed", "Load_Percentage", "HP_of_Tractor"])

    # Filter the dataset based on the selected implement
    filtered_df = df[df['Implement'] == implement]

    # Check if there is data to plot
    if not filtered_df.empty:
        # Plotting Fuel Efficiency vs. selected X-axis feature
        plt.figure(figsize=(10, 6))

        sns.lineplot(data=filtered_df, x=x_axis_feature, y='Fuel_Efficiency', marker='o')

        plt.title(f"Fuel Efficiency vs {x_axis_feature} for {implement}")
        plt.xlabel(x_axis_feature)
        plt.ylabel('Fuel Efficiency (liters per hectare)')
        plt.grid()

        st.pyplot(plt)
    else:
        st.warning(f"No data available for the selected Implement: {implement}.")






    # # part2
    #
    # st.title("Tractor Fuel Analytics Dashboard")
    #
    # # Select columns for bivariate analysis
    # x_col = st.selectbox("Select X-axis feature",
    #                      ["Speed", "Load_Percentage", "HP_of_Tractor", "Area_Covered"])
    #
    # y_col = st.selectbox("Select Y-axis feature",
    #                      ["Fuel_Consumed", "Fuel_Efficiency"])
    #
    # # Select a feature for grouping (hue)
    # hue_col = st.selectbox("Select hue (optional)",
    #                        [None, "Implement", "Soil_Type", "Terrain_Condition"], index=0)
    #
    # # Plot the scatterplot or line plot
    # st.subheader(f"{y_col} vs {x_col}")
    #
    # plt.figure(figsize=(8, 5))
    #
    # if hue_col:
    #     sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue_col)
    # else:
    #     sns.scatterplot(data=df, x=x_col, y=y_col)
    #
    # plt.title(f"{y_col} vs {x_col}")
    # st.pyplot(plt)
