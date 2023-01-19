# -*- coding: utf-8 -*-
"""
@author: Projet Multidisciplinaire Agregation algues - MAIN3 promo 2025
"""

import numpy as np
import cv2
import os
"""
pseudo code pour plus grande des agregats
pour chaque cellule/agregat ont fait le contour
on stock la valeur (perimetre ou air du contour)
on trie le tableau de maniere croissante ou decroissante de sorte que récuperer les val min max soit simple
on prend la taille du plus petit et on le set en taille minim de cellule
on calcule dans un nv tableau de taille meme que celui contenant perimetre/air
on calcule le nombre de cellule correspondant pour chaque en divisant l'air par l'air du plus petit élément
"""

#on prend l'hypothese ou au moins une cellule isolé
def nombre_cell(tab_taille_cell):
    taille_min_cell = np.min(tab_taille_cell)
    return np.sum(tab_taille_cell//taille_min_cell)
