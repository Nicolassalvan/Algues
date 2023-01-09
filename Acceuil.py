# Module qui permet l'affichage du message d'introduction


from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel

import data as d



class Intro_class(QGroupBox) : 
    def __init__(self) : 
        super().__init__()

        layout = QGridLayout()
        self.setLayout(layout)

        self.setTitle("Bienvenue")
        # self.setStyleSheet("border: 1px solid") 
        # self.setMaximumSize(d.grp_regtrans_maxw,d.grp_regtrans_maxh)


        intro_label = Intro_label_class()

        layout.addWidget(intro_label,0,0)



class Intro_label_class(QLabel) : 
    def __init__(self) : 
        super().__init__()

        self.setText(d.message_intro)    