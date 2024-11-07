import os
import datetime
import pandas as pd
import numpy as np
import streamlit as st
import random as r

#st.date_input('fecha', help = "click on the week that you're interested in", value = None)

t = datetime.datetime.today()
day_of_week = t.isoweekday()
suffix = (t.strftime('%Y%m%d'))+str(r.randint(1,30))
 
csv_file = "files.csv"
if os.path.exists(csv_file):
    files = pd.read_csv(csv_file,index_col = False)
else:
    files = pd.DataFrame(
        {'a':np.array([],dtype="object"),
         'b':np.array([],dtype="object")
        },
     index = []
    )
if suffix not in files.index:
     num1 = np.array([[r.random() for j in range(3)] for i in range(3)]).transpose()
     num2 = np.array([[2+r.random()for j in range(3)] for i in range(2)]).transpose()
     files.loc[suffix] = [num1,num2]
files.to_csv(csv_file)

      
st.dataframe(pd.read_csv(files))
  
    


  
  
