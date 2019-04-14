class player:
    def __init__(self):
        self.nome = None

    def ref(self, registro):
        self.nome = registro

'''
made by: https://github.com/auzne [code]
         https://github.com/Hokusho12 [history]
'''

jogo = player()

print('A MORTE DE FELIPE NETO')

p0 = str(input('Olá amiguinho você quer jogar?\n[S]im\n[N]ão\n')).upper()
if p0 != 'S':
    quit()

name = str(input('Qual seu nome: '))
jogo.ref(name)

print('Olá '+name+', bem-vindo a NerdLand')

p1 = str(input('O que faz aqui velho rapaz?\n[M]atar o Felipe Neto\n[D]ivertir-se\n[C]ONHECER O FELIPE NETO\n')).upper()
if p1 == 'M':
    print('PARABENS, VOCÊ REVELOU SEU PLANO IMBECIL, AGORA VOU PINTAR SEU CABELO ANTES QUE VOCÊ ME MATE HAHAHA')
    print('Felipe Neto pintou seu cabelo e você pereceu :(')
    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= FIM =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
    quit()
elif p1 == 'D':
    print('Felipe Neto comeu seu cu e você morreu')
    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= FIM =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
    quit()
elif p1 == 'C':
    p2 = str(input('Hum, entendi, então compre o Spray de Cabelo Sagrado do Felipe Neto em desconto, que você ganha um cupom para sorteio de conhecer o próprio Felipe Neto, quer o mapa da NetoLand para achar onde comprar o seu spray?\n[S]im\n[N]ão\n')).upper()
    if p2 == 'S':
        print('Okay, vou te dar o mapa da NetoLand')
        p3 = str(input('Para onde você deseja ir?\n[C]orredor escuro duvidoso\n[P]iscina da NetoLand\n')).upper()
        if p3 == 'C':
            p4 = str(input('Você foi para o corredor, e percebe que está sendo observado, o que quer fazer?\n[L]Ir para loja de spray\n[F]alar com o cara que está te observando\n[V]oltar\n')).upper()
            if p4 == 'V':
                print('O Bruno (escravo do Felipe Neto) apareceu e você morreu')
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= FIM =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                quit()
            elif p4 == 'F':
                print('Você e o cara começam a coversar muito, você conta seu plano para ele, e ele acho legal de ajudar, então ele te da a arma que tira a tinta de cabelo')
                p5 = str(input('Oque quer fazer?\n[L]Ir para loja de spray\n[V]oltar\n'))
                if p5 == 'V':
                    print('O Bruno (escravo do Felipe Neto) apareceu e você morreu')
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= FIM =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    quit()
                elif p5 == 'L':
                    print('Você vai para loja de spray e torra seu dinheiro lá para pegar cupons do sorteio')
                    print('Você ganha um ingresso e vai conhecer o Felipe Neto')
                    print('Você se aproxima de Felipe Neto com seu removedor de tinta')
                    print('Você usa ele em Felipe Neto e ele morre')
                    print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= VITÓRIA =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
                    quit()
            elif p4 == 'L':
                print('Você vai para loja de spray e torra seu dinheiro lá para pegar cupons do sorteio')
        elif p3 == 'P':
            print('Seu cu foi comido pelo salva-vidas (nome: Lucas Neto) e você morreu')
            print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= FIM =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
            quit()
    elif p2 == 'N':
        print('Okay, então morre paiçu')
        print('O atendente tira a cor do seu cabelo e você morre!')
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= FIM =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')  
        quit()