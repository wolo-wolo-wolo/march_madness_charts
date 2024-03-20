import streamlit as st
import pandas as pd

if 'kenpom_df' not in st.session_state:
    st.session_state['kenpom_df'] = pd.read_csv('KenPom Barttorvik.csv')


st.title("""
Multi-Page App

This is a hacky app to display KenPom data scatters across a few metrics.
""")
