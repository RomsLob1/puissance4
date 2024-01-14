from Model.Constantes import *
from Model.Plateau import *
from Model.Pion import *
from Model.Joueur import *

p = construirePlateau()
print(p)
pion = construirePion(const.JAUNE)
line = placerPionPlateau(p, pion, 2)
print("Placement d’un pion en colonne 2. Numéro de ligne :", line)
print(p)

# Essais sur les couleurs
print("\x1B[43m \x1B[0m : carré jaune ")
print("\x1B[41m \x1B[0m : carré rouge ")
print("\x1B[41mA\x1B[0m : A sur fond rouge")

def toStringPlateau(plateau : list) -> str :
    """
    A partir d'une liste 2d , retourne une chaine de caractère représentant le tableau
    :param plateau: Liste 2d formant un tableau
    :return: chaine de caractère qui représente le tableau
    """
    res = ""

    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if plateau[i][j] is not None and plateau[i][j].get(const.COULEUR) == 1:
                res += "|" + "\x1B[41m \x1B[0m"
            elif plateau[i][j] is not None and plateau[i][j].get(const.COULEUR) == 0:
                res += "|" + "\x1B[43m \x1B[0m"
            else:
                res += "|" + " "
        res += "|\n"

    for i in range(len(plateau[0]) * 2 + 1):
        res += "-"
    res += "\n"

    for i in range(len(plateau[0])):
        res += " " + str(i)

    return res

from Model.Constantes import *
from Model.Plateau import *
from Model.Pion import *
from random import randint, choice
p = construirePlateau()
for _ in range(40):
 placerPionPlateau(p, construirePion(choice(const.COULEURS)),
 randint(0, const.NB_COLUMNS - 1))
print(toStringPlateau(p))
print(detecter4verticalPlateau(p,0))
print(detecter4horizontalPlateau(p,0))
print(detecter4diagonaleIndirectePlateau(p,0))
print(detecter4diagonaleDirectePlateau(p,0))
