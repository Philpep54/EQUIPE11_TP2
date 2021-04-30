
##############################################
"""
    Le script suivant génère un array numpy 
    et le transforme en string afin de le 
    publier dans la base de données
"""
##############################################


import sqlite3
from TP2_dat import Solver
from TP2_Affichage import ar_Var_X, ar_Var_Y, ar_Var_Aij, ar_Var_Bij, ar_Var_dx, ar_Var_dy, ar_Var_ddx, ar_Var_ddy
import numpy as np
from data import *


""" Création des strings à partir des résultats de variables """

X = str(ar_Var_X())

Y = str(ar_Var_Y())

Aij = str(ar_Var_Aij())

Bij = str(ar_Var_Bij())

Dx = str(ar_Var_dx())

Dy = str(ar_Var_dy())

DDx = str(ar_Var_ddx())

DDy = str(ar_Var_ddy())


""" Préparation à la publication dans la basee de données """
bd_data = [X, Y, Aij, Bij, Dx, Dy, DDx, DDy]
connexion = sqlite3.connect(emplacement_DB)
cursor = connexion.cursor()
requete = ('''INSERT INTO configs (X, Y, Aij, Bij, dx, dy, ddx, ddy)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''')

