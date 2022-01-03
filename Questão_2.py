
print (20*"*")
print ("     Questão 2")
print (20*"*")
while True:
    nota1=float(input("Digite a primeira nota do aluno: "))
    nota2=float(input("Digite a segunda nota do aluno: "))
    media= (nota1+nota2)/2
    if media >9:
        print(f"a média do aluno é : {media}")
        print(f"O conceito do aluno é: A")
        print(f"A situação é: Aprovado com Distinção")
    elif media <9 and media>7.5:
        print(f"a média do aluno é : {media}")
        print(f"O conceito do aluno é: B")
        print(f"A situação é: Aprovado")
    elif media<7.5 and media >6:
        print(f"a média do aluno é : {media}")
        print(f"O conceito do aluno é: C")
        print(f"A situação é: Aprovado")
    elif media<6 and media>4:
        print(f"a média do aluno é : {media}")
        print(f"O conceito do aluno é: D")
        print(f"A situação é: Reprovado")
    elif media<4:
        print(f"a média do aluno é : {media}")
        print(f"O conceito do aluno é: E")
        print(f"A situação é: Reprovado")

