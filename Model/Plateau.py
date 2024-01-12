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


def detecter4horizontalPlateau(plateau : list, couleur : int) -> list :
    """
    Permet de retrouver les puissances 4 horizontaux
    :param plateau: plateau construit par la fonction construirePlateau
    :param couleur: couleur entre jaune et rouge
    :return: retourne une liste de 4 même couleur mis en paramètre
    """
    if type_plateau == False :
        raise TypeError(f" detecter4horizontalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int :
        raise TypeError(f"« detecter4horizontalPlateau : Le second paramètre n’est pas un entier ")
    a = 0
    for i in range(len(const.COULEURS)):
        if couleur == const.COULEURS[i]:
            a += 1
    if a == 0:
        raise ValueError(f" detecter4horizontalPlateau : La valeur de la couleur {couleur} n'est pas correcte")
    puissance4 = []
    for i in range(len(plateau)) :
        for j in range(len(plateau[i])-3) :
            if plateau[i][j] == couleur :
                if plateau[i][j+1] == couleur :
                    if plateau[i][j+2] == couleur :
                        if plateau[i][j+3] == couleur :
                            puissance4.append([construirePion(couleur),construirePion(couleur),construirePion(couleur),construirePion(couleur)])
                            break
    return puissance4
def detecter4verticalPlateau(plateau : list, couleur : int) -> list :
    """
    Permet de retrouver les puissances 4 verticals
    :param plateau: plateau construit par la fonction construirePlateau
    :param couleur: couleur entre jaune et rouge
    :return: retourne une liste de liste de 4 même couleur mis en paramètre
    """
    if type_plateau == False :
        raise TypeError(f" detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int :
        raise TypeError(f"« detecter4verticalPlateau : Le second paramètre n’est pas un entier ")
    puissance4 = []
    a = 0
    for i in range(len(const.COULEURS)):
        if couleur == const.COULEURS[i]:
            a += 1
    if a == 0:
        raise ValueError(f" detecter4verticalPlateau : La valeur de la couleur {couleur} n'est pas correcte")
    puissance4 = []
    for i in range(len(plateau[0])):
        for j in range(len(plateau)-3):
            if plateau[j][i] == couleur :
                if plateau[j+1][i] == couleur :
                    if plateau[j+2][i] == couleur :
                        if plateau[j+3][i] == couleur :
                            puissance4.append([construirePion(couleur),construirePion(couleur),construirePion(couleur),construirePion(couleur)])
                            break
    return puissance4

def detecter4diagonaleDirectePlateau(plateau : list, couleur : int) -> list :
    """
        Permet de retrouver les puissances 4 sur les diagonales directes
        :param plateau: plateau construit par la fonction construirePlateau
        :param couleur: couleur entre jaune et rouge
        :return: retourne une liste de liste de 4 même couleur mis en paramètre
        """
    if type_plateau == False :
        raise TypeError(f" detecter4diagonalDirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int :
        raise TypeError(f"« detecter4diagonalDirectePlateau : Le second paramètre n’est pas un entier ")
    puissance4 = []
    a = 0
    for i in range(len(const.COULEURS)):
        if couleur == const.COULEURS[i]:
            a += 1
    if a == 0:
        raise ValueError(f" detecter4diagonalDirectePlateau : La valeur de la couleur {couleur} n'est pas correcte")
    puissance4 = []
    for i in range(len(plateau[0])-3):
        for j in range(len(plateau)-3):
            if plateau[j][i] == couleur :
                if plateau[j+1][i+1] == couleur :
                    if plateau[j+2][i+2] == couleur :
                        if plateau[j+3][i+3] == couleur :
                            if i == 0 or j == 0:
                                puissance4.append([construirePion(couleur), construirePion(couleur), construirePion(couleur), construirePion(couleur)])
                            elif i > 0 and j < len(plateau) - 1:
                                if plateau[i -1][j - 1] != couleur:
                                    puissance4.append([construirePion(couleur), construirePion(couleur), construirePion(couleur), construirePion(couleur)])
    return puissance4

def detecter4diagonaleIndirectePlateau(plateau: list, couleur: int) -> list :
    """
        Permet de retrouver les puissances 4 sur les diagonales directes
        :param plateau: plateau construit par la fonction construirePlateau
        :param couleur: couleur entre jaune et rouge
        :return: retourne une liste de liste de 4 même couleur mis en paramètre
        """
    if type_plateau == False:
        raise TypeError(f" detecter4diagonalDirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError(f"« detecter4diagonalDirectePlateau : Le second paramètre n’est pas un entier ")
    puissance4 = []
    a = 0
    for i in range(len(const.COULEURS)):
        if couleur == const.COULEURS[i]:
            a += 1
    if a == 0:
        raise ValueError(f" detecter4diagonalDirectePlateau : La valeur de la couleur {couleur} n'est pas correcte")

    puissance4 = []
    for i in range(0,len(plateau[0])-3):

        for j in range(len(plateau)-1,2,-1):

            if plateau[j][i] == couleur :
                if plateau[j-1][i+1] == couleur :
                    if plateau[j-2][i+2] == couleur :
                        if plateau[j-3][i+3] == couleur :
                            if i == 0 or j == len(plateau)-1:
                                puissance4.append([construirePion(couleur), construirePion(couleur), construirePion(couleur), construirePion(couleur)])
                            elif i > 0 and j < len(plateau)-1:
                                if plateau[i+1][j-1] != couleur :
                                    puissance4.append([construirePion(couleur), construirePion(couleur),construirePion(couleur),construirePion(couleur)])
    return puissance4

def getPionsGagnantsPlateau(plateau : list) -> list :
    """
    Fonction qui renvoie une liste des pions formant une puissance 4 sur le plateau
    :param plateau: liste 2d qui représente un tableau
    :return: list des pions formant une puissance 4
    """
    if type_plateau == False:
        raise TypeError(f" getPionsGagnantsPlateau : Le paramètre n'est pas un plateau")
    puissance4 = []
    puissance4.append(detecter4verticalPlateau(plateau, const.JAUNE))
    puissance4.append(detecter4verticalPlateau(plateau, const.ROUGE))
    puissance4.append(detecter4horizontalPlateau(plateau, const.JAUNE))
    puissance4.append(detecter4horizontalPlateau(plateau, const.ROUGE))
    puissance4.append(detecter4diagonaleIndirectePlateau(plateau, const.JAUNE))
    puissance4.append(detecter4diagonaleIndirectePlateau(plateau, const.ROUGE))
    puissance4.append(detecter4diagonaleDirectePlateau(plateau, const.JAUNE))
    puissance4.append(detecter4diagonaleDirectePlateau(plateau, const.ROUGE))
    return puissance4

