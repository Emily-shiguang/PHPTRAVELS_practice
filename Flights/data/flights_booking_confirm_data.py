from Flights.tools import read_json


class FlightsBookingConfirmData:
    @staticmethod
    def get_test_data():
        datas = read_json.read_json("flights_booking_confirm.json")
        arrs = []
        for data in datas:
            arrs.append((data.get("test_case_name"),
                        data.get("proceed")))

        return arrs
