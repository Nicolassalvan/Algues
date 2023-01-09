# Module qui permet le lancement de la simulation


from PyQt5.QtWidgets import QButtonGroup, QGroupBox, QGridLayout, QPushButton, QRadioButton, QLabel

import data as d



class Simul_class(QGroupBox) :
    def __init__(self) : 
        super().__init__()

        layout = QGridLayout()
        self.setLayout(layout)

        self.setTitle("Simulation")
        # self.setStyleSheet("border: 1px solid;")

        self.choixstress_label = ChoixStress_label_class()

        self.grpbutton = QButtonGroup()                #on regroupe tous les bouttons dans le meme groupe
        self.grpbutton.setExclusive(True)
        self.stress_oui_radiobutton = QRadioButton("Oui", self)
        self.stress_non_radiobutton = QRadioButton("Non", self)
        self.grpbutton.addButton(self.stress_oui_radiobutton)
        self.grpbutton.addButton(self.stress_non_radiobutton)

        self.simul_button_gif = QPushButton("Lancer la simulation : gif", self)
        self.simul_button_mp4 = QPushButton("Lancer la simulation : mp4", self)
        self.simul_button_gif.setStyleSheet("background-color: white")
        self.simul_button_mp4.setStyleSheet("background-color: white")

        layout.addWidget(self.choixstress_label,0,0)
        layout.addWidget(self.stress_oui_radiobutton,0,1)
        layout.addWidget(self.stress_non_radiobutton,0,2)        
        layout.addWidget(self.simul_button_gif,1,0)
        layout.addWidget(self.simul_button_mp4,2,0)

        self.stress_oui_radiobutton.clicked.connect(self.choix_stress)
        self.stress_non_radiobutton.clicked.connect(self.choix_stress)


    def choix_stress(self) : 
        if self.stress_oui_radiobutton.isChecked() : 
            d.bool_stress = True

        else : 
            d.bool_stress = False



class ChoixStress_label_class(QLabel) : 
    def __init__(self) :
        super().__init__()

        self.setText("Voulez-vous appliquer un stress lors de la modélisation ?")


