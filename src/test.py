from TP2_dat import Solver
from data import *
import numpy as np
import matplotlib.pyplot as plt

inst = Solver(n, m, d, L, lon_u, lar_u, set_K, lon, poids, cd, Xa, Ya)
res = inst.solve()

""" Création de la liste de points """
X_ = res[0]
X = [i for i in X_.values()]

Y_ = res[1]
Y = [i for i in Y_.values()]

point = [(int(X[i]), int(Y[i])) for i in range(0, len(X))]

point2 = [(1,3), (3,5), (6,7), (10,10)]

""" creation "Usine" """
usine = [[0]*lon_u]*lar_u
usine = np.array(usine)

for i, j in enumerate(point):
    x1 = j[0]-1
    y1 = j[1]-1

    usine[y1][x1] = (i+1)

print(usine)
print(point)

plt.title('Test Usine')
heatmap = plt.pcolor(usine)
plt.show()


# print(X,Y)