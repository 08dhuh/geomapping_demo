import streamlit as st
import pandas as pd
import numpy as np
from geodrillcalc import geodrillcalc as gdc
import input_example as ie

st.set_page_config(layout="wide")


if 'is_production' not in st.session_state:
       st.session_state['is_production'] = False

if 'depth_data' not in st.session_state:
       st.session_state['depth_data'] = ie.depth_data
if 'initial_values' not in st.session_state:
       st.session_state['initial_values'] = ie.initial_values

geo_calc = gdc.GeoDrillCalcInterface()
wbd = geo_calc.calculate_and_return_wellbore_parameters(st.session_state['is_production'],
                                                  st.session_state['depth_data'],
                                                  st.session_state['initial_values'])

if 'wbd' not in st.session_state:
       st.session_state['wbd'] = wbd

if 'result' not in st.session_state:
       st.session_state['result'] = wbd.export_results_to_dict()
       
def display_input_section():
       st.subheader('Inputs')
       st.button('Is production pump')

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
       st.session_state['result'] = wbd.export_results_to_dict()
       

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
       #display_map()
       display_input_section()
       display_output_section()
