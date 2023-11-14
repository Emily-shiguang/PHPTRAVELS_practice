from Flights import pages

class FlightsBookingPage:
    def __init__(self, driver):
        self.driver = driver

    def get_user_firstname(self):
        return self.driver.find_element(*pages.user_first_name)

    def get_user_lastname(self):
        return self.driver.find_element(*pages.user_last_name)