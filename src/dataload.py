# dataload.py

from csv import DictReader
from collections import namedtuple

def dataload(filename, struct_name):
    """Importe les données contenues dans un fichier csv
    sous forme de namedtuple."""

    with open(f'data/{filename}.csv') as data_file:

        reader = DictReader(data_file)

        # Créer la structure à partir de l'entête du fichier
        Struct = namedtuple(struct_name, reader.fieldnames)

        # Traduit les données du fichier
        structs = []
        for row in reader:

            structs.append(
                Struct(*row.values())
            )
            
    return structs
