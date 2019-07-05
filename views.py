# AICToolbox
# Auteur : Robin BARKAS

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QMessageBox, QGroupBox, QFrame, QStackedLayout

import models
import services
import utils
import scenarios
import forms

class Principale(QWidget):
    def __init__(self):
        super().__init__()
        self.form_ordinateur = FormOrdinateur()
        self.selected_scenario_btn = None
        self.setUI()

    # Génère l'interface utilisateur
    def setUI(self):
        base = QVBoxLayout()
        top = QHBoxLayout()

        # Moitié haute de la fenêtre : 2 colonnes (liste des ordinateurs; liste des scénarios)
        col_top_left = QVBoxLayout()
        col_top_right = QVBoxLayout()

        col_top_left.addWidget(self.partial_scenarios())
        col_top_right.addWidget(self.partial_ordinateurs())

        top.addLayout(col_top_left, 1)
        top.addLayout(col_top_right, 1)

        base.addLayout(top)

        # Moitié basse : Log récapitulatif déroulement scénario
        base.addWidget(self.partial_result())

        self.setLayout(base)
        self.setGeometry(300,300,700,480)
        self.setWindowTitle('AICToolbox')

        self.show()

    # Colonne de gauche
    def partial_ordinateurs(self):
        group = QGroupBox("Sélectionner un poste")
        vbox = QVBoxLayout()

        # Liste des ordinateurs (boutons)
        self.grille_ordinateurs = utils.AutoGridLayout()

        for ordinateur in services.book.ordinateurs:
            btn = utils.OrdinateurButton(ordinateur)
            btn.clicked.connect(self.clicked_btn_ordinateur)
            self.grille_ordinateurs.autoAddWidget(btn)

        vbox.addLayout(self.grille_ordinateurs)
        vbox.addStretch(1)

        # Formulaire ajout d'un ordinateur
        self.form_ordinateur = FormOrdinateur()
        vbox.addLayout(self.form_ordinateur)

        btn_add_ordinateur = QPushButton("Ajouter")
        btn_add_ordinateur.clicked.connect(self.clicked_btn_add_ordinateur)
        vbox.addWidget(btn_add_ordinateur)

        group.setLayout(vbox)

        return group

    # Colonne de droite
    def partial_scenarios(self):
        group = QGroupBox("Scénario")
        vbox = QVBoxLayout()

        form_scenario = self.partial_scenarios_form()
        form_scenario.hide()

        vbox.addLayout(self.partial_scenarios_list())
        vbox.addStretch(1)
        vbox.addWidget(form_scenario)

        group.setLayout(vbox)

        return group

    # Liste des scénarios
    def partial_scenarios_list(self):
        grille = utils.AutoGridLayout()

        for scenario in scenarios.scenarios:
            btn = utils.ScenarioButton(scenario)
            btn.clicked.connect(self.clicked_btn_scenario)
            grille.autoAddWidget(btn)

        return grille

    # Label + conteneur formulaire scénario
    def partial_scenarios_form(self):
        self.form_scenario_frame = QFrame()
        vbox = QVBoxLayout()

        vbox.addWidget(QLabel("Paramètres du scénario"))

        self.form_scenario_container = QStackedLayout()
        vbox.addLayout(self.form_scenario_container)

        self.form_scenario_frame.setLayout(vbox)

        return self.form_scenario_frame

    # Moitié basse : log déroulement scénario
    def partial_result(self):
        group = QGroupBox("Résultat")

        self.console = ResultConsole()

        group.setLayout(self.console)

        return group

    def clicked_btn_ordinateur(self):
        sender = self.sender()
        # Empêche de décocher un bouton
        sender.setChecked(True)

        ordinateur = sender.ordinateur

        if (self.selected_scenario_btn):
            scenario = self.selected_scenario_btn.scenario
            self.run_scenario(scenario, ordinateur)

    def clicked_btn_scenario(self):
        if (self.selected_scenario_btn):
            self.selected_scenario_btn.setChecked(False)

        sender = self.sender()
        # Empêche de décocher un bouton
        sender.setChecked(True)

        self.selected_scenario_btn = sender

        # Initialisation du scénario
        scenario = sender.scenario

        if (scenario.form):
            self.form_scenario_frame.show()
            self.form_scenario_container.addWidget(scenario.form)
            self.form_scenario_container.setCurrentIndex(1)
        else:
            self.form_scenario_frame.hide()

    def clicked_btn_add_ordinateur(self):
        form = self.form_ordinateur
        ordinateur = form.to_ordinateur()
        services.book.add(ordinateur)

        btn = utils.OrdinateurButton(ordinateur)
        btn.clicked.connect(self.clicked_btn_ordinateur)

        self.grille_ordinateurs.autoAddWidget(btn)
        form.reset()

    def run_scenario(self, scenario, ordinateur):
        self.console.new_run(scenario, ordinateur)

        try:
            result = scenario.run(ordinateur)
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

    # Réinitialise (vide) les champs du formulaire
    def reset(self):
        self.edit_ip.setText("")
        self.edit_user.setText("")
        self.edit_name.setText("")

# Console de résultat. Elle affiche le détail du déroulement du scénario
# sous forme de lignes (similaire à un terminal)
# Chaque méthode new_* correspond à un type de ligne :
class ResultConsole(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.prompt = QVBoxLayout()
        self.addLayout(self.prompt)
        self.addStretch(1)

    # Début d'un scénario
    def new_run(self, scenario, ordinateur):
        self.prompt.addWidget(QLabel("Connexion à " + ordinateur.ssh_address))

    # Réalisation d'une nouvelle étape du scénario
    def new_step(self):
        self.prompt.addWidget(QLabel("Action effectuée"))

    # Affichage d'une erreur (texte rouge)
    def new_error(self, err):
        print(err)

        label = QLabel("Erreur")
        label.setStyleSheet("color: red")

        self.prompt.addWidget(label)

    # Fin du scénario, affichage du résultat s'il y en a un
    def end_run(self, result = None):
        if (result):
            self.prompt.addWidget(QLabel("Résultat : " + result))

        self.prompt.addWidget(QLabel("Scénario terminé"))
