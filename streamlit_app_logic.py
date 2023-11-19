import streamlit as st
import pandas as pd
import numpy as np
import streamlit_data_processing as sdp


def display_input_section():
    with st.sidebar:
        st.subheader('Inputs')
        st.button('reset inputs', on_click=sdp.reset)
        is_production = st.checkbox('production pump?')
        st.session_state['is_production'] = is_production
        depth_data = st.session_state['depth_data']
        updated_depth_data = st.data_editor(
            depth_data, 
            on_change=sdp.execute_calculation_with_session_states,
            column_config={ 'depth_data':st.column_config.NumberColumn(
                'depth to base(m)',
                min_value=0                
                )
            }

            )
        if updated_depth_data != depth_data:
            st.session_state['depth_data'] = updated_depth_data
            sdp.execute_calculation_with_session_states()

        initial_values = st.session_state['initial_values']
        updated_initial_values = st.data_editor(
            initial_values, on_change=sdp.execute_calculation_with_session_states)
        if updated_initial_values != initial_values:
            st.session_state['initial_values'] = updated_initial_values
            sdp.execute_calculation_with_session_states()
        # st.data_editor(st.session_state['depth_data'],
        #                on_change=sdp.execute_calculation_with_session_states)
        # st.data_editor(st.session_state['initial_values'],
        #                on_change=sdp.execute_calculation_with_session_states)


def display_output_section():
    st.subheader('Outputs')
    st.warning('If you encounter an error, please refresh the page.')
    col1, col2 = st.columns(2)
    interval = st.session_state['result'].pop('interval_stage_data')
    casing = st.session_state['result'].pop('casing_stage_data')
    error1 = st.session_state['result'].pop('production_screen_length_error')
    error2 = st.session_state['result'].pop('injection_screen_length_error')
    # Access the dictionary without the popped items
    with col1:
        st.dataframe(st.session_state['result'],
                     )
        st.dataframe(pd.DataFrame([error1, error2],
                                  columns=['min', 'max'],
                                  index=['production_screen_length_error',
                                         'injection_screen_length_error']))
    with col2:
        st.write(casing)
    st.dataframe(interval, use_container_width=True,
                 hide_index=True)
    st.session_state['result'] = st.session_state['wbd'].export_results_to_dict()


def display_map(longitude=None, latitude=None):
    longitude = longitude or 146.4511
    latitude = latitude or -38.2324

    df = pd.DataFrame(np.array([[longitude, latitude]]),
                      columns=['longitude', 'latitude'])

    st.map(df, latitude=latitude,
           longitude=longitude,
           size=0,
           zoom=9)
