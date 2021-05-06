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
        
    def test_polygon_area(self):
        '''Test le fonctionnement normal de la propriété area().'''

        # Créer une liste de points
        vertices = list(map(
            lambda coords : self.Vertex(*coords),
            [[-1, 1], [-1, -1], [1, -1], [1, 1]]
        ))

        # Vérifie que la valeur match le jeux de test
        self.assertEqual(Polygon(vertices).area, 4)

    def test_polygon_gravity(self):
        '''Test le fonctionnement normal de la propriété gravity().'''

        # Créer une liste de points
        vertices = list(map(
            lambda coords : self.Vertex(*coords),
            [[-1, 1], [-1, -1], [1, -1], [1, 1]]
        ))

        # Vérifie que la valeur match le jeux de test
        self.assertEqual(Polygon(vertices).gravity, self.Vertex(0, 0))

    def test_polygon_contains(self):
        '''Test le fonctionnement de la methode __contains__() avec
        un point.'''

        # Créer une liste de points
        vertices = list(map(
            lambda coords : self.Vertex(*coords),
            [[-1, 1], [-1, -1], [1, -1], [1, 1]]
        ))

        polygon = Polygon(vertices)

        # Vérifie que les données correspondent au jeux de test
        self.assertTrue(polygon.gravity in polygon)

    def test_polygon_segments(self):
        '''Test le fonctionnement de la propriété segments().'''

        # Créer une liste de points
        vertices = list(map(
            lambda coords : self.Vertex(*coords),
            [[-1, 1], [-1, -1], [1, -1], [1, 1]]
        ))

        # Créer le polygon de test
        polygon = Polygon(vertices)

        # Créer une deuxième liste de point 'décalés': 
        #  [A, B, C] => [B, C, A]
        neighbors = polygon.vertices[1:] + polygon.vertices[:1]

        for a,b,s in zip(polygon.vertices, neighbors, polygon.segments):
            self.assertEqual((a,b), s)

        
