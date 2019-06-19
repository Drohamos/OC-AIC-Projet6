# AICToolbox
# Auteur : Robin BARKAS

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QMessageBox, QGroupBox, QFrame

import models
import services
import utils
import scenarios
import scenarios_forms

class Principale(QWidget):
    def __init__(self):
        super().__init__()
        self.form_ordinateur = FormOrdinateur()
        self.selected_ordinateur_btn = None
        self.setUI()

    def setUI(self):
        base = QVBoxLayout()
        bottom = QHBoxLayout()

        col_left = QVBoxLayout()
        col_right = QVBoxLayout()

        col_left.addWidget(self.partial_ordinateurs())
        col_right.addWidget(self.partial_scenarios())

        bottom.addLayout(col_left, 1)
        bottom.addLayout(col_right, 1)

        base.addLayout(bottom)
        base.addWidget(self.partial_result())

        self.setLayout(base)
        self.setGeometry(300,300,800,600)
        self.setWindowTitle('Fenêtre principale')

        self.show()

    def partial_ordinateurs(self):
        group = QGroupBox("Sélectionner un poste")
        vbox = QVBoxLayout()

        self.grille_ordinateurs = utils.AutoGridLayout()

        for ordinateur in services.book.ordinateurs:
            btn = utils.OrdinateurButton(ordinateur)
            btn.clicked.connect(self.clicked_btn_ordinateur)
            self.grille_ordinateurs.autoAddWidget(btn)

        vbox.addLayout(self.grille_ordinateurs)
        vbox.addStretch(1)

        self.form_ordinateur = FormOrdinateur()
        vbox.addLayout(self.form_ordinateur)

        btn_add_ordinateur = QPushButton("Ajouter")
        btn_add_ordinateur.clicked.connect(self.clicked_btn_add_ordinateur)
        vbox.addWidget(btn_add_ordinateur)
        vbox.addStretch(2)

        group.setLayout(vbox)

        return group

    def partial_scenarios(self):
        group = QGroupBox("Scénario")
        vbox = QVBoxLayout()

        self.form_scenario = self.partial_scenarios_form()

        vbox.addLayout(self.partial_scenarios_list())
        vbox.addStretch(1)
        vbox.addWidget(self.form_scenario)

        group.setLayout(vbox)

        return group

    def partial_scenarios_list(self):
        grille = utils.AutoGridLayout()

        for scenario in scenarios.scenarios:
            btn = utils.ScenarioButton(scenario)
            btn.clicked.connect(self.clicked_btn_scenario)
            grille.autoAddWidget(btn)

        return grille

    # Label + conteneur formulaire scénario
    def partial_scenarios_form(self):
        frame = QFrame()
        vbox = QVBoxLayout()

        vbox.addWidget(QLabel("Paramètres du scénario"))
        vbox.addWidget(scenarios_forms.FormScenario(["test"]))

        frame.setLayout(vbox)

        return frame

    def partial_result(self):
        group = QGroupBox("Résultat")

        self.console = ResultConsole()

        group.setLayout(self.console)

        return group

    def clicked_btn_ordinateur(self):
        # Si un autre ordinateur était déjà sélectionné, on remet le bouton à son état initial
        if (self.selected_ordinateur_btn):
            self.selected_ordinateur_btn.setChecked(False)

        sender = self.sender()
        # Empêche de décocher un bouton
        sender.setChecked(True)

        self.selected_ordinateur_btn = sender

    def clicked_btn_scenario(self):
        ordinateur = self.selected_ordinateur_btn.ordinateur
        scenario = self.sender().scenario(ordinateur)

        self.run_scenario(scenario)

    def clicked_btn_add_ordinateur(self):
        form = self.form_ordinateur
        ordinateur = form.to_ordinateur()
        services.book.add(ordinateur)

        btn = utils.OrdinateurButton(ordinateur)
        btn.clicked.connect(self.clicked_btn_ordinateur)

        self.grille_ordinateurs.autoAddWidget(btn)
        form.reset()

    def run_scenario(self, scenario):
        self.console.new_run(scenario)

        try:
            result = scenario.execute()
        except Exception as err:
            self.console.new_error(err)
        else:
            self.console.end_run(result.stdout)

# Formulaire d'ajout/modification d'un ordinateur
# Le bouton de validation n'est pas inclus car géré par fenêtre parente
class FormOrdinateur(QHBoxLayout):
    edit_ip   = utils.LineEditWithPlaceholder("Adresse IP*")
    edit_user = utils.LineEditWithPlaceholder("Utilisateur")
    edit_name = utils.LineEditWithPlaceholder("Libellé")

    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.addWidget(self.edit_ip)
        self.addWidget(self.edit_user)
        self.addWidget(self.edit_name)

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

class ResultConsole(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.prompt = QVBoxLayout()
        self.addLayout(self.prompt)
        self.addStretch(1)

    def new_run(self, scenario):
        self.prompt.addWidget(QLabel("Connexion à " + scenario.ordinateur.ssh_address))

    def new_step(self):
        self.prompt.addWidget(QLabel("Action effectuée"))

    def new_error(self, err):
        print(err)

        label = QLabel("Erreur")
        label.setStyleSheet("color: red")

        self.prompt.addWidget(label)

    def end_run(self, result = None):
        if (result):
            self.prompt.addWidget(QLabel("Résultat : " + result))

        self.prompt.addWidget(QLabel("Scénario terminé"))
