from Flights.tools import read_json


class FlightsBookingData:
    @staticmethod
    def get_test_data():
        datas = read_json.read_json("flights_booking.json")
        arrs = []
        for data in datas.values():
            arrs.append((data.get("test_case_name"),
                         data.get("oneway_flight_selected_for_booking")))
        return arrs