from Model.Constantes import *
from Model.Pion import *
from random import randint, choice


#
# Le plateau représente la grille où sont placés les pions.
# Il constitue le coeur du jeu car c'est dans ce fichier
# où vont être programmées toutes les règles du jeu.
#
# Un plateau sera simplement une liste de liste.
# Ce sera en fait une liste de lignes.
# Les cases du plateau ne pourront contenir que None ou un pion
#
# Pour améliorer la "rapidité" du programme, il n'y aura aucun test sur les paramètres.
# (mais c'est peut-être déjà trop tard car les tests sont fait en amont, ce qui ralentit le programme...)
#

def type_plateau(plateau: list) -> bool:
    """
    Permet de vérifier que le paramètre correspond à un plateau.
    Renvoie True si c'est le cas, False sinon.

    :param plateau: Objet qu'on veut tester
    :return: True s'il correspond à un plateau, False sinon
    """
    if type(plateau) != list:
        return False
    if len(plateau) != const.NB_LINES:
        return False
    wrong = "Erreur !"
    if next((wrong for line in plateau if type(line) != list or len(line) != const.NB_COLUMNS), True) == wrong:
        return False
    if next((wrong for line in plateau for c in line if not(c is None) and not type_pion(c)), True) == wrong:
        return False
    return True

def construirePlateau() -> list :
    """
    Construit un plateau
    :return: Liste 2D formant un tableau de ligne
    """
    plateau = []
    for i in range(const.NB_LINES) :
        plateau.append([])
        for j in range(const.NB_COLUMNS):
            plateau[i].append(None)
    return plateau

def placerPionPlateau(plateau : list, pion : dict, colonne : int) -> int :
    """
    Place le Pion dans le plateau en choisissant la colonne donnée en paramètre, retourne la ligne ou le pion atterit
    :param plateau: Liste 2d formant un tableau
    :param pion: Dictionnaire représentant un pion
    :param colonne: Numéro de la colonne où déposer le pion
    :return: Ligne où atterit le pion
    """
    if type_plateau(plateau) == False :
        raise TypeError(f"placerPionPlateau : Le premier paramètre n'est pas un plateau")
    if type_pion == False :
        raise TypeError(f"placerPionPlateau : Le second paramètre n'est pas un pion")
    if type(colonne) != int :
        raise TypeError(f"« placerPionPlateau : Le troisième paramètre n’est pas un entier ")
    if colonne < 0 or colonne > len(plateau) :
        raise ValueError(f" placerPionPlateau : La valeur de la colonne ({colonne}) n'est pas correcte")
    ligne = -1
    i = const.NB_LINES -1
    while i >= 0 and ligne == -1:
        if plateau[i][colonne] is None:
            plateau[i][colonne] = pion
            ligne = i
        i = i - 1
    return ligne

def toStringPlateau(plateau : list) -> str :
    """
    A partir d'une liste 2d , retourne une chaine de caractère représentant le tableau
    :param plateau: Liste 2d formant un tableau
    :return: chaine de caractère qui représente le tableau
    """
    p = construirePlateau()
    for i in range(20):
        placerPionPlateau(p, construirePion(choice(const.COULEURS)), randint(0, const.NB_COLUMNS - 1))
    print(toStringPlateau(p))
