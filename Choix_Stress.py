# Module du choix des paramètres liés au stress  


from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel, QComboBox, QSpinBox

import data as d



class Stress_class(QGroupBox) : 
    def __init__(self) : 
        super().__init__()

        layout = QGridLayout()
        self.setLayout(layout)

        self.setTitle("Parametres du stress")

        self.type_label = Type_label_class()
        self.type_combobox = Type_combo_class()
        self.niv_label = NivStress_label_class()
        self.niv_spinbox = NivStress_spin_class()
        self.trigger_label = Trigger_label_class()
        self.trigger_combobox = Trigger_combobox_class()
        self.seuil_label = Seuil_label_class()
        self.seuil_spinbox = Seuil_spinbox_class()
        
        layout.addWidget(self.type_label,0,0)
        layout.addWidget(self.type_combobox,0,1)
        layout.addWidget(self.niv_label,1,0)
        layout.addWidget(self.niv_spinbox,1,1)
        layout.addWidget(self.trigger_label,2,0)
        layout.addWidget(self.trigger_combobox,2,1)
        layout.addWidget(self.seuil_label,3,0)
        layout.addWidget(self.seuil_spinbox,3,1)

        self.type_combobox.currentTextChanged.connect(self.niv_spinbox.TypeStressChanged)
        self.trigger_combobox.currentTextChanged.connect(self.seuil_spinbox.TriggerChanged)



class Type_label_class(QLabel) : 
    def __init__(self) : 
        super().__init__()

        self.setText("Type de stress :")



class Type_combo_class(QComboBox) :     #combobox <=> menus déroulant 
    def __init__(self) : 
        super().__init__()

        self.addItem("Thermique")
        self.addItem("Lumineux")
        self.addItem("Hydrique")
    
        self.currentTextChanged.connect(self.typechanged_f)     # Si le choix est changé, on modifie le type de stress dans le fichier data

        self.typechanged_f()
        
    def typechanged_f(self) : 
        d.type_stress = self.currentText()



class NivStress_label_class(QLabel) :  
    def __init__(self) :
        super().__init__()

        self.setText("Niveau de stress : ")



class NivStress_spin_class(QSpinBox) : 
    def __init__(self) :
        super().__init__()

        self.valueChanged.connect(self.changed)
        self.TypeStressChanged()

    def changed(self) : 
        if d.type_stress == "Thermique" : 
            d.stress_th = self.value()

        elif d.type_stress == "Lumineux" : 
            d.stress_lum = self.value()

        else : 
            d.stress_hydr = self.value()
    
    def TypeStressChanged(self) : 
        if d.type_stress == "Thermique" :
            self.setValue(d.stress_th)
            self.setSuffix(" °C")
            self.setMinimum(d.stress_th_min)
            self.setMaximum(d.stress_th_max)
        
        elif d.type_stress == "Lumineux" :
            self.setValue(d.stress_lum)
            self.setSuffix(" Lum")
            self.setMinimum(d.stress_lum_min)
            self.setMaximum(d.stress_lum_max)

        else : 
            self.setValue(d.stress_hydr)
            self.setSuffix(" \'hydr\'")
            self.setMinimum(d.stress_hydr_min)
            self.setMaximum(d.stress_hydr_max)



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