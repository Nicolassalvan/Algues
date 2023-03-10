"""
Created on Wed Jan  4 19:08:29 2023

@author: Team Algues
"""

import class_algue 
import matplotlib.pyplot as plt
import settings as config
import random as rand
import numpy as np

def check_deplacement(population, i, box, deplacement):
    """
    Cette fonction vérifie si le déplacement est possible ou non.

    Paramètres
    ------
    
    population : class Population
        Population d'algues, la classe est précisée dans le fichier class_algue.py
    i : int
        Indice de la cellule
    box : class Box
        Environnement où se déplace les cellules
    deplacement : array de 2 entiers
        Déplacement relatif possible [x,y]
        
    Retours
    ------
    
    - Si le déplacement est possible, elle renvoie True, -1
    - Si le déplacement n'est pas possible car en dehors de la box, elle renvoie False, -1
    - Si le déplacement n'est pas possible car une autre cellule est présente, elle renvoie False, j, 
    avec j l'indice de la cellule présente
    
    """
    # je vérifie que je ne sorte pas de la box
    if (population.x[i] + deplacement[0] > box.x_max or population.x[i] + deplacement[0] < 0):
        return False, -1
    if (population.y[i] + deplacement[1] > box.y_max or population.y[i] + deplacement[1] < 0):
        return False, -1

    # je vérifie que je ne me déplace pas sur une autre cellule
    for j in range(population.nombre_algues):
        if (i != j):
            if (population.x[i] + deplacement[0] == population.x[j] and population.y[i] + deplacement[1] == population.y[j]):
                return False, j
    return True, -1

def deplacement_sans_stresse(population,box):
    """
    La fonction modifie les coordonnées des cellules de la population sans prendre 
    en compte le stress
    
    Paramètres
    ------
    population : class Population
        Population d'algues, la classe est précisée dans le fichier class_algue.py
    box : class Box
        Environnement où se déplace les cellules
        
    Retours
    ------
    Aucun    
    """
    for i in range(population.nombre_algues):
        deplacement = np.array([rand.randint(-config.DEP_MAX, config.DEP_MAX),rand.randint(-config.DEP_MAX, config.DEP_MAX)])

        if (check_deplacement(population, i, box, deplacement)):
            population.x[i] += deplacement[0]
            population.y[i] += deplacement[1]

def deplacement_avec_stresse(population,box):
    """
    La fonction actualise les coordonnées des cellules de la population en prenant 
    en compte le stress.
    
    Paramètres
    ------
    population : class Population
        Population d'algues, la classe est précisée dans le fichier class_algue.py
    box : class Box
        Environnement où se déplace les cellules
        
    Retours
    ------
    Aucun    
    """
    for i in range(population.nombre_algues):
        if population.aggregat[i] == False :
            deplacement = np.array([rand.randint(-config.DEP_MAX, config.DEP_MAX),rand.randint(-config.DEP_MAX, config.DEP_MAX)])
            
            possible, indice = check_deplacement(population, i, box, deplacement)
            if (possible == False and indice != -1):
                if (population.aggregat[indice] == True):
                    if (rand.uniform(0,1) < config.probabilite_aggregation):
                        population.aggregat[i] = True
                        population.x[i] += deplacement[0]/2
                        population.y[i] += deplacement[1]/2
                else :
                    if (rand.uniform(0,1) < config.probabilite_aggregation_normal):
                        population.aggregat[i] = True
                        population.aggregat[indice] = True
                        population.x[i] += deplacement[0]/2
                        population.y[i] += deplacement[1]/2
            elif (possible == True):
                population.x[i] += deplacement[0]   
                population.y[i] += deplacement[1]