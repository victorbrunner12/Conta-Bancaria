# Sistema Bancário
Este é um sistema bancário básico que permite criar contas correntes e poupanças e realizar operações como saque e depósito nessas contas. O sistema usa a linguagem de programação Python.

##OBS: Sistema esta na branch MASTER

# Como usar
Para usar o sistema, execute o arquivo main.py. O programa perguntará que tipo de conta você deseja criar e, em seguida, pedirá algumas informações sobre o titular da conta, como nome e CPF. Depois de inserir essas informações, o sistema criará uma conta bancária e permitirá que você realize operações nessa conta.

O sistema suporta dois tipos de conta:

Conta Poupança  
Conta Corrente

# Classes  

# Conta
Essa é uma classe abstrata que define os atributos e métodos comuns a todas as contas. Ela recebe como argumentos o tipo de conta, o nome e CPF do titular da conta, o ID da conta e o saldo atual. Ela possui métodos abstratos para saque e depósito, que são implementados nas subclasses.

# Conta Poupança
A ContaPoupanca é uma conta de poupança que permite que o titular da conta deposite dinheiro e ganhe juros sobre o saldo. Para criar uma conta poupança, insira o valor 1 quando o programa perguntar qual tipo de conta deseja criar.

Ao criar uma conta poupança, o sistema solicitará algumas informações adicionais, como a taxa de rendimento da conta.

## Funções
ContaPoupanca.depositar(valor: float)  
Essa função permite depositar uma determinada quantia em dinheiro na conta poupança.  
O parâmetro valor é a quantia a ser depositada.

ContaPoupanca.sacar(valor: float)  
Essa função permite sacar uma determinada quantia em dinheiro da conta poupança.  
O parâmetro valor é a quantia a ser sacada. Se o saldo na conta não for suficiente para o saque, uma mensagem de erro será exibida.

# Conta Corrente
A ContaCorrente é uma conta corrente que permite que o titular da conta deposite dinheiro, faça pagamentos e saques. Para criar uma conta corrente, insira o valor 2 quando o programa perguntar qual tipo de conta deseja criar.

Ao criar uma conta corrente, o sistema solicitará algumas informações adicionais, como a renda mensal do titular da conta.

## Funções
ContaCorrente.depositar(valor: float)  
Essa função permite depositar uma determinada quantia em dinheiro na conta corrente.  
O parâmetro valor é a quantia a ser depositada.

ContaCorrente.sacar(valor: float)  
Essa função permite sacar uma determinada quantia em dinheiro da conta corrente.  
O parâmetro valor é a quantia a ser sacada. Se o saldo na conta não for suficiente para o saque, uma mensagem de erro será exibida.

# LimiteDisponibilizado
Essa é uma classe que calcula o limite de crédito disponível para uma conta corrente com base na renda mensal do titular da conta.

## Funções

calcula_limite()  
Essa função é responsável por calcular o limite que essa conta está habilitado a ter de acordo com a renda mensal do usuário.

# InputUsuario
Essa é uma classe que lê as entradas do usuário e valida os dados inseridos.

## Funções

ler_tipo_conta()  
Essa função recebe do usuário o tipo de conta que ele deseja abrir.

ler_taxa_rendimento()  
Essa função recebe do usuário a taxa de rendimento da conta do usuário.

ler_cpf_usuario()  
Essa função recebe do usuário o cpf dele. Formatado ou nao formatado.

ler_nome_usuario()  
Essa função recebe do usuário o nome dele.

ler_renda_mensal()  
Essa função rece do usuário a renda mensal dele. (OBS: Caso abra Conta Corrente, o limite é ajustado de acordo com a renda mensal)

# Visualizacao
Essa é uma classe que exibe as informações da conta na tela do usuário, como o saldo atual, o ID da conta e outras informações relevantes. Ela também exibe mensagens correspondentes a cada operação de saque e depósito realizada.

## Funções

visualiza_dados_conta_corrente()  
Essa função é responsável por printar na tela os dados da Conta Corrente instanciada.

visualiza_dados_conta_poupanca()  
Essa função é responsável por printar na tela os dados da Conta Poupança instanciada.

mensagem_saque()  
Essa função é responsavel por mostrar uma mensagem quando efetuado o saque.

mensagem_deposita()  
Essa função é responsavel por mostrar uma mensagem quando efetuado um depósito.

# Verificacao
Essa é uma classe que verifica informações de usuário, por enquanto tem apenas uma função.

## Funções

verifica_cpf_valido(cpf)  
Essa função é responsável por verificar se o CPF do usuário é válido. Se for válido ele retorna True, se não False.
O parâmetro 'cpf' é o CPF do usuário.
