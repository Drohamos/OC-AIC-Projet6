# AICToolbox
# Auteur : Robin BARKAS

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel
import models
import services
import utils

# Fenêtre principale : sélection du/des ordinateurs
class Principale(QWidget):
    def __init__(self):
        super().__init__()
        self.form = FormOrdinateur()
        self.setUI()
    
    def setUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(QLabel("Sélectionner un ordinateur :"))

        # Liste des ordinateurs
        self.grille = self.buttons_grid()
        vbox.addLayout(self.grille)

        vbox.addStretch(1)
        
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
        print("Connexion à " + self.sender().ordinateur.ssh_address)

    # Crée une boucle de boutons à partir de la liste des ordinateurs
    def buttons_grid(self):
        grille=AutoGridLayout()

        for ordinateur in services.book.ordinateurs:
            btn = OrdinateurButton(ordinateur)
            btn.clicked.connect(self.ordinateur_clicked)
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
