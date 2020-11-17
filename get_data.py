import requests
import pandas as pd

penn_cases = 'https://data.pa.gov/resource/j72v-r42c.json'
penn_deaths = 'https://data.pa.gov/resource/fbgu-sqgp.json'
penn_hospital = 'https://data.pa.gov/resource/kayn-sjhx.json'


def get_philly_data():
    """retrieve data from Penn dept health for phila county returns a df"""
    phila_response = requests.get(f'{penn_cases}?county=Philadelphia').json()
    phila_data = pd.DataFrame(phila_response).set_index('date').sort_index()
    return phila_data


def get_somerset_data():
    """retrieve data from Penn dept health for Somerset County. returns a df"""

    somerset_response = requests.get(f'{penn_cases}?county=Somerset').json()
    somerset = pd.DataFrame(somerset_response).set_index('date').sort_index()

    return somerset

