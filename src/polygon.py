# polygon.py

from collections import namedtuple
from math import acos, pi
from numpy import array, dot
from numpy.linalg import norm


class Polygon():
    """Représente un polygône en 2 dimensions."""

    def __init__(self, vertices):
        """Créer un polygône à partir d'une liste de sommets.

        Arguments:
        vertices => Liste de sommets (Doit contenir plus de 3 éléments)
        """

        # Vérifie que le polygône contient au moins trois sommets
        if len(vertices) < 3:
            raise ValueError('A polygon must have at least 3 vertices')

        self.vertices = vertices

    @property
    def segments(self):
        """Retourne les segments du polyône sous forme de pair (début,fin)."""

        # Créer une deuxième liste de point 'décalés':
        #  [A, B, C] => [B, C, A]
        neighbors = self.vertices[1:] + self.vertices[:1]

        segments = [
            (start, end) for start, end in zip(self.vertices, neighbors)
        ]

        return segments

    @property
    def area(self):
        """Retourne l'air du polygône."""

        # L'utilisation de liste et des built-in est plus rapide
        segments = []
        for a, b in self.segments:
            segments.append(a.x * b.y - b.x * a.y)

        return sum(segments) / 2

    @property
    def gravity(self):
        """Retourne le centre de gravité du polygône."""

        # L'utilisation des listes et des built-in est plus rapide
        x, y = [], []
        for a, b in self.segments:
            z = a.x * b.y - b.x * a.y
            x.append((a.x + b.x) * z)
            y.append((a.y + b.y) * z)

        x = sum(x) / (6 * self.area)
        y = sum(y) / (6 * self.area)

        return namedtuple('Gravity', ['x', 'y'])(x, y)

    def __contains__(self, point):
        """Retourne si un point est dans le polygône ou non.

        Arguments:
        point => Point dont l'appartenance est à vérifier.
        """

        # L'utilisation de liste et des built-in est plus rapide
        angles = []
        for a, b in self.segments:

            # Créer les vecteurs
            pa = array([a.x - point.x, a.y - point.y])
            pb = array([b.x - point.x, b.y - point.y])

            # Récupère le signe du déterminant
            sign_det = -1 if (a.x * b.y - a.y * b.x) < 0 else 1

            # Calcul de theta
            angles.append(sign_det * acos(dot(pa, pb) / (norm(pa) * norm(pb))))

        return sum(angles) != 0
