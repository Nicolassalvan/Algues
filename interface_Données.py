# Module qui permet l'affichage du message d'introduction



# Import des bibliothèques de PyQt5 

from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel

# Import du module data

import data as d



# Définition des classes

class Intro_class(QGroupBox) : 
    # Classe QGroupBox contenant les différents éléments d'introduction et de calcul des constantes

    def __init__(self) : 
        super().__init__()

            # Définition et ajout du layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

            # Choix du nom
        self.setTitle("Bienvenue")

            # Création des différents éléments
        self.intro_label = Intro_label_class()
        self.typestress_label = TypeStress_label_class()
        self.ctes_groupbox = Ctes_groupbox_class()

            # Ajout des éléments au layout
        self.layout.addWidget(self.intro_label,0,0)
        self.layout.addWidget(self.typestress_label,1,0)
        self.layout.addWidget(self.ctes_groupbox,0,1,2,1)

# Fin de la classe 



class Intro_label_class(QLabel) : 
    # Classe QLabel permettant d'afficher le message d'introduction de l'interface graphique

    def __init__(self) : 
        super().__init__()

            # Choix du texte
        self.setText(d.message_intro) 

# Fin de la classe 



class TypeStress_label_class(QLabel) : 
    # Classe QLabel permettant d'afficher le message explicatif sur le choix du stress

    def __init__(self) :
        super().__init__()
        
            # Choix du texte
        self.setText(d.message_type_stress)

# Fin de la classe 



class Ctes_groupbox_class(QGroupBox) :
    # Classe QGroupBox permettant de calculer et d'afficher les différentes constantes

    def __init__(self) :
        super().__init__()

            # Choix du nom
        self.setTitle("Données de la modélisation : ")

            # Définition et ajout du layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

            # Création des éléments
        self.surfboite_label = SurfBoite_label_class()
        self.dens_label = DensAlg_label_class()
        self.diamalg_label = DiamAlg_label_class()

            # Ajout des éléments au layout
        self.layout.addWidget(self.surfboite_label,0,0)
        self.layout.addWidget(self.dens_label,1,0)
        self.layout.addWidget(self.diamalg_label,2,0)

# Fin de la classe 

class SurfBoite_label_class(QLabel) : 
    # Classe QLabel permettant l'affichage de la surface de la boite

    def __init__(self) :
        super().__init__()

        self.actu()

    def actu(self) : 
        # Fonction permettant d'actualiser l'affichage avec les bonnes valeurs
            # Choix du texte
        d.surf_boite = d.larg_boite*d.long_boite
        self.setText("Surface de la boite : " + str(d.surf_boite) + " mm²")

# Fin de la classe 



class DensAlg_label_class(QLabel) : 
    # Classe QLabel permettant d'afficher la densité d'algues initiale

    def __init__(self) :
        super().__init__()

            # Choix du texte 
        self.setText("Densité d'algues : ")

    def actu(self) : 
        # Fonction permettant d'actualiser l'affichage avec les bonnes valeurs
        d.dens_alg = d.nb_alg / (d.larg_boite*d.long_boite)
            #Choix du texte
        self.setText("Densité d'algues : "+ str(d.dens_alg)+" /cm²")

# Fin de la classe



class DiamAlg_label_class(QLabel) : 
    # Classe QLabel permettant d'afficher le diamètre d'une algue

    def __init__(self) :
        super().__init__()
    
            # Choix du texte
        self.setText("Diamètre d'une algue : " + str(d.diam_alg) + " µm")

# Fin de la classe



# Fin du module