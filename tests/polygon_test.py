# polygon_test.py

from sys import path
from unittest import TestCase
from collections import namedtuple

# Ajoute le chemin vers les sources
path.append('src')

from polygon import Polygon

class TestPolygon(TestCase):
    '''Test les fonctionnalité de la classe Polygon.'''

    def setUp(self):
        '''Set-up l'environnement de test.'''

        self.Vertex = namedtuple('Vertex', ['x', 'y'])

    def test_polygon_area_with_normal_values(self):
        '''Test le fonctionnement normal de la propriété area().'''

        # Créer une liste de points
        vertices = list(map(
            lambda coords : self.Vertex(*coords),
            [[-1, 1], [-1, -1], [1, -1], [1, 1]]
        ))

        # Vérifie que la valeur match le jeux de test
        self.assertEqual(Polygon(vertices).area, 4)

    def test_polygon_area_with_no_values(self):
        '''Test le fonctionnement de la propriété area() avec un Polygon
        vide.'''

        # Une figure sans sommets n'a pas d'air
        self.assertEqual(Polygon([]).area, 0)

    def test_polygon_gravity_with_normal_values(self):
        '''Test le fonctionnement normal de la propriété gravity().'''

        # Créer une liste de points
        vertices = list(map(
            lambda coords : self.Vertex(*coords),
            [[-1, 1], [-1, -1], [1, -1], [1, 1]]
        ))

        # Vérifie que la valeur match le jeux de test
        self.assertEqual(Polygon(vertices).gravity, self.Vertex(0, 0))
