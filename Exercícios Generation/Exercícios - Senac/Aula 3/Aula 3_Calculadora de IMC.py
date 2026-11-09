print("Calculadora de IMC")
# Pedir para a pessoa inserir os seus dados
idade=int(input("Digite sua idade: "))
peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura: "))
# Operação de calculo do IMC
result1=altura*altura
imc=peso/result1
# Condicionamento
if(idade>=60) and (imc<22):
    print("Abaixo do peso")
elif(imc<=27):
    print("Peso normal")
elif(imc<=29.99):
    print("Sobrepeso")
elif(imc >= 30):
    print("Obsidade")
elif(idade<60) and (imc<18.5):
        print("Abaixo do peso")
elif(imc<=24.9):
        print("Peso normal")
elif(imc<=29.9):
        print("Sobrepeso")
elif(imc<=34.9):
        print("Obesidade Grau I")
elif(imc<=39.9):
        print("Obesidade Grau II")
elif(imc>=40):
        print("Obesidade Mórbida")