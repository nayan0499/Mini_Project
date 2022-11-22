from abc import ABC, abstractmethod


class OrderAbstract(ABC):

    @abstractmethod
    def add(self, order):
        raise NotImplementedError

    @abstractmethod
    def delete(self, order):
        raise NotImplementedError

    @abstractmethod
    def update(self, order, update_detail):
        raise NotImplementedError

    @abstractmethod
    def get(self):
        raise NotImplementedError

    @abstractmethod
    def save(self):
        raise NotImplementedError
