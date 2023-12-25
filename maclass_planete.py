import pygame, math

from pygame_initial import *
class planete:
    def __init__(self, name, rayon, vitesse, distance_sun, color, angle, x, y):
        self.name = name
        self.rayon = rayon
        self.vitesse = vitesse
        self.distance_sun = distance_sun
        self.color = color
        self.angle = angle
        self.x = x
        self.y = y
        

    def calcul_pos_XY(self):
        self.angle += self.vitesse
        self.x = LARGEUR_ECRAN/3  + self.distance_sun * math.cos(self.angle)
        self.y = (HAUTEUR_ECRAN/3) * 2 + self.distance_sun * math.sin(self.angle)  
        
    
    def dessine_planete(self):
        pygame.draw.circle(syst, (self.color), (int(self.x), int(self.y)), self.rayon, 0)
        