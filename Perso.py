# -*- coding: utf-8 -*-
import var as var

def init_perso():
    #la variable img_perso contiendra l'image et sera utilisable dans les autres fonctions du fichier Perso.py
    global img_perso
    # chargement de l'image du personnage dans la variable
    img_perso = loadImage("Perso.png")
    
def afficher_perso():
    # affichage de l'image du personnage aux coordonnées stockées dans coords_perso
    if var.coords_perso[1]<63: # limite de coordonnée du joueur pour le bloquer en haut
        var.movevarup = False
    if var.coords_perso[1]>337: # limite de coordonnée du joueur pour le bloquer en bas
        var.movevardown = False
        
    if var.movevarup == True:
        var.coords_perso[1]-=5 # vitesse deplacement
    if var.movevardown == True:
        var.coords_perso[1]+=5 # vitesse deplacement
    
    image(img_perso,var.coords_perso[0],var.coords_perso[1]) # le personnage apparait a l'écran ses coordonnées peuvent changer
    
def degat_monstre():
    for monstre in var.tab_monstre:
        # detection de collision entre le monstre et le joueur
        if var.coords_perso[0]+20 > monstre[0]-10 and var.coords_perso[0] < monstre[0]+10 and var.coords_perso[1] > monstre[1]-80 and var.coords_perso[1] < monstre[1]+80 or monstre[0]<10:
            var.tab_monstre.remove(monstre) # supression du monstre
            var.coeurvar +=1 # reduction des points de vie
    if var.coeurvar == 3:
        var.mort = True # si le joueur se fait toucher ou laisse passer un monstre 3 fois, il meurt
    

    
