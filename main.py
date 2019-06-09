from fabric import Connection

import warnings
import cryptography
warnings.simplefilter("ignore", cryptography.utils.CryptographyDeprecationWarning)

pc1 = Connection('linuxlocal@192.168.1.156')

result = pc1.run('hostname -s', hide=True)
print("Résultat : " + str(result.stdout))
print("Code retour : " + str(result.return_code))
print("Code erreur : " + str(result.stderr))