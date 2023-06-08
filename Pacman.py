import random
import os
from time import sleep

pontuacao_pacman = 0
pontuacao_gosh = 0

def pontuacao():
    global pontuacao_pacman, pontuacao_gosh
    print('* Pacman {} X {} Gosh *\n'.format(pontuacao_pacman, pontuacao_gosh))

if __name__ == '__main__':


    matriz = [['.' for _ in range(11)] for _ in range(11)]

    fruta_linha = random.randint(0, 10)
    fruta_coluna = random.randint(0, 10)

    #Criando a refenrencia na matriz da linha e coluna do Pacman
    inicio_linha = random.randint(0, 10)
    inicio_coluna = random.randint(0, 10)
    estado_pacman = 'O'

    #Criando a refenrencia na matriz da linha e coluna do Gosh
    inicio_linha_gosh = random.randint(0, 10)
    inicio_coluna_gosh = random.randint(0, 10)
    estado_gosh = 'F'

                    # Posição inicial do Gosh
    matriz[inicio_linha_gosh][inicio_coluna_gosh] = estado_gosh

                    # Posição inicial do Pacman
    matriz[inicio_linha][inicio_coluna] = estado_pacman

    matriz[fruta_linha][fruta_coluna] = 'X'

    if (fruta_linha == inicio_linha or fruta_coluna == inicio_coluna) and \
            (fruta_linha == inicio_linha_gosh or fruta_coluna == inicio_coluna_gosh):
        fruta_linha = random.randint(0, 10)
        fruta_coluna = random.randint(0, 10)
        matriz[fruta_linha][fruta_coluna] = 'X'


                        # Loop do game
    while True:
        # Para remover as virgulas da matriz (,.,.,.,.,.) (. . . . . .)

        for linha in matriz:
            print(' '.join(linha))
        pontuacao()

                            # Controle
        resposta = input("Deseja avançar mais casas? (s/n): ")
        if resposta.lower() == 'n':
            break

        matriz[inicio_linha][inicio_coluna] = '.'
        direcao = input("Informe a direção (c - cima, b - baixo, f - frente v - voltar): ")
        casas = int(input("Informe a quantidade de casas: "))

                             # Movimentando o Pacman
        if direcao == 'c' and inicio_linha - casas >= 0:
            matriz[inicio_linha_gosh][inicio_coluna_gosh] = '.'
            inicio_linha -= casas

        elif direcao == 'b' and inicio_linha + casas < 11:
            matriz[inicio_linha_gosh][inicio_coluna_gosh] = '.'
            inicio_linha += casas

        elif direcao == 'f' and inicio_coluna + casas < 11:
            matriz[inicio_linha_gosh][inicio_coluna_gosh] = '.'
            inicio_coluna += casas

        elif direcao == 'v' and inicio_coluna - casas >= 0:
            matriz[inicio_linha_gosh][inicio_coluna_gosh] = '.'
            inicio_coluna -= casas

        # Movimento do Gosh em direção ao Pacman
        if inicio_linha_gosh < inicio_linha and inicio_linha_gosh + casas < 11:
            matriz[inicio_linha_gosh][inicio_coluna_gosh] = '.'
            inicio_linha_gosh += casas
            matriz[inicio_linha_gosh][inicio_coluna_gosh] = 'F'

        elif inicio_linha_gosh > inicio_linha and inicio_linha_gosh - casas >= 0:
            matriz[inicio_linha_gosh][inicio_coluna_gosh] = '.'
            inicio_linha_gosh -= casas
            matriz[inicio_linha_gosh][inicio_coluna_gosh] = 'F'

        if inicio_coluna_gosh < inicio_coluna and inicio_coluna_gosh + casas < 11:
            matriz[inicio_linha_gosh][inicio_coluna_gosh] = '.'
            inicio_coluna_gosh += casas
            matriz[inicio_linha_gosh][inicio_coluna_gosh] = 'F'

        elif inicio_coluna_gosh > inicio_coluna and inicio_coluna_gosh - casas >= 0:
            matriz[inicio_linha_gosh][inicio_coluna_gosh] = '.'
            inicio_coluna_gosh -= casas
            matriz[inicio_linha_gosh][inicio_coluna_gosh] = 'F'

        elif inicio_coluna_gosh > inicio_coluna:
            inicio_coluna_gosh -= casas
            matriz[inicio_coluna_gosh][inicio_coluna_gosh] = '.'

                    # Mudança do estado do Pacman a cada iteração
        estado_pacman = 'O' if estado_pacman == 'o' else 'o'

        matriz[inicio_linha][inicio_coluna] = estado_pacman  # Troca a nova posição do pacman, removendo o '.' e add a srting do pacman
        matriz[inicio_linha_gosh][inicio_coluna_gosh] = estado_gosh  # Troca a nova posição do pacman, removendo o '.' e add a srting do Gosh

                    # Quando o Gosh tocar o pacman, o mesmo nasce em uma nova posicao
        if inicio_linha == inicio_linha_gosh and inicio_coluna == inicio_coluna_gosh:
            os.system('cls')  # Limpa a tela
            print("Pacman foi capturado!!")
            sleep(0.6)
            pontuacao_gosh += 1

            if fruta_linha == inicio_linha_gosh and fruta_coluna == inicio_coluna_gosh:
                os.system('cls')  # Limpa a tela
                print("Opss, vamos gerar uma nova posição para comida!!")
                sleep(0.6)
                fruta_linha = random.randint(0, 10)
                fruta_coluna = random.randint(0, 10)
                matriz[fruta_linha][fruta_coluna] = 'X'

                if (fruta_linha == inicio_linha or fruta_coluna == inicio_coluna) and \
                        (fruta_linha == inicio_linha_gosh or fruta_coluna == inicio_coluna_gosh):
                    fruta_linha = random.randint(0, 10)
                    fruta_coluna = random.randint(0, 10)
                    matriz[fruta_linha][fruta_coluna] = 'X'

            estado_pacman = 'O'
            inicio_linha = random.randint(0, 10)
            inicio_coluna = random.randint(0, 10)
            matriz[inicio_linha][inicio_coluna] = estado_pacman


                # Quando o Pacman come a fruta o jogo coloca uma fruta nova na matriz em posição aleatória
        if inicio_linha == fruta_linha and inicio_coluna == fruta_coluna:
            os.system('cls')  # Limpa a tela
            print("Pacman alcançou a comida!")
            sleep(0.6)
            pontuacao_pacman += 1
            fruta_linha = random.randint(0, 10)
            fruta_coluna = random.randint(0, 10)
            matriz[fruta_linha][fruta_coluna] = 'X'

            if (fruta_linha == inicio_linha or fruta_coluna == inicio_coluna) and \
                    (fruta_linha == inicio_linha_gosh or fruta_coluna == inicio_coluna_gosh):
                fruta_linha = random.randint(0, 10)
                fruta_coluna = random.randint(0, 10)
                matriz[fruta_linha][fruta_coluna] = 'X'
            estado_pacman = 'O'


        if fruta_linha == inicio_linha_gosh and fruta_coluna == inicio_coluna_gosh:
            os.system('cls')  # Limpa a tela
            print("Opss, vamos gerar uma nova posição para comida!!")
            sleep(0.6)
            fruta_linha = random.randint(0, 10)
            fruta_coluna = random.randint(0, 10)
            matriz[fruta_linha][fruta_coluna] = 'X'

            if (fruta_linha == inicio_linha or fruta_coluna == inicio_coluna) and \
                    (fruta_linha == inicio_linha_gosh or fruta_coluna == inicio_coluna_gosh):
                fruta_linha = random.randint(0, 10)
                fruta_coluna = random.randint(0, 10)
                matriz[fruta_linha][fruta_coluna] = 'X'
