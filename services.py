# AICToolbox
# Auteur : Robin BARKAS

import models
import pickle

class OrdinateurBookmarker:
    FILE_PATH = "bookmarks.cfg"

    def __init__(self):
        self.load()

    def load(self):
        self.ordinateurs = self.load_from_file()

    def load_from_file(self):
        ordinateurs = []

        try:
            # Ouverture du fichier en lecture
            file = open(self.FILE_PATH, "rb")
        # Il est normal que le fichier n'existe pas au premier lancement du logiciel,
        # on ignore donc l'exception "fichier non trouvé"
        except FileNotFoundError:
            pass
        else:
            try:
                ordinateurs = pickle.load(file)
            except EOFError:
                pass
            finally:
                file.close()

        return ordinateurs

    # Données fictives
    def load_from_mocks(self):
        return [
            # VM Linuxlocal
            models.Ordinateur("192.168.1.156", "linuxlocal"),
            # VM Linuxlocal
            models.Ordinateur("192.168.1.157", "linuxlocal"),
            # IP valide, non joignable (Timeout)
            models.Ordinateur("1.2.3.4"),
            # IP invalide
            models.Ordinateur("192.168.1.300", name="Test"),
            # IP invalide
            models.Ordinateur("192.168.1.400"),
            # IP invalide
            models.Ordinateur("192.168.1.500"),
        ]

    # Ajoute un ordinateur à la liste + dans le fichier de config
    def add(self, ordinateur):
        self.ordinateurs.append(ordinateur)
        self.save(self.ordinateurs)

    # Méthode générique pour persister la liste des ordinateurs
    def save(self, ordinateurs):
        self.save_to_file(ordinateurs)

    def save_to_file(self, ordinateurs):
        file = open(self.FILE_PATH, "wb")
        pickle.dump(ordinateurs, file)

# =====================
# Instances de services
# Permet de partager une même instance entre les modules qui importent les services
# Exemple : services.book
# =====================

book = OrdinateurBookmarker()