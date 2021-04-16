import sqlite3
import TP2_dat
import numpy as np
from data import *

simulation1 = TP2_dat.Solver(n, m, d, L, lon_u, lar_u, set_K, lon, poids)

list_data = simulation1.solve()

x = list_data[0]
upd_Var_X = []
for i in x.values():
    upd_Var_X.append(i)
ar_Var_X = np.reshape(upd_Var_X, len(set_K))
X = str(ar_Var_X)

y = list_data[1]
upd_Var_Y = []
for i in y.values():
    upd_Var_Y.append(i)
ar_Var_Y = np.reshape(upd_Var_Y, len(set_K))
Y = str(ar_Var_Y)

aij = list_data[2]
upd_Var_Aij = []
for i in aij.values():
    upd_Var_Aij.append(i)
ar_Var_Aij = np.reshape(upd_Var_Aij, (len(set_K),len(set_K)))
Aij = str(ar_Var_Aij)

bij = list_data[3]
upd_Var_Bij = []
for i in bij.values():
    upd_Var_Bij.append(i)
ar_Var_Bij = np.reshape(upd_Var_Bij, (len(set_K),len(set_K)))
Bij = str(ar_Var_Bij)

dx = list_data[4]
upd_Var_dx = []
for i in dx.values():
    upd_Var_dx.append(i)
ar_Var_dx = np.reshape(upd_Var_dx, (len(set_K),len(set_K)))
Dx = str(ar_Var_dx)

dy = list_data[5]
upd_Var_dy = []
for i in dy.values():
    upd_Var_dy.append(i)
ar_Var_dy = np.reshape(upd_Var_dy, (len(set_K),len(set_K)))
Dy = str(ar_Var_dy)

bd_data = [X, Y, Aij, Bij, Dx, Dy]


connexion = sqlite3.connect(emplacement_DB)

cursor = connexion.cursor()

requete = ('''INSERT INTO configs (X, Y, Aij, Bij, dx, dy)
            VALUES (?, ?, ?, ?, ?, ?)''')

cursor.execute(requete, (bd_data))
cursor.execute("COMMIT")
cursor.close()

