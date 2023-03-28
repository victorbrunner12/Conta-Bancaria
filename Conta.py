from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, tipo_conta: str, nome_titular: str, cpf_titular, id_conta: int, saldo: float):
        self.tipo_conta = tipo_conta
        self.nome_titular = nome_titular
        self.cpf_titular = cpf_titular
        self.__id_conta = id_conta
        self.__saldo = saldo

    @property
    def id_conta(self) -> int:
        return self.__id_conta

    @id_conta.setter
    def id_conta(self, value: int):
        self.__id_conta = value

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, value: float):
        self.__saldo = value

    @abstractmethod
    def sacar(self, valor: float):
        pass

    @abstractmethod
    def depositar(self, valor: float):
        pass