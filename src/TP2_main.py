
##########################################################
"""
    Le script main.py sert à afficher le résultat issue
    de TP2_affichage dans le terminal et publie ceux-ci
    dans la base de données à l'aide de TP2_pytosql
"""
##########################################################


from data import *
from TP2_dat import Solver
from TP2_pytosql import requete, bd_data, cursor
from TP2_Affichage import pr_ar


#########################################################
#   S'assurer d'initialiser la base de données dans     #
#   TP2_BD avant de publier le résultat dans celle-ci   #
#########################################################


""" Résoudre le problème """
inst = Solver(n, m, d, L, lon_u, lar_u, set_K, lon, poids, cd, Xa, Ya)
res = inst.solve()

""" Afficher le résultat dans le terminal """
pr_ar()

""" Publier les résultat dans la base de données """
cursor.execute(requete, (bd_data))
cursor.execute("COMMIT")
cursor.close()
