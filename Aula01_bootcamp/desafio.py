CONSTANTE_BONUS = 1000
#1 O programa deve começar solicitando ao usuário que insira seu nome.
nome_usuario = input("Por favor, insira seu nome: ")
#2 Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário.#  Considere que este valor pode ser um número decimal.
salario_usuario = float(input("Por favor, insira o valor do seu salário: "))
#3 Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
bonus_usuario = float(input("Por favor, insira o seu bônus recebido: "))
#4 O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
valor_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario
#5 Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
print(f"O usuário {nome_usuario}, possui o seu valor bônus foi de {valor_bonus}.")
