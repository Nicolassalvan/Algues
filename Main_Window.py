#Programme principal, création de la fenetre principale et liens entre tous les parametres

#Développé sur Visual Studio, Spyder et ***, avec PyQt5 et matplotlib 


# Insertions 

    # Insertion du système
import sys

    # Insertions des différentes bibliothéques utiles au projet 
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize ,Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QLabel, QApplication
from PyQt5.QtGui import QFont, QFontDatabase

    # Insertions des différents modules 

from interface_Données import *
from Plot import *
from interface_Choix_Algues import *
from interface_Choix_Stress import *
from interface_Choix_Simulation import *
from interface_Launch_Simulation import *

from class_algue import *
#from Test import * 

import data as d




# Définition de la classe de la fenètre principale



class MainWindow(QMainWindow) : 
    # Classe de la fenêtre principale de l'interface de départ
    def __init__(self) :
        super().__init__()

            # Dimensions et Titre
        self.setWindowTitle("Modélisation Chlamydomonas Reinhardtii")
        self.setGeometry(0,0,1200,700)

            # Ajout du layout (support)
        self.layout = QGridLayout()

            # Créations des différents éléments 
        self.Intro = Intro_class()
        self.Alg = Alg_class()
        self.Stress = Stress_class()
        self.Simul= ChoixSimul_class()
        self.LaunchSimul = Simul_class()

            # Ajout des éléments au layout 
        self.layout.addWidget(self.Intro,0,0,1,2)           # le widget est en position 0,0 et occuper 1 ligne et 2 colonne
        self.layout.addWidget(self.LaunchSimul,0,2)
        self.layout.addWidget(self.Alg,1,0)
        self.layout.addWidget(self.Stress,1,1)
        self.layout.addWidget(self.Simul,1,2)

            # Création d'un central widget qui comprend tous les éléments de la fenêtre principale
        self.centralWidget_f()

            # Choix de la police et taille d'affichage
        self.ChangeFont()

            # Connection des éléments de le fenêtre, actualisation des affichages et affichage de la fenêtre
        self.connect()
        self.actu()
        self.show()


    def connect(self) : 
        # Fonction de connections des différents éléments de la fenètre
        self.Simul.larg_spinbox.valueChanged.connect(self.actu)         # Ici on connecte par exemple le changement de la valeur de la largeur de la boite à l'actualisatio des calculs affichés
        self.Simul.long_spinbox.valueChanged.connect(self.actu)
        self.Alg.nb_spinbox.valueChanged.connect(self.actu)

        
    def actu(self) : 
        # Fonction d'actualisation globale de la fenètre
        self.Stress.seuil_spinbox.TriggerChanged()
        self.Intro.ctes_groupbox.dens_label.actu()
        self.Intro.ctes_groupbox.surfboite_label.actu()

    
    def ChangeFont(self) :  
        # Choix de la police et taille des caractères

            # Création d'une police QFont
        font = QFont('Arial', 10)

            # Application de la police créée
        self.Intro.intro_label.setFont(font)
        self.Intro.typestress_label.setFont(font)
        self.Intro.ctes_groupbox.surfboite_label.setFont(font)
        self.Intro.ctes_groupbox.dens_label.setFont(font)
        self.Intro.ctes_groupbox.diamalg_label.setFont(font)

        self.Alg.nb_label.setFont(font)
        self.Alg.tdiv_label.setFont(font)
        self.Alg.vit_label.setFont(font)
        # self.Alg.diam_label.setFont(font)

        self.Stress.niv_label.setFont(font)
        self.Stress.seuil_label.setFont(font)
        self.Stress.trigger_label.setFont(font)

        self.Simul.larg_label.setFont(font)
        self.Simul.long_label.setFont(font)
        self.Simul.tsim_label.setFont(font)
        self.Simul.vitsim_label.setFont(font)

        self.LaunchSimul.choixstress_label.setFont(font)
        self.LaunchSimul.stress_oui_radiobutton.setFont(font)
        self.LaunchSimul.stress_non_radiobutton.setFont(font)
        self.LaunchSimul.simul_button_gif.setFont(font)
        self.LaunchSimul.simul_button_mp4.setFont(font)


    def centralWidget_f(self) :             
        # definition du central Widget sur lequel poser les différents elements
 
            # Création du widget
        widget = QWidget()

            # Le Layout créé précédement est appliqué à ce widget (les éléments ajoutés au layout aussi)
        widget.setLayout(self.layout)
        
            # Le central widget est appliqué à la fenêtre
        self.setCentralWidget(widget)
    


# Module d'affichage de la fenêtre principale

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec())