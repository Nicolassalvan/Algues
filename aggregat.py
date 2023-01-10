import class_algue as cla 
import matplotlib.pyplot as plt
import settings as config
import random as rand
import numpy as np

def recherche_aggregat(aggregat,indice):
    """
    Paramètre
    ==========
    aggregat : tableau des algues aggrégées
    indice : indice de l'algue à tester

    Cette fonction permet de déterminer dans quelle aggrégats se trouve la cellule d'indice indice

    retourne l'indice de l'aggrégat dans lequel se trouve la cellule d'indice indice
    """

    for i in range(len(aggregat)):
        for j in range(len(aggregat[i])):
            if aggregat[i][j] == indice:
                return i

def update_aggregat(population,aggregat):
    """
    Met à jour l'état d'aggrégation d'une cellule en contact avec une autre cellule
    Si une cellule entre en contact avec une cellule aggregé alors elle a plus de chance de s'aggréger

    Cette fonction aura besoin de la fonction recherche_aggregat

    Paramètre
    =========
    population : liste des algues
    aggregat : liste des algues aggrégées


    Retour : Ne retourne rien
    """

    #cette boucle permet de tester s'il y a des cellules autour d'une cellule d'indice i
    for i in range(population.nombre_algues):
        if population.aggregat[i] == False:
            j = 0
            verif = 0

            #Cette boucle a pour but de vérifier si la cellule s'aggrège ou non avec une autre cellule autour d'elle
            while (j!= population.nombre_algues and verif == 0):

                #cette condition permet de savoir si il y a une cellule autour de la cellule d'indice i
                if (np.abs(population.x[i] - population.x[j]) <= 1 and np.abs(population.y[i] - population.y[j]) <= 1 and i != j):

                    #si la cellule à côté est aggrégée alors la cellule d'indice i a plus de chance de s'aggréger
                    if (population.aggregat[j] == True):

                        #Si la cellule à côté est aggrégée, alors la cellule d'indice i a une probabilité de s'aggréger plus élevée
                        if (rand.uniform(0,1)< config.probabilite_aggregation):

                            #si la proba est réussi, alors ajouter cette cellule dans l'aggrégat
                            population.aggregat[i] = True
                            population.x[i] = (population.x[j]+population.x[i])/2
                            population.y[i] = (population.y[j]+population.y[i])/2
                            indice = recherche_aggregat(aggregat,j)
                            aggregat[indice].append(i)

                            #je fais vérif = 1 pour arrêter la boucle car la cellule s'est aggrégée
                            verif = 1
                    else :
                        #si la cellule à côté n'est pas aggrégée alors la cellule d'indice i a une probabilité de s'aggréger normal
                        if (rand.uniform(0,1) < config.probabilite_aggregation_normal):

                            #si la proba est réussi, alors ajouter les deux cellules comme étant un nouvelle aggrégat
                            population.aggregat[i] = True
                            population.aggregat[j] = True
                            population.x[i] = (population.x[j]+population.x[i])/2
                            population.y[i] = (population.y[j]+population.y[i])/2
                            aggregat.append([i,j])

                            #je fais vérif = 1 pour arrêter la boucle car la cellule s'est aggrégée
                            verif = 1
                j+=1
                            

def check_deplacement_aggregat(population, i, box, aggregat,deplacement):
    """
    Vérifie si le déplacement d'un aggrégat à l'indice i est possible

    Paramètre 
    =========
    population : liste de cellule
    i : indice de l'aggrégat dans le tableau aggrégat
    box : limite de l'environnement 
    aggregat : le tableau contenant les différents aggrégats de l'environnement 


    retour 
    =========
    Retourne True si le déplacement est possible
    False sinon
    """
    
    #On vérifie d'abord sur la bordure
    nombre_cellule = len(aggregat[i])
    for j in range(nombre_cellule):

        #Ces deux conditions servent à vérifier si l'aggrégat ne veut pas sortir de la box
        if (population.x[aggregat[i][j]] + deplacement[0] < 0 or population.x[aggregat[i][j]] + deplacement[0] > box.x_max):
            return False
        if (population.y[aggregat[i][j]] + deplacement[1] < 0 or population.y[aggregat[i][j]] + deplacement[1] > box.y_max):
            return False

        #cette boucle vérifie si l'aggrégat ne veut pas se déplacer vers une cellule
        for k in range(population.nombre_algues):

            #je vérifie que la cellule n'est pas dans l'aggrégat
            if(k != aggregat[i][j]):
                if (np.abs(population.x[aggregat[i][j]] + deplacement[0] - population.x[k]) <= 1 and np.abs(population.y[aggregat[i][j]] + deplacement[1] - population.y[k]) <= 1):
                    if (population.aggregat[k] == False):
                        return False
                    else :
                        if (k not in aggregat[i]):
                            return False
    return True

def deplacement_aggregat(population,box, aggregat):
    """

    La fonction déplace toutes les cellules qui sont aggrégé
    
    Paramètre 
    ===========
    population : liste de cellule
    box : limite de notre environnement 
    aggregat : tableau des différents aggrégats de notre environnement 


    Retour 
    ===========
    Ne retourne rien
    """
    
    #On parcourt tous les aggrégats
    for i in range(len(aggregat)):
        deplacement = [rand.uniform(-config.Dep_max,config.Dep_max),rand.uniform(-config.Dep_max,config.Dep_max)]

        #On vérifie si le déplacement est possible
        #Si oui, alors on déplace l'aggrégat
        #Sinon, on ne fait rien
        if (check_deplacement_aggregat(population,i,box,aggregat,deplacement)):
            nombre_cellule = len(aggregat[i])
            for j in range(nombre_cellule):
                population.x[aggregat[i][j]] += deplacement[0]
                population.y[aggregat[i][j]] += deplacement[1]

        
    



        