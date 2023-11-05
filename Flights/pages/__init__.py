from selenium.webdriver.common.by import By

"""home page configuration data"""
home_url = "https://phptravels.net/"

"""FLIGHTS page configuration data for search"""
flights_link = (By.CSS_SELECTOR, "a[href*='flights']")
flights_type = (By.CSS_SELECTOR, "#flight_type")
one_way = (By.XPATH, "//label[@for='one-way']")
round_trip = (By.XPATH, "//label[@for='round-trip']")
flying_from_span = (By.CSS_SELECTOR, "span[data-select2-id='2']")
flying_from_city = (By.CSS_SELECTOR, "input[class='select2-search__field']")
destination_to_span = (By.CSS_SELECTOR, "span[data-select2-id='5']")
destination_to_city = (By.CSS_SELECTOR, "input[class='select2-search__field']")
depart_date = (By.CSS_SELECTOR, "#departure")
return_date = (By.CSS_SELECTOR, "#return_date")
travellers = (By.CSS_SELECTOR, "[class*='travellers']")
adults = (By.CSS_SELECTOR, "#fadults")
adults_dec_btn = (By.CSS_SELECTOR, "div[class='dropdown-item adult_qty'] div[class='qtyDec']")
adults_inc_btn = (By.CSS_SELECTOR, "div[class='dropdown-item adult_qty'] div[class='qtyInc']")
children = (By.CSS_SELECTOR, "#fchilds")
children_dec_btn = (By.CSS_SELECTOR, "div[class='dropdown-item child_qty'] div[class='qtyDec']")
children_inc_btn = (By.CSS_SELECTOR, "div[class='dropdown-item child_qty'] div[class='qtyInc']")
infants = (By.CSS_SELECTOR, "#finfant")
infants_dec_btn = (By.CSS_SELECTOR, "div[class='dropdown-item infant_qty'] div[class='qtyDec']")
infants_inc_btn = (By.CSS_SELECTOR, "div[class='dropdown-item infant_qty'] div[class='qtyInc']")
flights_search_btn = (By.CSS_SELECTOR, "button[id='flights-search']")
flights_found = (By.CSS_SELECTOR, "span[class='j_listABTit']")
no_results_found = (By.CSS_SELECTOR, "img[alt='no results']")
back_to_search = (By.PARTIAL_LINK_TEXT, "Back To Search")

"""FLIGHTS page configuration data for filter"""
all_flights = (By.CSS_SELECTOR, "#all")
direct = (By.CSS_SELECTOR, "#direct")
stops1 = (By.PARTIAL_LINK_TEXT, "Stops 1")
stops2 = (By.PARTIAL_LINK_TEXT, "Stops 2")
# price_range_low = ???????
# price_range_high = ?????
oneway_airlines = (By.CSS_SELECTOR, "ul[class*='oneway']")
return_airlines = (By.CSS_SELECTOR, "ul[class*='return']")




