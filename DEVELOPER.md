
  
# AICToolbox - Documentation développeur

## Prérequis

- Python (3.7+)
- Librairies pip :
  - PyQt5
  - Fabric (2.4+)

## Arborescence
- **main<i></i>.py**
Fichier d'entrée de l'application. Sert à effectuer les actions suivantes :
  - Initialiser l'application Qt
  - Charger les services
  - Afficher la fenêtre principale du programme
- **models<i></i>.py**
Contient le *modèle* d'un ordinateur, c'est à dire une classe qui définit ce qu'est un objet *Ordinateur*, les différents attributs qu'il possède ainsi que sa fonction d'initialisation (\_\_init\_\_).
- **utils<i></i>.py**
Ensemble de fonctions (ou même de classes) d'utilité générale. Dans notre cas, il s'agit principalement d'éléments d'interface qui sont réutilisés plusieurs fois dans l'application.
- **services<i></i>.py**
Les services sont des classes qui ont la particularité de n'avoir qu'une seule instance, qui peut être utilisée à plusieurs endroits de l'application.
Par exemple, on voit qu'une instance de la classe _OrdinateurBookmarker_ est créée dans le contexte global du fichier service :
`book = OrdinateurBookmarker()`
Cette instance devient dès alors accessible dans n'importe quel fichier ou le module (fichier) services est importé.
Par exemple :

      import services
      print(services.book.ordinateurs)

- **views<i></i>.py**
Contient toutes les classes qui définissent l'interface de l'application. Elles héritent des classes de la librairie Qt (QWidget, QHBoxLayout, etc...) et les combinent pour créer et mettre en forme les éléments présentés à l'écran.
- **forms<i></i>.py**
Les formulaires sont aussi des classes héritées de Qt, avec pour particularité d'avoir des valeurs associées.
- **scenarios<i></i>.py**
Les scénarios sont des ensemble de commandes qui peuvent être exécutées sur un ordinateur. Ce fichier contient la classe mère qui définit le comportement général d'un scénario. Chaque scénario hérite de celle-ci et y ajoute ses particularités.
A la fin du fichier, une liste de tous les scénarios est créée. Celle-ci est par exemple utilisée dans les vues, ou elle permet d'afficher les boutons cliquables correspondant aux différents scénarios.

## Tests

Les tests sont stockés dans le fichier *test_models.py*.

Il contient déjà une série de tests portant sur l'ajout d'un ordinateur à la liste des postes cibles sur lesquels il est possible de se connecter. Ces tests vérifient l’efficacité des fonctions de validation du formulaire et de nettoyage des données saisies. Par exemple :

- Formulaire vide
- Formulaire incomplet
- Type de donnée incorrect

### Exécution des tests
Pour lancer les tests, ouvrir un terminal et entrer la commande suivante :

    python -m unittest

L'ensemble des tests sera automatiquement exécuté. Si un ou plusieurs tests échouent, un rapport détaillé permet d'analyser l'origine du problème.

## Voies d'amélioration
- Permettre d’exécuter un scénario sur plusieurs ordinateurs
- Automatiser la création de clé SSH

## Diagrammes de séquence

Les diagrammes ci-dessous représentent de façon détaillée le fonctionnement des étapes-clé du logiciel :

### Initialisation

![](https://raw.githubusercontent.com/Drohamos/OC-AIC-Projet6/master/documentation/uml_initialisation.png)

### Exécution d'un scénario

![](https://raw.githubusercontent.com/Drohamos/OC-AIC-Projet6/master/documentation/uml_scenario.png)