from selenium.webdriver import Keys

from Flights.data.flights_search_data import FlightsPageSearchData
from Flights.pages.HomePage import HomePage
from Flights.base.BaseClass import BaseClass
from parameterized import parameterized
from time import sleep


class TestFlightsSearch(BaseClass):
    @parameterized.expand(FlightsPageSearchData.get_test_data())
    def test_flights_search(self,
                            test_case_name,
                            flights_type,
                            one_way,
                            round_trip,
                            flying_from,
                            destination_to,
                            depart_date,
                            return_date,
                            number_of_adults,
                            number_of_children,
                            number_of_infants,
                            expected_result):
        log = self.get_logger(test_case_name)
        home_page = HomePage(self.driver)
        sleep(1)
        flights_page = home_page.get_flights_link()
        log.info("Entered FLIGHTS page")

        self.select_option_by_text(flights_page.get_flights_type(), flights_type)
        log.info("flights type selected is: " + flights_type)

        if one_way == "Y":
            flights_page.get_one_way().click()
            log.info("one way is selected")
        if round_trip == "Y":
            flights_page.get_round_trip().click()
            log.info("round trip is selected")

        flights_page.get_flying_from_span().click()
        flights_page.get_flying_from_city().send_keys(flying_from)
        sleep(2)
        flights_page.get_destination_to_city().send_keys(Keys.ENTER)
        log.info("flying from " + flying_from)

        flights_page.get_destination_to_span().click()
        flights_page.get_destination_to_city().send_keys(destination_to)
        sleep(2)
        flights_page.get_destination_to_city().send_keys(Keys.ENTER)
        log.info("destination to " + destination_to)

        flights_page.get_depart_date().clear()
        flights_page.get_depart_date().send_keys(depart_date)
        log.info("{} {}".format("depart date is ", depart_date))
        if round_trip == "Y":
            flights_page.get_return_date().clear()
            flights_page.get_return_date().send_keys(return_date)
            log.info("{} {}".format("return date is ", return_date))

        flights_page.get_num_of_travellers().click()

        flights_page.get_num_of_adults().clear()
        flights_page.get_num_of_adults().send_keys(number_of_adults)
        flights_page.get_adults_inc_btn().click()
        flights_page.get_adults_dec_btn().click()
        log.info("{} {}".format("number of adults is ", number_of_adults))

        flights_page.get_num_of_children().clear()
        flights_page.get_num_of_children().send_keys(number_of_children)
        flights_page.get_children_inc_btn().click()
        flights_page.get_children_dec_btn().click()
        log.info("{} {}".format("number of children is ", number_of_children))

        flights_page.get_num_of_infants().clear()
        flights_page.get_num_of_infants().send_keys(number_of_infants)
        flights_page.get_infants_inc_btn().click()
        flights_page.get_infants_dec_btn().click()
        log.info("{} {}".format("number of infants is ", number_of_infants))

        flights_page.get_search_btn().click()

        sleep(5)

        if expected_result == "Flights Found":
            alert_text = flights_page.get_success_msg().text
            assert expected_result in alert_text
            log.info("{} {}".format("expected_result: ", alert_text))

        if expected_result == "No Results Found":
            flights_page.get_no_results_found()
            log.info("expected_result: No Results Found")
            flights_page.get_back_to_search().click()

        # self.driver.get_screenshot_as_file("../Images/.png")

        # self.driver.refresh()

    # @pytest.fixture(params=FlightsPageData.get_test_data())
    # def get_data(self, request):
    #     return request.param
