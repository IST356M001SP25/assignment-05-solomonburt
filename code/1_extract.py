import pandas as pd
import numpy as np
import streamlit as st
import pandaslib as pl
  
#TODO Write your extraction code here

def process_survey_data(survey_url, cache_dir="cache/"):
    """
    Reads a Google Sheet CSV, extracts/saves years' data.
    Fetches/saves cost of living for every year.
    """

    survey_data = pd.read_csv(survey_url)
    survey_data['year'] = survey_data['Timestamp'].str.extract(r'(\d{4})')  # Extract year using regex

    survey_data.to_csv(f'{cache_dir}survey_data.csv', index=False)

    years = survey_data['year'].unique()

    for year in years:
        if pd.notna(year): #check for nan values
            try:
                col_data = pd.read_html(f"https://www.numbeo.com/cost-of-living/rankings.jsp?title={int(year)}&displayColumn=0")[1]
                col_data['year'] = int(year)
                col_data.to_csv(f'{cache_dir}cost_of_living_{year}.csv', index=False)
            except (ValueError, IndexError) as e:
                print(f"Error processing year {year}: {e}") #Print error for debugging.

def process_state_data(state_url, cache_dir="cache/"):
    """
    Reads/saves (state) data from Google Sheet CSV.
    """
    state_data = pd.read_csv(state_url)
    state_data.to_csv(f'{cache_dir}state_data.csv', index=False)

# Main execution
survey_url = "https://docs.google.com/spreadsheets/d/1IPS5dBSGtwYVbjsfbaMCYIWnOuRmJcbequohNxCyGVw/export?resourcekey=&gid=1625408792&format=csv"
state_url = "https://docs.google.com/spreadsheets/d/14wvnQygIX1eCVo7H5B7a96W1v5VCg6Q9yeRoESF6epw/export?format=csv"

process_survey_data(survey_url)
process_state_data(state_url)