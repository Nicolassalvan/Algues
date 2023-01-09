# Fichier contenant toutes les variables et constantes nécessaires dans différents fichiers 



# Les paramètres min et max permettent de limiter les entrées possibles lors de la mise en place 
# et ainsi éviter des cas d'erreurs



# Paramètres algues 

diam_alg = 2            # en micro m
diam_alg_min = 0.1
diam_alg_max = 10

vit_alg = 10            # en m/s
vit_alg_min = 0
vit_alg_max = 100

dens_alg = 12           # en 10 alg/mL
dens_alg_min = 0
dens_alg_max = 100

t_div_alg = 10          # en h
t_div_alg_min = 5
t_div_alg_max = 15



# Paramètres stress

bool_stress = True

type_stress = "Thermique"

stress_th = 50          # en °C
stress_th_min = 20
stress_th_max = 100

stress_lum = 20         # en Lumens
stress_lum_min = 0
stress_lum_max = 100

stress_hydr = 10        #
stress_hydr_min = 0
stress_hydr_max = 20


trigger = "Temps"

trigger_pop = 10        # en millier d'algues
trigger_pop_min = 1
trigger_pop_max = 100

trigger_t = 10          # en h
trigger_t_min = 1
trigger_t_max = 100



# Paramètre boite de pétri et simulation

larg_boite = 5      # en cm
larg_boite_min = 0
larg_boite_max = 10

long_boite = 5      # en cm
long_boite_min = 0
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

message_intro = "Bienvenue, \nDans cette interface, vous avez à déterminer les différents paramètres qui seront pris en compte pour la modéilisation\nBien à vous"