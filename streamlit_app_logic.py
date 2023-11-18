import streamlit as st
import pandas as pd
import numpy as np
from . import streamlit_data_processing as sdp


def display_input_section():
       st.subheader('Inputs')
       is_production = st.checkbox('production pump?')
       st.session_state['is_production'] = is_production

def display_output_section():
       st.subheader('Outputs')
       col1, col2, col3 = st.columns(3)
       interval = st.session_state['result'].pop('interval_stage_data')
       casing = st.session_state['result'].pop('casing_stage_data')
       error1 = st.session_state['result'].pop('production_screen_length_error')
       error2 = st.session_state['result'].pop('injection_screen_length_error')
       # Access the dictionary without the popped items
       with col1:
              st.dataframe(st.session_state['result'],
                    )
              st.dataframe(pd.DataFrame([error1, error2], 
                                        columns = ['min','max'],
                                        index=['production_screen_length_error',
                                               'injection_screen_length_error']))
       with col2:
              st.write(casing)
       with col3:   
              st.dataframe(interval,use_container_width=True, 
                    hide_index=True)
       st.session_state['result'] = st.session_state['wbd'].export_results_to_dict()
       


def display_map(longitude=None,latitude=None):
       longitude = longitude or 146.4511
       latitude = latitude or -38.2324

       df = pd.DataFrame(np.array([[longitude, latitude]]), 
                     columns=['longitude', 'latitude'])

       st.map(df,latitude=latitude,
              longitude=longitude,
              size=0,
              zoom=9)