
from abc import ABC, abstractmethod
class Repository(ABC): 
 
    @abstractmethod
    def add(self, product):
        raise NotImplementedError
    @abstractmethod
    def delete(self, index):
        raise NotImplementedError
    @abstractmethod
    def update(self, index, **kwargs):
        raise NotImplementedError
    @abstractmethod
    def get(self):
        raise NotImplementedError
    @abstractmethod
    def save(self):
        raise NotImplementedError



 
