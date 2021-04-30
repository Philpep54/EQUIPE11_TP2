
##############################################
"""
    Le script suivant génère un array numpy 
    et le transforme en string afin de le 
    publier dans la base de données
"""
##############################################


import sqlite3
from TP2_dat import Solver
from TP2_Affichage import dic_Var_X, dic_Var_Y, dic_Var_Aij, dic_Var_Bij, dic_Var_dx, dic_Var_dy, dic_Var_ddx, dic_Var_ddy
import numpy as np
from data import *


""" Création des strings à partir des résultats de variables """
x = dic_Var_X
upd_Var_X = []
for i in x.values():
    upd_Var_X.append(i)
ar_Var_X = np.reshape(upd_Var_X, len(set_K))
X = str(ar_Var_X)

y = dic_Var_Y
upd_Var_Y = []
for i in y.values():
    upd_Var_Y.append(i)
ar_Var_Y = np.reshape(upd_Var_Y, len(set_K))
Y = str(ar_Var_Y)

aij = dic_Var_Aij
upd_Var_Aij = []
for i in aij.values():
    upd_Var_Aij.append(i)
ar_Var_Aij = np.reshape(upd_Var_Aij, (len(set_K),len(set_K)))
Aij = str(ar_Var_Aij)

bij = dic_Var_Bij
upd_Var_Bij = []
for i in bij.values():
    upd_Var_Bij.append(i)
ar_Var_Bij = np.reshape(upd_Var_Bij, (len(set_K),len(set_K)))
Bij = str(ar_Var_Bij)

dx = dic_Var_dx
upd_Var_dx = []
for i in dx.values():
    upd_Var_dx.append(i)
ar_Var_dx = np.reshape(upd_Var_dx, (len(set_K),len(set_K)))
Dx = str(ar_Var_dx)

dy = dic_Var_dy
upd_Var_dy = []
for i in dy.values():
    upd_Var_dy.append(i)
ar_Var_dy = np.reshape(upd_Var_dy, (len(set_K),len(set_K)))
Dy = str(ar_Var_dy)

ddx = dic_Var_ddx
upd_Var_ddx = []
for i in ddx.values():
    upd_Var_ddx.append(i)
ar_Var_ddx = np.reshape(upd_Var_ddx, len(set_K))
DDx = str(ar_Var_ddx)

ddy = dic_Var_ddy
upd_Var_ddy = []
for i in ddy.values():
    upd_Var_ddy.append(i)
ar_Var_ddy = np.reshape(upd_Var_ddy, len(set_K))
DDy = str(ar_Var_ddy)


""" Préparation à la publication dans la basee de données """
bd_data = [X, Y, Aij, Bij, Dx, Dy, DDx, DDy]
connexion = sqlite3.connect(emplacement_DB)
cursor = connexion.cursor()
requete = ('''INSERT INTO configs (X, Y, Aij, Bij, dx, dy, ddx, ddy)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''')

