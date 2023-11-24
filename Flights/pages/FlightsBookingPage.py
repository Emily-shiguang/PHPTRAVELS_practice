from Flights import pages

class FlightsBookingPage:
    def __init__(self, driver):
        self.driver = driver

    def get_user_firstname(self):
        return self.driver.find_element(*pages.user_first_name)

    def get_user_lastname(self):
        return self.driver.find_element(*pages.user_last_name)

    def get_user_email(self):
        return self.driver.find_element(*pages.user_email)

    def get_user_phone(self):
        return self.driver.find_element(*pages.user_phone)

    def get_user_address(self):
        return self.driver.find_element(*pages.user_address)

    def get_user_nationality(self):
        return self.driver.find_element(*pages.user_nationality)

    def get_user_nationality_search(self):
        return self.driver.find_element(*pages.user_nationality_search)
    def get_user_current_country(self):
        return self.driver.find_element(*pages.user_current_country)

    def get_user_current_country_search(self):
        return self.driver.find_element(*pages.user_current_country_search)

    def get_traveller1_title(self):
        return self.driver.find_element(*pages.traveller1_title)

    def get_traveller1_firstname(self):
        return self.driver.find_element(*pages.traveller1_firstname)

    def get_traveller1_lastname(self):
        return self.driver.find_element(*pages.traveller1_lastname)

    def get_traveller1_nationality(self):
        return self.driver.find_element(*pages.traveller1_nationality)

    def get_traveller1_dob_month(self):
        return self.driver.find_element(*pages.traveller1_dob_month)

    def get_traveller1_dob_day(self):
        return self.driver.find_element(*pages.traveller1_dob_day)

    def get_traveller1_dob_year(self):
        return self.driver.find_element(*pages.traveller1_dob_year)

    def get_traveller1_passport_no(self):
        return self.driver.find_element(*pages.traveller1_passport_no)

    def get_traveller1_passport_issuance_month(self):
        return self.driver.find_element(*pages.traveller1_passport_issuance_month)

    def get_traveller1_passport_issuance_day(self):
        return self.driver.find_element(*pages.traveller1_passport_issuance_day)

    def get_traveller1_passport_issuance_year(self):
        return self.driver.find_element(*pages.traveller1_passport_issuance_year)

    def get_traveller1_passport_expiry_month(self):
        return self.driver.find_element(*pages.traveller1_passport_expiry_month)

    def get_traveller1_passport_expiry_day(self):
        return self.driver.find_element(*pages.traveller1_passport_expiry_day)

    def get_traveller1_passport_expiry_year(self):
        return self.driver.find_element(*pages.traveller1_passport_expiry_year)

    def get_pay_paypal(self):
        return self.driver.find_element(*pages.pay_paypal)

    def get_pay_bank_transfer(self):
        return self.driver.find_element(*pages.pay_bank_transfer)

    def get_pay_later(self):
        return self.driver.find_element(*pages.pay_later)

    def get_pay_stripe(self):
        return self.driver.find_element(*pages.pay_stripe)

    def get_agree_chb(self):
        return self.driver.find_element(*pages.agree_chb)

    def get_hide_btn(self):
        return pages.hide_btn

    def get_confirm_booking_btn(self):
        return self.driver.find_element(*pages.confirm_booking_btn)