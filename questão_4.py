

print (20*"*")
print ("     Questão 4")
print (20*"*")


kmoran=float(input("Digite a quantidade de morangos em Kg: "))
kmaça=float(input("Digite a quantidade de maçã em Kg: "))

if kmoran<=5:
    morango=2.50
    soma=kmoran*morango
    print(f"O preço total dos morangos é: {soma} Reais.")
elif kmoran>=6:
    morango=2.20
    soma=kmoran+morango
    print(f"O preço total dos morangos é: {soma} Reais.")


if kmaça<=5:
    maça=1.80
    soma1=kmaça*maça
    print(f"O preço total das maças é: {soma1} Reais.")
elif kmaça>=6:
    maça=1.50
    soma1=kmaça*maça
    print(f"O preço total das maças é: {soma1} Reais.")

