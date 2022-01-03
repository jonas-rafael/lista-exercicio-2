print (20*"*")
print ("     Questão 3")
print (20*"*")


#Faça um programa que faça cinco perguntas para uma pessoa sobre um crime. As perguntas são:
#- Telefonou para a vítima?
#- Esteve no local do crime?
#- Mora perto da vítima?
#- Devia para a vítima?
#- Já trabalhou com a vítima?

while True:
    print("Responda usando 1 para sim ou 0 para não, qualquer outra forma resposta não será aceita!")
    r1=int(input("Você telefonou para vitima? "))
    r2=int(input("Você esteve no local do crime? "))
    r3=int(input("Você mora perto da vitima? "))
    r4=int(input("Você devia para vitima? "))
    r5=int(input("Você já trabalho com a vitima?"))
    respostas= r1+r2+r3+r4+r5
    if r1 != 1 or 0 and r2 != 1 or 0 and r3 != 1 or 0 and r4 != 1 or 0 and r5 != 1 or 0:
        print("Opção invalida!")
        break
    elif respostas < 2:
        print("Suspeito!")
    elif respostas >= 3 and respostas <=4:
        print("Cumplice!")
    elif respostas >= 5:
        print("Assassino!")
    elif respostas <= 0:
        print("Inocente!")

