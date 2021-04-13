from TP2_dat import Solver

set_K = [1,2,3,4,5,6]
larg_on = [4,3,5,4,6,5]
poids = [0,4,5,2,3,6,4,0,4,3,5,3,5,4,0,4,7,8,2,3,4,0,3,3,3,5,7,3,0,5,6,3,8,3,5,0]

affichage = Solver(set_K, larg_on, poids)

print(affichage.solve())