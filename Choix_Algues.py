# Module du choix des paramètres liés aux algues  


from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel, QSpinBox

import data as d



class Alg_class(QGroupBox) : 
    def __init__(self) :
        super().__init__()

        layout = QGridLayout()
        self.setLayout(layout)

        self.setTitle("Parametres de l'algue")


        self.diam_label = Diam_label_class()
        self.diam_spinbox = Diam_spinbox_class()
        self.vit_label = Vit_label_class()
        self.vit_spinbox = Vit_spinbox_class()
        self.dens_label = Dens_label_class()
        self.dens_spinbox = Dens_spinbox_class()
        self.tdiv_label = Tdiv_label_class()
        self.tdiv_spinbox = Tdiv_spinbox_class()

        layout.addWidget(self.diam_label,0,0)
        layout.addWidget(self.diam_spinbox,0,1)
        layout.addWidget(self.vit_label, 1,0)
        layout.addWidget(self.vit_spinbox,1,1)
        layout.addWidget(self.dens_label,2,0)
        layout.addWidget(self.dens_spinbox,2,1)
        layout.addWidget(self.tdiv_label,3,0)
        layout.addWidget(self.tdiv_spinbox,3,1)



class Diam_label_class(QLabel) : 
    def __init__(self) : 
        super().__init__()

        self.setText("Diamètre de l'algue :")


class Diam_spinbox_class(QSpinBox) : 
    def __init__(self) :
        super().__init__()

        self.setSuffix(" µm")
        self.setValue(d.diam_alg)
        self.setMinimum(d.diam_alg_min)
        self.setMaximum(d.diam_alg_max)

        self.valueChanged.connect(self.changed)

    def changed(self) : 
        d.diam_alg = self.value()



class Vit_label_class(QLabel) : 
    def __init__(self) :
        super().__init__()

        self.setText("Vitesse moyenne : ")



class Vit_spinbox_class(QSpinBox) : 
    def __init__(self) :
        super().__init__()

        self.setSuffix(" m/s")
        self.setValue(d.vit_alg)
        self.setMinimum(d.vit_alg_min)
        self.setMaximum(d.vit_alg_max)

        self.valueChanged.connect(self.changed)

    def changed(self) :
        d.vit_alg = self.value()
        



class Dens_label_class(QLabel) : 
    def __init__(self) :
        super().__init__()

        self.setText("Nombre de départ : ")


class Dens_spinbox_class(QSpinBox) :
    def __init__(self) :
        super().__init__()

        self.setSuffix(" *10")
        self.setValue(d.nb_alg)
        self.setMinimum(d.nb_alg_min)
        self.setMaximum(d.nb_alg_max)

        self.valueChanged.connect(self.changed)

    def changed(self) : 
        d.nb_alg = self.value()*10



class Tdiv_label_class(QLabel) : 
    def __init__(self) :
        super().__init__()

        self.setText("Temps de division : ")



class Tdiv_spinbox_class(QSpinBox) : 
    def __init__(self) :
        super().__init__()

        self.setSuffix(" h")
        self.setValue(d.t_div_alg)
        self.setMinimum(d.t_div_alg_min)
        self.setMaximum(d.t_div_alg_max)

        self.valueChanged.connect(self.changed)

    def changed(self) : 
        d.t_div_alg = self.value()