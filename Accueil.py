# Module qui permet l'affichage du message d'introduction


from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel
# from PyQt5.QtWidgets import *

import data as d



class Intro_class(QGroupBox) : 
    def __init__(self) : 
        super().__init__()

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.setTitle("Bienvenue")
        # self.setStyleSheet("border: 1px solid") 
        # self.setMaximumSize(d.grp_regtrans_maxw,d.grp_regtrans_maxh)


        self.intro_label = Intro_label_class()
        self.typestress_label = TypeStress_label_class()
        self.ctes_groupbox = Ctes_groupbox_class()

        self.layout.addWidget(self.intro_label,0,0)
        self.layout.addWidget(self.typestress_label,1,0)
        self.layout.addWidget(self.ctes_groupbox,0,1,2,1)



class Intro_label_class(QLabel) : 
    def __init__(self) : 
        super().__init__()

        self.setText(d.message_intro) 
        # QFont arial ('Arial', 10)   
        # self.setFont(arial)


class TypeStress_label_class(QLabel) : 
    def __init__(self) :
        super().__init__()

        self.setText(d.message_type_stress)



class Ctes_groupbox_class(QGroupBox) : 
    def __init__(self) :
        super().__init__()

        self.setTitle("Données de la modélisation : ")

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.dens_label = QLabel("Densité d'algues : ")

        self.layout.addWidget(self.dens_label,0,0)
        