from Verificacao import Verificacao

class InputUsuario():
    def ler_tipo_conta(self):
        try:
            tipo_conta = input("Bem vindo!\nDigite (1) - Para abrir uma Conta Poupança\nDigite (2) - Para abrir uma Conta Corrente\n>>")

            return tipo_conta
        except ValueError as ve:
            print(ve)

    def ler_taxa_rendimento(self):
        try:
            taxa_rendimento = input("Digite a taxa de rendimento da conta poupança. (Ex: 12 % ao ano): ")

            return taxa_rendimento
        except ValueError as ve:
            print(ve)

    def ler_cpf_usuario(self):
        try:
            cpf = input("Digite seu CPF formatado com pontos e traços: ")

            if Verificacao().verifica_cpf_valido(cpf):
                return cpf
            else:
                raise ValueError("DIGITE UM CPF VÁLIDO! Tente novamente.")

        except ValueError as ve:
            print(ve)

    def ler_nome_usuario(self):
        try:
            nome = input("Digite o seu nome: ")

            return nome
        except ValueError as ve:
            print(ve)

    def ler_renda_mensal(self):
        try:
            renda_mensal = input("Digite a sua renda mensal: ")

            return renda_mensal
        except Exception as ex:
            print(ex)