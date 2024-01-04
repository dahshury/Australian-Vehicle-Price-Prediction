import streamlit as st
import numpy as np
import pandas as pd
from mlAusCar.pipeline.prediction import PredictionPipeline
from mlAusCar.utils.common import filter_choices

st.write("<h1 style='text-align: center';>Australian Car Price Prediction</h1>", unsafe_allow_html=True)

st.image("./static/assets/img/img.jpeg",use_column_width=True)  # Display image in the column

columns=['Brand', 'Model', 'Body Type', 'Drive Type', 'Fuel Type', 'Transmission Type', 'Number of cylinders', 'Fuel Consumption(L/100km)', 'Displacement (L)', 'State', 'Condition', 'Drived Kilometers', 'Year of Manufacture']
actual_col_names=['Brand', 'Model', 'BodyType', 'DriveType', 'FuelType', 'Transmission', 'CylindersinEngine', 'FuelConsumption(L)/100km', 'EngineDisplacement(L)', 'State', 'UsedOrNew', 'Kilometers', 'Year']
filters={}

fixed_selection_cols = ["Brand", "UsedOrNew", "State"]
input_columns=["Kilometers", "Year"]

# Predict function
def predict(filters):
    try:
        formatted_dict = {key: [value] for key, value in filters.items()}
        data = pd.DataFrame(formatted_dict)
        # return data
        obj = PredictionPipeline(model_path='XG Boost model.pkl')
        prediction = obj.predict(data)
        formatted_price = "${:,.0f}".format(np.exp(prediction[0]))
        predicted_text = f"The predicted price is <span style='color: gold;'>{formatted_price}</span> AUD"
        st.markdown(f"<p style='font-size:30px; text-align:center;'>{predicted_text}</p>", unsafe_allow_html=True)
    except Exception as e:
        raise e
    
# Form input data
with st.form("Please fill/select the data"):
    col1,col2,col3=st.columns(3)
    form_cols = [col1,col2,col3]
    for i, col in enumerate(columns):
        options=filter_choices(filters)
        fixed_options=filter_choices({})
        if actual_col_names[i] in fixed_selection_cols:
            filters[actual_col_names[i]]=form_cols[i%3].selectbox(f"Select {col}", options=fixed_options[actual_col_names[i]])
        
        elif actual_col_names[i] in input_columns:
            if actual_col_names[i] =="Year":
                filters[actual_col_names[i]]=form_cols[i%3].number_input(f"Type the {col}", min_value=1900, max_value=2022, step=1)
            else:
                filters[actual_col_names[i]]=form_cols[i%3].number_input(f"Type the {col}", step=1)
        else:
            filters[actual_col_names[i]]=form_cols[i%3].selectbox(f"Select {col}", options=options["choices"][actual_col_names[i]])
        
    btn=st.form_submit_button("Predict")
if btn:
    predict(filters)