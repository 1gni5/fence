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

    def test_polygon_all(self):
        """Vérifie que toutes les méthodes public fonctionne avec toute les
        valeurs du jeu de test.  
        """

        TestSet = namedtuple('TestSet', ['vertices', 'area', 'gravity', 'cow'])

        # Jeu de test
        test_sets = [
            TestSet(
                vertices = [[-1, 1], [-1, -1], [1, -1], [1, 1]],
                area = 4,
                gravity = self.Vertex(0, 0),
                cow = True,
            ),
            TestSet(
                vertices =  [
                    [-16.6, -20.1], [-12.6, -18.6],
                    [-11.6, -16.6], [-15.1, -15.1]
                ],
                area = 13.125,
                gravity = self.Vertex(-14.226, -17.555),
                cow = True,
            ),
            TestSet(
                vertices = [
                    [-1.1, -1.5], [2.1, 3.012],
                    [5.6, -1.21], [1.97, 4.07]
                ],
                area = 3.563,
                gravity = self.Vertex(1.978, 1.903),
                cow = False,
            ),
        ]

        # Test pour chaque jeu de données
        for test_set in test_sets:
            
            # Créer une liste de points
            vertices = list(map(
                lambda coords : self.Vertex(*coords),
                test_set.vertices,
            ))

            # Créer le polygon de test
            polygon = Polygon(vertices)

            # Comparaison des aires
            self.assertAlmostEqual(
                polygon.area,
                test_set.area,
                3,
            )

            # Comparaison des centres de gravité
            self.assertAlmostEqual(
                polygon.gravity.x,
                test_set.gravity.x,
                2,
            )
                        # Comparaison des centres de gravité
            self.assertAlmostEqual(
                polygon.gravity.y,
                test_set.gravity.y,
                2,
            )

            # Comparaison des positions de la vache
            self.assertEqual(
                polygon.gravity in polygon,
                test_set.cow
            )
        
