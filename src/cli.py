# cli.py

from sys import argv
from matplotlib import pyplot
from os import system
from platform import system as OS

from polygon import Polygon
from dataload import load_from_csv

def cowsay(answer):

    # Essaye d'exécuter la commande
    cmd = f"cowsay \' Je suis à l {answer} ! \'"
    result = system(cmd)

def draw(pen, cow):
    """Dessine l'enclot ainsi que la vache."""

    # Paramètre la fenêtre de graphe
    pyplot.title("FENCE (Fence Exist No Cow Escape)")
    pyplot.axis('equal')

    # Dessine l'enclot
    vertices = pen.vertices + pen.vertices[:1]
    
    pyplot.plot(
    	[ vertex.x for vertex in vertices ],
    	[ vertex.y for vertex in vertices ],
    	marker='o', label='Enclos'
    )

    # Dessine la vache
    pyplot.scatter(*cow, label='Vache', marker='x', color='r')
    
    # Affiche le graphique
    pyplot.legend()
    pyplot.show()

def extract_args_and_options(argv):
    """Extrait la liste ds arguments et des options,
    retourne 2 listes."""

    # Tout ce qui commence par "--" est une option
    options = list(
        filter(lambda x : x.startswith('--'), argv[1:])
    )

    # Tout ce qui n'est pas une option est un argument
    arguments = list(
        filter(lambda x : x not in options, argv[1:])
    )

    return arguments, options

def main():

    # Filtre les arguments et les options
    arguments, options = extract_args_and_options(argv)

    # Pour chaque fichier passé en paramètre
    for filename in arguments:

        # Si l'utilisateur fourni plusieurs fichiers sources
        if len(argv[1:]) > 1:
            print(f'{filename}', end=": ")

        # Créer l'enclos et la vache
        pen = Polygon(load_from_csv(filename))
        cow = pen.gravity

        # Affiche la réponse
        answer = 'intérieur' if cow in pen else 'extérieur'
        print(f"La vache est à l'{answer} de l'enclos.")

        # Utilise la command cowsay
        if '--cowsay' in options:
            cowsay(answer)

        # Affiche le graphique
        if '--graph' in options:
            draw(pen, cow)

    # L'utilisateur n'a pas fourni de fichier
    if len(arguments) == 0:
        print(f'{argv[0]}: missing operand. Usage: {argv[0]} filename [filename2, ..., filenameN] [--graph]')


if __name__ == '__main__':
    main()
