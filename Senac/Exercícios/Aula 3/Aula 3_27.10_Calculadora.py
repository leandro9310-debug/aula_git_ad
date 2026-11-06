print("CALCULADORA")
print(" ")
valor1=float(input("Insira o primeiro valor: "))
operador=input("Insira o sinal da operação(+, -, *, /, =): ")
valor2=float(input("Insira o segundo valor: "))
print(" ")
if(operador=="+"):
    resultado=valor1 + valor2
else:
    if(operador=="-"):
        resultado=valor1 - valor2
    else:
        if(operador=="*"):
            resultado = valor1 * valor2
        else:
            if(operador=="/"):
                resultado = valor1 / valor2
                if valor2 == "0"
                else:
                    print("Erro:Não se faz divisão por 0!")
                print("Operador Inválido!")
print(f"O resultado da operação é: {resultado:.2f}")