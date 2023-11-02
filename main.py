import streamlit as st
import pandas as pd
import numpy as np

longitude = 146.4511
latitude = -38.2324

df = pd.DataFrame(np.array([[longitude, latitude]]), 
                  columns=['longitude', 'latitude'])

st.map(df,latitude=latitude,
       longitude=longitude,
       size=0,
       zoom=9)
