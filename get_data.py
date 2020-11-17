import requests
import pandas as pd

penn_cases = 'https://data.pa.gov/resource/j72v-r42c.json'
penn_deaths = 'https://data.pa.gov/resource/fbgu-sqgp.json'
penn_hospital = 'https://data.pa.gov/resource/kayn-sjhx.json'


def get_penn_data(county):
    """retrieve data from Penn dept health for phila county returns a df"""
    response = requests.get(f'{penn_cases}?county={county}').json()
    penn_data = pd.DataFrame(response)
    penn_data['date'] = pd.to_datetime(penn_data['date'])
    penn_data = penn_data.set_index('date').sort_index()

    return penn_data



