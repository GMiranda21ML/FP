programa
{
	
	funcao inicio()
	{
		real raio, pi = 3.14
		
		escreva("Digite o valor do raio: ")
		leia(raio)
		
		real area = pi * (raio * raio)
		
		se (area > 78.5) {
			escreva("Área: ", area, "\nA piscina é grande")
		} senao se (area == 78.5) {
			escreva("Área: ", area, "\nA piscina tem tamanho médio")
		} senao {
			escreva("Área: ", area, "\nA piscina é pequena")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 383; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */