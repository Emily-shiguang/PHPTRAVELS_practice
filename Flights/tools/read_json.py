import json

def read_json(filename):
    filepath = "../data/" + filename
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    datas = read_json("flights_search.json")
    print(datas)

    arrs = []
    for data in datas.values():
        print(data)
        arrs.append((data.get("test_case_name"),
                    data.get("one_way"),
                    data.get("round_trip"),
                    data.get("flights_type"),
                    data.get("flying_from"),
                    data.get("destination_to"),
                    data.get("depart_date"),
                    data.get("return_date"),
                    data.get("number_of_adults"),
                    data.get("number_of_children"),
                    data.get("number_of_infants"),
                    data.get("expected_result")))
    print(arrs)