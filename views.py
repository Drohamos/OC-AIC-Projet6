# AICToolbox
# Auteur : Robin BARKAS

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QMessageBox, QGroupBox

import models
import services
import utils
import scenarios

class Principale(QWidget):
    def __init__(self):
        super().__init__()
        self.form = FormOrdinateur()
        self.selected_ordinateur_btn = None
        self.setUI()

    def setUI(self):
        base = QHBoxLayout()

        col_left = QVBoxLayout()
        col_right = QVBoxLayout()

        col_left.addWidget(self.partial_ordinateurs())
        col_left.addWidget(self.partial_scenarios())
        col_right.addWidget(self.partial_result())

        base.addLayout(col_left)
        base.addLayout(col_right)

        self.setLayout(base)
        self.setGeometry(300,300,800,600)
        self.setWindowTitle('Fenêtre principale')

        self.show()

    def partial_ordinateurs(self):
        group = QGroupBox("Ordinateur")
        vbox = QVBoxLayout()

        grille = AutoGridLayout()

        for ordinateur in services.book.ordinateurs:
            btn = OrdinateurButton(ordinateur)
            #btn.clicked.connect(self.ordinateur_clicked)
            grille.autoAddWidget(btn)

        vbox.addLayout(grille)     

        group.setLayout(vbox)

        return group

    def partial_scenarios(self):
        group = QGroupBox("Scénario")
        
        vbox = QVBoxLayout()

        grille = AutoGridLayout()

        for scenario in scenarios.scenarios:
            btn = ScenarioButton(scenario)
            #btn.clicked.connect(self.scenario_clicked)
            grille.autoAddWidget(btn)

        vbox.addLayout(grille)    

        group.setLayout(vbox)

        return group

    def partial_result(self):
        group = QGroupBox("Résultat")
        
        vbox = QVBoxLayout()

        group.setLayout(vbox)

        return group
    

# Fenêtre principale : sélection du/des ordinateurs
class Principale_Old(QWidget):
    def __init__(self):
        super().__init__()
        self.form = FormOrdinateur()
        self.selected_ordinateur_btn = None
        self.setUI()
    
    def setUI(self):
        vbox = QVBoxLayout()

        # Liste des ordinateurs
        vbox.addWidget(QLabel("Sélectionner un ordinateur :"))

        ordinateurGroupBox = QGroupBox()

        self.grille = self.ordinateurs_buttons_grid()
        ordinateurGroupBox.setLayout(self.grille)
        vbox.addWidget(ordinateurGroupBox)
        vbox.addStretch(1)

        # Liste des scénarios
        vbox.addWidget(QLabel("Sélectionner un scénario :"))

        self.scenarios = self.scenarios_buttons_grid()
        vbox.addLayout(self.scenarios)
        vbox.addStretch(2)
        
        # Formulaire d'ajout
        vbox.addWidget(self.form)

        # Bouton de validation du formulaire
        add_ordinateur = QPushButton("Ajouter")
        add_ordinateur.clicked.connect(self.add_ordinateur_clicked)
        vbox.addWidget(add_ordinateur)

        self.setLayout(vbox)
        self.setGeometry(300,300,500,250)
        self.setWindowTitle('Fenêtre principale')

        self.show()

    def add_ordinateur_clicked(self):
        ordinateur = self.form.to_ordinateur()
        services.book.add(ordinateur)
        
        btn = OrdinateurButton(ordinateur)
        btn.clicked.connect(self.ordinateur_clicked)

        self.grille.autoAddWidget(btn)
        self.form.reset()

    def ordinateur_clicked(self):
        # Si un autre ordinateur était déjà sélectionné, on remet le bouton à son état initial
        if (self.selected_ordinateur_btn):
            self.selected_ordinateur_btn.setChecked(False)

        sender = self.sender()
        # Empêche de décocher un bouton
        sender.setChecked(True)

        self.selected_ordinateur_btn = sender

    def scenario_clicked(self):
        ordinateur = self.selected_ordinateur_btn.ordinateur
        scenario = self.sender().scenario(ordinateur)
        result = scenario.execute()

        alert = QMessageBox()
        alert.setWindowTitle("Réponse du scénario")
        alert.setText(result.stdout)
        alert.exec()

        print(result.stdout)

    # Crée une boucle de boutons à partir de la liste des ordinateurs
    def ordinateurs_buttons_grid(self):
        grille=AutoGridLayout()

        for ordinateur in services.book.ordinateurs:
            btn = OrdinateurButton(ordinateur)
            btn.clicked.connect(self.ordinateur_clicked)
            grille.autoAddWidget(btn)

        return grille
        
    def scenarios_buttons_grid(self):
        grille=AutoGridLayout()

        for scenario in scenarios.scenarios:
            btn = ScenarioButton(scenario)
            btn.clicked.connect(self.scenario_clicked)
            grille.autoAddWidget(btn)

        return grille


class AutoGridLayout(QGridLayout):
    def __init__(self, cols = 2):
        super().__init__()
        self.iterator = utils.GridIterator(cols)

    def autoAddWidget(self, widget):
        self.addWidget(widget, self.iterator.row(), self.iterator.col())

# Bouton de connexion à un ordinateur
class OrdinateurButton(QPushButton):
    def __init__(self, ordinateur):
        # Le label sera l'adresse ip de l'ordinateur
        super().__init__(ordinateur.ip)
        # On stocke une copie complète de l'objet ordinateur 
        self.ordinateur = ordinateur

        self.setCheckable(True)

# Bouton de sélection d'un scénario
class ScenarioButton(QPushButton):
    def __init__(self, scenario):
        # Le label sera l'adresse ip de l'ordinateur
        super().__init__(scenario.label)
        # On stocke une toutes les infos du scénario
        self.scenario = scenario

# Raccourci pour créer LineEdit avec placeholder
class LineEditWithPlaceholder(QLineEdit):
    def __init__(self, placeholder):
        super().__init__()
        self.setPlaceholderText(placeholder)

# Formulaire d'ajout/modification d'un ordinateur
# Le bouton de validation n'est pas inclus car géré par fenêtre parente
class FormOrdinateur(QWidget):
    edit_ip   = LineEditWithPlaceholder("Adresse IP*")
    edit_user = LineEditWithPlaceholder("Utilisateur")
    edit_name = LineEditWithPlaceholder("Libellé")

    def __init__(self):
        super().__init__()
        self.setUI()
    
    def setUI(self):
        hbox = QHBoxLayout()
        
        hbox.addWidget(self.edit_ip)
        hbox.addWidget(self.edit_user)
        hbox.addWidget(self.edit_name)

        self.setLayout(hbox)

    # Instancie un objet Ordinateur à partir de l'état actuel du formulaire
    def to_ordinateur(self):
        ordinateur = models.Ordinateur(self.edit_ip.text(), self.edit_user.text(), self.edit_name.text())

        return ordinateur

    # Modifie l'état du formulaire pour correspondre à un objet ordinateur donné
    def fill_from_ordinateur(self, ordinateur):
        self.edit_ip.setText(ordinateur.ip)
        self.edit_user.setText(ordinateur.user)
        self.edit_name.setText(ordinateur.name)

    def reset(self):
        self.edit_ip.setText("")
        self.edit_user.setText("")
        self.edit_name.setText("")
