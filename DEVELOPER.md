
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
- **forms<i></i>.py**
- **scenarios<i></i>.py**

## Tests
