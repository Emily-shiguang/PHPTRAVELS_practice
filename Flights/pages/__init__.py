from selenium.webdriver.common.by import By

"""HOME page configuration data"""
# home_url = "https://phptravels.net/"
home_url = "https://phptravels.site/"

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
url_for_flights_fiter = "https://phptravels.site/flights/lhe/dxb/oneway/economy/09-12-2023/2/2/1"
all_flights = (By.CSS_SELECTOR, "#all")
direct = (By.CSS_SELECTOR, "#direct")
stops1 = (By.CSS_SELECTOR, "input[value='.oneway_1']")
stops2 = (By.CSS_SELECTOR, "input[value='.oneway_2']")
flight_stops = (By.CSS_SELECTOR, "div[class*='text-end'] h6[class='mb-0'] strong")
price_range_low = (By.CSS_SELECTOR, "span[class*='irs-from']")
price_range_high = (By.CSS_SELECTOR, "span[class*='irs-to']")
oneway_airlines = (By.CSS_SELECTOR, "label[for*='oneway']")
return_airlines_exist= (By.PARTIAL_LINK_TEXT, "Return Airlines")
return_airlines = (By.CSS_SELECTOR, "label[for*='return']")


"""FLIGHTS page configuration data for booking"""
url_for_flights_booking = "https://phptravels.site/flights/lhe/dxb/oneway/economy/07-12-2023/1/0/0"
oneway_flights = (By.CSS_SELECTOR, "p[class='mb-1']")
select_flight_btn = (By.CSS_SELECTOR, "button[class*='btn-dark']")

"""Flights Booking page configuration data"""
user_first_name = (By.CSS_SELECTOR, "input[name='user[first_name]']")
user_last_name = (By.CSS_SELECTOR, "input[name='user[last_name]']")
user_email = (By.CSS_SELECTOR, "input[name='user[email]']")
user_phone = (By.CSS_SELECTOR, "input[name='user[phone]']")
user_address = (By.CSS_SELECTOR, "input[name='user[address]']")
user_nationality = (By.CSS_SELECTOR, "div[class*='nationality'] div[class='filter-option']")
user_nationality_search = (By.CSS_SELECTOR, "div[class*='nationality'] input[type='search']")
user_current_country = (By.CSS_SELECTOR, "div[class*='country'] div[class='filter-option']")
user_current_country_search = (By.CSS_SELECTOR, "div[class*='country'] input[type='search']")
traveller1_title = (By.CSS_SELECTOR, "select[name='title_1']")
traveller1_firstname = (By.CSS_SELECTOR, "input[name='first_name_1']")
traveller1_lastname = (By.CSS_SELECTOR, "input[name='last_name_1']")
traveller1_nationality = (By.CSS_SELECTOR, "select[name='nationality_1']")
traveller1_dob_month = (By.CSS_SELECTOR, "select[name='dob_month_1']")
traveller1_dob_day = (By.CSS_SELECTOR, "select[name='dob_day_1']")
traveller1_dob_year = (By.CSS_SELECTOR, "select[name='dob_year_1']")
traveller1_passport_no = (By.CSS_SELECTOR, "input[name='passport_1']")
traveller1_passport_issuance_month = (By.CSS_SELECTOR, "select[name='passport_issuance_month_1']")
traveller1_passport_issuance_day = (By.CSS_SELECTOR, "select[name='passport_issuance_day_1']")
traveller1_passport_issuance_year = (By.CSS_SELECTOR, "select[name='passport_issuance_year_1']")
traveller1_passport_expiry_month = (By.CSS_SELECTOR, "select[name='passport_month_expiry_1']")
traveller1_passport_expiry_day = (By.CSS_SELECTOR, "select[name='passport_day_expiry_1']")
traveller1_passport_expiry_year = (By.CSS_SELECTOR, "select[name='passport_year_expiry_1']")
pay_paypal = (By.CSS_SELECTOR, "div[class*='paypal']")
pay_bank_transfer = (By.CSS_SELECTOR, "div[class*='bank_transfer']")
pay_later = (By.CSS_SELECTOR, "div[class*='pay_later']")
pay_stripe = (By.CSS_SELECTOR, "div[class*='stripe']")
agree_chb = (By.CSS_SELECTOR, "#agreechb")
hide_btn = (By.CSS_SELECTOR, "#cookie_stop")
confirm_booking_btn = (By.CSS_SELECTOR, "div[class*='btn-box']")

"""Flights Booking confirm page configuration data"""
url_for_flights_booking_confirm = "https://phptravels.site/flights/invoice/20231117031638"
proceed_btn = (By.CSS_SELECTOR, "input[class*='btn-success']")

