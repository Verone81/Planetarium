import pygame
import time
#import os
from variable import *
from pygame_initial import *
from maclass_planete import planete

# construction des planete
mercure = planete("mercure",1, 0.33, 4.4,(128, 0, 0), rad, xx_planete, yy_planete)
venus = planete("venus",1 , -0.21, 9.68,(34,139,34), rad, xx_planete, yy_planete)
terre = planete("terre", 1, 0.135, 21.3,(188,143,143), rad, xx_planete, yy_planete)
mars = planete("mars", 1, 0.085 , 46.9,(255,69,0), rad, xx_planete, yy_planete)
jupiters = planete("jupiters", 70.249, 0.055, 200,(255,140,0), rad, xx_planete, yy_planete)
saturne = planete("saturne",18.986 , 0.035, 300,(192,192,192), rad, xx_planete, yy_planete)
uranus = planete("uranus",5.131, -0.02, 450,(30,144,255), rad, xx_planete, yy_planete)
neptune = planete("neptune", 3.385, 0.015, 900,(153,50,204), rad, xx_planete, yy_planete)

#frame_number = 0
clock = pygame.time.Clock()
play = True

# boucle d'animation
while play:
    clock.tick(50)
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                play = False
            elif event.key == pygame.K_p:
                time.sleep(5)
       
    syst.fill((15, 15, 15))

    # calculce des mouvement
    pygame.draw.circle(syst,(255, 255, 0),(LARGEUR_ECRAN/3, HAUTEUR_ECRAN/3 * 2), 3, 0)   
    mercure.calcul_pos_XY()
    mercure.dessine_planete()
    venus.calcul_pos_XY()
    venus.dessine_planete()
    terre.calcul_pos_XY()
    terre.dessine_planete()
    mars.calcul_pos_XY()
    mars.dessine_planete()
    jupiters.calcul_pos_XY()
    jupiters.dessine_planete()
    saturne.calcul_pos_XY()
    saturne.dessine_planete()
    uranus.calcul_pos_XY()
    uranus.dessine_planete()
    neptune.calcul_pos_XY()
    neptune.dessine_planete()
    #pygame.image.save(syst, f'frames/frame_{frame_number:04d}.png')
    #frame_number += 1

    pygame.display.flip()
pygame.quit()
