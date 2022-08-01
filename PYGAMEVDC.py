import pygame
import random
from tkinter import messagebox
from tkinter import *
from adcpygame import palavras, indo
from pygame.locals import *


#Começo do programa

pygame.init()

#Cores

AZ = (124, 144, 219)  #Azul
VM = (158, 43, 37)  #Vermelho
CREME = (248, 244, 227)
CIN = (212, 205, 195)  # Cinza
VD = (36, 187, 68) #Verde
VCL = (198, 216, 175)  #Verde Claro
RO = (252, 200, 178)  #Rosa
PR = (34, 34, 34)  #PRETO
BR = (250, 250, 250)  #BRANCO
AM = (252, 246, 176)  #AMARELO
OR = (254, 127, 45)

#Frame e config. da tela

FPS = 30
clock = pygame.time.Clock()
tela = (626, 750)
MSGF = (313, 400)
escrita_font = pygame.font.SysFont('franklingothicmedium', 50)
tiny_font = pygame.font.SysFont('Bahnschrift', 40)

# DISPLAY
DISPLAY = pygame.display.set_mode(tela)
DISPLAY.fill(BR)
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
    excc = escrita_font.render(exc, True, (BR))
    botao((AZ), (173, 300, 248, 70))
    DISPLAY.blit(excc, (178, 304) )
    pygame.display.flip()
    pygame.time.delay(1200)



#Inicio do game
k = 0
m = 0

def inici (inic, DISPLAY):
    #PALAVRA
    palavra = random.choice(palavras)
    acerto = list(palavra.upper())


    #Input

    user_input = ''

    input_box = pygame.Rect(72, 550, 20, 50)
    color_active = pygame.Color(CIN)
    color_passive = pygame.Color(VCL)
    color = color_passive
    text_display = escrita_font.render(user_input, True, (BR))
    active = False

    print('b')
    inici = False
    k = 0

    #DISPLAY
    DISPLAY.fill(BR)
    pygame.display.set_caption("miso")

    quad = [72, 450, 80, 80]

    for linha in range (5):
        if linha > 0:
            quad[0] = quad[0] + 100
        for coluna in range (4):
            quad[1] = quad[1] - 100
            botao(VCL, quad)
            if coluna == 3:
                quad[1] = 450
        botao(RO, quad)

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


    active = False


    #INICIO DO JOGO

    while not inici:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()



            if event.type == pygame.MOUSEBUTTONDOWN:

                if input_box.collidepoint(event.pos):
                    active = True

                else:
                    active = False

            if event.type == pygame.KEYDOWN:

                if active == True:

                    if event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]

                    else:
                        if len(user_input) < 5:
                            user_input += event.unicode


            if active:
                color = color_active

            else:
                color = color_passive



            #input box
            botao(color, input_box)
            text_display = escrita_font.render(user_input.upper(), True, (BR))
            DISPLAY.blit(text_display, (input_box.x+150, input_box.y-3))
            input_box.w = max(480, 100)

            jnt = ' '.join(letras[:14])
            sep = ' '.join(letras[14:])
            letritas = tiny_font.render(jnt, True, (PR))
            letr1tas = tiny_font.render(sep, True, (PR))
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
                            letr_input = escrita_font.render(' ' + A.upper(), True, (BR))
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
            DISPLAY.fill(PR)
            end = 'FIM DE JOGO !'
            eend = tiny_font.render(end, True, (BR))
            DISPLAY.blit(eend, (40, 104) )
            pygame.display.flip()
            pygame.time.delay(3000)



        clock.tick(60)
