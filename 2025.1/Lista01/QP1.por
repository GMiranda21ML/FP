programa
{
	
	funcao inicio()
	{
		real lado1, lado2, lado3

		escreva("Digite o valor do lado 1: ")
		leia(lado1)
		escreva("Digite o valor do lado 2: ")
		leia(lado2)
		escreva("Digite o valor do lado 3: ")
		leia(lado3)

		se ((lado1 + lado2 > lado3) e (lado1 + lado3 > lado2) e (lado2 + lado3 > lado1)) {
			se ((lado1 == lado2) e (lado2 == lado3)) {
				escreva("Triângulo Equilatero")
			} senao se ((lado1 == lado2) ou (lado1 == lado3) ou (lado2 == lado3)) {
				escreva("Triângulo Isósceles")
			} senao {
				escreva("Triângulo Escaleno")
			}
		} senao {
			escreva("Estes valores nao formam um triângulo")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 569; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */