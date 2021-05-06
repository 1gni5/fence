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

    def test_polygon_init_with_less_than_3_vertices(self):
        '''Essaye de créer un polygon avec moins de 3 sommets.'''

        # Créer une liste de points
        vertices = list(map(
            lambda coords : self.Vertex(*coords),
            [[-1, 1], [-1, -1], [1, -1], [1, 1]]
        ))
        
        # Un polygône doit avoir au moins 3 sommet
        with self.assertRaises(ValueError):
            Polygon([])
            
        with self.assertRaises(ValueError):
            Polygon(vertices[:1])

        with self.assertRaises(ValueError):
            Polygon(vertices[:2])
        
    def test_polygon_area_with_normal_values(self):
        '''Test le fonctionnement normal de la propriété area().'''

        # Créer une liste de points
        vertices = list(map(
            lambda coords : self.Vertex(*coords),
            [[-1, 1], [-1, -1], [1, -1], [1, 1]]
        ))

        # Vérifie que la valeur match le jeux de test
        self.assertEqual(Polygon(vertices).area, 4)

    def test_polygon_gravity_with_normal_values(self):
        '''Test le fonctionnement normal de la propriété gravity().'''

        # Créer une liste de points
        vertices = list(map(
            lambda coords : self.Vertex(*coords),
            [[-1, 1], [-1, -1], [1, -1], [1, 1]]
        ))

        # Vérifie que la valeur match le jeux de test
        self.assertEqual(Polygon(vertices).gravity, self.Vertex(0, 0))
