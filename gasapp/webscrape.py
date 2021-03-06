
import bs4 #beautifulsoup4 - HTML parser python
from bs4 import BeautifulSoup
from selenium import webdriver #to get the HTML that conatains excecuted JavaScript - the InspectElement vs ViewPageSource


base_url = 'https://www.google.com/maps/dir/' #google maps base url
gas_price_url = 'https://gasprices.aaa.com/?state=' #triple A base url

class WebScraper:

    def __init__(self, start, end):
        self.start = start
        self.end = end


        #switch to determine whether getting google maps or AAA HTML
        #large refactoring would've been required otherwise
    def get_HTML(self, switch, state): #returns the HTML of the web page so it can be parsed
        if switch:
            specific_url = base_url + self.start + "/" + self.end
        else:
            specific_url = gas_price_url + state

        chromedriver_PATH = '/Users/Jakob/Desktop/Personal/CS/chromedriver'
        options = webdriver.ChromeOptions()
        options.add_argument('headless') #makes it so a new window doesnt open
        options.add_argument('window-size=1200x600')
        driver = webdriver.Chrome(chromedriver_PATH, chrome_options=options)
        # url = 'https://www.google.com/maps/dir/Willis+Tower+Skydeck,+233+S+Wacker+Dr,+Chicago,+IL+60606/Griffith+Observatory,+2800+E+Observatory+Rd,+Los+Angeles,+CA+90027/@36.6162744,-121.0097401,4z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x880e2cbf1d3c61a7:0xcee917a8ddbc62f1!2m2!1d-87.635915!2d41.8788761!1m5!1m1!1s0x80c2bf61e9d408cb:0x73ff07b1c2d6dadc!2m2!1d-118.3003935!2d34.1184341'
        driver.get(specific_url)
        exc_js_html = driver.page_source

        if switch:
            return HTML_parser(exc_js_html) #gets final DOM: JavaScript has actually been excecuted (thank the lord)
        else:
            return gas_scrape(exc_js_html)


def HTML_parser(html): #gets the miles from google maps source
    noTomatoSoup = bs4.BeautifulSoup(html, 'html.parser')
    div_list = noTomatoSoup.find_all("div")
    tester_element = div_list[0]

    filtered_list = []
    for item in div_list:

        if len(item.contents) == 1 and type(item.contents[0]) == bs4.element.NavigableString and "miles" in item.contents[0]:

                filtered_list.append(item)
                mile_list = [item.contents[0] for item in filtered_list] #list of navigable strings that are the miles ie: 34.4 miles

    return mile_list[0]

def gas_scrape(html):
    noTomatoSoup = bs4.BeautifulSoup(html, 'html.parser')
    td_list = noTomatoSoup.find_all("td")

    price_list = td_list[3:7]
    final_list = [float(td.contents[0].strip("$")) for td in price_list]
    gas_types = ["Regular", "Mid-Grade", "Premium", "Diesel"]
    final_dict = dict(zip(gas_types, final_list))


    return final_dict














# def driver():
#     address_tup = get_user_info()
#     google_maps(address_tup[0], address_tup[1])
#     html = get_HTML(address_tup[0], address_tup[1])
#     soup = HTML_parser(html)
#     print(soup)



# driver()






































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































