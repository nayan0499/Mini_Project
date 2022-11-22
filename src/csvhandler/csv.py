import csv


def load_from_file(file_name, item_type):
    list = []
    with open(file_name, "r") as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            obj = item_type.dict_to_obj(row)
            list.append(obj)
        return list

def save_to_file(list, file_name, keys):
    with open(file_name, 'w', newline='') as f:
        w = csv.DictWriter(f, keys,
                            quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for x in list:
            w.writerow(x.__dict__)
