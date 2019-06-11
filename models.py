# AICToolbox
# Auteur : Robin BARKAS

# Définit un ordinateur distant sur lequel on peut se connecter
class Ordinateur:
    def __init__(self, ip, user="sysadmin", name=None):
        self.ip   = ip
        self.user = user
        self.name = name

    @property
    def ssh_address(self):
        return self.user + "@" + self.ip

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, ip):
        if not (isinstance(ip, str)):
            raise Exception("ip doit être une chaîne de caractères")

        # Suppression des espaces inutiles
        ip = ip.strip()

        if not (ip):
            raise Exception("ip ne peut pas être vide")

        self.__ip = ip