# Module contenant toutes les variables et constantes nécessaires dans différents fichiers 


# Import des biblipthèques PyQt5 

from PyQt5.QtGui import QFont, QFontDatabase

# Import du fichier settings
import settings as config


# Les paramètres min et max permettent de limiter les entrées possibles lors de la mise en place 
# et ainsi éviter des cas d'erreurs


# Définition des variables 

# Paramètres algues 

    # Diameètre d'une algue
diam_alg = 2            # en micro m    

    # Densité des algues dans la boite
dens_alg = 0

    # Vitesse des algues
vit_alg = 10            # en m/s
vit_alg_min = 0
vit_alg_max = 100

    # Nombre d'algues initial
nb_alg = 20             # en alg
nb_alg_min = 1
nb_alg_max = 100

    # Temps de division des algues 
t_div_alg = 10          # en h
t_div_alg_min = 5
t_div_alg_max = 50



# Paramètres stress

    # Choix d'application d'un stress
bool_stress = True      # booléen permettant de déterminer si oui on non le stress sera appliquer lors de la simulation


    # Niveau de stress appliqué 
stress_niv = 50          # en %
stress_min = 0
stress_max = 101


    # Type de trigger déclencheur du stress
trigger = "Population"

    # Trigger en fonction du nombre d'algues 
trigger_pop = 10        # en millier d'algues
trigger_pop_min = 1
trigger_pop_max = 100

    # Trigger en fonction du temps écoulé 
trigger_t = 10          # en h
trigger_t_min = 1
trigger_t_max = 100



# Paramètre boite de pétri et simulation

    # Largeur de la boite
larg_boite = 5      # en mm
larg_boite_min = 1
larg_boite_max = 10

    # Longueur de la boite
long_boite = 5      # en cm
long_boite_min = 1
long_boite_max = 10

    # Surface de la boite
surf_boite = 0      # en mm²

    # Vitesse de simulation
vit_simul = 10      #
vit_simul_min = 0
vit_simul_max = 100

    # Temps de simulation 
t_simul = 2         # en jours
t_simul_min = 0
t_simul_max = 10


# Taille et police de caractère 

font = QFont('Arial', 10)


# Messages 

message_intro = "Bienvenue, \nDans cette interface, vous avez à déterminer les différents paramètres qui seront pris en compte pour la modéilisation\n\nBien à vous."
message_type_stress = "Ici, le stress sera abiotique (thermqiue, hydrique, oxydatif, lumineux...).\nDans ce modèle, on associe le stress à une probabilité de survie de la cellule et à une architecture en agregats des cellules"
message_type_stress += "\nAfin de faciliter les choix possibles, le stress sera designé en tant que pourcentage. \nDépassé 100, les cellules sont détruites par l'environnement."



def transfert_val() : 
    # Fonction qui permet de transferer les valeurs de data dans le dossier settings, 
    # pour rejoindre les fonctions du modèle mathématiques


    return 0


# Fin du module