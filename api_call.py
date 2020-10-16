"""
Generates API call to covid project to try and parse out active cases in canada
"""
import requests
import json


def main():
    """
    Entrypoint into program.
    """

    call_api()


def call_api():
    """
    call https://services9.arcgis.com/pJENMVYPQqZZe20v/arcgis/rest/services/Canada_COVID19_Case_Details/FeatureServer/0/query?where=1%3D1&outFields=row_id,date_reported,age_group,gender,province,case_status,health_region&outSR=4326&f=json
    Read the json and turn it into a CSV or pandas dataframe
    """

    api_url = "https://services9.arcgis.com/pJENMVYPQqZZe20v/arcgis/rest/services/Canada_COVID19_Case_Details/FeatureServer/0/"
    api_argument = "query?where=1%3D1&outFields=row_id,date_reported,age_group,gender,province,case_status,health_region&outSR=4326&f=json"
    response = requests.get(f'{api_url}{api_argument}')
    web_data = response.json()  # returns a list of dicts
    print(type(web_data))
    print(web_data)


if __name__ == '__main__':
    main()
