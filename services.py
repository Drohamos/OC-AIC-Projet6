# AICToolbox
# Auteur : Robin BARKAS

import models

class OrdinateurBookmarker:
    def __init__(self):
        self.load()

    # @todo implémenter récupération dans fichier
    def load(self):
        self.loadMocks()

    def loadMocks(self):
        self.ordinateurs = [
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

    def add(self, ordinateur):
        self.ordinateurs.append(ordinateur)

    # @todo implémenter sauvegarde dans fichier
    def save(self):
        print("Lise des ordinateurs sauvegardée")

# =====================
# Instances de services
# Permet de partager une même instance entre les modules qui importent les services
# Exemple : services.book
# =====================

book = OrdinateurBookmarker()