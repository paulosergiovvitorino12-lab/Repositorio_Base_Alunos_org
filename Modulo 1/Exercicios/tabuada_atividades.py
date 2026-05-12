n = int(input("Digite um numero: "))
v = int(input("Quantas vezs vai ser exibida?: "))
numero_final = int(input("DIgite aonde a tabuada deve acabar: "))

for i in range(v,numero_final + 1):
    print(n, "x", i, "=", n*i)
  