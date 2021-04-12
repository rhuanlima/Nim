#FUNCTION COMPUTADOR ESCOLHE JOGADA DE ACONDO COM O MODULO(INTRUÇOES)
def computador_escolhe_jogada(n,m):
	removidor=0 
	while n%(m+1)!=0:
		n=n-1
		removidor=removidor+1
	return removidor
#FUNCTION JOGADOR
def usuario_escolhe_jogada(n,m):
	n=m
	m=int(input("Insira o Numero: "))
	while m>n or m == 0:
		print("Numero Inserido Esta Incorreto")
		m=int(input("Insira Outro Numero:"))
	return m
#FUNCTION PARTIDA
def partida():
	n=int(input("Quantas peças?:"))
	m=int(input("Limite de peças por jogada?:"))
	if n % (m+1) ==0:
		print("Você começa!")
		while (n>0 or n==0):
			Con=usuario_escolhe_jogada(n,m)
			n=n-Con
			print("O Numero de Peças retiradas Foi",Con)
			if n ==0:
				print("USUARIO GANHOU")
				break
			else:
				Con=computador_escolhe_jogada(n,m)
				n=n-Con
				print("O Numero De Peças Retidas Pelo Computador Foi",Con)
				if n ==0:
					print("O Computador Ganhou!!!")
					break
	else:#Else Caso o Computador Começe
		print("Computador começa!")
		while (n>0):
			Con=computador_escolhe_jogada(n,m)
			n=n-Con
			print("O Numero de Peças Retiradas Pelo Computador",Con)
			if n ==0:
				print("O Computador Ganhou!!!")
				break
			else:
				Con=usuario_escolhe_jogada(n,m)
				n=n-Con
				print("O Numero de Peças Retiradas Foi,",Con)
				if n==0:
					print("Você Ganhou,Parabéns")
					break
def campeonato():# 3 Rodadas(3x-Partida)
	partida()
	print("COMPUTADOR 1 X JOGADOR 0")
	partida()
	print("COMPUTADOR 2 X JOGADOR 0")
	partida()
	print("COMPUTADOR 3 X JOGADOR 0")
#FUNCTION MAIN(INICIALIZADOR DO GAME)
def main():#function main
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()#Space#
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato 2")
    print()#Space#
    selecionador=int(input("Insira o Modo Desejado:"))#selecionando o Modo#
    while selecionador != 1 and selecionador != 2 :
        print("Numero Incorreto,Tente Novamente!")
        print()
        selecionador=int(input("Insira o Modo Desejado:"))#selecionando o Modo#
    if selecionador ==1:#Selecionar-Partida#
        print("Voce escolheu uma partida apenas!")
        partida() # Chamando a Function "Partida"#
    elif selecionador ==2:#Selecionar-Campeonato#
        print("Voce escolheu um campeonato!")
        campeonato() #Chamando a Function "Campeonato"#
main()#Iniciando Game(Main)#
