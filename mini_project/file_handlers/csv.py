import csv 


def load_from_file(list_name, item_type):
    list = []
    with open(f"mini_project/data/{list_name}.csv", "r") as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            obj = item_type.dict_to_obj(row)
            list.append(obj)
        return list

def save_to_file(list):
    # You will need 'wb' mode in Python 2.x
    with open(f'mini_project/data/{list.list_name}.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, list.item_type.keys(),
                            quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for x in list.items:
            w.writerow(x.__dict__)