# Module du choix des paramètres liés à la boite  


from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel, QSpinBox, QComboBox

import data as d



class ChoixSimul_class(QGroupBox) : 
    def __init__(self) : 
        super().__init__()

        layout = QGridLayout()
        self.setLayout(layout)

        self.setTitle("Parametres de la simulation")


        self.long_label = Long_label_class()
        self.long_spinbox = Long_spinbox_class()
        self.larg_label = Larg_label_class()
        self.larg_spinbox = Larg_spinbox_class()
        self.tsim_label = TSimul_label_class()
        self.tsim_spinbox = TSimul_spinbox_class()
        self.vitsim_label = VitSimul_label_class()
        self.vitsim_spinbox = VitSimul_spinbox_class()

        layout.addWidget(self.long_label,0,0)
        layout.addWidget(self.long_spinbox,0,1)
        layout.addWidget(self.larg_label,1,0)
        layout.addWidget(self.larg_spinbox,1,1)
        layout.addWidget(self.tsim_label,2,0)
        layout.addWidget(self.tsim_spinbox,2,1)
        layout.addWidget(self.vitsim_label,3,0)
        layout.addWidget(self.vitsim_spinbox,3,1)
        



class Long_label_class(QLabel) : 
    def __init__(self) : 
        super().__init__()

        self.setText("Longueur de la boite :")



class Long_spinbox_class(QSpinBox) : 
    def __init__(self) :
        super().__init__()

        self.setSuffix(" cm")
        self.setValue(d.long_boite)
        self.setMinimum(d.long_boite_min)
        self.setMaximum(d.long_boite_max)

        self.valueChanged.connect(self.changed)

    def changed(self) : 
        d.long_boite = self.value()



class Larg_label_class(QLabel) : 
    def __init__(self) : 
        super().__init__()

        self.setText("Largeur de la boite :")



class Larg_spinbox_class(QSpinBox) : 
    def __init__(self) :
        super().__init__()

        self.setSuffix(" cm")
        self.setValue(d.larg_boite)
        self.setMinimum(d.larg_boite_min)
        self.setMaximum(d.larg_boite_max)

        self.valueChanged.connect(self.changed)

    def changed(self) : 
        d.larg_boite = self.value()



class TSimul_label_class(QLabel) : 
    def __init__(self) :
        super().__init__()

        self.setText("Temps de modélisation :")



class TSimul_spinbox_class(QSpinBox) : 
    def __init__(self) :
        super().__init__()

        self.setSuffix(" j")
        self.setMinimum(d.t_simul_min)
        self.setMaximum(d.t_simul_max)

        self.valueChanged.connect(self.changed)

    def changed(self) : 
        d.t_simul = self.value()



class VitSimul_label_class(QLabel) : 
    def __init__(self) :
        super().__init__()

        self.setText("Vitesse de la simulation : ")



class VitSimul_spinbox_class(QSpinBox) : 
    def __init__(self) :
        super().__init__()

        self.setSuffix(" h/s")
        self.setMinimum(d.vit_simul_min)
        self.setMaximum(d.vit_simul_max)

        self.valueChanged.connect(self.changed)

    def changed(self) : 
        d.vit_simul = self.value()