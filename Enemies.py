# -*- coding: utf-8 -*-
import var as var # importation de l'onglet var avec prefix .var
from random import *
import random
def init_monstre():
    global img_monstre
    img_monstre = loadImage("Monstre.png") # Image du monstre

def afficher_monstre():
    if len(var.tab_monstre)==var.nbr: # nombre max d'ennemis par vague
            var.respawn = False # var.respawn defini si les monstre respawn ou pas
    if len(var.tab_monstre)<=var.nbr and var.respawn:
        var.tab_monstre.append([random.randint(850,1000),random.randint(60,335),random.uniform((var.speedbase)+0.2*var.vague,(var.speedbase+0.5)+0.2*var.vague)]) # definition du placement aléatoire des monstres et leur vitesse
    for monstre in var.tab_monstre:
        image(img_monstre,monstre[0],monstre[1])
    if  var.respawn == False and len(var.tab_monstre)==0: # augmentation de la vague si les monstres sont mort
        var.respawn = True
        var.nbr+=1 # nombre d'ennemis augmente de 1 par vague
        var.vague +=1
        
        
def deplacer_monstre():
    for monstre in var.tab_monstre:
        monstre[0] -=monstre[2] # vitesse de l'enemie en fonction du paramettre donné dans tab_monstre
        if monstre[0] <= -10:
            var.tab_monstre.remove(monstre) # le monstre est retiré s'il est en dehors de l'ecran
        
def tuer_monstre():
    for monstre in var.tab_monstre: 
        for bullet in var.tab_bullets:
            if bullet[0]+50 > monstre[0]-10 and bullet[0]+50 < monstre[0]+10 and bullet[1] > monstre[1]-40 and bullet[1] < monstre[1]+40: # detection de collision entre une balle et un monstre
                var.tab_monstre.remove(monstre) # le monstre meurt

                var.tab_bullets.remove(bullet) # la balle disparait
                var.score +=10 # augmentation du score 
