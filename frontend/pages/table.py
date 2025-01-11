"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd

df = pd.DataFrame({
  "id:": [ 0, 1, 2, 3, 4, 5, 6, 7 ],
  "name": [ 0, 1, 2, 3, 4, 5, 6, 7 ]
  # 0 : {
  #   "id": 0,
  #   "name": "name",
  #   "group": "group",
  #   "cron_expression" : "cron_expression",
  #   "status": "status",
  #   "description" : "description",
  #   "action" : "action"
  # },
  # 1 : {
  #   "id": 1,
  #   "name": "name",
  #   "group": "group",
  #   "cron_expression" : "cron_expression",
  #   "status": "status",
  #   "description" : "description",
  #   "action" : "action"
  # }
})

st.write(df)