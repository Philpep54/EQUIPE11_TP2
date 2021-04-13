import numpy as np
from data import *
from TP2_dat import Solver

#------------------------Variables------------------------#

inst = Solver(n, m, d, L, lon_u, lar_u, set_K, larg_on, poids)
res = inst.solve()

""" DataFrame """
df_Var_X = res[6]
df_Var_Y = res[7]
df_Var_Aij = res[8]
df_Var_Bij = res[9]
df_Var_dx = res[10]
df_Var_dy = res[11]

""" Dictionnaire """
dic_Var_X = res[0]
dic_Var_Y = res[1]
dic_Var_Aij = res[2]
dic_Var_Bij = res[3]
dic_Var_dx = res[4]
dic_Var_dy = res[5]

""" Array """
def ar_Var_X():
    upd_Var_X = []
    for i in dic_Var_X.values():
        upd_Var_X.append(i)
    ar_Var_X = np.reshape(upd_Var_X, len(set_K))
    return ar_Var_X

def ar_Var_Y():
    upd_Var_Y = []
    for i in dic_Var_Y.values():
        upd_Var_Y.append(i)
    ar_Var_Y = np.reshape(upd_Var_Y, len(set_K))
    return ar_Var_Y

def ar_Var_Aij():
    upd_Var_Aij = []
    for i in dic_Var_Aij.values():
        upd_Var_Aij.append(i)
    ar_Var_Aij = np.reshape(upd_Var_Aij, (len(set_K),len(set_K)))
    return ar_Var_Aij

def ar_Var_Bij():
    upd_Var_Bij = []
    for i in dic_Var_Bij.values():
        upd_Var_Bij.append(i)
    ar_Var_Bij = np.reshape(upd_Var_Bij, (len(set_K),len(set_K)))
    return ar_Var_Bij

def ar_Var_dx():
    upd_Var_dx = []
    for i in dic_Var_dx.values():
        upd_Var_dx.append(i)
    ar_Var_dx = np.reshape(upd_Var_dx, (len(set_K),len(set_K)))
    return ar_Var_dx

def ar_Var_dy():
    upd_Var_dy = []
    for i in dic_Var_dy.values():
        upd_Var_dy.append(i)
    ar_Var_dy = np.reshape(upd_Var_dy, (len(set_K),len(set_K)))
    return ar_Var_dy


#------------------------Affichage------------------------#

def pr_df():
    print(f"\n{res[12]}\n")
    print(f"\nX:\n {df_Var_X}")
    print(f"\nY:\n {df_Var_Y}")
    print(f"\nAij:\n {df_Var_Aij}")
    print(f"\nBij:\n {df_Var_Bij}")
    print(f"\ndx:\n {df_Var_dx}")
    print(f"\ndy:\n {df_Var_dy}")

def pr_dic():
    print(f"\n{res[12]}\n")
    print(f"\nX:\n {dic_Var_X}")
    print(f"\nY:\n {dic_Var_Y}")
    print(f"\nAij:\n {dic_Var_Aij}")
    print(f"\nBij:\n {dic_Var_Bij}")
    print(f"\ndx:\n {dic_Var_dx}")
    print(f"\ndy:\n {dic_Var_dy}")

def pr_ar():
    print(f"\n{res[12]}\n")
    print(f"\n{ar_Var_X()} X")
    print(f"\n{ar_Var_Y()} Y")
    print(f"\n{ar_Var_Aij()} Aij")
    print(f"\n{ar_Var_Bij()} Bij")
    print(f"\n{ar_Var_dx()} dx")
    print(f"\n{ar_Var_dy()} dy")

""" Afficher les DataFrame """
# pr_df()

""" Afficher les Dictionnaire """
# pr_dic()

""" Afficher les Array """
pr_ar()
