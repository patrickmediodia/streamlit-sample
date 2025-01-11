import os
import requests
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
API_ENDPOINT = os.environ.get("API_ENDPOINT")

# def process_row(row):
#     return st.button(
#         f"Action for row {row.id}",
#         type="primary"
#     )

def main():
    # get data from endpoint
    data = requests.get(f'{API_ENDPOINT}/table').json()
    df = pd.DataFrame(data)

    # # add additional column for actions
    # df['Actions'] = df.apply(lambda row: process_row(row), axis=1)

    for index, row in df.iterrows():
        columns = st.columns([ 1 for _ in range(len(row)) ])
        for column in columns:
            for value in row:
                with column:
                    st.write(value)
            # if column.number != len(row) - 1:
            #     st.write(row)
            # else:
            #     st.button(f"Button for {row.id} clicked!")

if __name__ == "__main__":
    main()
