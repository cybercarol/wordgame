import pygame
from utils.colors import *

palavras = ['abano', 'senso', 'plena', 'vigor', 'ideia', 'poder', 'moral', 'haver', 'fazer', 'sobre', 'anexo', 'casal', 'genro', 'causa']

d = {'A' :  (66, 628, 35, 35),
     'B' : (104, 628, 34, 35),
     'C' : (140, 628, 34, 35),
     'D' : (176, 628, 34, 35),
     'E' : (212, 628, 34, 35),
     'F' : (249, 628, 32, 35),
     'G' : (283, 628, 32, 35),
     'H' : (318, 628, 34, 35),
     'I' : (354, 628, 20, 35),
     'J' : (378, 628, 30, 35),
     'K' : (410, 628, 33, 35),
     'L' : (447, 628, 32, 35),
     'M' : (482, 628, 36, 35),
     'N' : (522, 628, 34, 35),
     'O' : (93, 669, 32, 36),
     'P' : (128, 669, 34, 36),
     'Q' : (166, 669, 32, 36),
     'R' : (203, 669, 32, 36),
     'S' : (240, 669, 30, 36),
     'T' : (273, 669, 30, 36),
     'U' : (307, 669, 31, 36),
     'V' : (343, 669, 30, 36),
     'W' : (379, 669, 37, 36),
     'X' : (421, 669, 30, 36),
     'Y' : (454, 669, 29, 36),
     'Z' : (488, 669, 29, 36)

}




def botao(DISPLAY, cor, tam):
    pygame.draw.rect(DISPLAY, cor, tam)


def indo(chute, acerto, cont_inp, nomes, DISPLAY, k):
    print(cont_inp)
    b = ['0', '0', '0', '0', '0']
    a = [ord(chute[0]), ord(chute[1]), ord(chute[2]), ord(chute[3]), ord(chute[4])]
    cont = [0, 0, 0, 0, 0]
    cont1 = [0, 0, 0, 0, 0]
    o = -1
    g = []
    c = [False, False, False, False, False]

    for x in range(5):
        o = o + 1

        if chute[o] in acerto:
            if chute [o] != acerto[o]:
                b[o] = '2'

            elif chute[o] == acerto[o]:
                b[o] = '1'
                a[o] = chute[o]

        elif chute[o] not in acerto:
            b[o] = '3'

    for w in range (5):
        if b[w] == '2':
            if (chr(a[w]) in a):
                h = chr(a[w])
                g = a.index(h)
                cont1[w] = acerto.count(chute[g])

            else:
                a[w] = chute[w]

        elif b[w] == '1':
            cont1[w] = 1

        else:
            cont1[w] = 0

        cont[w] = acerto.count(acerto[w])



    for y in range(5):
        e = (d[chute[y]])

        place = cont_inp[y]
        if type(a[y]) == int:
            v = chr(a[y])
            existe = a.count(v)
        else:
            existe = 0

        if (chute[y] in str(a[y])) and (b[y] == '1'):
            botao(DISPLAY, LIME_GREEN, nomes[place])
            botao(DISPLAY, LIME_GREEN, (e))
            c[y] = True

        elif b[y] == '2':
            print(a, b, cont, cont1)
            c[y] = False
            if cont1[y] == 2 and existe == 1:
                botao(DISPLAY, DANDELION_YELLOW, nomes[place])
                cont1 = [1, 1, 1, 1, 1]

            elif (chute[y] in str(a[y])):
                botao(DISPLAY, DANDELION_YELLOW, nomes[place])
                botao(DISPLAY, DANDELION_YELLOW, (e))


            elif existe == 0 and (cont[y] == 1) and (cont1[y] > 0):
                botao(DISPLAY, DANDELION_YELLOW, nomes[place])
                cont1[0] = cont1[0] - 1
                cont1[1] = cont1[1] - 1
                cont1[2] = cont1[2] - 1
                cont1[3] = cont1[3] - 1
                cont1[4] = cont1[4] - 1

            elif (chute[y] not in a):
                botao(DISPLAY, DANDELION_YELLOW, nomes[place])
                botao(DISPLAY, DANDELION_YELLOW, (e))

            else:
                botao(DISPLAY, RED, nomes[place])
                botao(DISPLAY, RED, (e))

        else:
            c[y] = False
            botao(DISPLAY, RED, nomes[place])
            botao(DISPLAY, RED, (e))



    if c == [True, True, True, True, True]:
        k = 6
        return k


    print (acerto)
    print(chute)
