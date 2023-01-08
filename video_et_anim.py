#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 19:08:29 2023

@author: Team Algues
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers 
import settings 
from class_algue import *

def video_et_animation(population, rectangle):
    """
    Lance la simulation de la population dans la zone délimitée par un rectangle. 
    Créé un fichier .mp4 à partir du déroulement de la simulation et affiche un plot
    de la simulation. Utilise la fonction update_frame pour update l'état de la 
    population.

    Parameters
    ----------
    population : class Population
        population d'algues.
    rectangle : Box
        zone de simulation.

    Returns
    -------
    None.
    
    """
    # initialisation du plot
    plt.close('all')

    fig = plt.figure(1)
    ax = plt.axes()


    ax.set_xlim(-5, rectangle.x_max + 5)
    ax.set_ylim(-5, rectangle.x_max + 5)

    scat = ax.scatter([], [], s=5)
    
    # initialisation de l'animation
    animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, 1000, 1), fargs=(population, rectangle,scat,), interval=20)
    plt.show()

    # Initialisations du writer
    writer = writers['ffmpeg']
    writer = writer(fps=15, metadata={'artist': 'me'}, bitrate=1800)

    animation.save('Les_Belles_Algues.mp4', writer)
    
    
    

def animation_frame(i, population, rect, scat):
    """
    Update chaque frame de l'animation en mettant à jour les morts, les reproductions, 
    l'aggrégation, les déplacements et l'âge des algues de la population. 
    
    Parameters
    ------
    i: int
        numero de la frame
    population: class population 
        population d'algues
    rect: class Box
        rectangle dans lequel sont simulées les algues
    """
    # On met à jour la population avec les cellules qui meurent 
    #update_death(population, rect, ... )
    
    # on met à jour les reproductions des cellules 
    #update_reprod(population, rect, ...)
    
    # On met à jour les aggrégats??? 
    
    # On met à jour les déplacements des cellules 
    
    # On met à jour l'âge des cellules
    
    
    # Update de l'animation avec un scatter
    data = np.c_[population.x, population.y]
    scat.set_offsets(data)


# === Test === #
boite = Box(100, 100)
pop = Population(1000, boite)

video_et_animation(pop, boite)


    
     
    
        
    
    
    