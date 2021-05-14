# dataload.py

from sys import path
from unittest import TestCase
from collections import namedtuple

# Ajoute le chemin vers les sources
path.append('src')

from dataload import load_from_csv

class TestDataLoad(TestCase):
    """Test les fonctionnalités de la méthode dataload()."""

    def setUp(self):
        """Met en place l'environnement de test."""

        self.Point = namedtuple('Point', ['x', 'y'])
        
    def test_dataload(self):
        """Test le cas d'utilisation normal de dataload()."""

        # Créer le résultat attendu
        valid_points = list(map(
            lambda coords : self.Point(*coords),
            [[-1, 1], [-1, -1], [1, -1], [1, 1]]
        ))

        # Récupère les informations à partir du fichier
        points = load_from_csv('data/test/valid.csv')

        self.assertEqual(valid_points, points)

            
