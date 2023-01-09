# Module qui permet le lancement de la simulation


from PyQt5.QtWidgets import QGroupBox, QGridLayout, QPushButton, QRadioButton, QLabel

import data as d



class Simul_class(QGroupBox) :
    def __init__(self) : 
        super().__init__()

        layout = QGridLayout()
        self.setLayout(layout)

        self.setTitle("Simulation")
        # self.setStyleSheet("border: 1px solid;")

        self.choixstress_label = ChoixStress_label_class()
        self.choixstress_checkbox = ChoixStress_checkbox_class()

        self.simul_button = QPushButton("Lancer la simulation", self)
        self.simul_button.setStyleSheet("background-color: white")

        layout.addWidget(self.choixstress_label,0,0)
        layout.addWidget(self.choixstress_checkbox,1,0)
        layout.addWidget(self.simul_button,2,0)



class ChoixStress_label_class(QLabel) : 
    def __init__(self) :
        super().__init__()

        self.setText("Voulez-vous appliquer un stress lors de la modélisation ?")



class ChoixStress_checkbox_class(QRadioButton) : 
    def __init__(self) :
        super().__init__()

        self.setText("Oui")

