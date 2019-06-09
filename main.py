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


import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout, QVBoxLayout
    
# Fenêtre prinicpale : sélection du/des ordinateurs
class Principale(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    
    def setUI(self):
        grille = self.buttons_grid()

        vbox = QVBoxLayout()
        vbox.addLayout(grille)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setGeometry(300,300,500,250)
        self.setWindowTitle('Fenêtre principale')

        self.show()

    def buttons_grid(self):
        grille=QGridLayout()

        btn1=QPushButton("Bouton1")
        btn2=QPushButton("Bouton2")
        btn3=QPushButton("Bouton3")
        btn4=QPushButton("Bouton4")
        btn5=QPushButton("Bouton5")
        btn6=QPushButton("Bouton6")
        
        grille.addWidget(btn1, 1,1)
        grille.addWidget(btn2, 1,2)
        grille.addWidget(btn3, 2,1)
        grille.addWidget(btn4, 2,2)
        grille.addWidget(btn5, 3,1)
        grille.addWidget(btn6, 3,2)

        return grille
    
monApp=QApplication(sys.argv)
fenetre=Principale()
sys.exit(monApp.exec_())