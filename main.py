# AICToolbox
# Réalisé dans le cadre de la formation Administrateur Infrastructure et Cloud proposée par OpenClassrooms
# Auteur : Robin BARKAS
# Licence : MIT
# Créé le 09/06/2019

import sys
from PyQt5.QtWidgets import QApplication

monApp=QApplication(sys.argv)

import models
import services
import utils
import views

fenetre=views.Principale()
sys.exit(monApp.exec_())