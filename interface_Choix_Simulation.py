# Module du choix des paramètres liés à la boite  



# Import des bibliothèques de PyQt5

from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel, QSpinBox, QComboBox

# Import du module data 

import data as d



# Définition des classes

class ChoixSimul_class(QGroupBox) : 
    # Classe GroupBox contenant les éléments permettant de choisir les paramètres de la simulation

    def __init__(self) : 
        super().__init__()

            # Définition et ajout du layout 
        layout = QGridLayout()
        self.setLayout(layout)

            # Choix du nom
        self.setTitle("Parametres de la simulation")

            # Création des différents éléments
        self.long_label = Long_label_class()
        self.long_spinbox = Long_spinbox_class()
        self.larg_label = Larg_label_class()
        self.larg_spinbox = Larg_spinbox_class()
        self.tsim_label = TSimul_label_class()
        self.tsim_spinbox = TSimul_spinbox_class()
        self.vitsim_label = VitSimul_label_class()
        self.vitsim_spinbox = VitSimul_spinbox_class()

            # Ajout des différents éléments au layout
        layout.addWidget(self.long_label,0,0)
        layout.addWidget(self.long_spinbox,0,1)
        layout.addWidget(self.larg_label,1,0)
        layout.addWidget(self.larg_spinbox,1,1)
        layout.addWidget(self.tsim_label,2,0)
        layout.addWidget(self.tsim_spinbox,2,1)
        layout.addWidget(self.vitsim_label,3,0)
        layout.addWidget(self.vitsim_spinbox,3,1)
        
# Fin de la classe 



class Long_label_class(QLabel) : 
    # Classe QLabel introduisant le choix de la longueur de la boite

    def __init__(self) : 
        super().__init__()

            # Choix du texte
        self.setText("Longueur de la boite :")

# Fin de la classe



class Long_spinbox_class(QSpinBox) : 
    # Classe QSpinbox permettant le choix de la longeur de la boite

    def __init__(self) :
        super().__init__()

            # Choix du Suffix, de la valeur initiale, du min et du max
        self.setSuffix(" cm")
        self.setValue(d.long_boite)
        self.setMinimum(d.long_boite_min)
        self.setMaximum(d.long_boite_max)

            # Connexion du changement de la valeur à la fonction changed
        self.valueChanged.connect(self.changed)

    def changed(self) : 
        # Fonction permettant d'actualiser la valeur du fichier data avec la valeur courante
        d.long_boite = self.value()

# Fin de la classe



class Larg_label_class(QLabel) : 
    # Classe QLabel introduisant le choix de la largeur de la boite

    def __init__(self) : 
        super().__init__()

            # Choix du texte
        self.setText("Largeur de la boite :")

# Fin de la classe 



class Larg_spinbox_class(QSpinBox) : 
    # Classe QSpinbox permettant le choix de la largeur de la boite

    def __init__(self) :
        super().__init__()

            # Choix du suffix, de la valeur initiale, du min et du max
        self.setSuffix(" cm")
        self.setValue(d.larg_boite)
        self.setMinimum(d.larg_boite_min)
        self.setMaximum(d.larg_boite_max)

            # Connexion du changement de la valeur à la fonction changed
        self.valueChanged.connect(self.changed)

    def changed(self) : 
        # Fonction permettant d'actualiser la valeur du fichier data avec la valeur courante
        d.larg_boite = self.value()

# Fin de la classe



class TSimul_label_class(QLabel) : 
    # Classe QLabel introduisant le choix du temps de modélisation 

    def __init__(self) :
        super().__init__()

            # Choix du texte
        self.setText("Temps de modélisation :")

# Fin de la classe 



class TSimul_spinbox_class(QSpinBox) : 
    # Clsse QSpinbox permettant le choix du temps de simulation

    def __init__(self) :
        super().__init__()

            # Choix du Suffix, de la valeur initiale, du min et du max
        self.setSuffix(" j")
        self.setMinimum(d.t_simul_min)
        self.setMaximum(d.t_simul_max)

            # Connexion du changement de la valeur à la fonction changed
        self.valueChanged.connect(self.changed)

    def changed(self) : 
        # Fonction permettant d'actualiser la valeur du fichier data avec la valeur courante
        d.t_simul = self.value()

# Fin de la classe 



class VitSimul_label_class(QLabel) : 
    # Classe QLabel introduisant le choix de la vitesse de simulation

    def __init__(self) :
        super().__init__()

            # Choix du texte
        self.setText("Vitesse de la simulation : ")

# Fin de la classe 



class VitSimul_spinbox_class(QSpinBox) : 
    # Classe QSpinbox permettant le choix de la vitesse de simulation

    def __init__(self) :
        super().__init__()

            # Choix du Suffix, de la valeur initiale, du min et du max
        self.setSuffix(" h/s")
        self.setMinimum(d.vit_simul_min)
        self.setMaximum(d.vit_simul_max)

            # Connexion du changement de la valeur à la fonction changed
        self.valueChanged.connect(self.changed)

    def changed(self) : 
        # Fonction permettant d'actualiser la valeur du fichier data avec la valeur courante
        d.vit_simul = self.value()

# Fin de la classe 



# Fin du module