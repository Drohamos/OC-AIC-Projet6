# AICToolbox
# Réalisé dans le cadre de la formation Administrateur Infrastructure et Cloud proposée par OpenClassrooms
# Auteur : Robin BARKAS
# Créé le 09/06/2019

# Cache les avertissements de dépréciation envoyés par les dépendances de la librairie Fabric
import warnings
import cryptography
warnings.simplefilter("ignore", cryptography.utils.CryptographyDeprecationWarning)

import sys
from PyQt5.QtWidgets import QApplication

monApp=QApplication(sys.argv)

import models
import services
import utils
import views

fenetre=views.Principale()
sys.exit(monApp.exec_())