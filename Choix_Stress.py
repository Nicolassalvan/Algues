# Module du choix des paramètres liés au stress  

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel, QComboBox, QSpinBox

import data as d



class Stress_class(QGroupBox) : 
    def __init__(self) : 
        super().__init__()
        
        self.setTitle("Parametres du stress")

        layout = QGridLayout()
        self.setLayout(layout)

        self.niv_label = NivStress_label_class()
        self.niv_spinbox = NivStress_spin_class()
        self.trigger_label = Trigger_label_class()
        self.trigger_combobox = Trigger_combobox_class()
        self.seuil_label = Seuil_label_class()
        self.seuil_spinbox = Seuil_spinbox_class()
        
        layout.addWidget(self.niv_label,0,0)
        layout.addWidget(self.niv_spinbox,0,1)
        layout.addWidget(self.trigger_label,2,0)
        layout.addWidget(self.trigger_combobox,2,1)
        layout.addWidget(self.seuil_label,3,0)
        layout.addWidget(self.seuil_spinbox,3,1)

        self.trigger_combobox.currentTextChanged.connect(self.seuil_spinbox.TriggerChanged)



class NivStress_label_class(QLabel) :  
    def __init__(self) :
        super().__init__()

        self.setText("Niveau de stress : ")



class NivStress_spin_class(QSpinBox) : 
    def __init__(self) :
        super().__init__()

        self.valueChanged.connect(self.changed)
        self.setValue(d.stress_niv)
        self.setSuffix(" %")
        self.setMinimum(d.stress_min)
        self.setMaximum(d.stress_max)

    def changed(self) : 
        d.stress_niv = self.value()
    



class Trigger_label_class(QLabel) : 
    def __init__(self) :
        super().__init__()

        self.setText("Choix du déclencheur de stress : ")



class Trigger_combobox_class(QComboBox) : 
    def __init__(self) :
        super().__init__()

        self.addItem("Durée")
        self.addItem("Population")

        self.currentTextChanged.connect(self.changed)

    def changed(self) : 
        d.trigger = self.currentText()



class Seuil_label_class(QLabel) : 
    def __init__(self) :
        super().__init__()

        self.setText("Seuil de déclenchement du stress : ")



class Seuil_spinbox_class(QSpinBox) : 
    def __init__(self) :
        super().__init__()

        self.TriggerChanged()

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