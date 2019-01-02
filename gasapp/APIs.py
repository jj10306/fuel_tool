import requests
from pprint import pprint
from requests_html import HTMLSession


def mapquestAPI(address):
    base_url = 'http://www.mapquestapi.com/geocoding/v1/address?key=lAFrTRNju9GH2Y0LxuFq9KFWvAWQnt80&location='
    address = '6038 Twinpoint Way, Woodstock, GA, 30189'

    r = requests.get(base_url + address)
    data = r.json()
    latLng = data['results'][0]['locations'][0]['latLng']
    return (latLng['lat'], latLng['lng'])
def tripleA():
    r = requests
    API_KEY = 'rfej9napna'
    base_url = 'http://devapi.mygasfeed.com/'
    #https://html.python-requests.org/#tutorial-usage
    session = HTMLSession()

    r = session.get('https://gasprices.aaa.com/?state=GA')
    print(r.content)
# tripleA()

def gas_price(): #returns the avg gas price in the state
    return 2.3