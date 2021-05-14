# cli.py

from sys import argv

from polygon import Polygon
from dataload import load_from_csv

def main():

    # Pour chaque fichier passé en paramètre
    for filename in argv[1:]:

        # Si l'utilisateur fourni plusieurs fichiers sources
        if len(argv[1:]) > 1:
            print(f'{filename}', end=": ")

        # Créer l'enclos et la vache
        pen = Polygon(load_from_csv(filename))
        cow = pen.gravity

        # Affiche la réponse
        answer = 'intérieur' if cow in pen else 'extérieur'
        print(f"La vache est à l'{answer} de l'enclos.")

    # L'utilisateur n'a pas fourni de fichier
    if len(argv) <= 1:
        print(f'{argv[0]}: missing operand. Usage: {argv[0]} filename [filename2, ..., filenameN]')

if __name__ == '__main__':
    main()
