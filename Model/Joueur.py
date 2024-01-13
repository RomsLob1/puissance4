from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *



#
# Ce fichier contient les fonctions gérant le joueur
#
# Un joueur sera un dictionnaire avec comme clé :
# - const.COULEUR : la couleur du joueur entre const.ROUGE et const.JAUNE
# - const.PLACER_PION : la fonction lui permettant de placer un pion, None par défaut,
#                       signifiant que le placement passe par l'interface graphique.
# - const.PLATEAU : référence sur le plateau de jeu, nécessaire pour l'IA, None par défaut
# - d'autres constantes nécessaires pour lui permettre de jouer à ajouter par la suite...
#

def type_joueur(joueur: dict) -> bool:
    """
    Détermine si le paramètre peut correspondre à un joueur.

    :param joueur: Paramètre à tester
    :return: True s'il peut correspondre à un joueur, False sinon.
    """
    if type(joueur) != dict:
        return False
    if const.COULEUR not in joueur or joueur[const.COULEUR] not in const.COULEURS:
        return False
    if const.PLACER_PION not in joueur or (joueur[const.PLACER_PION] is not None
            and not callable(joueur[const.PLACER_PION])):
        return False
    if const.PLATEAU not in joueur or (joueur[const.PLATEAU] is not None and
        not type_plateau(joueur[const.PLATEAU])):
        return False
    return True

def construireJoueur(couleur : int) -> dict :
    """
    construit un joueur à partir en initialisant sa couleur
    :param couleur: couleur du joueur
    :return: dictionnaire composé de la couleur, du plateau et d'une fonction qui représente le joueur
    """
    if type(couleur) != int :
        raise TypeError("construireJoueur : Le paramètre n'est pas un entier")
    if (couleur != const.ROUGE and couleur != const.JAUNE) :
        raise ValueError(f"construireJoueur : L'entier donné ({couleur}) n'est pas une couleur")
    joueur = {const.COULEUR: couleur, const.PLATEAU: None, const.PLACER_PION : None}
    return joueur

def getCouleurJoueur(joueur : dict) -> int :
    """
    Donne la couleur du joueur
    :param joueur: Dictionnaire représentant un joueur
    :return: la couleur du joueur
    """
    if type_joueur(joueur) == False :
        raise TypeError("getCouleurJoueur : Le paramètre ne correspond pas à un joueur")
    return joueur[const.COULEUR]

def getPlateauJoueur(joueur : dict) -> list :
    """
        Donne la variable plateau du joueur
        :param joueur: Dictionnaire représentant un joueur
        :return: plateau du joueur
        """
    if type_joueur(joueur) == False :
        raise TypeError("getPlateauJoueur : le paramètre ne correspond pas à un joueur")
    return joueur[const.PLATEAU]

def getPlacerPionJoueur(joueur : dict) -> callable :
    """
        Donne la fonction PlacerPion du joueur
        :param joueur: Dictionnaire représentant un joueur
        :return: PlacerPion du joueur
        """
    if type_joueur(joueur) == False :
        raise TypeError("getPlacerPionJoueur : Le paramètre ne correspond pas à un joueur")
    return joueur[const.PLACER_PION]

def getPionJoueur(joueur : dict) -> dict :
    """
    Créer un pion avec la couleur du joueur
    :param joueur: Dictionnaire représentant un joueur
    :return: pion avec la couleur du joueur
    """
    if type_joueur(joueur) == False :
        raise TypeError("getPionJoueur : Le paramètre ne correspond pas à un joueur")
    pion = {const.COULEUR : joueur[const.COULEUR], const.ID : None}
    return pion

def setPlateauJoueur(joueur : dict, plateau : list) -> None :
    """
    Met en place le plateau dans le dictionnaire joueur
    :param joueur: Dictionnaire représentant un joueur
    :param plateau: Liste 2D qui représentent le plateau
    :return: None
    """
    if type_joueur(joueur) == False :
        raise TypeError("setPlateauJoueur : Le premier paramètre ne correspond pas à un joueur")
    if type_plateau(plateau) == False :
        raise TypeError("setPlateauJoueur : Le second paramètre ne correspond pas à un plateau")
    joueur[const.PLATEAU] = plateau
    return None

def setPlacerPionJoueur(joueur : dict, placerPion : callable) -> None :
    """
    Met ne place la fonction PlacerPion dans le dictionnaire joueur
    :param joueur: Dictionnaire représentent un joueur
    :param placerPion: fonction
    """
    if type_joueur(joueur) == False :
        raise TypeError("setPlacerPionJoueur : Le premier paramètre ne correspond pas à un joueur")
    if callable(placerPion) == False :
        raise TypeError("setPlateauPionJoueur :Le second paramètre n'est pas une fonction")
    joueur[const.PLACER_PION] = placerPion
    return None

def _placerPionJoueur(joueur : dict) -> int :

    libre = False
    while libre == False :
        colonne = randint(0, const.NB_COLUMNS - 1)
        if joueur[const.PLATEAU[0][colonne]] == None :
            libre = True

    return colonne
