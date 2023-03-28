from Conta import Conta
from Visualizacao import Visualizacao

class ContaCorrente(Conta):
    def __init__(self, tipo_conta: str, nome_titular: str, cpf_titular, id_conta: int, saldo: float, limite: float):
        super().__init__(tipo_conta=tipo_conta, nome_titular=nome_titular, cpf_titular=cpf_titular, id_conta=id_conta, saldo=saldo)
        self.__limite = limite

    @property
    def limite(self) -> float:
        return self.__limite

    @limite.setter
    def limite(self, value: float):
        self.__limite = value

    def sacar(self, valor: float):
        if valor > self.saldo + self.limite:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor
        Visualizacao(objeto_conta=self).mensagem_saque(valor)

    def depositar(self, valor: float):
        self.saldo += valor
        Visualizacao(objeto_conta=self).mensagem_deposita(valor)

class LimiteDisponibilizado:
    def __init__(self, renda_mensal):
        self.__renda_mensal = renda_mensal

    def calcula_limite(self):
        try:
            limite = float(self.__renda_mensal) * 0.2

            return limite
        except ValueError as ve:
            print(ve)