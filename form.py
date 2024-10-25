import os
import datetime
import pandas as pd
import numpy as np
import streamlit as st


csv_file = 'results_option.csv'
if os.path.exists(csv_file):
    # read from file
    results_option = pd.read_csv(csv_file, index_col=False)
else:
    # create empty dataframe with the right columns & dtypes
    results_option = pd.DataFrame(
        {'Correo': np.array([]).astype(str),
         'Opcion1': np.array([], dtype=np.float64),
         'Opcion2': np.array([], dtype=np.float64),
         'Opcion3': np.array([], dtype=np.float64),
         }
    )

st.write('Correo:')
st.dataframe(results_option)

with st.form('input_form'):
    qavalue = st.text_input('Correo')
    c = st.radio("Opcion1:",("A","B","C"), horizontal = True)
    if c == "A":
        num = 2
    if c == "B":
        num = 7
    if 2 == "C":
        num = 2
    travalue = st.number_input('num')

    trvalue = st.number_input('Opcion2')
    clickSubmit = st.form_submit_button('Submit')

if clickSubmit:
    results_option.loc[len(results_option)] = [ qavalue, travalue, trvalue]
    results_option.to_csv(csv_file, index=False)
else:
    st.markdown("Please submit to save")
