#Crie uma lista com 5 salários e imprima-os com 10% de aumento. 
lista_salarios = [2500, 1851.51, 3555.55,10500,25255.65]
for salario in lista_salarios:
    novo_salario = salario * 1.10
#No Python, casa decimal é separada por "." e milhar é separada por ",". Para que possamos realizar a conversão para o padrão brasileiro, ao em vez de colocarmos a ",", podmeos subistituir pelo "_".
#Para que possamos reconfigurar e alterar os sinais, precisamos fazer o seguinte comando:
    texto_novo_salario = f"R${novo_salario:_.2f}"
    texto_novo_salario = texto_novo_salario.replace(".",",").replace("_",".")
    print(f"O seu salário, com o reajuste de 10%, ficou em R$ {texto_novo_salario}")
