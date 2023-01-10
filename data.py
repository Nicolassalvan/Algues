# Fichier contenant toutes les variables et constantes nécessaires dans différents fichiers 

import settings as config


# Les paramètres min et max permettent de limiter les entrées possibles lors de la mise en place 
# et ainsi éviter des cas d'erreurs



# Paramètres algues 

diam_alg = 2            # en micro m
diam_alg_min = 0.1
diam_alg_max = 10

dens_alg = 0

vit_alg = 10            # en m/s
vit_alg_min = 0
vit_alg_max = 100

nb_alg = 12           # en 10 alg
nb_alg_min = 1
nb_alg_max = 100

t_div_alg = 10          # en h
t_div_alg_min = 5
t_div_alg_max = 15



# Paramètres stress

bool_stress = True      # booléen permettant de déterminer si oui on non le stress sera appliquer lors de la simulation


stress_niv = 50          # en %
stress_min = 0
stress_max = 101



trigger = "Population"

trigger_pop = 10        # en millier d'algues
trigger_pop_min = 1
trigger_pop_max = 100

trigger_t = 10          # en h
trigger_t_min = 1
trigger_t_max = 100



# Paramètre boite de pétri et simulation

larg_boite = 5      # en cm
larg_boite_min = 1
larg_boite_max = 10

long_boite = 5      # en cm
long_boite_min = 1
long_boite_max = 10

vit_simul = 10      #
vit_simul_min = 0
vit_simul_max = 100

t_simul = 2         # en jours
t_simul_min = 0
t_simul_max = 10



# Paramètre interface graphique 

larg_wind = 0
long_wind = 0


# Messages 

message_intro = "Bienvenue, \nDans cette interface, vous avez à déterminer les différents paramètres qui seront pris en compte pour la modéilisation\n\nBien à vous."
message_type_stress = "Ici, le stress sera abiotique (thermqiue, hydrique, oxydatif, lumineux...).\nDans ce modèle, on associe le stress à une probabilité de survie de la cellule et à une architecture en agregats des cellules"
message_type_stress += "\nAfin de faciliter les choix possibles, le stress sera designé en tant que pourcentage. \nDépassé 100, les cellules sont détruites par l'environnement."



def transfert_val() : 
    # Fonction qui permet de transferer les valeurs de data dans le dossier settings, 
    # pour rejoindre les fonctions du modèle mathématiques


    return 0