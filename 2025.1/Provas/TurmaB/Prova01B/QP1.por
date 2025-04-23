programa
{
	
	funcao inicio()
	{
		inteiro qntInteira = 0, qntMeiaEntrada = 0, qntVIP = 0, qntComboFamilia = 0, opcao

		para (inteiro i = 0; i < 10; i++) {
			escreva("Digite 1 para inteira\n")
			escreva("Digite 2 para meia-entrada\n")
			escreva("Digite 3 para VIP\n")
			escreva("Digite 4 para combo família\n")
			escreva("Digite sua opção: ")
			leia(opcao)

			se (opcao == 1) {
				qntInteira++
			} senao se (opcao == 2) {
				qntMeiaEntrada++
			} senao se (opcao == 3) {
				qntVIP++
			} senao se (opcao == 4) {
				qntComboFamilia++
			} senao {
				escreva("Opção invalida\n")
			}
			
		}

		escreva("\nQuantidade de inteiras: ", qntInteira)
		escreva("\nQuantidade de meia-entrada: ", qntMeiaEntrada)
		escreva("\nQuantidade de VIPs: ", qntVIP)
		escreva("\nQuantidade de combo familia: ", qntComboFamilia)
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 661; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */