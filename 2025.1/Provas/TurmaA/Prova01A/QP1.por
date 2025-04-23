programa
{
	
	funcao inicio()
	{
		inteiro qntDinheiro = 0, qntCredito = 0, qntDebito = 0, qntPix = 0, opcao

		para (inteiro i = 0; i < 10; i++) {
			escreva("Digite 1 para pagar em dinheiro\n")
			escreva("Digite 2 para pagar com cartão de crédito\n")
			escreva("Digite 3 para pagar com cartão de débito\n")
			escreva("Digite 4 para pagar com pix\n")
			escreva("Digite sua opção: ")
			leia(opcao)

			se (opcao == 1) {
				qntDinheiro++
			} senao se (opcao == 2) {
				qntCredito++
			} senao se (opcao == 3) {
				qntDebito++
			} senao se (opcao == 4) {
				qntPix++
			} senao {
				escreva("Opção invalida\n")
			}
			
		}

		escreva("\nQuantidade de pagamentos em dinheiro: ", qntDinheiro)
		escreva("\nQuantidade de pagamentos com cartão de crédito: ", qntCredito)
		escreva("\nQuantidade de pagamentos com cartão de débito: ", qntDebito)
		escreva("\nQuantidade de pagamentos com pix: ", qntPix)
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 909; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */