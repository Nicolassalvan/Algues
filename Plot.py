#Classe d'affichage du tableau

from PyQt5.QtWidgets import QGroupBox, QGridLayout

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Plot_class(QGroupBox) : 
    def __init__(self) : 
        super().__init__()

        self.setTitle("Simulation des algues : ")

        layout = QGridLayout()
        self.setLayout(layout)

        self.fig = plt.figure()                     #création du graph 
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas,0,0)