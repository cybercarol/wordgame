import pygame
import os
from PYGAMEVDC import inici
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


#Funções

def botao(cor, tam):
    pygame.draw.rect(DISPLAY, cor, tam)

def press(bo, tamanho):
    mouse = pygame.mouse.get_pos()
    if bo.collidepoint(mouse):
        botao(VM, tamanho)
    else:
        botao(AZ, tamanho)

#MENU

b1 = (206, 325, 208, 55)
b2 = (206, 415, 208, 55)
b3 = (206, 505, 208, 55)
esc_font = pygame.font.SysFont('Verdana', 20)

jogo = esc_font.render("INICIAR", True, BR)
regras = esc_font.render("REGRAS", True, BR)
sair = esc_font.render("  SAIR", True, BR)


title = pygame.image.load(os.path.join('MISO.png'))


# DISPLAY
DISPLAY = pygame.display.set_mode(tela)
pygame.display.set_caption("miso")


#LETRAS
cont_inp = []
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#final

def popup(A):
    exc = '!' + A
    excc = escrita_font.render(exc, True, (BR))
    botao((AZ), (230, 300, 150, 70))
    DISPLAY.blit(excc, (274, 304) )
    pygame.display.flip()
    pygame.time.delay(1200)
    


#Inicio do game
k = 0
m = 0
fim = False
inic = 1

while not fim:
    DISPLAY.fill(CREME)
    DISPLAY.blit(title, (205, 150))
    bb1 = pygame.Rect(b1)
    botao( AZ, b1)
    bb2 = pygame.Rect(b2)
    botao( AZ, b2)
    bb3 = pygame.Rect(b3)
    botao( AZ, b3)

    press(bb1, b1)
    press(bb2, b2)
    press(bb3, b3)

    DISPLAY.blit(jogo, (270, 340))
    DISPLAY.blit(regras, (268, 430))
    DISPLAY.blit(sair, (270, 520))
    
    
    
    for event in pygame.event.get():

        if event.type == QUIT:
            inic = 1
            fim = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if bb1.collidepoint(event.pos):
                inic = 0
                fim = True

            if bb2.collidepoint(event.pos):
                Tk().wm_withdraw()
                messagebox.showinfo('REGRAS','Tente adivinhar a palavra! Chute 5 letras, se acertar a posição e a letra, aparecerá um quadrinho verde. Caso acerte a letra e não a posição, um amarelo, e errando os dois, um vermelho. Você tem 5 chances, boa sorte!')
                
            if bb3.collidepoint(event.pos):
                inic = 1
                fim = True
        
    pygame.display.update()

if fim == True and inic == 0:
    inici(inic, DISPLAY)

elif fim == True and inic == 1:
    pygame.quit()
    
clock.tick(60)

pygame.quit()

























