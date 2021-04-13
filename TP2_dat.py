import amplpy
import os

# ampl_path => L'emplacement de AMPL et nos dossiers .mod et .run
# ampl_env => l'environnement AMPL dans Python
# ampl => notre traducteur, permet de lire les models

ampl_env = amplpy.Environment()
ampl_path = os.path.normpath('/Applications/Document/ULaval/AMPL/ampl_macos64')
ampl_env = amplpy.Environment(ampl_path)
ampl = amplpy.AMPL(ampl_env)

#--------------------Configuration--------------------#

ampl.setOption('solver', 'gurobi')

#-------------------Lecture du .mod-------------------#

model_dir = os.path.normpath('/Applications/Document/ULaval/AMPL/ampl_macos64')
ampl.read(os.path.join(model_dir, 'TP2_mod1.mod'))

#----------------------Paramètre----------------------#

""" Paramètre n """
df = ampl.getParameter('n')
df.set(6)

""" Paramètre m """
df = ampl.getParameter('m')
df.set(3)

""" Paramètre d """
df = ampl.getParameter('d')
df.set(12)

""" Paramètre L """
df = ampl.getParameter('L')
df.set(27)

""" Paramètre Lon_u """
df = ampl.getParameter('Lon_u')
df.set(24)

""" Paramètre Lar_u """
df = ampl.getParameter('Lar_u')
df.set(60)

""" Set K """
set_K = [1,2,3,4,5,6]
df = amplpy.DataFrame('K')
df.setColumn('K', set_K)
ampl.setData(df, 'K')

""" Paramètre lon """
larg_on = [4,3,5,4,6,5]
df = amplpy.DataFrame("K", "lon")
df.setValues({I: larg_on[i]
                for i, I in enumerate(set_K)})
ampl.setData(df)

""" Paramètre c """
poids = [0,4,5,2,3,6,4,0,4,3,5,3,5,4,0,4,7,8,2,3,4,0,3,3,3,5,7,3,0,5,6,3,8,3,5,0]
df = amplpy.DataFrame(('I','J'), 'c')
df.setValues({(I,J): poids[(len(set_K))*i+j]
            for i, J in enumerate(set_K)
            for j, I in enumerate(set_K)})
ampl.setData(df)
ampl.solve()

#----------------------Affichage----------------------#

X = ampl.getVariable('X')
X_val = X.getValues()
X_val_dic = X_val.toDict()

Y = ampl.getVariable('Y')
Y_val = Y.getValues()
Y_val_dic = Y_val.toDict()

A = ampl.getVariable('Aij')
A_val = A.getValues()
A_val_dic = A_val.toDict()

B = ampl.getVariable('Bij')
B_val = B.getValues()
B_val_dic = B_val.toDict()

dx = ampl.getVariable('dx')
dx_val = dx.getValues()
dx_val_dic = dx_val.toDict()

dy = ampl.getVariable('dy')
dy_val = dy.getValues()
dy_val_dic = dy_val.toDict()

# print(X_val)
# print(Y_val)
# print(A_val)
# print(B_val)
# print(dx_val)
# print(dy_val)

print(f"X: {X_val_dic}")
print(f"Y: {Y_val_dic}")
# print(f"Aij: {A_val_dic}")
# print(f"Bij: {B_val_dic}")
# print(f"dx: {dx_val_dic}")
# print(f"dy: {dy_val_dic}")


