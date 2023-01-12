# Module qui permet le lancement de la simulation


# Import des bibliothèque PyQt5

from PyQt5.QtWidgets import QButtonGroup, QGroupBox, QGridLayout, QPushButton, QRadioButton, QLabel

# Import du module data

import data as d



# Définition des classes

class Simul_class(QGroupBox) :
    # Classe QGroupbox contenant les éléments permettant de choisir les paramètres du lancement de la simulation

    def __init__(self) : 
        super().__init__()

            # Choix et ajout du layout 
        layout = QGridLayout()
        self.setLayout(layout)

            # Choix du nom
        self.setTitle("Simulation")

            # Création des éléments 
        self.choixstress_label = ChoixStress_label_class()


            # Création d'un groupe de bouttons (ici pour le choix d'application ou non d'un stress lors de la simulation)
        self.grpbutton = QButtonGroup()                
        self.grpbutton.setExclusive(True)                               # Les bouttons ne peuvent etre selectionnés en même temps
        self.stress_oui_radiobutton = QRadioButton("Oui", self)         # Création d'un boutton oui
        self.stress_oui_radiobutton.setChecked(True)                    # Initialement séléctionné
        self.stress_non_radiobutton = QRadioButton("Non", self)         # Création d'un boutton non
        self.grpbutton.addButton(self.stress_oui_radiobutton)           # Ajout des bouttons au groupe de bouttons
        self.grpbutton.addButton(self.stress_non_radiobutton)

            # Création d'un boutton permettant de lancer la simulation en format gif
        self.simul_button_gif = QPushButton("Lancer la simulation : gif", self)
        self.simul_button_gif.setStyleSheet("background-color: white")      # Choix de la couleur de fond

            # Création d'un boutton permettant de lancer la simulation en format mp4
        self.simul_button_mp4 = QPushButton("Lancer la simulation : mp4", self)
        self.simul_button_mp4.setStyleSheet("background-color: white")      # Choix de la couleur de fond

            # Ajout des éléments au layout
        layout.addWidget(self.choixstress_label,0,0)
        layout.addWidget(self.stress_oui_radiobutton,0,1)
        layout.addWidget(self.stress_non_radiobutton,0,2)        
        layout.addWidget(self.simul_button_gif,1,0)
        layout.addWidget(self.simul_button_mp4,2,0)

            # Appel de la fonction connection
        self.connect_f()


    def connect_f(self) : 
        # Fonction de connexion des éléments entre eux
        self.stress_oui_radiobutton.clicked.connect(self.choix_stress)      # Par exemple : le boutton de choix de stress oui est connecté à la fonction de la classe choix_stress
        self.stress_non_radiobutton.clicked.connect(self.choix_stress)



    def choix_stress(self) : 
        # Fonction permettant d'actualiser la valeur du fichier data avec la valeur courante
        if self.stress_oui_radiobutton.isChecked() :        # Si le choix de stress oui est séléctionné 
            d.bool_stress = True                            # on fixe le booléen de stress de data à True 

        else : 
            d.bool_stress = False

    
# Fin de la classe



class ChoixStress_label_class(QLabel) : 
    # Classe QLabel introduisant le choix de l'application d'un stress lors de la simulation

    def __init__(self) :
        super().__init__()

            # Choix du texte
        self.setText("Voulez-vous appliquer un stress lors de la modélisation ?")

# Fin de la classe



# Fin du module