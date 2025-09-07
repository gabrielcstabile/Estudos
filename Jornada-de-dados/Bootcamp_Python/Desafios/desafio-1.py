"""
Desafio Aula 1
Escreva um programa em Python que solicita ao usuário:
- Nome
- Salário mensal
- Valor do bônus recebido

O programa deve imprimir uma mensagem saudando o usuário
e informando o valor do bônus em comparação ao salário.
"""
"""
Desafio Aula 1
Solicita nome, salário mensal e percentual de bônus do usuário.
Exibe uma saudação personalizada e o valor final do bônus.
"""

# Constante de acréscimo fixo ao bônus
CONSTANTE_BONUS = 1000


def ler_float(mensagem: str, minimo: float = 0) -> float:
    """
    Lê um valor float digitado pelo usuário, garantindo que seja numérico
    e maior ou igual a um mínimo definido.

    Args:
        mensagem (str): Texto exibido para solicitar a entrada.
        minimo (float, opcional): Valor mínimo permitido. Padrão é 0.

    Returns:
        float: O valor válido digitado pelo usuário.
    """
    while True:
        try:
            valor: float = float(input(mensagem))
            if valor < minimo:
                print(f"⚠️ O valor não pode ser menor que {minimo}. Tente novamente.\n")
                continue
            return valor
        except ValueError:
            print("⚠️ Entrada inválida! Digite apenas números.\n")
        except KeyboardInterrupt:
            print("\n❌ Operação cancelada pelo usuário (Ctrl+C).")
            exit(1)  # Encerra o programa de forma controlada

try:
    # Entrada de dados
    nome: str = input("Digite o seu nome: ")
    salario: float = ler_float("Digite o seu salário: R$ ", minimo=0)
    bonus_percentual: float = ler_float("Digite o bônus em percentual (%): ", minimo=0)

    # Cálculo do bônus (convertendo percentual em fração)
    valor_bonus: float = CONSTANTE_BONUS + salario * (bonus_percentual / 100)

    # Saída formatada
    print(f"\nOlá {nome}, tudo bem?")
    print(f"Seu salário é R$ {salario:.2f}")
    print(f"O valor do seu bônus é: R$ {valor_bonus:.2f}")

except KeyboardInterrupt:
    print("\n❌ Operação cancelada pelo usuário (Ctrl+C).")
