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
    Déterminer la couleur du pion
    :param couleur: couleur du pion
    :return: Pion construit avec la couleur donnée en paramètre
    """
    if couleur == const.ROUGE :
        pion = {const.COULEUR : const.ROUGE, const.ID : None}
    elif couleur == const.JAUNE :
        pion = {const.COULEUR : const.JAUNE, const.ID : None}
    if type(couleur) != int :
        raise TypeError(f"construirePion : Le paramètre n'est pas de type entier")
    if (couleur != const.ROUGE and couleur != const.JAUNE) :
        raise ValueError(f"construirePion : la couleur ({couleur}) n'est pas correcte")
    return pion

print(construirePion(2))


