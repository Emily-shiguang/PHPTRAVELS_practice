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
