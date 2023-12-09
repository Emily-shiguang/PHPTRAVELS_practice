from selenium.webdriver.support.wait import WebDriverWait

from Flights import pages
from selenium.webdriver.support import expected_conditions as ec


class FlightsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_flights_type(self):
        element = WebDriverWait(self.driver,
                                timeout=15,
                                poll_frequency=0.5).until(lambda x: x.find_element(*pages.flights_type))
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(element))
        return element

    def get_one_way(self):
        return self.driver.find_element(*pages.one_way)

    def get_round_trip(self):
        return self.driver.find_element(*pages.round_trip)

    def get_flying_from_span(self):
        element = WebDriverWait(self.driver,
                                timeout=30,
                                poll_frequency=0.5).until(lambda x: x.find_element(*pages.flying_from_span))
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(element))
        return element

    def get_flying_from_city(self):
        return self.driver.find_element(*pages.flying_from_city)

    def get_destination_to_span(self):
        return self.driver.find_element(*pages.destination_to_span)

    def get_destination_to_city(self):
        return self.driver.find_element(*pages.destination_to_city)

    def get_depart_date(self):
        return self.driver.find_element(*pages.depart_date)

    def get_return_date(self):
        return self.driver.find_element(*pages.return_date)

    def get_num_of_travellers(self):
        return self.driver.find_element(*pages.travellers)

    def get_num_of_adults(self):
        element = WebDriverWait(self.driver,
                                timeout=30,
                                poll_frequency=0.5).until(lambda x: x.find_element(*pages.adults))
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(element))
        return element

    def get_adults_dec_btn(self):
        return self.driver.find_element(*pages.adults_dec_btn)

    def get_adults_inc_btn(self):
        return self.driver.find_element(*pages.adults_inc_btn)

    def get_num_of_children(self):
        return self.driver.find_element(*pages.children)

    def get_children_dec_btn(self):
        return self.driver.find_element(*pages.children_dec_btn)

    def get_children_inc_btn(self):
        return self.driver.find_element(*pages.children_inc_btn)

    def get_num_of_infants(self):
        return self.driver.find_element(*pages.infants)

    def get_infants_dec_btn(self):
        return self.driver.find_element(*pages.infants_dec_btn)

    def get_infants_inc_btn(self):
        return self.driver.find_element(*pages.infants_inc_btn)

    def get_search_btn(self):
        return self.driver.find_element(*pages.flights_search_btn)

    def get_success_msg(self):
        return self.driver.find_element(*pages.flights_found)

    def get_no_results_found(self):
        return self.driver.find_element(*pages.no_results_found)

    def get_back_to_search(self):
        return self.driver.find_element(*pages.back_to_search)

    def open_url_for_flights_filter(self):
        self.driver.get(pages.url_for_flights_fiter)

    def get_all_flights(self):
        return self.driver.find_element(*pages.all_flights)

    def get_direct(self):
        return self.driver.find_element(*pages.direct)

    def get_stops1(self):
        return self.driver.find_element(*pages.stops1)

    def get_stops2(self):
        return self.driver.find_element(*pages.stops2)

    def get_flight_stops(self):
        return self.driver.find_elements(*pages.flight_stops)

    def get_price_range_low(self):
        return self.driver.find_element(*pages.price_range_low)

    def get_price_range_high(self):
        return self.driver.find_element(*pages.price_range_high)

    def get_oneway_airlines(self):
        return self.driver.find_elements(*pages.oneway_airlines)

    def verify_element_exist(self):
        try:
            self.driver.find_element(*pages.return_airlines_exist)
            return True
        except:
            return False
    def get_return_airlines(self):
        return self.driver.find_elements(*pages.return_airlines)

    def open_url_for_flights_booking(self):
        self.driver.get(pages.url_for_flights_booking)

    def get_flight_list(self):
        return self.driver.find_elements(*pages.flight_list)

    def get_oneway_flights(self):
        return self.driver.find_elements(*pages.oneway_flights)

    def get_select_flight_btn(self):
        return self.driver.find_element(*pages.select_flight_btn)
