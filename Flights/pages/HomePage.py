from selenium.webdriver.support.wait import WebDriverWait

from Flights import pages
from Flights.pages.FlightsPage import FlightsPage
from selenium.webdriver.support import expected_conditions as ec


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_flights_link(self):
        element = WebDriverWait(self.driver,
                                timeout=30,
                                poll_frequency=0.5).until(lambda x: x.find_element(*pages.flights_link))
        WebDriverWait(self.driver, 60).until(ec.element_to_be_clickable(element))
        element.click()
        flights_page = FlightsPage(self.driver)
        return flights_page
