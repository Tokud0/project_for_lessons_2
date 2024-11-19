import streamlit as st
import pandas as pd
import numpy as np
class Project1:
    def __init__(self):
        pass
    def app(self):
        st.write("Creation of DataFrame")

        def load_data(file):
            if file is not None:
                data = pd.read_csv(file)
                return data
            return None

        upload = st.file_uploader("Choose a CSV file")
        if upload is not None:
            df = load_data(upload)
            st.dataframe(df, height=400, width=600)

            column = st.selectbox("Choose column for filter", df.columns)

            if column:

                unique_values = df[column].unique()
                selected_levels = st.multiselect("Select Stress Level(s)", options=unique_values, default=unique_values)

                filtered_df = df[df[column].isin(selected_levels)]
                st.dataframe(filtered_df, height=400, width=600)
        else:
            st.write("Please upload a CSV file")

        st.markdown("""<style>
        h1 {
        color: green;
        font-size: 18px;
        text-align: center;
        }
        </style>""", unsafe_allow_html=True)