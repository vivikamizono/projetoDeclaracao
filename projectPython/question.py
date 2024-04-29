import re
import streamlit as st;
import pandas as pd;
import numpy as np;
from os import write

# Titulo
def centralize_text(text):
    return f"<div style='text-align: center;'>{text}</div>"
st.markdown(centralize_text("<h1>Declaração de Bens</h1>"), unsafe_allow_html=True)

