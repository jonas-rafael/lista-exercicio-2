print (20*"*")
print ("     Questão 1")
print (20*"*")

while True:
    salario=float(input("Digite o valor do salário: "))

    if salario < 280:
        aumento= (20/100)*salario
        salariofinal= salario + aumento

        print(f"o salário antes do reajuste é {salario}")
        print(f"O percentual do aumento do aumento é de 20")
        print(f"o valor do aumento é {aumento:2f}")
        print(f"O valor do salário reajustado é {salariofinal}")
        print(20 * "*")

    elif salario > 280 and salario <= 700:
        aumento = (20 / 100) * salario
        salariofinal = salario + aumento

        print(f"o salário antes do reajuste é {salario}")
        print(f"O percentual do aumento do aumento é de 20")
        print(f"o valor do aumento é {aumento:2f}")
        print(f"O valor do salário reajustado é {salariofinal}")
        print(20 * "*")

    elif salario > 700 and salario <1500:
        aumento = (20 / 100) * salario
        salariofinal = salario + aumento

        print(f"o salário antes do reajuste é {salario}")
        print(f"O percentual do aumento do aumento é de 20")
        print(f"o valor do aumento é {aumento:2f}")
        print(f"O valor do salário reajustado é {salariofinal}")
        print(20*"*")

    elif salario> 1500:
        aumento = (20 / 100) * salario
        salariofinal = salario + aumento

        print(f"o salário antes do reajuste é {salario}")
        print(f"O percentual do aumento do aumento é de 20")
        print(f"o valor do aumento é {aumento:2f}")
        print(f"O valor do salário reajustado é {salariofinal}")
        print(20 * "*")