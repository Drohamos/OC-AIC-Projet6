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

test()
        
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
    
def line_with_placeholder(placeholder):
    line_edit = QLineEdit()
    line_edit.setPlaceholderText(placeholder)

    return line_edit
    
# Fenêtre prinicpale : sélection du/des ordinateurs
class Principale(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    
    def setUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(QLabel("Sélectionner un ordinateur :"))

        # Liste des ordinateurs
        grille = self.buttons_grid()
        vbox.addLayout(grille)

        vbox.addStretch(1)

        # Formulaire
        form_hbox = QHBoxLayout()
        
        edit_ip = line_with_placeholder("Adresse IP*")
        edit_user = line_with_placeholder("Utilisateur")
        edit_name = line_with_placeholder("Libellé")

        form_hbox.addWidget(edit_ip)
        form_hbox.addWidget(edit_user)
        form_hbox.addWidget(edit_name)

        vbox.addLayout(form_hbox)
        vbox.addWidget(QPushButton("Ajouter"))


        self.setLayout(vbox)
        self.setGeometry(300,300,500,250)
        self.setWindowTitle('Fenêtre principale')

        self.show()

    def ordinateur_clicked(self):
        print("Connexion à " + self.sender().text())

    def buttons_grid(self):
        grille=QGridLayout()

        it = GridIterator(2)

        for ordinateur in book.ordinateurs:
            btn = QPushButton(ordinateur.ip)
            btn.clicked.connect(self.ordinateur_clicked)
            grille.addWidget(btn, it.row(), it.col())

        return grille
    
book = OrdinateurBookmarker()
    
monApp=QApplication(sys.argv)
fenetre=Principale()
sys.exit(monApp.exec_())