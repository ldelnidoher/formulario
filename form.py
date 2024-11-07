import os
import datetime
import pandas as pd
import numpy as np
import streamlit as st
import random as r

def save_uploadedfile(uploadedfile):
     with open(os.path.join("tempDir",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to tempDir".format(uploadedfile.name))

st.date_input('fecha', help = "click on the week that you're interested in", value = None)

t = datetime.datetime.today()
day_of_week = t.isoweekday()
suffix = (t.strftime('%Y%m%d'))+str(r.randint(1,30))
 
csv_file = "files.csv"
if os.path.exists(csv_file):
    files = pd.read_csv(csv_file,index_col = False)
else:
    files = pd.DataFrame(
        {'a':np.array([]),
         'b':np.array([]),
        }
    )

num1 = [r.random() for i in range(10)]
num2 = [2+r.random() for i in range(10)]
if not str(suffix)+'1.txt' in files['a'].values:
  n1 = f'{suffix}1.txt'
  n2 = f'{suffix}2.txt'
  a = np.savetxt(n1,np.array(num1),fmt = '% 1.5f', delimiter = ' \t')
  b = np.savetxt(n2,np.array(num2),fmt = '% 1.5f', delimiter = ' \t')
  files.loc[len(files.index)] = [str(suffix)+'1.txt',str(suffix)+'2.txt']

  with open(os.path.join("tempDir",n1),"wb") as f:
     f.write(n.getbuffer())

  with open(os.path.join("tempDir",n2),"wb") as f:
     f.write(n.getbuffer())
      
st.dataframe(pd.read_csv(n1))
  
     
st.dataframe(files)


  
  
