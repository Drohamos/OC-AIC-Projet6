# AICToolbox
# Réalisé dans le cadre de la formation Administrateur Infrastructure et Cloud proposée par OpenClassrooms
# Auteur : Robin BARKAS
# Licence : MIT
# Créé le 09/06/2019

import sys
from PyQt5.QtWidgets import QApplication

# Initialisation de PyQT (doit se faire avant le chargement de tout autre module)
monApp=QApplication(sys.argv)

import services
import views

# Ouverture de la fenêtre principale
fenetre=views.Principale()
sys.exit(monApp.exec_())