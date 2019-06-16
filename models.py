# AICToolbox
# Auteur : Robin BARKAS

# Définit un ordinateur distant sur lequel on peut se connecter
class Ordinateur:
    DEFAULT_USER = "sysadmin"
    DEFAULT_NAME = ""

    def __init__(self, ip, user=DEFAULT_USER, name=DEFAULT_NAME):
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
        if not (check_is_str(ip)):
            raise TypeError("ip doit être une chaîne de caractères")

        # Suppression des espaces inutiles
        ip = ip.strip()

        if (check_is_empty(ip)): raise ValueError("ip ne peut pas être vide")

        self.__ip = ip

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        user = user.strip()
        self.__user = default_if_empty(user, self.DEFAULT_USER)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        name = name.strip()
        self.__name = default_if_empty(name, self.DEFAULT_NAME)

def check_is_str(var):
    return (isinstance(var, str))

# Si chaine de caractères vide, on renvoie sa valeur par défaut
def default_if_empty(str_, default):
    if (check_is_empty(str_)):
        return default
    return str_

def check_not_empty(str_):
    if (check_is_empty(str_)): return False
    else: return True

def check_is_empty(str_, strict = True):
    return (str_ == "")