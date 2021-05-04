# polygon.py

class Polygon():
    '''Représente un polygône en 2 dimensions'''

    def __init__(self, vertices):
        '''Créer un polygône à partir d'une liste de namedtuple.'''

        self.vertices = vertices

    @property
    def area(self):
        '''Calcule l'air du polygône.'''

        # Les figures à moins de 3 points n'ont pas d'air
        if len(self.vertices) < 3:
            return 0

        # Créer une deuxième liste de point 'décalés': 
        #  [A, B, C] => [B, C, A]
        neighbors = self.vertices[1:] + self.vertices[:1]

        # L'utilisation de liste et des built-in est plus rapide
        segments = []
        for a,b in zip(self.vertices, neighbors):
            segments.append(a.x * b.y - b.x * a.y)

        return sum(segments) / 2
