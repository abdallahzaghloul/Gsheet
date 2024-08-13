import streamlit as st
import numpy as np
import gspread
import streamlit_gsheets
from streamlit_gsheets import GSheetsConnection
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()
