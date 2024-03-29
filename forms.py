# AICToolbox
# Auteur : Robin BARKAS

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QMessageBox, QGroupBox, QFrame

import utils

# Définit un formulaire, lié à un scénario, permettant de saisir les paramètres de celui-ci
# Ex : nom d'utilisateur, mot de passe...
class FormScenario(QFrame):
    def __init__(self, fields):
        super().__init__()
        self.fields = []
        self.setUI(fields)

    def setUI(self, fields):
        self.hbox = QHBoxLayout()

        for field in fields:
            lineEdit = utils.LineEditWithPlaceholder(field)

            if (field.startswith("Mot de passe")):
                lineEdit.setEchoMode(QLineEdit.Password)

            self.fields.append(lineEdit)
            self.hbox.addWidget(lineEdit)

        self.setLayout(self.hbox)

    def add_line_edit (self, placeholder = None):
        line_edit = QLineEdit()

        if not (placeholder is None):
            line_edit.setPlaceholderText(placeholder)

    def get_values(self):
        values = []
        for field in self.fields:
            values.append(field.text())

        return values
