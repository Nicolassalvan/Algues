#Programme principal, création de la fenetre principale et liens entre tous les parametres

#Développé sur Visual Studio, Spyder et ***, avec PyQt5 et matplotlib 




# Import du système

import sys

# Import des bibliothèques PyQt5

from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QApplication

# Import des modules

from interface_Données import *
from Plot import *
from interface_Choix_Algues import *
from interface_Choix_Stress import *
from interface_Choix_Simulation import *
from interface_Launch_Simulation import *

import data as d

from class_algue import * 
from video_et_anim import *



# Définition de la classe de la fenètre principale



class MainWindow(QMainWindow) : 
    # Classe QMainwindow définissant la fenêtre principale de l'interface 

    def __init__(self) :
        super().__init__()

            # Choix de la dimension et du nom
        self.setWindowTitle("Modélisation Chlamydomonas Reinhardtii")
        # self.setGeometry(0,0,1200,700)

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

            # Création d'un central widget comprenant tous les éléments de la fenêtre principale (appel de fonction)
        self.centralWidget_f()

            # Choix de la police et taille d'affichage (appel de fonction)
        self.ChangeFont()

            # Connection des éléments de le fenêtre et actualisation des affichages (appel de fonction)
        self.connect()
        self.actu()

        # self.show()

        self.showMaximized()            # Affichage de la fenêtre en plein écran

    def connect(self) : 
        # Fonction de connections des différents éléments de la fenètre
        self.Simul.larg_spinbox.valueChanged.connect(self.actu)         # Ici on connecte par exemple le changement de la valeur de la largeur de la boite à l'actualisatio des calculs affichés
        self.Simul.long_spinbox.valueChanged.connect(self.actu)
        self.Alg.nb_spinbox.valueChanged.connect(self.actu)
        
        self.LaunchSimul.simul_button_gif.clicked.connect(self.launch_simul_gif)
        self.LaunchSimul.simul_button_mp4.clicked.connect(self.launch_simul_mp4)


    def actu(self) : 
        # Fonction d'actualisation globale de la fenètre
        self.Stress.seuil_spinbox.TriggerChanged()
        self.Intro.ctes_groupbox.dens_label.actu()
        self.Intro.ctes_groupbox.surfboite_label.actu()


    def ChangeFont(self) :  
        # Choix de la police et taille des caractères

            # Application de la police 4.setFont(d.font)
        self.setFont(d.font)

        
    def create_box(self) : 
        # Fonction permettant de créer un élément de classe Box

        # box = Box(d.long_boite, d.larg_boite)
        box = Box(1000,1000)                # Test
        return box


    def create_pop(self, box : Box) : 
        # fonction permettant de créer une population d'algue 

        pop = Population(d.nb_alg, box)
        return pop


    def launch_simul_gif(self) : 
        # Fonction de lancement de la simulation en gif
        
        print("Lancement de la simulation en gif dans cette fonction")
        self.close()

        self.box = self.create_box()
        self.pop = self.create_pop(self.box)

        gif_simulation(self.pop, self.box)

        print("Done")

    
    def launch_simul_mp4(self) : 
        # Fonction de lancement de la simulation en mp4

        print("Lancement de la simulation en mp4 dans cette fonction")
        self.close()
        self.box = self.create_box()
        self.pop = self.create_pop(self.box)

        video_simulation(self.pop, self.box)

        print("Done")


    def centralWidget_f(self) :             
        # definition du central Widget sur lequel poser les différents elements
 
            # Création du widget
        widget = QWidget()

            # Le Layout créé précédement est appliqué à ce widget (les éléments ajoutés au layout aussi)
        widget.setLayout(self.layout)
        
            # Le central widget est appliqué à la fenêtre
        self.setCentralWidget(widget)


    
# Fin de la classe 



# Module d'affichage de la fenêtre principale

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec())