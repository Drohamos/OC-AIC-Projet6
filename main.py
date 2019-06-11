from fabric import Connection

# Cache les avertissements de dépréciation envoyés par les dépendances de la librairie Fabric
import warnings
import cryptography
warnings.simplefilter("ignore", cryptography.utils.CryptographyDeprecationWarning)

class OrdinateurBookmarker:
    def __init__(self):
        self.load()

    # @todo implémenter récupération dans fichier
    def load(self):
        self.ordinateurs = [
            Ordinateur("192.168.1.156", "linuxlocal"),
            Ordinateur("192.168.1.157", "linuxlocal"),
            Ordinateur("192.168.1.300", name="Test"),
            Ordinateur("192.168.1.400"),
            Ordinateur("192.168.1.500"),
        ]

    def add(self, ordinateur):
        self.ordinateurs.append(ordinateur)

    # @todo implémenter sauvegarde dans fichier
    def save(self):
        print("Lise des ordinateurs sauvegardée")

# Définit un ordinateur distant sur lequel on peut se connecter
class Ordinateur:
    def __init__(self, ip, user="sysadmin", name=None):
        self.ip   = ip
        self.user = user
        self.name = name

    @property
    def ssh_address(self):
        return self.user + "@" + self.ip

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, ip):
        if not (isinstance(ip, str)):
            raise Exception("ip doit être une chaîne de caractères")

        # Suppression des espaces inutiles
        ip = ip.strip()

        if not (ip):
            raise Exception("ip ne peut pas être vide")

        self.__ip = ip

def test():
    book = OrdinateurBookmarker()

    for pc in book.ordinateurs:
        print (pc.ip)

        co1 = Connection(pc.ssh_address)

        result = co1.run('hostname -s', hide=True)
        print("Résultat : " + str(result.stdout))
        print("Code retour : " + str(result.return_code))
        print("Code erreur : " + str(result.stderr))

        co1.close()
        
class GridIterator:
    currentRow = 1
    currentCol = 1

    def __init__(self, numCols):
        self.numCols = numCols

    def row(self):
        return self.currentRow

    def col(self):
        previousCol = self.currentCol

        self.currentCol += 1
        if (self.currentCol > self.numCols):
            self.currentRow += 1
            self.currentCol = 1

        return previousCol

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel

monApp=QApplication(sys.argv)

def line_with_placeholder(placeholder):
    line_edit = QLineEdit()
    line_edit.setPlaceholderText(placeholder)

    return line_edit
    
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
        grille = self.buttons_grid()
        vbox.addLayout(grille)

        vbox.addStretch(1)
        
        vbox.addWidget(self.form)

        add_ordinateur = QPushButton("Ajouter")
        add_ordinateur.clicked.connect(self.add_ordinateur_clicked)
        vbox.addWidget(add_ordinateur)

        self.setLayout(vbox)
        self.setGeometry(300,300,500,250)
        self.setWindowTitle('Fenêtre principale')

        self.show()

    def add_ordinateur_clicked(self):
        print("Ajout ordinateur")
        print(self.form.to_ordinateur())

    def ordinateur_clicked(self):
        print("Connexion à " + self.sender().ordinateur.ssh_address)

    # Crée une boucle de boutons à partir de la liste des ordinateurs
    def buttons_grid(self):
        grille=QGridLayout()
        
        it = GridIterator(2)

        for ordinateur in book.ordinateurs:
            btn = OrdinateurButton(ordinateur)
            btn.clicked.connect(self.ordinateur_clicked)
            grille.addWidget(btn, it.row(), it.col())

        return grille

# Bouton de connexion à un ordinateur
class OrdinateurButton(QPushButton):
    def __init__(self, ordinateur):
        # Le label sera l'adresse ip de l'ordinateur
        super().__init__(ordinateur.ip)
        # On stocke une copie complète de l'objet ordinateur 
        self.ordinateur = ordinateur

class FormOrdinateur(QWidget):
    edit_ip = line_with_placeholder("Adresse IP*")
    edit_user = line_with_placeholder("Utilisateur")
    edit_name = line_with_placeholder("Libellé")

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
        ordinateur = Ordinateur(self.edit_ip.text(), self.edit_user.text(), self.edit_name.text())

        return ordinateur

    # Modifie l'état du formulaire pour correspondre à un objet ordinateur donné
    def fill_from_ordinateur(self, ordinateur):
        self.edit_ip.setText(ordinateur.ip)
        self.edit_user.setText(ordinateur.user)
        self.edit_name.setText(ordinateur.name)

book = OrdinateurBookmarker()
    
fenetre=Principale()
sys.exit(monApp.exec_())