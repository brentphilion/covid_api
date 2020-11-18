"""
Generates API call to covid project to try and parse out active cases in canada
"""
import requests
import wget
import pandas as pd
import csv


def main():
    """
    Entrypoint into program.
    """
#    web_data = call_api()  Rebasing code using Johns hopkins
    web_data = get_from_jhu()
    pandas_parse()

#    save_csv(web_data)

def call_api():
    """
    call https://services9.arcgis.com/pJENMVYPQqZZe20v/arcgis/rest/services/Canada_COVID19_Case_Details/FeatureServer/0/query?where=1%3D1&outFields=row_id,date_reported,age_group,gender,province,case_status,health_region&outSR=4326&f=json
    Read the json and turn it into a CSV or pandas dataframe
    """

    api_url = "https://services9.arcgis.com/pJENMVYPQqZZe20v/arcgis/rest/services/Canada_COVID19_Case_Details/FeatureServer/0/"
    api_argument = "query?where=1%3D1&outFields=row_id,date_reported,age_group,gender,province,case_status,health_region&outSR=4326&f=json"
    response = requests.get(f'{api_url}{api_argument}')
    web_data = response.json()  # returns a list of dicts

    return (web_data)

def get_from_jhu():
    """
    Pull data form Johns hopkins using wget instead

    """

    # url of the raw csv dataset
    urls = [
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv',
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
        ]
    [wget.download(url) for url in urls]

    return ()
def parse_data():
    pass



def save_csv(web_data):
    csv_fields = {'row_id','date_reported','age_group','gender','province','case_status','health_region'}
    with open('cases.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_fields)
        writer.writeheader()
        writer.writerows(web_data)

def pandas_parse():
    confirmed_df = pd.read_csv('time_series_covid19_confirmed_global.csv')
    deaths_df = pd.read_csv('time_series_covid19_deaths_global.csv')
    recovered_df = pd.read_csv('time_series_covid19_recovered_global.csv')
    print(confirmed_df.head())
    print(deaths_df.head())
    print(recovered_df.head())



"""
code i stole

df = pd.DataFrame.from_dict(d, orient='index')

with open('Names.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(cars)
    Fields=row_id,date_reported,age_group,gender,province,case_status,health_region
 """

if __name__ == '__main__':
    main()
