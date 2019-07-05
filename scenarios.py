# AICToolbox
# Auteur : Robin BARKAS

from fabric import Connection
from invoke import Responder

# Cache les avertissements de dépréciation envoyés par les dépendances de la librairie Fabric
import warnings
import cryptography
warnings.simplefilter("ignore", cryptography.utils.CryptographyDeprecationWarning)

import forms

# Classe scenario générique, ne devrait pas être utilisée directement
class Scenario:
    def __init__(self):
        pass

    # Formulaire du scénario
    # Par défaut, renvoie None (pas de formulaire)
    # Sinon, renvoie le widget Qt correspondant
    @property
    def form(self):
        return None

    # Préparation de la connexion (création instance)
    def setup_conec(self):
        print("Préparation connexion à " + self.ordinateur.ssh_address)
        self.conec = Connection(self.ordinateur.ssh_address, connect_timeout=2)

    def run(self, ordinateur):
        self.ordinateur = ordinateur
        self.setup_conec()
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

class ScenarioWithParams(Scenario):
    @property
    def form(self):
        raise NotImplementedError("La méthode form() de ce scénario n'a pas été implémentée")

class GetHostnameScenario(Scenario):
    label = "Récupérer hostname"

    def execute(self):
        result = self.conec.run('hostname -s', hide=True)

        self.close()

        return result

class GetInterfaceDetailsScenario(ScenarioWithParams):
    label = "Afficher détails interface réseau"
    form  = forms.FormScenario(["Interface réseau"])

    def execute(self):
        interface = self.form.fields[0].text()

        result = self.conec.run('ip addr show ' + interface, hide=True)

        self.close()

        return result

class CreateSessionScenario(ScenarioWithParams):
    label = "Créer une session"
    form  = forms.FormScenario(["Nom d'utilisateur", "Mot de passe", "Mot de passe root"])

    def execute(self):
        username = self.form.fields[0].text()
        new_password = self.form.fields[1].text() + '\n'
        root = self.form.fields[2].text() + '\n'

        sudopass = Responder(pattern=r'\[sudo\] password', response=root)
        new_user_pass = Responder(pattern=r'UNIX password', response=new_password)
        
        # Réinitialisation champ root
        self.form.fields[2].setText("")

        self.conec.run('sudo useradd ' + username, pty=True, watchers=[sudopass])
        result = self.conec.run('sudo passwd ' + username, pty=True, watchers=[sudopass, new_user_pass])


        self.close()

        return result

# Liste des classes correspondant à un scénario, utilisée pour générer les boutons
# Exemple d'instanciation à partir de cette liste : scenarios.GetHostnameScenario()
scenarios = [
    GetHostnameScenario,
    GetInterfaceDetailsScenario,
    CreateSessionScenario
]