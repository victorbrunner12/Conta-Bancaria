from ContaCorrente import ContaCorrente, LimiteDisponibilizado
from ContaPoupanca import ContaPoupanca
from InputUsuario import InputUsuario
from Visualizacao import Visualizacao

if __name__=='__main__':
    tipo_conta = InputUsuario().ler_tipo_conta()
    if tipo_conta == '1' or tipo_conta == '2':
        nome = InputUsuario().ler_nome_usuario()
        cpf = InputUsuario().ler_cpf_usuario()

        if tipo_conta == '1':
            taxa_de_rendimento = InputUsuario().ler_taxa_rendimento()
            conta_poupanca = ContaPoupanca(tipo_conta=tipo_conta, nome_titular=nome, cpf_titular=cpf, id_conta=1, saldo=1000.00, taxa_de_rendimento=taxa_de_rendimento)

            Visualizacao(objeto_conta=conta_poupanca).visualiza_dados_conta_poupanca()

            conta_poupanca.depositar(50000)
            conta_poupanca.sacar(50000)

            conta_poupanca.sacar(50000) # Gera erro para demonstrar tratamento com Try/Except

        elif tipo_conta == '2':
            renda_mensal = InputUsuario().ler_renda_mensal()
            limite = LimiteDisponibilizado(renda_mensal=renda_mensal).calcula_limite()
            conta_corrente = ContaCorrente(tipo_conta=tipo_conta, nome_titular=nome, cpf_titular=cpf, id_conta=2, saldo=1500.00, limite=limite)

            Visualizacao(objeto_conta=conta_corrente).visualiza_dados_conta_corrente()

            conta_corrente.depositar(50000)
            conta_corrente.sacar(50000)
            conta_corrente.sacar(50000) # Gera erro para demonstrar tratamento com Try/Except
        else:
            raise ValueError("Tipo de conta inválido.")
    else:
        raise ValueError("Tipo de conta inválido.")

