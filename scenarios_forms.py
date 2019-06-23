# AICToolbox
# Auteur : Robin BARKAS

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QMessageBox, QGroupBox, QFrame

import utils

# Définit un formulaire, lié à un scénario, permettant de saisir les paramètres de celui-ci
# Ex : nom d'utilisateur, mot de passe...
class FormScenario(QFrame):
    def __init__(self, fields):
        super().__init__()
        self.setUI(fields)

    def setUI(self, fields):
        self.hbox = QHBoxLayout()
        self.setLayout(self.hbox)

        for field in fields:
            self.hbox.addWidget(utils.LineEditWithPlaceholder("Interface (ex : ens33)"))

    def add_line_edit (self, placeholder = None):
        line_edit = QLineEdit()

        if not (placeholder is None):
            line_edit.setPlaceholderText(placeholder)