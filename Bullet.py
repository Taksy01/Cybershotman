# -*- coding: utf-8 -*-
import var as var # importation de l'onglet var avec prefix .var
from random import* # utilisation de la librarie random pour genérer de l'aléatoire
def init_bullets():
    global img_bullet
    img_bullet = loadImage("Bullet.png") # image des balles
    
def afficher_bullets():
    for bullet in var.tab_bullets:  # image des balles
        image(img_bullet, bullet[0]+50, bullet[1])
        
def tirer(dimensions):
    if var.jouer == True:
        if len(var.tab_bullets)<5: # nombre max de balle a l'écran de 5
            var.tab_bullets.append(dimensions[:]) # augmentation de la coordonnée x de chaque balle
def tirerrandom(dimensions):  # cheat move
    var.tab_bullets.append(dimensions[:])

def deplacer_bullets():
    o=0
    b = len(var.tab_bullets)
    while o < b:
        if var.tab_bullets[o][0]<817:
            var.tab_bullets[o][0] +=10 # vitesse des balles
        else:
            var.tab_bullets.pop(o) # supression des balles en dehors de l'écran
            b-=1
        o +=1
