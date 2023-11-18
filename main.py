import streamlit as st
import streamlit_data_processing as sdp
import streamlit_app_logic as sal

#App Settings
st.set_page_config(layout="wide")


#Session Starts


if __name__=='__main__':
       #display_map()
       sdp.initialise_session_state()
       sal.display_input_section()
       sal.display_output_section()
