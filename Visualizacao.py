

class Visualizacao:
    def __init__(self, objeto_conta):
        self.objeto_conta = objeto_conta

    def visualiza_dados_conta_corrente(self):
        print(f'ID da conta: {self.objeto_conta.id_conta}\nSaldo: {self.objeto_conta.saldo}\nLimite: {self.objeto_conta.limite}')

    def visualiza_dados_conta_poupanca(self):
        print(
            f'ID da conta: {self.objeto_conta.id_conta}\nSaldo: {self.objeto_conta.saldo}\nTaxa de rendimento: {self.objeto_conta.taxa_de_rendimento}\nTaxa de rendimento anual: {self.objeto_conta.taxa_anual} %')

    def mensagem_saque(self, valor_saque):
        print(f"Sucesso! Você sacou {valor_saque} R$\nSeu saldo agora é = {self.objeto_conta.saldo} R$")

    def mensagem_deposita(self, valor_deposito):
        print(f"Sucesso! Você depositou {valor_deposito}R$\nSeu saldo agora é = {self.objeto_conta.saldo} R$")