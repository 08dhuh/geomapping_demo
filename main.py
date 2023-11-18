import streamlit as st
from . import streamlit_data_processing as sdp
from . import streamlit_app_logic as sal

#App Settings
st.set_page_config(layout="wide")


#Session Starts
       
def display_input_section():
       st.subheader('Inputs')
       is_production = st.checkbox('production pump?')
       st.session_state['is_production'] = is_production




if __name__=='__main__':
       #display_map()
       sdp.initialise_session_state()
       display_input_section()
       sal.display_output_section()
