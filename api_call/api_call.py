"""
Generates API call to covid project to try and parse out active cases in canada
"""
import requests
import pandas as pd
import csv



def main():
    """
    Entrypoint into program.
    """
    web_data= call_api()

    pandas_parse(web_data)

#    save_csv(web_data)

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

    return (web_data, response)

def parse_data():
    pass

def save_csv(web_data):
    csv_fields = {'row_id','date_reported','age_group','gender','province','case_status','health_region'}
    with open('cases.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_fields)
        writer.writeheader()
        writer.writerows(web_data)

def pandas_parse(response):
    cases = pd.read_json(response)
    "df.to_csv(index=False)"

"""
code i stole
with open('Names.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(cars)
    Fields=row_id,date_reported,age_group,gender,province,case_status,health_region
 """

if __name__ == '__main__':
    main()
