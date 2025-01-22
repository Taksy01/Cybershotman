# -*- coding: utf-8 -*-
import var as var #importation de l'onglet var avec prefix .var
def init_coeur():
    global img_coeurrempli # image du coeur rempli
    global img_coeurvide # image du coeur vide
    img_coeurrempli = loadImage("CoeurRempli.png")
    img_coeurvide = loadImage("CoeurVide.png")

def afficher_coeur():
    if var.coeurvar == 0: # condition pour afficher full coeur
        image(img_coeurrempli,690,20,40,40)
        image(img_coeurrempli,730,20,40,40)
        image(img_coeurrempli,770,20,40,40)
    if var.coeurvar == 1: # condition pour afficher 2 coeurs et 1 vide
        image(img_coeurrempli,690,20,40,40)
        image(img_coeurrempli,730,20,40,40)
        image(img_coeurvide,770,18,40,44)
    if var.coeurvar == 2: # condition pour afficher 1 coeur et 2 vide
        image(img_coeurrempli,690,20,40,40)
        image(img_coeurvide,730,18,40,44)
        image(img_coeurvide,770,18,40,44)
    if var.coeurvar == 3: # condition pour afficher 3 coeurs vide
        image(img_coeurvide,690,18,40,44)
        image(img_coeurvide,730,18,40,44)
        image(img_coeurvide,770,18,40,44)
        
