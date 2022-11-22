from abc import ABC, abstractmethod


class CourierAbstract(ABC):

    @abstractmethod
    def add(self, courier):
        pass

    @abstractmethod
    def delete(self, index):
        pass

    @abstractmethod
    def update(self, index, updated_courier):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def save(self):
        pass
