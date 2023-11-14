from parameterized import parameterized
from Flights.data.flights_booking_data import FlightsBookingData
from Flights.base.BaseClass import BaseClass
from Flights.pages.FlightsPage import FlightsPage
from time import sleep

class TestFlightsBooking(BaseClass):
    @parameterized.expand(FlightsBookingData.get_test_data())
    def test_flights_booking(self,
                             test_case_name,
                             oneway_flight_selected_for_booking):
        log = self.get_logger(test_case_name)
        flights_page = FlightsPage(self.driver)
        flights_page.open_url_for_flights_booking()
        sleep(30)
        log.info("Entering flights page for booking")

        self.driver.execute_script("window.scrollBy(0, 150);")
        sleep(2)
        oneway_flights = FlightsPage.get_oneway_flights(self)
        for oneway_flight in oneway_flights:
            oneway_flight_name = oneway_flight.text
            log.info(oneway_flight_name)
            # print("oneway_flight_name " + oneway_flight_name)
            # print(oneway_flight_selected_for_booking)
            if oneway_flight_name == oneway_flight_selected_for_booking:
                FlightsPage.get_select_flight_btn(self).click()
                log.info("Select Flight " + oneway_flight_name)
                sleep(5)