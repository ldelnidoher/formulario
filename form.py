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
         'Opcion1': np.array([]),
         'Opcion2': np.array([]),
         }
    )
st.dataframe(results_option)
st.write('Correo:')
qavalue = st.text_input('Correo')
if qavalue in results_option['Correo'].loc:
    st.text("Ya has registrado una respuesta")
else:
    with st.form('input_form'):
        c = st.radio("Opción 1:",("A","B","C"), horizontal = True)
        if c == "A":
            travalue = 2
        if c == "B":
            travalue = 7
        if 2 == "C":
            travalue = 2
        trvalue = st.number_input('Opción 2:')
        clickSubmit = st.form_submit_button('Submit')

    if clickSubmit:
        results_option.loc[len(results_option)] = [ qavalue, travalue, trvalue]
        results_option.to_csv(csv_file, index=False)
    else:
        st.markdown("Please submit to save")
