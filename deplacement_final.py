import class_algue as cla 
import matplotlib.pyplot as plt
import aggregat as aggr
import settings as config
import random as rand
import numpy as np

def check_deplacement(population, i, box, deplacement):
    """

    Cette fonction vérifie si le déplacement est possible ou non.
    Si le déplacement est possible, elle renvoie True, -1
    Si le déplacement n'est pas possible car en dehors de la box, elle renvoie False, -1
    Si le déplacement n'est pas possible car une autre cellule est présente, elle renvoie False, j, avec j l'indice de la cellule présente


    Paramètre 
    =============

    population : liste de cellules
    i : indice de la cellule
    box : environnement où se déplace les cellules
    deplacement : déplacement possible (x,y)
    """
    # je vérifie que je ne sorte pas de la box
    if (population.x[i] + deplacement[0] > box.x_max or population.x[i] + deplacement[0] < 0):
        return False
    if (population.y[i] + deplacement[1] > box.y_max or population.y[i] + deplacement[1] < 0):
        return False

    # je vérifie que je ne me déplace pas sur une autre cellule
    for j in range(population.nombre_algues):
        if (i != j):
            if (population.x[i] + deplacement[0] == population.x[j] and population.y[i] + deplacement[1] == population.y[j]):
                return False
    return True

def deplacement_sans_stresse(population,box):
    """
    La fonction modifie les coordonnées des cellules de la population sans prendre en compte le stress

    retourne la population modifiée

    Paramètre
    =============
    population : liste de cellules
    box : environnement où se déplace les cellules
    """
    for i in range(population.nombre_algues):
        if (population.aggregat[i] == False):
            deplacement = np.array([rand.randint(-config.Dep_max, config.Dep_max),rand.randint(-config.Dep_max, config.Dep_max)])

            if (check_deplacement(population, i, box, deplacement)):
                population.x[i] += deplacement[0]
                population.y[i] += deplacement[1]
    return population
                
