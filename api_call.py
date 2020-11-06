"""
Generates API call to covid project to try and parse out active cases in canada
"""
import requests
import json
import pandas
import csv



def main():
    """
    Entrypoint into program.
    """
    web_data= call_api()

    save_data(web_data)

"""
    parse_data(web_data)
"""

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
    return (web_data)

def parse_data():
    pass

def save_data(web_data):
    with open('cases.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = {} )
        writer.writeheader()
        writer.writerows(web_data)

"""
code i stole
with open('Names.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(cars)
 """

if __name__ == '__main__':
    main()
