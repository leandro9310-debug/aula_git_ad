programa
{
	funcao inicio()
	{
		inteiro numero

		escreva("Digite um número: ")
		leia(numero)

		escreva(eh_divisivel_por_4_ou_9(numero))
	}

	funcao logico eh_divisivel_por_4_ou_9(inteiro n)
	{
		retorne (n % 4 == 0) ou (n % 9 == 0)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */