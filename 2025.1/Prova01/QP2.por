programa
{
	
	funcao inicio()
	{
		real raio, altura, pi = 3.14
		
		escreva("Digite o valor do raio: ")
		leia(raio)
		escreva("Digite a altura do silo: ")
		leia(altura)
		
		real volume = pi * (raio * raio) * altura
		
		se (volume > 500.0) {
			escreva("Volume: ", volume, "\nO silo tem grande capacidade de armazenamento")
		} senao se (volume == 500.0) {
			escreva("Voluma: ", volume, "\nO silo tem capacidade média de armazenamento")
		} senao {
			escreva("Volume: ", volume, "\nO silo tem pequena capacidade de armazenamento")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 545; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */