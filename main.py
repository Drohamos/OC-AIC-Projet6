from fabric import Connection

# Cache les avertissements de dépréciation envoyés par les dépendances de la librairie Fabric
import warnings
import cryptography
warnings.simplefilter("ignore", cryptography.utils.CryptographyDeprecationWarning)

# Définit un ordinateur distant sur lequel on peut se connecter
class Ordinateur:
    def __init__(self):
        self.name = "VM LinuxLocal"
        self.ip   = "192.168.1.156"
        self.user = "linuxlocal"
    
    # Renvoie adresse ssh (user@ip)
    def _get_ssh_address(self):
        return self.user + "@" + self.ip

pc1 = Connection('linuxlocal@192.168.1.156')

result = pc1.run('hostname -s', hide=True)
print("Résultat : " + str(result.stdout))
print("Code retour : " + str(result.return_code))
print("Code erreur : " + str(result.stderr))

pc1.close()