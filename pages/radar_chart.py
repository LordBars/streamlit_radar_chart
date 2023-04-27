import streamlit as st
import plotly.express as px
import pandas as pd

def radar_chart(val1, val2, val3, val4, val5):
    data = {
        "r": [val1,
           val2,
           val3, 
           val4, 
           val5,
           ],
        "theta": ["sDa(%)", "ASE(%)", "ED Gross(kWh/m2)", "PV Production(kWh/m2)", "Net Energy(kWh/m2)"] 
    }
    df = pd.DataFrame(data)
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    st.write(fig)

if __name__ == '__main__':

    # pages
    st.sidebar.markdown("# Radar Chart")
    st.markdown("# Radar Chart")

    val1 = st.slider("sDa(%)", 0, 100, 5)
    val2 = st.slider('ASE(%)',0, 100, 20)
    val3 = st.slider('ED Gross(kWh/m2)', 0, 100, 40)
    val4 = st.slider('PV Production(kWh/m2)', 0, 150, 30)
    val5 = st.slider('Net Energy(kWh/m2)', 0, 100, 30)
    radar_chart(val1, val2, val3, val4, val5)


