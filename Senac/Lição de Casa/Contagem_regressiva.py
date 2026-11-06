#Faça um programa para escreve a contagem regressiva do lançamemento de um foguete. 
#O programa deve imprimir 10, 9, 8, 7...1, 0 e Fogo!
from time import sleep
#"from": é o comando reservado para se usado em conjunto com import para carregar partes específicas (como funções, classes ou variáveis) de um módulo para o escopo atua. 
#"sleep": é o comando para pausar a execução do programa atual por um determinado número de segundos.
for cont in range(10, -1, -1):
  print(cont)
  sleep(1)
print("Fogo!")