from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self,nome,preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    #esse método sirva como um modelo para que outras classes derivadas o implementem.
    def aplicar_desconto(self):
        pass