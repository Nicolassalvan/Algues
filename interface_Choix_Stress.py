# Module permettant le choix des paramètres liés au stress  

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel, QComboBox, QSpinBox

import data as d



class Stress_class(QGroupBox) : 
    # Classe QGroupBox contenant les différents éléments du choix concercnant le stress

    def __init__(self) : 
        super().__init__()

            # Nom du groupbox        
        self.setTitle("Parametres du stress")

            # Définition du layout et ajout
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

            # Création du lien entre le choix du type de trigger et le Spinbox du niveau de trigger associé
        self.trigger_combobox.currentTextChanged.connect(self.seuil_spinbox.TriggerChanged)



class NivStress_label_class(QLabel) : 
    # Classe QLabel 
    def __init__(self) :
        super().__init__()

            # Définition du Texte
        self.setText("Niveau de stress : ")



class NivStress_spin_class(QSpinBox) :
    # Classe  permettant de choisir le niveau du stress, en %
    def __init__(self) :
        super().__init__()

            # Connexion à la fonction changed, appelée lorsque la valeur est changée
        self.valueChanged.connect(self.changed)

            # Choix de la valeur initiale, du suffix, du min et du max
        self.setValue(d.stress_niv)
        self.setSuffix(" %")
        self.setMinimum(d.stress_min)
        self.setMaximum(d.stress_max)

    def changed(self) : 
        # Fonction d'actualisation de la valeur du niveau de stres dans le fichier data
        d.stress_niv = self.value()
    



class Trigger_label_class(QLabel) : 
    #Classe QLabel introduisant le choix du trigger pour le stress 

    def __init__(self) :
        super().__init__()

            # Choix du texte
        self.setText("Choix du déclencheur de stress : ")



class Trigger_combobox_class(QComboBox) : 
    # Classe permettant de choisir le type de trigger

    def __init__(self) :
        super().__init__()

            # Ajout des choix possibles
        self.addItem("Durée")
        self.addItem("Population")

            # Connexions entre le changement du trigger et la fonction changed
        self.currentTextChanged.connect(self.changed)

    def changed(self) : 
        # Fonction d'actualisation de la valeur de trigger dans le fichier data
        d.trigger = self.currentText()



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
        if d.trigger == "Durée" : 
            d.trigger_t = self.value()
        
        else :
            d.trigger_pop = self.value()
        
    def TriggerChanged(self) : 
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