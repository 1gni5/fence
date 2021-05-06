# polygon.py

from collections import namedtuple

class Polygon():
    '''Représente un polygône en 2 dimensions'''

    def __init__(self, vertices):
        '''Créer un polygône à partir d'une liste de namedtuple.'''

        # Vérifie que le polygône contient au moins un sommet
        if len(vertices) >= 3:
            self.vertices = vertices
        else:
            raise ValueError('A polygon must have at least 3 vertices')

    @property
    def area(self):
        '''Calcule l'air du polygône.'''

        # Créer une deuxième liste de point 'décalés': 
        #  [A, B, C] => [B, C, A]
        neighbors = self.vertices[1:] + self.vertices[:1]

        # L'utilisation de liste et des built-in est plus rapide
        segments = []
        for a,b in zip(self.vertices, neighbors):
            segments.append(a.x * b.y - b.x * a.y)

        return sum(segments) / 2

    @property
    def gravity(self):
        '''Retourne le centre de gravité du polygon sous 
        forme de namedtuple.'''

        # Créer une deuxième liste de point 'décalés': 
        #  [A, B, C] => [B, C, A]
        neighbors = self.vertices[1:] + self.vertices[:1]

        # L'utilisation des listes et des built-in est plus rapide
        x,y = [],[]
        for a,b in zip(self.vertices, neighbors):
            z = a.x * b.y - b.x * a.y
            x.append( (a.x + b.x) * z )
            y.append( (a.y + b.y) * z )

        x = sum(x) / (6 * self.area)
        y = sum(y) / (6 * self.area)

        return namedtuple('Gravity', ['x', 'y'])(x,y)
            
