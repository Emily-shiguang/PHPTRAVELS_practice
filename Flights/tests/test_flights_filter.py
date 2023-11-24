from Flights.base.BaseClass import BaseClass
from Flights.data.flights_filter_data import FlightsPageFilterData
from parameterized import parameterized
from Flights.pages.FlightsPage import FlightsPage
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class TestFlightsFilter(BaseClass):
    @parameterized.expand(FlightsPageFilterData.get_test_data())
    def test_flights_filter(self,
                            test_case_name,
                            all_flights,
                            direct,
                            stops1,
                            stops2,
                            price_range_low,
                            price_range_high,
                            oneway_airlines_selected,
                            return_airlines_selected):
        log = self.get_logger(test_case_name)
        flights_page = FlightsPage(self.driver)
        flights_page.open_url_for_flights_filter()
        sleep(3)
        log.info("Entered flights page for filter")

        # Flight Stops for filter
        if all_flights == "Y":
            flights_page.get_all_flights().click()
            log.info("Flight Stops: All Flights")
        if direct == "Y":
            flights_page.get_direct().click()
            log.info("Flight Stops: Direct")
            flight_stops_list = flights_page.get_flight_stops()
            for flight_stops in flight_stops_list:
                if flight_stops.text != "Flight Stops 0":
                    raise Exception("Flight Stops not matching")
        if stops1 == "Y":
            flights_page.get_stops1().click()
            log.info("Flight Stops: Stops 1")
        if stops2 == "Y":
            flights_page.get_stops2().click()
            log.info("Flight Stops: Stops 2")

        # select Price Range for filter
        action = ActionChains(self.driver)

        price_low_btn = flights_page.get_price_range_low()
        # print(price_low_btn.location.get("x"))
        # print(price_low_btn.location.get("y"))
        # print(price_low_btn.get_attribute("textContent"))
        start_low = price_low_btn.get_attribute("textContent")
        start_low_no_space = start_low.replace(" ", "")
        action.move_to_element(price_low_btn)
        action.click_and_hold(price_low_btn)
        # action.move_by_offset(30, 0)
        offsetx_low = int((int(price_range_low)-int(start_low_no_space))/6.45)
        action.move_by_offset(offsetx_low, 0)

        action.release()
        action.perform()
        sleep(1)

        price_high_btn = flights_page.get_price_range_high()
        # print(price_high_btn.location.get("x"))
        # print(price_high_btn.location.get("y"))
        # print(price_high_btn.get_attribute("textContent"))
        start_high = price_high_btn.get_attribute("textContent")
        start_high_no_space = start_high.replace(" ", "")
        action.move_to_element(price_high_btn)
        action.click_and_hold(price_high_btn)
        # action.move_by_offset(-20, 0)
        offsetx_high = int((int(start_high_no_space) - int(price_range_high))/6.45)
        action.move_by_offset(-offsetx_high, 0)

        action.release()
        action.perform()
        sleep(1)

        # # Select Oneway Airlines for filter
        # oneway_airlines = flights_page.get_oneway_airlines()
        # for oneway_airline in oneway_airlines:
        #     oneway_airline_name = oneway_airline.text
        #     log.info(oneway_airline_name)
        #     if oneway_airline_name == oneway_airline1:
        #         oneway_airline.click()
        #         log.info(oneway_airline_name + " is selected")
        #     if oneway_airline_name == oneway_airline2:
        #         oneway_airline.click()
        #         log.info(oneway_airline_name + " is selected")
        # sleep(2)
        #
        # # Select Return Airlines for filter
        # self.driver.execute_script("window.scrollBy(0, 650);")
        # sleep(2)
        # return_airlines = flights_page.get_return_airlines()
        # for return_airline in return_airlines:
        #     return_airline_name = return_airline.text
        #     log.info(return_airline_name)
        #     if return_airline_name == return_airline1:
        #         return_airline.click()
        #         log.info(return_airline_name + " is selected")
        #     if return_airline_name == return_airline2:
        #         return_airline.click()
        #         log.info(return_airline_name + " is selected")
        # sleep(2)

        # Select Oneway Airlines for filter
        self.driver.execute_script("window.scrollBy(0, 150);")
        sleep(1)
        oneway_airlines = flights_page.get_oneway_airlines()
        for oneway_airline in oneway_airlines:
            oneway_airline_name = oneway_airline.text
            log.info(oneway_airline_name)
            if oneway_airline_name in oneway_airlines_selected:
                oneway_airline.click()
                log.info("oneway airline: " + oneway_airline_name + " is selected")
        sleep(1)

        # Select Return Airlines for filter
        if flights_page.verify_element_exist():
            self.driver.execute_script("window.scrollBy(0, 650);")
            sleep(2)
            log.info("Return Airlines exist")
            return_airlines = flights_page.get_return_airlines()
            for return_airline in return_airlines:
                return_airline_name = return_airline.text
                log.info(return_airline_name)
                if return_airline_name in return_airlines_selected:
                    return_airline.click()
                    log.info("Return airline: " + return_airline_name + " is selected")
            sleep(2)
        else:
            log.info("Return Airlines do not exist")




