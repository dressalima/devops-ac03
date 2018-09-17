importar jogovelha
import sys

erroInicializar =  Falsa
jogo = jogovelha.inicializar ()

se  len (jogo) ! =  3 :
	erroInicializar =  Verdadeiro
else :
	para linha no jogo:
		se  len (linha) ! =  3 :
			erroInicializar =  Verdadeiro
		else :
			para o elemento na linha:
				if elemento ! =  ' . ' :
					erroInicializar =  Verdadeiro
se erroInicializar:
	sys.exit ( 1 )
else :
	sys.exit ( 0 )
