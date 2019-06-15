import unittest
import models

# https://realpython.com/python-testing/#unit-tests-vs-integration-tests

# Ces tests permettent de s'assurer que l'instanciation d'un ordinateur renvoie
# le résultat attendu, et que les valeurs par défaut sont bien appliquées quand nécessaire
class TestOrdinateurInstanciation(unittest.TestCase):
    def test_without_params(self):
        with self.assertRaises(Exception):
            ordinateur = models.Ordinateur()
    
    def test_with_empty_ip(self):
        with self.assertRaises(Exception):
            ordinateur = models.Ordinateur("")
        with self.assertRaises(Exception):
            ordinateur = models.Ordinateur("   ")

    # Adresse ip doit être string
    def test_with_invalid_type_ip(self):
        with self.assertRaises(Exception):
            ordinateur = models.Ordinateur(123456)
        with self.assertRaises(Exception):
            ordinateur = models.Ordinateur([])
        with self.assertRaises(Exception):
            ordinateur = models.Ordinateur(10.20)

    # On entre seulement l'adresse IP, devrait réussir
    def test_with_only_ip(self):
        ordinateur = models.Ordinateur("1.2.3.4")

    # L'adresse ip est bien nettoyée
    def test_ip_is_stripped(self):
        expected_ip = "1.2.3.4"
        self.assertEqual(expected_ip, models.Ordinateur("1.2.3.4").ip)
        self.assertEqual(expected_ip, models.Ordinateur(" 1.2.3.4").ip)
        self.assertEqual(expected_ip, models.Ordinateur("1.2.3.4 ").ip)

    # Les paramètres vides devraient être remplis par leur valeur par défaut
    def test_missing_params_replaced_by_defaults(self):
        ordinateur = models.Ordinateur("1.2.3.4")
        self.assertEqual("sysadmin", ordinateur.user)
        self.assertEqual(None,       ordinateur.name)


    # On entre une adresse ip valide, suivie de paramètres vides
    # Les paramètres vides devraient être remplis par leur valeur par défaut
    def test_empty_params_replaced_by_defaults(self):
        ordinateur = models.Ordinateur("1.2.3.4", "", "")
        self.assertEqual("sysadmin", ordinateur.user)