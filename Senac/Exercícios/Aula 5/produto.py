#Criamndo dicionário com os produtos e seus respectivos preços.
tabela = { "alface":2.00, 
          "tomate":15.00, 
          "batata":5.00, 
          "cenoura":3.00, 
          "abacaxi":7.00, 
          "manga":6.00, 
          "morango":10.00, 
          "uva":8.00, 
          "laranja":4.00, 
          "banana":2.50 }
#Imprimindo a tabela de produtos e preços.
#print(tabela)
while True:
    produto = input("Digite o nome do produto que deseja consultar o preço: ").lower().strip()
    #O comando "lower()" transforma a string em minúscula e o "strip()" remove espaços em branco no início e no final da string.
    if (produto == "sair"):
        break
    elif produto not in tabela:
        print("Produto não encontrado na tabela.")
    else:
        print("O", produto, "custa R$", tabela[produto])
    