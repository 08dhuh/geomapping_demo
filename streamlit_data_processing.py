import numpy as np
import streamlit as st
import input_example as ie
from geodrillcalc import geodrillcalc as gdc

input_units = ['m³/day',
               'm/day',
               '',
               'yrs',
               'm',
               'm/yr',
               'm',
               'm']

def initialise_session_state():    
    if 'is_production' not in st.session_state:
        st.session_state['is_production'] = True
    if 'depth_data' not in st.session_state:
        st.session_state['depth_data'] = ie.depth_data
    if 'initial_values' not in st.session_state:
        st.session_state['initial_values'] = ie.initial_values

    execute_calculation_with_session_states()
    if 'result' not in st.session_state:
       st.session_state['result'] = st.session_state['wbd'].export_results_to_dict()

def execute_calculation_with_session_states():
    geo_calc = gdc.GeoDrillCalcInterface()
    wbd = geo_calc.calculate_and_return_wellbore_parameters(st.session_state['is_production'],
                                                  st.session_state['depth_data'],
                                                  st.session_state['initial_values'])
    st.session_state['wbd'] = wbd
    st.session_state['result'] = st.session_state['wbd'].export_results_to_dict()

def reset():
    """
    initialises the result chart
    """
    st.session_state['is_production'] = True
    st.session_state['depth_data'] = ie.depth_data
    st.session_state['initial_values'] = ie.initial_values
    #execute_calculation_with_session_states()


#{f'{key} ({input_units[i]})': ie.initial_values[key] for i,key in enumerate(ie.initial_values.keys())}