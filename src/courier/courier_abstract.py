
from abc import ABC, abstractmethod
class CourierAbstract(ABC): 
 
    @abstractmethod
    def add(self, product):
        pass
    @abstractmethod
    def delete(self, index):
        pass
    @abstractmethod
    def update(self, index, **kwargs):
        pass
    @abstractmethod
    def get(self):
        pass
    @abstractmethod
    def save(self):
        pass



 
