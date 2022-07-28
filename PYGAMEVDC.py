import pygame
import random
from tkinter import messagebox
from tkinter import *
from adcpygame import palavras, indo
from pygame.locals import *


# Começo do programa
pygame.init()

# Cores
PORTAGE_BLUE = (124, 144, 219)
RED = (158, 43, 37)
PROMENADE_GREEN = (248, 244, 227)
WESTAR_GREY = (212, 205, 195)
LIME_GREEN = (36, 187, 68)
PIXIE_GREEN = (198, 216, 175)
APRICOT_ORANGE = (252, 200, 178)
BLUE_BELL = (34, 34, 34)
WHITE = (250, 250, 250)
BANANA_YELLOW = (252, 246, 176)
DANDELION_YELLOW = (254, 127, 45)

#Frame e config. da tela

FPS = 30
clock = pygame.time.Clock()
tela = (626, 750)
MSGF = (313, 400)
escrita_font = pygame.font.SysFont('franklingothicmedium', 50)
tiny_font = pygame.font.SysFont('Bahnschrift', 40)

# DISPLAY
DISPLAY = pygame.display.set_mode(tela)
DISPLAY.fill(WHITE)
pygame.display.set_caption("miso")

#Funções

def botao(cor, tam):
    pygame.draw.rect(DISPLAY, cor, tam)


#LETRAS
cont_inp = []
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#final

def popup(A):
    exc = '!' + A
    excc = escrita_font.render(exc, True, (WHITE))
    botao(PORTAGE_BLUE, (173, 300, 248, 70))
    DISPLAY.blit(excc, (178, 304) )
    pygame.display.flip()
    pygame.time.delay(1200)



#Inicio do game
k = 0
m = 0

def inici(DISPLAY):
    #PALAVRA
    palavra = random.choice(palavras)
    acerto = list(palavra.upper())


    #Input
    user_input = ''
    text_display = escrita_font.render(user_input, True, (WHITE))
    active = False
    inici = False
    k = 0

    #DISPLAY
    DISPLAY.fill(WHITE)
    pygame.display.set_caption("miso")

    quad = [72, 450, 80, 80]

    for linha in range (5):
        if linha > 0:
            quad[0] = quad[0] + 100
        for coluna in range (4):
            quad[1] = quad[1] - 100
            botao(PIXIE_GREEN, quad)
            if coluna == 3:
                quad[1] = 450
        botao(APRICOT_ORANGE, quad)

    #boxez

    dim = [82, 60, 60, 60]
    nomes = [None]* 25
    vez = 1
    vzs = 0

    for abc in range (5):
        if abc > 0:
            dim[1] = dim[1] + 100

        for col in range(5):
            vzs = vzs + 1
            if col > 0:
                dim[0] = dim[0] + 100
            nomes[vzs-1] = pygame.Rect(dim)

            if col == 4:
                dim[0] = 82

    #INICIO DO JOGO

    while not inici:
        input_rect = pygame.Rect(72, 550, 480, 50)
        color = WESTAR_GREY if active else PIXIE_GREEN
        pygame.draw.rect(DISPLAY, color, input_rect)
        text_display = escrita_font.render(user_input.upper(), True, WHITE)
        DISPLAY.blit(text_display, text_display.get_rect(center=input_rect.center))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                active = input_rect.collidepoint(event.pos)

            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        if len(user_input) < 5:
                            user_input += event.unicode

            jnt = ' '.join(letras[:14])
            sep = ' '.join(letras[14:])
            letritas = tiny_font.render(jnt, True, (BLUE_BELL))
            letr1tas = tiny_font.render(sep, True, (BLUE_BELL))
            DISPLAY.blit(letritas, (70, 620))
            DISPLAY.blit(letr1tas, (96, 660))


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    chute = list(user_input.upper())

                    #Condições de Fucionamento
                    comeca = 0

                    if  len(chute) != 5:
                        Tk().wm_withdraw()
                        messagebox.showinfo('Menos de 5 letras','Eita! Digite uma palavra com 5 letras.')
                    else:
                        for i in range(5):
                            if chute[i] in letras:
                                comeca = comeca +1

                        if comeca != 5:
                            Tk().wm_withdraw()
                            messagebox.showinfo('Apenas letras',' Ei! Apenas letras são aceitas. Tente novamente.')


                    if comeca == 5:
                        k = k + 1
                        vez = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
                        cont_inp = vez [k-1]
                        indo(chute, acerto, cont_inp, nomes, DISPLAY, m)
                        if (indo(chute, acerto, cont_inp, nomes, DISPLAY, m)) != None:
                            k = str(indo(chute, acerto, cont_inp, nomes, DISPLAY, m))
                            k = int(k)
                            print(k)


                        for i in range (5):
                            A = chute[i]
                            letr_input = escrita_font.render(' ' + A.upper(), True, (WHITE))
                            DISPLAY.blit(letr_input, nomes[cont_inp[i]])

                        pygame.display.flip()

                        user_input = user_input[:-5]

                    if k == 5 or k == 6:
                        if k == 5:
                            emj = 'perdeu : ['
                            popup( emj )


                        if k == 6:
                            mj = ' ganhou : )'
                            popup( mj )

                        inici = True

                    else:
                        user_input = user_input[:-5]

                pygame.display.flip()

        if inici == True:
            DISPLAY = pygame.display.set_mode(MSGF)
            DISPLAY.fill(BLUE_BELL)
            end = 'FIM DE JOGO !'
            eend = tiny_font.render(end, True, (WHITE))
            DISPLAY.blit(eend, (40, 104) )
            pygame.display.flip()
            pygame.time.delay(3000)

        clock.tick(60)
        pygame.display.update()
