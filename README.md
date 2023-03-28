# Sistema de Contas Bancárias
Esse sistema é uma simulação de um sistema bancário que permite a criação e manipulação de contas corrente e poupança.

# Funcionalidades
# InputUsuario
A classe InputUsuario é responsável por coletar as informações do usuário através do input do terminal. Ela possui os seguintes métodos:

ler_tipo_conta(): lê o tipo de conta que o usuário deseja criar (1 para poupança, 2 para corrente).
ler_nome_usuario(): lê o nome do usuário.
ler_cpf_usuario(): lê o CPF do usuário.
ler_taxa_rendimento(): lê a taxa de rendimento da conta poupança.
ler_renda_mensal(): lê a renda mensal do usuário.
Visualizacao
A classe Visualizacao é responsável pela exibição de mensagens na tela. Ela possui os seguintes métodos:

mensagem_saque(valor): exibe uma mensagem informando o valor sacado da conta.
mensagem_deposito(valor): exibe uma mensagem informando o valor depositado na conta.
visualiza_dados_conta_poupanca(): exibe na tela as informações da conta poupança.
visualiza_dados_conta_corrente(): exibe na tela as informações da conta corrente.

# Conta
A classe abstrata Conta é a classe base para as classes ContaPoupanca e ContaCorrente. Ela possui os seguintes métodos abstratos que devem ser implementados pelas subclasses:

sacar(valor): método abstrato que realiza o saque de um valor da conta.
depositar(valor): método abstrato que realiza o depósito de um valor na conta.
Além disso, a classe Conta possui os seguintes atributos e métodos:

id_conta: atributo que armazena o ID da conta.
saldo: atributo que armazena o saldo da conta.
__init__(tipo_conta, nome_titular, cpf_titular, id_conta, saldo): método construtor que inicializa os atributos da conta.

# ContaCorrente
A classe ContaCorrente é uma subclasse de Conta que representa uma conta corrente. Ela possui os seguintes atributos e métodos:

limite: atributo que armazena o limite de crédito da conta corrente.
sacar(valor): método que realiza o saque de um valor da conta corrente. Caso o valor do saque seja maior do que o saldo somado ao limite de crédito, uma exceção é lançada informando que o saldo é insuficiente. Caso contrário, o valor do saque é subtraído do saldo da conta e uma mensagem é exibida informando o valor do saque.
depositar(valor): método que realiza o depósito de um valor na conta corrente. O valor do depósito é adicionado ao saldo da conta e uma mensagem é exibida informando o valor depositado.
