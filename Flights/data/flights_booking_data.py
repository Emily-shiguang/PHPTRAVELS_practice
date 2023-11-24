from Flights.tools import read_json


class FlightsBookingData:
    @staticmethod
    def get_test_data():
        datas = read_json.read_json("flights_booking.json")
        arrs = []
        for data in datas.values():
            arrs.append((data.get("test_case_name"),
                         data.get("oneway_flight_selected_for_booking"),
                         data.get("user_first_name"),
                         data.get("user_last_name"),
                         data.get("user_email"),
                         data.get("user_phone"),
                         data.get("user_address"),
                         data.get("user_nationality"),
                         data.get("user_current_country"),
                         data.get("traveller1_title"),
                         data.get("traveller1_firstname"),
                         data.get("traveller1_lastname"),
                         data.get("traveller1_nationality"),
                         data.get("traveller1_dob_month"),
                         data.get("traveller1_dob_day"),
                         data.get("traveller1_dob_year"),
                         data.get("traveller1_passport_no"),
                         data.get("traveller1_passport_issuance_month"),
                         data.get("traveller1_passport_issuance_day"),
                         data.get("traveller1_passport_issuance_year"),
                         data.get("traveller1_passport_expiry_month"),
                         data.get("traveller1_passport_expiry_day"),
                         data.get("traveller1_passport_expiry_year"),
                         data.get("payment_method")))
        return arrs
