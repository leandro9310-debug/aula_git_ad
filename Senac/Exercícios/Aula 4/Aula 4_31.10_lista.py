lista_produtos = ["Pão", "Café", "Leite", "Queijo", "Presunto"]

#Para que conseguimos imprimir uma lista de compras uma debaixo da outra, precisamos seguir o modelo a baixo:
#print(lista_produtos[0]), print(lista_produtos[1]), print(lista_produtos[2]), print(lista_produtos[3]), print(lista_produtos[4])

#Comando para aincluirmos um novo item na lista, precisamos colocar o comando ".append":
lista_produtos.append("Farinha de trigo")
print(lista_produtos)

#Comando para excluirmosm um item na lista, precisamos colocar o comando ".remove":
lista_produtos.remove("Café")
print(lista_produtos)