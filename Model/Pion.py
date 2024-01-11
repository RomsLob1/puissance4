# Model/Pion.py

from Model.Constantes import *

#
# Ce fichier implémente les données/fonctions concernant le pion
# dans le jeu du Puissance 4
#
# Un pion est caractérisé par :
# - sa couleur (const.ROUGE ou const.JAUNE)
# - un identifiant de type int (pour l'interface graphique)
#
# L'identifiant sera initialisé par défaut à None
#

def type_pion(pion: dict) -> bool:
    """
    Détermine si le paramètre peut être ou non un Pion

    :param pion: Paramètre dont on veut savoir si c'est un Pion ou non
    :return: True si le paramètre correspond à un Pion, False sinon.
    """
    return type(pion) == dict and len(pion) == 2 and const.COULEUR in pion.keys() \
        and const.ID in pion.keys() \
        and pion[const.COULEUR] in const.COULEURS \
        and (pion[const.ID] is None or type(pion[const.ID]) == int)

def construirePion(couleur : int) -> dict :
    """
    Construire un pion ayant une couleur et un id
    :param couleur: couleur du pion
    :return: Pion construit avec la couleur donnée en paramètre
    """
    pion = {const.COULEUR : couleur, const.ID : None}

    if type(couleur) != int :
        raise TypeError(f"construirePion : Le paramètre n'est pas de type entier")
    if (couleur != const.ROUGE and couleur != const.JAUNE) :
        raise ValueError(f"construirePion : la couleur ({couleur}) n'est pas correcte")
    return pion

def getCouleurPion(pion : dict) -> int :
    """
    Déterminer la couleur du pion
    :param pion: Pion construit à partir de la fonction construirePion
    :return: Couleur du pion
    """
    if type_pion == False :
        raise TypeError(f"getCouleurPion : Le paramètre n'est pas un pion")
    return pion[const.COULEUR]

def setCouleurPion(pion : dict, couleur2 : int) -> None :
    """
    Change la couleur du pion par la couleur passée en paramètre
    :param pion: Pion construit à partir de la fonction construirePion
    :param couleur: Couleur qui remplacera celle du pion en paramètre
    :return: None
    """
    pion[const.COULEUR] = couleur2
    if type_pion == False :
        raise TypeError(f"setCouleurPion : Le premier paramètre n'est pas un pion")
    if type(couleur2) != int:
        raise TypeError(f"setCouleurPion : Le second paramètre n'est pas de type entier")
    a = 0
    for i in range(len(const.COULEURS)):
        if couleur2 == const.COULEURS[i] :
            a += 1
    if a == 0 :
        raise ValueError(f"construirePion : le second paramètre ({couleur2}) n'est pas une couleur")
    return None

def getIdPion(pion : dict) -> int :
    """
    Obtenir l'ID du pion
    :param pion: Pion construit à partir de la fonction construirePion
    :return: ID du pion
    """
    if type_pion == False :
        raise TypeError(f"getIDPion : Le paramètre n'est pas un pion")
    return pion[const.ID]

def setIdPion(pion : dict, Id : int) -> None :
    """
    Changer l'ID du pion avec l'ID passé en paramètre de la fonction
    :param pion: Pion construit à partir de la fonction construirePion
    :param Id: Pion construit à partir de la fonction construirePion
    :return: Le nouvel Id du pion qui est l'Id passé en paramètre
    """
    pion[const.ID] = Id
    if type_pion == False :
        raise TypeError(f"getIDPion : Le paramètre n'est pas un pion")
    if type(Id) != int:
        raise TypeError(f"setCouleurPion : Le second paramètre n'est pas de type entier")
    return None

