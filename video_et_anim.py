"""
Created on Wed Jan  4 19:08:29 2023

@author: Team Algues
"""

# Interface graphique
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers, PillowWriter

import numpy as np

import settings 
import class_algue as algue

import deplacement as move
import reproduction as reprod

# ===== CREATION D'UN FICHIER .mp4 ===== #


def video_simulation(population, rectangle):
    """
    Lance la simulation de la population dans la zone délimitée par un rectangle. 
    Créé un fichier .mp4 à partir du déroulement de la simulation.
    Utilise la fonction update_frame pour update l'état de la population.

    Paramètres
    ----------
    population : class Population
        Population d'algues.
    rectangle : Box
        Zone de simulation.

    Retours
    -------
    None.
    """
    # initialisation du plot
    plt.close('all')

    fig, ax = plt.subplots()

    ax.set_xlim(-5, rectangle.x_max + 5)
    ax.set_ylim(-5, rectangle.x_max + 5)

    scat = ax.scatter([], [], s=5)
    
    # initialisation de l'animation
    animation = FuncAnimation(
        fig, func=animation_frame, frames=np.arange(0, 1000, 1),
        fargs=(population, rectangle,scat,), interval=50)

    # Initialisations du writer
    writer = writers['ffmpeg']
    writer = writer(fps=15, metadata={'artist': 'me'}, bitrate=1800)

    animation.save('Les_Belles_Algues.mp4', writer)

   

# ===== CREATION D'UN GIF ===== #    

def gif_simulation(population, rectangle):
    """
    Lance la simulation de la population dans la zone délimitée par un rectangle. 
    Créé un fichier .gif à partir du déroulement de la simulation.
    Utilise la fonction update_frame pour update l'état de la population.

    Paramètres
    ----------
    population : class Population
        population d'algues.
    rectangle : Box
        zone de simulation.

    Retours
    -------
    Aucun.    
    """
    # initialisation du plot
    plt.close('all')

    fig, ax = plt.subplots()

    ax.set_xlim(-5, rectangle.x_max + 5)
    ax.set_ylim(-5, rectangle.x_max + 5)

    scat = ax.scatter([], [], s=5)
    
    # initialisation de l'animation
    animation = FuncAnimation(
        fig, func=animation_frame, frames=np.arange(0, 1000, 1),
        fargs=(population, rectangle,scat,), interval=50)

    # Initialisations du writer
    writer = PillowWriter(fps=15, metadata={'artist': 'me'}, bitrate=1800)

    animation.save('Les_Belles_Algues.gif', writer)


# ===== FONCTION QUI MET A JOUR LA POPULATION ===== #

def animation_frame(i, population, rect, scat):
    """
    Update chaque frame de l'animation en mettant à jour les morts, les reproductions, 
    l'aggrégation, les déplacements et l'âge des algues de la population. 
    
    Paramètres
    ------
    i: int
        numero de la frame
    population: class population 
        population d'algues
    rect: class Box
        rectangle dans lequel sont simulées les algues
        
    Retours
    ------
    Aucun
    """
    # On met à jour la population avec les cellules qui meurent 
    #update_death(population, rect, ... )
        
    # On met à jour les aggrégats??? 
    
    # On met à jour l'âge et la reproduction des cellules
    if population.nombre_algues < settings.NB_ALGUES_MAX:
        reprod.update_age_et_reprod(population, rect)
        
    # On met à jour les déplacements des cellules 
    move.deplacement_sans_stresse(population, rect)
    
    # Update de l'animation avec un scatter
    data = np.c_[population.x, population.y]
    scat.set_offsets(data)
    scat.set_sizes(population.taille)

# # === Test === #

# boite = algue.Box(1000, 1000)
# pop = algue.Population(10, boite)
# video_simulation(pop, boite)