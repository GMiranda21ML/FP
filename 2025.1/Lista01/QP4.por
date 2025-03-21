programa
{
	
	funcao inicio()
	{
		inteiro opcao
		real c, f

		escreva("Digite 1 para converter de Celsius para Fahrenheit\n")
		escreva("Digite 2 para converter de Fahrenheit para Celsius\n")
		escreva("Digite sua opção: ")
		leia(opcao)

		se (opcao != 1 e opcao != 2) {
			escreva("Opção invalida!")
		} senao {
			se (opcao == 1) {
				escreva("Digite a temperatura em Celsius: ")
				leia(c)
				f = (c * 9/5) + 32
				escreva(c, "ºC -> ", f, "ºF")
			} senao {
				escreva("Digite a temperatura em Fahrenheit: ")
				leia(f)
				c = (f - 32) * 5 / 9
				escreva(f, "ºF -> ", c, "ºC")
			}
			
		}
		
	}
	
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 617; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */