import pandas as pd
import streamlit as st
import pandaslib as pl

# TODO: Write your transformation code here

def analyze_and_save_data(cache_dir="cache/"):
    """
    Loads/analyzes/saves data from cache.
    """

    # Load data from cache
    survey_data = pd.read_csv(f'{cache_dir}survey_data.csv')
    states_data = pd.read_csv(f'{cache_dir}state_data.csv')

    # Load cost of living data
    cost_of_living_dfs = []
    for year in survey_data['year'].dropna().unique(): #Handle nan values
        try:
            cost_of_living_df = pd.read_csv(f'{cache_dir}cost_of_living_{int(year)}.csv')
            cost_of_living_dfs.append(cost_of_living_df)
        except FileNotFoundError:
            print(f"Warning: File not found for year {year}")

    cost_of_living_data = pd.concat(cost_of_living_dfs, ignore_index=True)

    # Clean country names (assuming a function similar to pl.clean_country_usa exists)
    def clean_country_usa(country_name): #Example country cleaning function
        if country_name == "United States" or country_name == "USA":
            return "USA"
        else:
            return country_name

    survey_data['_country'] = survey_data['What country do you work in?'].apply(clean_country_usa)

    # Merge survey data with state data
    survey_states_merged = pd.merge(survey_data, states_data, left_on="If you're in the U.S., what state do you work in?", right_on='State', how='inner')

    # Create full city column
    survey_states_merged['_full_city'] = survey_states_merged['What city do you work in?'] + ', ' + survey_states_merged['Abbreviation'] + ', ' + survey_states_merged['_country']

    # Merge with cost of living data
    combined_data = pd.merge(survey_states_merged, cost_of_living_data, left_on=['year', '_full_city'], right_on=['year', 'City'], how='inner')

    # Clean salary data (assuming a function similar to pl.clean_currency exists)
    def clean_currency(salary_str): #Example currency cleaning function
        if isinstance(salary_str, str):
            try:
                salary = float(salary_str.replace(",", "").replace("$", ""))
                return salary
            except ValueError:
                return None
        else:
            return salary_str

    combined_data["_annual_salary_cleaned"] = combined_data["What is your annual salary? (You'll indicate the currency in a later question. If you are part-time or hourly, please enter an annualized equivalent -- what you would earn if you worked the job 40 hours a week, 52 weeks a year.)"].apply(clean_currency)

    # Adjust salary based on cost of living
    combined_data['_annual_salary_adjusted'] = combined_data.apply(lambda row: row["_annual_salary_cleaned"] * (100 / row['Cost of Living Index']) if pd.notna(row["_annual_salary_cleaned"]) and row['Cost of Living Index'] != 0 else None, axis=1)

    # Save combined data
    combined_data.to_csv(f'{cache_dir}survey_dataset.csv', index=False)

    # Analyze and save salary data by location and age
    salary_by_location_age = combined_data.pivot_table(index='_full_city', columns='How old are you?', values='_annual_salary_adjusted', aggfunc='mean')
    salary_by_location_age.to_csv(f'{cache_dir}annual_salary_adjusted_by_location_and_age.csv')

    # Analyze and save salary data by location and education
    salary_by_location_education = combined_data.pivot_table(index='_full_city', columns='What is your highest level of education completed?', values='_annual_salary_adjusted', aggfunc='mean')
    salary_by_location_education.to_csv(f'{cache_dir}annual_salary_adjusted_by_location_and_education.csv')

    st.write(salary_by_location_education)

# Execute the analysis
analyze_and_save_data()