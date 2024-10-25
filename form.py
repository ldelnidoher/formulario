import os
import datetime
import pandas as pd
import numpy as np
import streamlit as st


csv_file = 'results_option.csv'
if os.path.exists(csv_file):
    # read from file
    results_option1 = pd.read_csv(csv_file, index_col=False)
else:
    # create empty dataframe with the right columns & dtypes
    results_option1 = pd.DataFrame(
        {'Correo': np.array([]).astype(str),
         'Opcion1': np.array([], dtype=np.float64),
         'Opcion2': np.array([], dtype=np.float64),
         'Opcion3': np.array([], dtype=np.float64),
         }
    )

st.write('Correo:')
st.dataframe(results_option1)

with st.form('input_form'):
    qavalue = st.text_input('Correo')
    travalue = st.number_input('Opcion1')
    trvalue = st.number_input('Opcion2')
    clickSubmit = st.form_submit_button('Submit')

if clickSubmit:
    results_option.loc[len(results_option)] = [ qavalue, travalue, trvalue]
    results_option.to_csv(csv_file, index=False)
else:
    st.markdown("Please submit to save")
