# AICToolbox
# Auteur : Robin BARKAS

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QMessageBox, QGroupBox
from fabric import Connection

# Permet de générer l'incrémentation du numéro de ligne/colonne
# Utilisé pour générer une grille automatiquement à partir d'une liste
class GridIterator:
    currentRow = 1
    currentCol = 1

    def __init__(self, numCols):
        self.numCols = numCols

    # Quand le nombre de colonne dépasse le maximum défini,
    # on incrémente la ligne et on réinitialise la colonne
    def incrementCol(self):
        if (self.currentCol == self.numCols):
            self.currentRow += 1
            self.currentCol = 1
        else:
            self.currentCol += 1

    def row(self):
        return self.currentRow

    def col(self):
        col = self.currentCol

        self.incrementCol()

        return col

def test(ordinateur, scenario):
    result = scenario.run()

    print("Résultat : " + str(result.stdout))
    print("Code retour : " + str(result.return_code))
    print("Code erreur : " + str(result.stderr))

# Permet de créer une grille avec un nombre fixé de colonnes,
# les numéros de ligne/colonne sont générés automatiquement
class AutoGridLayout(QGridLayout):
    def __init__(self, cols = 2):
        super().__init__()
        self.iterator = GridIterator(cols)

    def autoAddWidget(self, widget):
        self.addWidget(widget, self.iterator.row(), self.iterator.col())

# Bouton de connexion à un ordinateur
class OrdinateurButton(QPushButton):
    def __init__(self, ordinateur):
        if (ordinateur.name):
            # Le label sera l'adresse ip de l'ordinateur
            super().__init__(ordinateur.name + " (" + ordinateur.ip + ")")
        else:
            # Le label sera l'adresse ip de l'ordinateur
            super().__init__(ordinateur.ip)
        # On stocke une copie complète de l'objet ordinateur
        self.ordinateur = ordinateur

# Bouton de sélection d'un scénario
class ScenarioButton(QPushButton):
    def __init__(self, scenario):
        # Le label sera l'adresse ip de l'ordinateur
        super().__init__(scenario.label)
        # On stocke une toutes les infos du scénario
        self.scenario = scenario()
        self.setCheckable(True)

# Raccourci pour créer LineEdit avec placeholder
class LineEditWithPlaceholder(QLineEdit):
    def __init__(self, placeholder):
        super().__init__()
        self.setPlaceholderText(placeholder)