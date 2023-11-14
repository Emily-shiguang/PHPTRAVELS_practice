from Flights.tools import read_json


class FlightsPageFilterData:
    @staticmethod
    def get_test_data():
        datas = read_json.read_json("flights_filter.json")
        arrs = []
        for data in datas.values():
            arrs.append((data.get("test_case_name"),
                         data.get("all_flights"),
                         data.get("direct"),
                         data.get("stops1"),
                         data.get("stops2"),
                         data.get("price_range_low"),
                         data.get("price_range_high"),
                         data.get("oneway_airlines_selected"),
                         data.get("return_airlines_selected")))
        return arrs
