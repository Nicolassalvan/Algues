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

import deplacement_final as move
import agregat as aggr

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

def gif_simulation(population, rectangle,agregat):
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
    aggregat : Liste des aggrégats
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
        fig, func=animation_frame, frames=np.arange(0, 500, 1),
        fargs=(population, rectangle,agregat,scat,), interval=50)

    # Initialisations du writer
    writer = PillowWriter(fps=15, metadata={'artist': 'me'}, bitrate=1800)

    animation.save('Les_Belles_Algues.gif', writer)


# ===== FONCTION QUI MET A JOUR LA POPULATION ===== #

def animation_frame(i, population, rect, agregat,scat):
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
    aggregat : Liste des aggrégats
        
    Retours
    ------
    Aucun
    """
    # On met à jour la population avec les cellules qui meurent 
    #update_death(population, rect, ... )
        
    # On met à jour les aggrégats??? 
    aggr.update_agregat(population,agregat)
    aggr.update_agregat2(population, agregat)
    # On met à jour l'âge et la reproduction des cellules
        
    # On met à jour les déplacements des cellules 

    move.deplacement_cellule(population, rect)
    aggr.deplacement_agregat(population, rect, agregat)
    # Update de l'animation avec un scatter
    data = np.c_[population.x, population.y]
    scat.set_offsets(data)
    scat.set_sizes(population.taille)

# === Test === #
agregat=[]
boite = algue.Box(100, 100)
pop = algue.Population(1000, boite)
gif_simulation(pop, boite,agregat)