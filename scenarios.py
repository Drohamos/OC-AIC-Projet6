from fabric import Connection

# Cache les avertissements de dépréciation envoyés par les dépendances de la librairie Fabric
import warnings
import cryptography
warnings.simplefilter("ignore", cryptography.utils.CryptographyDeprecationWarning)

class Scenario:
    def __init__(self, ordinateur):
        self.ordinateur = ordinateur
        self.setupConec()

    # Ce scénario n'a pas de formulaire, il renvoie donc False
    @property
    def form(self):
        return None

    # Préparation de la connexion (création instance)
    def setupConec(self):
        print("Préparation connexion à " + self.ordinateur.ssh_address)
        self.conec = Connection(self.ordinateur.ssh_address, connect_timeout=5)

    def run(self):
        return self.execute()

    def execute(self):
        raise NotImplementedError("La méthode execute() de ce scénario n'a pas été implémentée")

    def close(self):
        print("Fermeture de la connexion avec " + self.ordinateur.ssh_address)
        self.conec.close()

class GetHostnameScenario(Scenario):
    def execute(self):
        result = self.conec.run('hostname -s', hide=True)
        # Erreurs possibles :
        #   TimeoutError
        #   UnexpectedExit (commande invalide ?)

        self.close()

        return result