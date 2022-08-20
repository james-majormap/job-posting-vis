import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.offline as pyo


st.title('채용공고 자연어 분석')


@st.cache
def load_data():
    data = pd.read_csv('gs://majormap-public-data/job_postings_umap_data.csv')
    return data


data_load_state = st.text('Loading data...')
data = load_data()




pyo.init_notebook_mode()


fig = px.scatter(
    data,
    x='x',
    y='y',
    hover_name='name',
    color='category',
    width=800,
    height=600,
)

st.write(fig)
