from Flights import pages

class FlightsBookingConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    def get_proceed_btn(self):
        return self.driver.find_element(*pages.proceed_btn)