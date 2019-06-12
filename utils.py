# AICToolbox
# Auteur : Robin BARKAS

from fabric import Connection

# Permet de générer l'incrémentation du numéro de ligne/colonne
# Utilisé pour générer une grille automatiquement à partir d'une liste
class GridIterator:
    currentRow = 1
    currentCol = 1

    def __init__(self, numCols):
        self.numCols = numCols

    # Quand le nombre de colonne dépasse le maximum défini,
    # on incrémente la ligne et on réinitialise la colonne
    def incrementCol(self):
        if (self.currentCol == self.numCols):
            self.currentRow += 1
            self.currentCol = 1
        else: 
            self.currentCol += 1

    def row(self):
        return self.currentRow
    
    def col(self):
        col = self.currentCol

        self.incrementCol()

        return col

def test(ordinateur):
        co1 = Connection(ordinateur.ssh_address)

        result = co1.run('hostname -s', hide=True)
        print("Résultat : " + str(result.stdout))
        print("Code retour : " + str(result.return_code))
        print("Code erreur : " + str(result.stderr))

        co1.close()