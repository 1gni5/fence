# dataload.py

from csv import DictReader, QUOTE_NONNUMERIC
from collections import namedtuple

def load_from_csv(filename):
    """Créer une liste de point à partir du contenu d'un
    fichier csv."""

    with open(f'{filename}') as data_file:

        # Créer une structure de Point
        Point = namedtuple('Point', ['x', 'y'])

        reader = DictReader(data_file, quoting=QUOTE_NONNUMERIC)

        # Récupère les données
        points = []
        for row in reader:

            points.append(
                Point(row['x'], row['y'])
            )

    return points
        
