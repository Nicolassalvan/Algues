# Module permettant le choix des paramètres liés au stress  



# Import des bibliothèques de PyQt5

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel, QComboBox, QSpinBox

# Import du module data

import data as d



# Définition des classes

class Stress_class(QGroupBox) : 
    # Classe QGroupBox contenant les éléments permettant de choisir les paramètres du stress

    def __init__(self) : 
        super().__init__()

            # Choix du nom        
        self.setTitle("Parametres du stress")

            # Définition et ajout du layout
        layout = QGridLayout()
        self.setLayout(layout)

            # Création des différents éléments 
        self.niv_label = NivStress_label_class()
        self.niv_spinbox = NivStress_spin_class()
        self.trigger_label = Trigger_label_class()
        self.trigger_combobox = Trigger_combobox_class()
        self.seuil_label = Seuil_label_class()
        self.seuil_spinbox = Seuil_spinbox_class()
        
            # Ajouts des éléments au layout
        layout.addWidget(self.niv_label,0,0)
        layout.addWidget(self.niv_spinbox,0,1)
        layout.addWidget(self.trigger_label,2,0)
        layout.addWidget(self.trigger_combobox,2,1)
        layout.addWidget(self.seuil_label,3,0)
        layout.addWidget(self.seuil_spinbox,3,1)

            # Connexion entre le choix du type de trigger et la fonction adequat du choix du seuil du trigger 
        self.trigger_combobox.currentTextChanged.connect(self.seuil_spinbox.TriggerChanged)

# Fin de la classe 



class NivStress_label_class(QLabel) : 
    # Classe QLabel introduisant le choix du niveau de stress
    def __init__(self) :
        super().__init__()

            # Définition du Texte
        self.setText("Niveau de stress : ")



class NivStress_spin_class(QSpinBox) :
    # Classe QSpinbox permettant le choix du niveau du stress

    def __init__(self) :
        super().__init__()

            # Choix de la valeur initiale, du suffix, du min et du max
        self.setValue(d.stress_niv)
        self.setSuffix(" %")
        self.setMinimum(d.stress_min)
        self.setMaximum(d.stress_max)

            # Connexion du changement de la valeur à la fonction changed
        self.valueChanged.connect(self.changed)

    def changed(self) : 
        # Fonction permettant d'actualiser la valeur du fichier data avec la valeur courante
        d.stress_niv = self.value()

# Fin de la classe



class Trigger_label_class(QLabel) : 
    #Classe QLabel introduisant le choix du trigger pour le stress 

    def __init__(self) :
        super().__init__()

            # Choix du texte
        self.setText("Choix du déclencheur de stress : ")



class Trigger_combobox_class(QComboBox) : 
    # Classe Combobox permettant de choisir le type de trigger

    def __init__(self) :
        super().__init__()

            # Ajout des choix possibles
        self.addItem("Durée")
        self.addItem("Population")

            # Connexion du changement de la valeur à la fonction changed
        self.currentTextChanged.connect(self.changed)

    def changed(self) : 
        # Fonction d'actualisation de la valeur de trigger dans le fichier data
        d.trigger = self.currentText()

# Fin de la classe 



class Seuil_label_class(QLabel) : 
    # Classe Qlabel permettant l'introduction du choix du niveau du trigger

    def __init__(self) :
        super().__init__()

            # Choix du texte
        self.setText("Seuil de déclenchement du stress : ")



class Seuil_spinbox_class(QSpinBox) : 
    # Classe QSpinBox permettant le choix de la valeur du seuil du trigger
    def __init__(self) :
        super().__init__()

            # appel de la fonction TriggerChanged permettant de proposer les bons reglages
        self.TriggerChanged()

            # Connexion du changement de la valeur et de la fonction changed 
        self.valueChanged.connect(self.changed)

    def changed(self) :
        # Fonction permettant d'actualiser la valeur du fichier data avec la valeur courante 
        if d.trigger == "Durée" :           # On veille à modifier la bonne valeur dans data ici
            d.trigger_t = self.value()
        
        else :
            d.trigger_pop = self.value()
        
    def TriggerChanged(self) : 
        # Fonction permettant de choisir les bons min, max, suffix et valeurs en fonction du type de trigger choisi
        if d.trigger == "Durée" : 
            self.setSuffix(" h")
            self.setValue(d.trigger_t)
            self.setMinimum(d.trigger_t_min)
            self.setMaximum(d.trigger_t_max)
        
        else :
            self.setSuffix(" x10^3 algues")
            self.setValue(d.trigger_pop)
            self.setMinimum(d.trigger_pop_min)
            self.setMaximum(d.trigger_pop_max)

# Fin de la classe



# Fin du module