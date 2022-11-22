import csv



def load_from_file(file_name, item_type):
    obj_list = []
    with open(file_name, "r") as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            obj = item_type.dict_to_obj(row)
            obj_list.append(obj)
        return obj_list


def save_to_file(obj_list, file_name, keys):
    with open(file_name, 'w', newline='') as f:
        w = csv.DictWriter(f, keys,
                           quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for x in obj_list:
            w.writerow(x.__dict__)
