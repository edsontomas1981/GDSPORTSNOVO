from abc import ABC, abstractmethod


class Carrinho_lista:
    def __init__(self):
        pass

    @abstractmethod
    def create_or_update(self):
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    
