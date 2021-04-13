from TP2_dat import Solver

#-------------------------Données-------------------------#

set_K = [1,2,3,4,5,6]
larg_on = [4,3,5,4,6,5]
poids = [0,4,5,2,3,6,4,0,4,3,5,3,5,4,0,4,7,8,2,3,4,0,3,3,3,5,7,3,0,5,6,3,8,3,5,0]

#------------------------Variables------------------------#

inst = Solver(set_K, larg_on, poids)
res = inst.solve()

Var_X = res[0]
Var_Y = res[1]
Var_Aij = res[2]
Var_Bij = res[3]
Var_dx = res[4]
Var_dy = res[5]

#------------------------Affichage------------------------#

print(f"\nX:\n {Var_X}")
print(f"\nY:\n {Var_Y}")
print(f"\nAij:\n {Var_Aij}")
print(f"\nBij:\n {Var_Bij}")
print(f"\ndx:\n {Var_dx}")
print(f"\ndy:\n {Var_dy}")

