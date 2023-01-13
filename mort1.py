import numpy as np
import class_algue as algue
import settings

def update_mort(population):
    """
    Met à jour la suppression d'algue en fonction du stress.

    Parametres:
    ------
    population: class population
        représente une population d'algues
    settings.STRESS est constant
    """
    tab_mort=np.array([])
    for i in range(population.nombre_algues):
        if(population.aggregat[i]==False and np.random.binomial(1,settings.STRESS,1)==1):
            tab_mort=np.append(tab_mort,i)
    population.supprimer_algue(tab_mort.astype(int))
