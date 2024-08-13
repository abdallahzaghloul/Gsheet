import streamlit as st
import numpy as np
import pandas as pd
import os.path
import streamlit_gsheets
from streamlit_gsheets import GSheetsConnection
#from google.auth.transport.requests import Request
#from google.oauth2.credentials import Credentials
#from google_auth_oauthlib.flow import InstalledAppFlow
#from googleapiclient.discovery import build
#from googleapiclient.errors import HttpError

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()
