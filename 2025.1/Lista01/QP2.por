programa
{
	
	funcao inicio()
	{
		inteiro numeroTotalEleitores, votosBrancos, votosValidos

		escreva("Digite a quantidade de total de eleitoras: ")
		leia(numeroTotalEleitores)
		escreva("Digite a quantidade de votos brancos: ")
		leia(votosBrancos)
		escreva("Digite a quantidade de votos validos: ")
		leia(votosValidos)

		real percentualBrancos = (votosBrancos * 100.0) / numeroTotalEleitores
		real percentualValidos = (votosValidos * 100.0) / numeroTotalEleitores

		escreva("\nPercentual de votos brancos/nulos: ", percentualBrancos)
		escreva("\nPercentual de votos validos: ", percentualValidos)

		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 622; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */