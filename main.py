import streamlit as st
import pandas as pd
import numpy as np


def display_map(longitude=None,latitude=None):
       longitude = longitude or 146.4511
       latitude = latitude or -38.2324

       df = pd.DataFrame(np.array([[longitude, latitude]]), 
                     columns=['longitude', 'latitude'])

       st.map(df,latitude=latitude,
              longitude=longitude,
              size=0,
              zoom=9)

if __name__=='__main__':
       display_map()
