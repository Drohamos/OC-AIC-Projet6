# AICToolbox - Documentation utilisateur

**Pour la documentation développeur, voir le fichier DEVELOPER.md**

## Prérequis
### Python
<u>Version recommandée : 3.7.3 (32 ou 64 bits)</u>

Le langage Python est disponible au téléchargement à l’adresse suivante : [https://www.python.org/downloads/](https://www.python.org/downloads/)

### PyQt5

Une fois le langage Python installé, il est possible de télécharger la librairie PyQt via le gestionnaire de paquets _pip_. Cela se fait avec la commande suivante :

> pip install PyQt5

### Fabric

<u>Version recommandée : 2.4</u>

La librairie Fabric s’installe avec la commande suivante :

> pip install Fabric==2.4

### Configuration des machines cibles

Pour des raisons de sécurité et de simplicité d'utilisation, les machines cibles doivent déjà être configurées pour autoriser l'authentification SSH par clé publique/privée.

Plus d'informations : https://doc.ubuntu-fr.org/ssh#authentification_par_un_systeme_de_cles_publiqueprivee

## Démarrage du logiciel

Ouvrir un terminal / invite de commande et utiliser la commande suivante :

> python {dossier contenant le logiciel}/main.py

Par exemple, si le logiciel est dans le dossier "C:/Users/Robin/Desktop/" :

> python C:/Users/Robin/Desktop/main.py

## Utilisation du logiciel

### Vue d’ensemble

Le logiciel se présente sous la forme d’une fenêtre, divisée en trois sections :

![](https://raw.githubusercontent.com/Drohamos/OC-AIC-Projet6/master/documentation/ensemble-avec-params.png)

 1. Sélection du scénario
Cette section offre un choix de scénarios, qui correspondent à un ensemble de commandes qui seront exécutées sur le poste cible.
Certains scénarios ont besoin que l’on saisisse des informations (par exemple pour créer une session : nom d’utilisateur et mot de passe). Ces informations devront être saisies dans un formulaire qui s’affichera en dessous de la liste des scénarios.
 2. Sélection du poste cible
 Cette section nous permet de choisir parmi une liste de cibles (ordinateur ou serveur) l’adresse de celle à laquelle nous souhaitons nous connecter.
 Il y a aussi possibilité d’utiliser un formulaire pour ajouter une cible, qui sera ensuite sauvegardée dans la liste.
 3. Affichage du résultat
La section résultat donne un retour d’informations sur le scénario en cours d’exécution (résultat, erreurs rencontrées, etc..)

## Ajout d'un client

Au premier démarrage du logiciel, la liste des postes clients sera vide. Pour en ajouter un, utiliser le formulaire en bas de la section « Sélectionner un poste » (encadré vert) :

![](https://raw.githubusercontent.com/Drohamos/OC-AIC-Projet6/master/documentation/cible-ajout.png)

Le formulaire demande trois informations :
- Adresse IP (**obligatoire**)
Adresse IP de la machine cible, par exemple : *192.168.1.10*
- Utilisateur (*facultatif*)
Nom d’utilisateur à utiliser sur la machine cible, par exemple : *toto*
Si ce champ est laissé vide, le logiciel utilisera par défaut l’utilisateur *sysadmin*
- Libellé (*facultatif*)
Nom permettant de se rappeler plus facilement de la machine, par exemple : *Serveur mail*

Une fois les informations complétées, cliquer sur « Ajouter ». Un nouveau bouton sera ajouté dans la liste.

NB : La liste est automatiquement enregistrée de façon à pouvoir être conservée après la fermeture du logiciel.

## Exécution d’un scénario simple

L’exécution d’un scénario simple se fait en deux étapes :

1 : Dans la section 1, cliquer sur le scénario à exécuter :

![](https://raw.githubusercontent.com/Drohamos/OC-AIC-Projet6/master/documentation/scenario-selection.png)

2 : Dans la section 2, cliquer sur le bouton correspondant au poste sur lequel le scénario devra s’exécuter, il devrait s’afficher en surbrillance :

![](https://raw.githubusercontent.com/Drohamos/OC-AIC-Projet6/master/documentation/cible-selection.png)

Le scénario sera immédiatement exécuté et son résultat sera visible dans la section 3 :

![](https://raw.githubusercontent.com/Drohamos/OC-AIC-Projet6/master/documentation/resultat-surligne.png)