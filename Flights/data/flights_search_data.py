from Flights.tools import read_json


class FlightsPageSearchData:
    @staticmethod
    def get_test_data():
        datas = read_json.read_json("flights_search.json")
        arrs = []
        for data in datas.values():
            arrs.append((data.get("test_case_name"),
                         data.get("flights_type"),
                         data.get("one_way"),
                         data.get("round_trip"),
                         data.get("flying_from"),
                         data.get("destination_to"),
                         data.get("depart_date"),
                         data.get("return_date"),
                         data.get("number_of_adults"),
                         data.get("number_of_children"),
                         data.get("number_of_infants"),
                         data.get("expected_result")))
        return arrs
