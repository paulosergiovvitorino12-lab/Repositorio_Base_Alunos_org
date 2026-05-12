peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

print("IMC:", round(imc, 2))
  

if imc >= 30:
    print("Cuidado com a Saúde")
else:
    print("Tudo ok")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 24.9:
    print("Peso normal")
elif imc < 29.9:
    print("Sobrepeso")
elif imc < 34.9:
    print("Obesidade Grau I")
elif imc < 39.9:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III (mórbida)") 