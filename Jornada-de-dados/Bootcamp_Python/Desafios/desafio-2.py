# Você foi contratado para desenvolver um programa que valide informações básicas de um funcionário e calcule o valor do bônus que ele receberá.

# O programa deve:

# Validar o nome do funcionário:

# Não pode estar vazio.
# Não pode conter apenas números.

# Validar o salário:

# O valor deve ser positivo.
# Se a entrada for inválida (não numérica ou negativa), deve solicitar novamente.

# Validar o bônus:

# O valor também deve ser positivo.
# Caso contrário, deve solicitar novamente.

# Exibir o resultado:

# Após as três validações, o programa deve calcular o valor do bônus usando a fórmula:

# bônus_recebido = 1000 + salário * bônus

# E então mostrar a seguinte mensagem formatada:
# O valor do bônus do [nome] é de R$ [bônus_recebido]

nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido is not True:
    try:
        nome: str = input("Digite o seu nome: ")
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")            
        elif nome.isdigit():
            raise ValueError("O nome não deve conter números.")            
        else:
            nome_valido = True
            print("Nome válido: ", nome)

    except ValueError as e:
        print(e)

        
while salario_valido is not True:
    try:
        salario = 10000.0
        if salario < 0:
            print("Por favor, digite um valor positivo para o salário.")
        else:
            salario_valido = True
    except ValueError:
        print("Entrada inválida para o salário, por favor, digite um número.")

while bonus_valido is not True:
    try:
        bonus = 3.0
        if bonus < 0:
            print ("Por favor, digite um nº positivo para o bônus")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada inválida, digite um número.")

bonus_recebido = 1000 + salario * bonus

print(f"O valor do bônus do {nome} é de R$ {bonus_recebido}")
        