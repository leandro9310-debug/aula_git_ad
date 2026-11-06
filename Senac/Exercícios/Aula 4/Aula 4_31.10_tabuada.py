print("Tabuada")
print(" ")
valor = int(input("Insira qual tabuada você deseja ver: "))

for cont in range(11):
    resultado = valor * cont 
    print(f"{valor} X {cont} = {resultado}")