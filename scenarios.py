from fabric import Connection

# Cache les avertissements de dépréciation envoyés par les dépendances de la librairie Fabric
import warnings
import cryptography
warnings.simplefilter("ignore", cryptography.utils.CryptographyDeprecationWarning)

class Scenario:
    def __init__(self, ordinateur):
        self.ordinateur = ordinateur
        self.setup_conec()

    # Formulaire du scénario
    # Par défaut, renvoie None (pas de formulaire)
    # Sinon, renvoie le widget Qt correspondant
    @property
    def form(self):
        return None

    # Préparation de la connexion (création instance)
    def setup_conec(self):
        print("Préparation connexion à " + self.ordinateur.ssh_address)
        self.conec = Connection(self.ordinateur.ssh_address, connect_timeout=5)

    def run(self):
        return self.execute()
        # @todo Nettoyage (fermeture connexion) automatique après exécution
        # actuellement implémenté manuellement dans chaque scénario

    def execute(self):
        raise NotImplementedError("La méthode execute() de ce scénario n'a pas été implémentée")
        # Erreurs possibles :
        #   TimeoutError
        #   UnexpectedExit (commande invalide ?)

    def close(self):
        print("Fermeture de la connexion avec " + self.ordinateur.ssh_address)
        self.conec.close()

class GetHostnameScenario(Scenario):
    label = "Récupérer hostname"

    def execute(self):
        result = self.conec.run('hostname -s', hide=True)

        self.close()

        return result

class GetInterfaceDetailsScenario(Scenario):
    label = "Afficher détails interface réseau"

    @property
    def interface(self):
        return "ens33"

    def execute(self):
        interface = self.interface

        result = self.conec.run('ip addr show ' + interface, hide=True)

        self.close()

        return result

# Liste des classes correspondant à un scénario
# Exemple d'instanciation à partir de cette liste : scenarios.GetHostnameScenario()
scenarios = [
    GetHostnameScenario,
    GetInterfaceDetailsScenario
]