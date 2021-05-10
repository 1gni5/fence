# cli.py

from sys import argv
from dataload import dataload
from polygon import Polygon

def main():

    # Pour chaque fichier passé en paramètre
    for filename in argv[1:]:

        # Si l'utilisateur fourni plusieurs fichiers sources
        if len(argv[1:]) > 1:
            print(f'{filename}', end=": ")

        # Créer l'enclos et la vache
        pen = Polygon(dataload(filename))
        cow = pen.gravity

        # Affiche la réponse
        if cow in pen:
            print("La vache est à l'intérieur de l'enclos.")
        else:
            print("La vache est à l'extérieur de l'enclos.")

    # L'utilisateur n'a pas fourni de fichier
    if len(argv) <= 1:
        print(f'{argv[0]}: missing operand. Usage: {argv[0]} filename [filename2, ..., filenameN]')

if __name__ == '__main__':
    main()
