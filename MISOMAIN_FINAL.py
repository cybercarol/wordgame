import pygame
import os
from PYGAMEVDC import inici
from tkinter import messagebox
from tkinter import *
from pygame.locals import *
from utils.colors import *
from button import Button

# Começo do programa
pygame.init()

#Frame e config. da tela

FPS = 30
clock = pygame.time.Clock()
tela = (626, 750)
MSGF = (313, 400)
escrita_font = pygame.font.SysFont('franklingothicmedium', 50)
tiny_font = pygame.font.SysFont('Bahnschrift', 40)

#MENU

b1 = (206, 325, 208, 55)
b2 = (206, 415, 208, 55)
b3 = (206, 505, 208, 55)



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
    excc = escrita_font.render(exc, True, (WHITE))
    botao(PORTAGE_BLUE, (230, 300, 150, 70))
    DISPLAY.blit(excc, (274, 304) )
    pygame.display.flip()
    pygame.time.delay(1200)



#Inicio do game
k = 0
m = 0
fim = False
inic = 1

start_button, rules_button, exit_button = buttons = [
    Button('INICIAR', 208, 55),
    Button('REGRAS', 208, 55),
    Button('SAIR', 208, 55)
]

while not fim:
    DISPLAY.fill(PROMENADE_GREEN)
    DISPLAY.blit(title, (205, 150))

    for offset_index, button in enumerate(buttons):
        button.draw(DISPLAY, offset_index)

    for event in pygame.event.get():

        if event.type == QUIT:
            inic = 1
            fim = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.is_mouse_hover():
                inici(DISPLAY)

            if rules_button.is_mouse_hover():
                Tk().wm_withdraw()
                messagebox.showinfo('REGRAS','Tente adivinhar a palavra! Chute 5 letras, se acertar a posição e a letra, aparecerá um quadrinho verde. Caso acerte a letra e não a posição, um amarelo, e errando os dois, um vermelho. Você tem 5 chances, boa sorte!')

            if exit_button.is_mouse_hover():
                pygame.quit()

    pygame.display.update()


clock.tick(60)

pygame.quit()
