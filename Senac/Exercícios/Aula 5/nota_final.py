notas = [6.5, 10, 9.75, 4.5]
#media = sum(notas) / 4

cont = 0
soma = 0

while cont < 4:
    soma = soma + notas[cont]
    cont = cont + 1
resultado = soma / 4

if resultado > 7:
    print(f"Sua média é: {resultado:.2f}. APROVADO!")
else:
    print(f"Sua média é: {resultado:.2f}. REPROVADO!")