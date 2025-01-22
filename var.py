# -*- coding: utf-8 -*-
# initialisation de toute les variable
movevarup=False # Variable qui defini le mouvement du joueur vers le haut
movevardown=False # Variable qui defini le mouvement du joueur vers le base

coords_perso = [50,200] # coordonnées de base du personnage
coeurvar=0 # vie de base (dégats subits)
tab_bullets = [] # stock les coordonnée des balles
tab_monstre =[] # stock les coordonnée des monstres
score = 0 # score de base
highscore = 0 # record qui prend comme valeur le score le plus haut atteint
mort = False # detecte si le joueur est mort
jouer = False # detecte si joue
canreplay = False # verifier la fonction pour relancer une partie
respawn = True # verifier la fonction faire apparaitre les ennemis
nbr=5 # nombre de base d'ennemis vague 1
speedbase = 1 # vitesse de base d'ennemis vague 1 
vague =1 # numero de la vague
