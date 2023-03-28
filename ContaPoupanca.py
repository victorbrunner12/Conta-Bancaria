from Conta import Conta
from Visualizacao import Visualizacao

class ContaPoupanca(Conta):
    def __init__(self, tipo_conta: str, nome_titular: str, cpf_titular, id_conta: int, saldo: float, taxa_de_rendimento: str):
        super().__init__(tipo_conta=tipo_conta, nome_titular=nome_titular, cpf_titular=cpf_titular, id_conta=id_conta, saldo=saldo)
        self.__taxa_de_rendimento = taxa_de_rendimento
        self.__taxa_anual = TaxaRendimento(self.taxa_de_rendimento).get_taxa_anual()

    @property
    def taxa_de_rendimento(self) -> str:
        return self.__taxa_de_rendimento

    @taxa_de_rendimento.setter
    def taxa_de_rendimento(self, value: str):
        self.__taxa_de_rendimento = value
        self.__taxa_anual = TaxaRendimento(self.taxa_de_rendimento).get_taxa_anual()

    @property
    def taxa_anual(self) -> float:
        return self.__taxa_anual

    @taxa_anual.setter
    def taxa_anual(self, value: float):
        self.__taxa_anual = value

    def sacar(self, valor: float):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor
        Visualizacao(objeto_conta=self).mensagem_saque(valor)

    def depositar(self, valor: float):
        self.saldo += valor
        Visualizacao(objeto_conta=self).mensagem_deposita(valor)

class TaxaRendimento:
    def __init__(self, taxa: str):
        self.__taxa = taxa

    @property
    def taxa(self) -> str:
        return self.__taxa

    @taxa.setter
    def taxa(self, value: str):
        self.__taxa = value

    def _get_multiplicador_taxa(self):
        if "seg" in self.taxa.lower() or "segundos" in self.taxa.lower():
            return 60 * 60 * 24 * 365
        elif "min" in self.taxa.lower() or 'minutos' in self.taxa.lower():
            return 60 * 24 * 365
        elif "hora" in self.taxa.lower() or 'horas' in self.taxa.lower():
            return 24 * 365
        elif "dia" in self.taxa.lower() or 'dias' in self.taxa.lower():
            return 365
        elif "mes" in self.taxa.lower() or 'm' in self.taxa.lower():
            return 12
        elif "ano" in self.taxa.lower() or 'a' in self.taxa.lower():
            return 1
        else:
            raise ValueError("Taxa inválida")

    def get_taxa_anual(self) -> float:
        taxa_anual = float(self.taxa.split("%")[0])
        multiplicador_taxa = self._get_multiplicador_taxa()
        return taxa_anual * multiplicador_taxa