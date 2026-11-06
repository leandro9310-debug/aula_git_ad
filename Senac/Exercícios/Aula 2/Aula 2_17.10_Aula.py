#Declarando e atribuindo valores as variáveis string
nome="Leandro"
sobrenome="Soares"
#print(nome)
#print(sobrenome)
nomecompleto=nome+" "+sobrenome
#print(nomecompleto.upper())
#Declaração de tipo de Dados INT
idade=33
#print(idade)
print (" ")
print("Cadastro de Funcionário")
nomedofuncionário=input("Digite seu primeiro nome: ")
sobrenomedofuncionário=input("Digite o seu sobrenome: ")
nomecompletodofun=nomedofuncionário+" "+sobrenomedofuncionário
idadedocolaborador=input("Qual a sua idade: ")
print("Nome em Sistema: {}".format(nomecompletodofun).upper())
print("Sua idade é: {}".format(idadedocolaborador))
print(" ")
#Tentativa de colocar tudo em uma mesma frase
print("Nome em Sistema é: {} e sua idade é: {}".format(nomecompletodofun.upper(),idadedocolaborador))
