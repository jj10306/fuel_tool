#this file houses all of the
#logic for instantiating objects to query, web scrape, and hit API endpoints
from gasapp.query import Query
from gasapp.webscrape import WebScraper




class Driver:
    #id is the Vehicle object's id to get gas info
    #start and end are the addresses that are used to get the milage between and hit the APIs
    def __init__(self, id, start, end):
        self.id = id
        self.start = start
        self.end = end

    def drive(self):
        query_obj = Query(self.id)
        gas_tup = query_obj.get_gas() #tuple of (fuel_type, mpg)
        webScrape_obj = WebScraper(self.start, self.end)
        mileage = float(webScrape_obj.get_HTML(True, "").split()[0])
        return {'fuel_type': gas_tup[0],
        'mpg': float(gas_tup[1]), 'distance': mileage,
        'prices': {}}