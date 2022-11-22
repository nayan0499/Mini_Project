from src.csvhandler.csv import load_from_file, save_to_file
from src.courier.courier_abstract import CourierAbstract
from src.courier.courier import Courier

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


class CourierRepo(CourierAbstract):

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self.list = load_from_file(file_name, Courier)

    def add(self, courier):
        self.list.append(courier)

    def update(self, index, updated_courier):
        selected_courier = self.list[index]
        for k, v in updated_courier.items():
            if k == "name":
                selected_courier.name = v
            elif k == "phone":
                selected_courier.phone = v

    def delete(self, index):
        self.list.pop(index)

    def get(self):
        return self.list

    def save(self):
        save_to_file(self.list, self.file_name, Courier.keys)


courier_repo = CourierRepo(r"C:\Users\NayanGurung\Generation\week7\recent_mini_project - Copy\src\data\courier.csv")
