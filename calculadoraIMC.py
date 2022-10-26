#Declarando variáveis
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso/altura**2 # fómula para calcular imc

#saida de dados 
print("-" * 30)
print("OS dados coletados foram:")
print("Seu nome: ",nome)
print("Sua idade: ",idade," anos")
print("Sua altura: ",altura, " mts")
print("Seu peso ", peso," kgs")
print("Seu IMC = ",imc)

if imc < 16:
    print("MAgreza Grave!")
elif imc < 18.5:
    print("Magreza Leve!")
if imc < 16:
    print("MAgreza Grave!")
elif imc < 18.5:
    print("Magreza Leve!")
elif imc < 25:
    print("Saudável!")
elif imc < 30:
    print("Sobrepeso!!!!!")
elif imc < 35:
    print("Obesidade grau I!!!!")
elif imc < 40:
    print("Obesidade grau 2 ?!")
else :
    print("Obesidade Grau III")