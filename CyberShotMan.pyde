"""
on recupère les données des autres onglets
"""
from Bullet import*
from Perso import*
from Enemies import*
from Barre import*
from vague import*
import var as var
from random import*
def setup():
    """
    fonction setup : lancée une fois au démarrage de l'application
                     pour l'initialiser
    """
    size (800, 400) # définition de la taille de la fenêtre de l'application
    imageMode(CENTER) # on affichera les images en précisant les coords du centre
    init_perso() # initialisation du personnage 
    init_bullets() # initialisation des balles
    init_monstre() # initialisation des monstres
    init_coeur() # initialisation des coeur

def draw():
    """
    fonction draw : lancée régulièrement (~60 fois/s), elle est destinée à réaliser
                    tous les affichages de l'application
    """
    
    fill(0)
    background(255) # couleur du background blanc
    imageMode(CENTER)   
    if var.jouer == False:
        text("Appuyez sur ESPACE pour commencer",220,200) # message de debut pour lancer le jeu
    if (key==" "):
        var.jouer = True # Variable qui detecte si le jeu est en marche
    if var.mort == True and var.jouer == True:
        """
        Le programme ci dessous s'execute si le jeu est lancé et que le joueur meurt
        Cela permet d'arreter le jeu si le joueur meurt
        """
        
        textSize(30)
        text("Tu es mort",320,200)
        text("Appuie sur R pour recommencer",175,250)
        text("Score: {}".format(var.score),310,100)
        text("Vague: {}".format(var.vague),310,150)
        if var.canreplay == True: # detection si le joueur appuie sur R (voir en bas dans KeyPressed())
            """
            reset des variable score et statistiques des enemies
            """
            var.mort = False # Le personnage n'est plus mort et le jeu reprend
            var.coeurvar = 0 # reset de la vie
            var.tab_monstre = [] # reset des monstres
            var.tab_bullets = [] # reset des balles
            var.coords_perso = [50,200] # du personnage
            var.score = 0 # reset du score
            
    
    if var.mort == False and var.jouer == True:
        """
        Le programme ci dessous s'execute si le jeu est lancé et que le joueur n'est PAS mort
        toute les fonctions utile au fonctionnement du jeu sont lancées
        """
        afficher_perso() # affichage du perso
        afficher_bullets() # affichage des balles
        deplacer_bullets() # fonction de deplacement des balles
        deplacer_monstre() # fonction de deplacement des monstres
        afficher_monstre() # affichage des monstres
        tuer_monstre()     # fonction pour tuer les monstres
        degat_monstre()    # fonction des degat de monstre sur le joueur
        nbr = 5 # Nombre d'ennemis de base
        text("Vague {}".format(var.vague),100,25) # affichage des vagues
        text("Score:",330,25) # affichage du score
        text(var.score,400,25)
        
    afficher_coeur() # affichage de la fonction coeur dans les 2 cas du dessus
    textSize(20)
    if var.highscore < var.score:
            var.highscore = var.score
    text("Highscore:",480,25) # affichage du highscore
    text(var.highscore,600,25)

def keyPressed(): # detection de pression de touche et modification de variable bool
    if (key=="a"):
        var.movevarup = True
    if (key=="q"):
        var.movevardown = True
    if (key==" ") and var.mort == False:
        tirer(var.coords_perso)
    if (key=="c") and var.mort == False:
        tirerrandom([var.coords_perso[0],randint(70,330)])
    if (key=="r"):
        var.canreplay=True

def keyReleased(): # a l'inverse detection de release de touche et modification de variable bool
    if (key=="a"):
        var.movevarup = False
    if (key=="q"):
        var.movevardown = False
    if (key=="r"):
        var.canreplay=False
        
