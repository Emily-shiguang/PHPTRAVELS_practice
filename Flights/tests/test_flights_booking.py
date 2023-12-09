from parameterized import parameterized
from Flights.data.flights_booking_data import FlightsBookingData
from Flights.base.BaseClass import BaseClass
from Flights.pages.FlightsPage import FlightsPage
from Flights.pages.FlightsBookingPage import FlightsBookingPage
from selenium.webdriver.common.by import By
from time import sleep


class TestFlightsBooking(BaseClass):
    @parameterized.expand(FlightsBookingData.get_test_data())
    def test_flights_booking(self,
                             test_case_name,
                             oneway_flight_selected_for_booking,
                             user_first_name,
                             user_last_name,
                             user_email,
                             user_phone,
                             user_address,
                             user_nationality,
                             user_current_country,
                             traveller1_title,
                             traveller1_firstname,
                             traveller1_lastname,
                             traveller1_nationality,
                             traveller1_dob_month,
                             traveller1_dob_day,
                             traveller1_dob_year,
                             traveller1_passport_no,
                             traveller1_passport_issuance_month,
                             traveller1_passport_issuance_day,
                             traveller1_passport_issuance_year,
                             traveller1_passport_expiry_month,
                             traveller1_passport_expiry_day,
                             traveller1_passport_expiry_year,
                             payment_method
                             ):
        log = self.get_logger(test_case_name)
        flights_page = FlightsPage(self.driver)
        flights_page.open_url_for_flights_booking()
        sleep(2)
        log.info("Entered flights page for booking")

        # self.driver.execute_script("window.scrollBy(0, 150);")
        # oneway_flights = FlightsPage.get_oneway_flights(self)
        # for oneway_flight in oneway_flights:
        #     oneway_flight_name = oneway_flight.text
        #     log.info(oneway_flight_name)
        #     # print("oneway_flight_name " + oneway_flight_name)
        #     # print(oneway_flight_selected_for_booking)
        #     if oneway_flight_name == oneway_flight_selected_for_booking:
        #         print("XXXXXX")
        #         FlightsPage.get_select_flight_btn(self).click()
        #         log.info("Select Flight: " + oneway_flight_name)
        #         log.info("Entered flights booking page")

        self.driver.execute_script("window.scrollBy(0, 120);")
        sleep(1)
        flight_list = FlightsPage.get_flight_list(self)
        for oneway_flight in flight_list:
            self.driver.execute_script("window.scrollBy(0, 120);")
            sleep(1)
            oneway_flight_name = oneway_flight.find_element(By.CSS_SELECTOR, "p[class='mb-1']").text
            log.info(oneway_flight_name)
            # print("oneway_flight_name " + oneway_flight_name)
            # print(oneway_flight_selected_for_booking)
            if oneway_flight_name == oneway_flight_selected_for_booking:
                oneway_flight.find_element(By.CSS_SELECTOR, "button[onclick*='moreDetail']").click()
                sleep(1)
                self.driver.execute_script("window.scrollBy(0, 120);")
                sleep(1)
                self.driver.execute_script("window.scrollBy(0, -120);")
                sleep(1)
                oneway_flight.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
                log.info("Select Flight: " + oneway_flight_name)
                log.info("Entered flights booking page")
                break

        log.info("Filling in personal information")
        self.driver.execute_script("window.scrollBy(0, 90);")
        flights_booking_page = FlightsBookingPage(self.driver)
        flights_booking_page.get_user_firstname().send_keys(user_first_name)
        log.info("First Name: " + user_first_name)
        flights_booking_page.get_user_lastname().send_keys(user_last_name)
        log.info("Last Name: " + user_last_name)
        flights_booking_page.get_user_email().send_keys(user_email)
        log.info("Email: " + user_email)
        flights_booking_page.get_user_phone().send_keys(user_phone)
        log.info("Phone: " + user_phone)
        flights_booking_page.get_user_address().send_keys(user_address)
        log.info("Address: " + user_address)
        flights_booking_page.get_user_nationality().click()
        flights_booking_page.get_user_nationality_search().send_keys(user_nationality)
        self.verify_element_presence(user_nationality)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, user_nationality).click()
        log.info("Nationality: " + user_nationality)
        flights_booking_page.get_user_current_country().click()
        flights_booking_page.get_user_current_country_search().send_keys(user_current_country)
        self.verify_element_presence(user_current_country)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, user_current_country).click()
        log.info("Current Country: " + user_current_country)
        sleep(2)

        log.info("Filling in travellers information")
        self.driver.execute_script("window.scrollBy(0, 450);")
        sleep(2)
        self.select_option_by_text(flights_booking_page.get_traveller1_title(), traveller1_title)
        log.info("Traveller1_title: " + traveller1_title)
        flights_booking_page.get_traveller1_firstname().send_keys(traveller1_firstname)
        log.info("Traveller1_firstname: " + traveller1_firstname)
        flights_booking_page.get_traveller1_lastname().send_keys(traveller1_lastname)
        log.info("Traveller1_lastname: " + traveller1_lastname)
        self.select_option_by_text(flights_booking_page.get_traveller1_nationality(), traveller1_nationality)
        log.info("Traveller1_nationality: " + traveller1_nationality)
        self.select_option_by_text(flights_booking_page.get_traveller1_dob_month(), traveller1_dob_month)
        self.select_option_by_text(flights_booking_page.get_traveller1_dob_day(), traveller1_dob_day)
        self.select_option_by_text(flights_booking_page.get_traveller1_dob_year(), traveller1_dob_year)
        log.info("Traveller1_DOB: " + traveller1_dob_month + " " + traveller1_dob_day + " " + traveller1_dob_year)
        flights_booking_page.get_traveller1_passport_no().send_keys(traveller1_passport_no)
        log.info("Traveller1_passport_no: " + traveller1_passport_no)
        self.select_option_by_text(flights_booking_page.get_traveller1_passport_issuance_month(),
                                   traveller1_passport_issuance_month)
        self.select_option_by_text(flights_booking_page.get_traveller1_passport_issuance_day(),
                                   traveller1_passport_issuance_day)
        self.select_option_by_text(flights_booking_page.get_traveller1_passport_issuance_year(),
                                   traveller1_passport_issuance_year)
        log.info("Traveller1_passport_issuance_date: " + traveller1_passport_issuance_month
                 + " " + traveller1_passport_issuance_day
                 + " " + traveller1_passport_issuance_year)
        self.select_option_by_text(flights_booking_page.get_traveller1_passport_expiry_month(),
                                   traveller1_passport_expiry_month)
        self.select_option_by_text(flights_booking_page.get_traveller1_passport_expiry_day(),
                                   traveller1_passport_expiry_day)
        self.select_option_by_text(flights_booking_page.get_traveller1_passport_expiry_year(),
                                   traveller1_passport_expiry_year)
        log.info("Traveller1_passport_expiry_date: " + traveller1_passport_expiry_month
                 + " " + traveller1_passport_expiry_day
                 + " " + traveller1_passport_expiry_year)
        sleep(2)

        self.driver.execute_script("window.scrollBy(0, 450);")
        sleep(2)
        if payment_method == "paypal":
            flights_booking_page.get_pay_paypal().click()
            log.info("Payment_method: paypal")
        if payment_method == "pay_bank_transfer":
            flights_booking_page.get_pay_bank_transfer().click()
            log.info("Payment_method: pay_bank_transfer")
        if payment_method == "pay_later":
            flights_booking_page.get_pay_later().click()
            log.info("Payment_method: pay_later")
        if payment_method == "pay_stripe":
            flights_booking_page.get_pay_stripe().click()
            log.info("Payment_method: pay_stripe")

        flights_booking_page.get_agree_chb().click()

        if self.verify_element_exist(flights_booking_page.get_hide_btn()):
            self.driver.find_element(*(flights_booking_page.get_hide_btn())).click()

        sleep(2)

        flights_booking_page.get_confirm_booking_btn().click()
        sleep(2)







