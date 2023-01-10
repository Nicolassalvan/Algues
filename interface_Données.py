# Module qui permet l'affichage du message d'introduction


from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel
# from PyQt5.QtWidgets import *

import data as d



class Intro_class(QGroupBox) : 
    # Classe groupBox qui contient les différents éléments d'introduction et de calcul des constantes

    def __init__(self) : 
        super().__init__()

            # Définition du layout du groupbox
        self.layout = QGridLayout()
        self.setLayout(self.layout)

            # Nom du GroupBox
        self.setTitle("Bienvenue")

            # Création des différents éléments
        self.intro_label = Intro_label_class()
        self.typestress_label = TypeStress_label_class()
        self.ctes_groupbox = Ctes_groupbox_class()

            # Ajout des éléments au layout
        self.layout.addWidget(self.intro_label,0,0)
        self.layout.addWidget(self.typestress_label,1,0)
        self.layout.addWidget(self.ctes_groupbox,0,1,2,1)



class Intro_label_class(QLabel) : 
    # Classe du message d'introduction à la fenêtre

    def __init__(self) : 
        super().__init__()

            # Choix du text du QLabel
        self.setText(d.message_intro) 



class TypeStress_label_class(QLabel) : 
    # Classe du message d'explication du choix du stress

    def __init__(self) :
        super().__init__()
        
            # Choix du text du QLabel
        self.setText(d.message_type_stress)



class Ctes_groupbox_class(QGroupBox) :
    # Classe permettant de calculer et d'afficher les différentes constantes de la simulation

    def __init__(self) :
        super().__init__()

            # Nom du Groupbox
        self.setTitle("Données de la modélisation : ")

            # Définition du layout et ajout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

            # Création des éléments
        self.surfboite_label = SurfBoite_label_class()
        self.dens_label = DensAlg_label_class()
        self.diamalg_label = DiamAlg_label_class()

            # Ajout des éléments au layout
        self.layout.addWidget(self.surfboite_label,0,0)
        self.layout.addWidget(self.dens_label,1,0)
        self.layout.addWidget(self.diamalg_label,2,0)


class SurfBoite_label_class(QLabel) : 
    # Classe permettant l'affichage de la surface de la boite

    def __init__(self) :
        super().__init__()

        self.setText("Surface de la boite : " + str(d.larg_boite*d.long_boite) + " cm²")

    def actu(self) : 
        self.setText("Surface de la boite : " + str(d.larg_boite*d.long_boite) + " cm²")



class DensAlg_label_class(QLabel) : 
    # Classe permettant d'afficher la densité d'algues initiale

    def __init__(self) :
        super().__init__()

        self.setText("Densité d'algues : ")

    def actu(self) : 
        d.dens_alg = d.nb_alg / (d.larg_boite*d.long_boite)
        self.setText("Densité d'algues : "+ str(d.dens_alg)+" /cm²")



class DiamAlg_label_class(QLabel) : 
    # Classe permettant d'afficher le diamètre d'une algue
    def __init__(self) :
        super().__init__()
    
        self.setText("Diamètre d'une algue : " + str(d.diam_alg) + " µm")
