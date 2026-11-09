print("CALCULADORA")
print(" ")
valor1=float(input("Insira o primeiro valor: "))
operador=input("Insira o sinal da operação: ")
valor2=float(input("Insira o segundo valor: "))
print(" ")
if(operador=="+"):
    resultado=valor1 + valor2
elif(operador=="-"):
    resultado=valor1 - valor2
elif(operador=="*"):
    resultado = valor1 * valor2
elif(operador=="/"):
    resultado = valor1 / valor2
else:
    print("Operador Inválido!")
print("O resultado da operação é: ",resultado)