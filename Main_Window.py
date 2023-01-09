#Programme principal, création de la fenetre principale et liens entre tous les parametres

#Développé sur Visual Studio, Spyder et ***, avec PyQt5 et matplotlib 


# Insertions 

    # Insertion du système
import sys

    # Insertions des différentes bibliothéques utiles au projet 
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize ,Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QGridLayout, QLabel, QApplication


    # Insertions des différents modules 

from Accueil import *
from Plot import *
from Choix_Algues import *
from Choix_Stress import *
from Choix_Simulation import *
from Simulation import *
#from Test import * 



# Définition de la classe de la fenètre principale



class MainWindow(QMainWindow) : 
    def __init__(self) :
        super().__init__()

        self.setWindowTitle("Modélisation Chlamydomonas Reinhardtii")
        self.setGeometry(0,0,1200,700)

        self.layout = QGridLayout()

        self.Intro = Intro_class()
        self.Alg = Alg_class()
        self.Stress = Stress_class()
        self.Simul= ChoixSimul_class()
        self.LaunchSimul = Simul_class()

        self.layout.addWidget(self.Intro,0,0,1,2)           # le widget est en position 0,0 et occuper 1 ligne et 2 colonne
        self.layout.addWidget(self.LaunchSimul,0,2)
        self.layout.addWidget(self.Alg,1,0)
        self.layout.addWidget(self.Stress,1,1)
        self.layout.addWidget(self.Simul,1,2)

        self.centralWidget_f()

        self.connect()
        self.actu()
        self.show()


    def connect(self) : 
        # Fonction de connections des différents éléments de la fenètre
        self.LaunchSimul.simul_button_gif.clicked.connect(self.launch_simul_gif)
        self.LaunchSimul.simul_button_mp4.clicked.connect(self.launch_simul_mp4)

        
    def actu(self) : 
        # Fonction d'actualisation globale de la fenètre
        self.Stress.seuil_spinbox.TriggerChanged()

    
    def launch_simul_gif(self) : 
        # Fonction de lancement de la simulation
        print("Lancement de la simulation en gif dans cette fonction")
    
    def launch_simul_mp4(self) : 
        # Fonction de lancement de la simulation
        print("Lancement de la simulation en mp4 dans cette fonction")
        

    def centralWidget_f(self) :             
        # definition du central Widget sur lequel poser les différents elements 
        widget = QWidget()
        widget.setLayout(self.layout)
        
        self.setCentralWidget(widget)
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec())