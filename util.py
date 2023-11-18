import numpy as np
import streamlit as st

def num_formatter(num: float or np.ndarray, decimal=2):
    """
    This function formats a given float 'num' to a specific number of decimal places.

    Parameters:
    - num (float): The float number to format
    - decimal (int): Number of decimal places to round to (default: 2)

    Returns:
    - float: Formatted number with the specified number of decimal places
    """
    try:
        if type(num) is float:
            return round(num, decimal)
        if type(num) is np.ndarray:
            return np.around(num, decimal)
        else:
            raise TypeError
    except TypeError as e:
        return st.error(e)
    

