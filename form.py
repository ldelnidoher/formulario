This is an issue with how you're using to_csv and read_csv, and pandas in general, not a streamlit issue.

Since the index isn't relevant to you, you should use to_csv(..., index=False), and when you read the file, you should use read_csv(..., index_col=False)

Reference:

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

Here's the full code, with some reorg/modifications:

import os
import datetime
import pandas as pd
import numpy as np
import streamlit as st


csv_file = 'results_option1.csv'
if os.path.exists(csv_file):
    # read from file
    results_option1 = pd.read_csv(csv_file, index_col=False)
else:
    # create empty dataframe with the right columns & dtypes
    results_option1 = pd.DataFrame(
        {'time': np.array([]).astype('datetime64[ns]'),
         'Primary Air Flow Rate': np.array([], dtype=np.float64),
         'Primary Air Temperature': np.array([], dtype=np.float64),
         'Reference Air Temperature': np.array([], dtype=np.float64),
         }
    )

st.write('before')
st.dataframe(results_option1)

with st.form('input_form'):
    qavalue = st.number_input('Primary Air Flow Rate')
    travalue = st.number_input('Primary Air Temperature')
    trvalue = st.number_input('Reference Air Temperature')
    clickSubmit = st.form_submit_button('Submit')

if clickSubmit:
    timestamp = datetime.datetime.now()
    results_option1.loc[len(results_option1)] = [timestamp, qavalue, travalue, trvalue]
    results_option1.to_csv(csv_file, index=False)
    st.write('after')
    st.dataframe(results_option1)
else:
    st.markdown("Please submit to save")
