print (20*"*")
print ("     Questão 3")
print (20*"*")

resp=[]

resp.append(input("Você telefonou para vitima? ").lower())
resp.append(input("Você esteve no local do crime? ").lower())
resp.append(input("Você mora perto da vitima? ").lower())
resp.append(input("Você devia para vitima? ").lower())
resp.append(input("Você já trabalho com a vitima?").lower())


somaresp = 0
for i in resp:
    if i == "sim":
        somaresp += 1


if  somaresp < 2:
    print("Suspeito!")
elif somaresp >= 3 and somaresp <=4:
    print("Cumplice!")
elif somaresp >= 5:
    print("Assassino!")
elif somaresp <= 0:
    print("Inocente!")