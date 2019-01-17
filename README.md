<img src="https://github.com/jj10306/fuel_tool/blob/master/demo_images/main_page.png">

# Fuel Tool: Gas Expense Calculator :fuelpump:
Flask web application that calculates a user’s gas expense based on user-provided data regarding their trip and vehicle

- Information is gathered about the user's vehicle through the dropdowns and then the database is queried to get the user's vehicle's mpg. (Please Note: The dropdowns are dynamically populated based on the previous dropdown's value. For example, if you chose Nissan as the Make, then only the Nissan 'makes' would appear in the Make dropdown. Same logic applies for the Year dropdown)
- The start and end addresses of the user's trip is gathered from the text fields of the form and then the mileage is obtained via scraping https://www.google.com/maps/dir/ (driving directions between the two addresses)
- The gas price is gathered based on the current average gas price in the state of their start address, via scraping of https://gasprices.aaa.com/ 
- The following formula was applied to get the user's fuel expense for the trip:
  Cost ($) = distance_traveled (miles) / vehicle_mpg (miles per gallon) * gas_price ($ per gallon)

*Disclaimer*

My intentions with this project were to get my feet (or fingers, rather) wet with web scraping and full stack dev. The frontend is minimal and far from jawdroppingly beautiful, but instead I wanted to take this project as time to learn the interactions between the database, the server-side, and the client-side

*End Disclaimer*


<img src="https://github.com/jj10306/fuel_tool/blob/master/demo_images/result_page.png">


## Built With
Backend: Flask

Frontend: Bootstrap

Database: SQLite

- Web Scraping: Utilizes Selenium WebDriver to get JavaScript manipulated DOM of Google Maps, Beautiful Soup package then used to parse source HTML and extract the user’s travel mileage
- Refined 14 MB of CSV general vehicle data to 2 MB of fuel-related vehicle data and migrated the refined data into a SQLite database
- Web scrapes https://gasprices.aaa.com/ to get current gas prices in the user’s state
- Uses client-side JavaScript to make AJAX callbacks dynamically resizing/populate dropdowns without loading a new page
- Uses Flask-Bootstrap integration to make a 
