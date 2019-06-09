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
            Ordinateur(),
            Ordinateur(),
        ]

    # @todo implémenter sauvegarde dans fichier
    def save(self):
        print("Lise des ordinateurs sauvegardée")

# Définit un ordinateur distant sur lequel on peut se connecter
class Ordinateur:
    def __init__(self):
        self.name = "VM LinuxLocal"
        self.ip   = "192.168.1.156"
        self.user = "linuxlocal"
    
    @property
    def ssh_address(self):
        return self.user + "@" + self.ip

pc1 = Ordinateur()
co1 = Connection(pc1.ssh_address)

result = co1.run('hostname -s', hide=True)
print("Résultat : " + str(result.stdout))
print("Code retour : " + str(result.return_code))
print("Code erreur : " + str(result.stderr))

co1.close()