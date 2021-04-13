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

ampl.setOption('solver', 'cplex')

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
print(df)
""" Paramètre c """
poids = [0,4,5,2,3,6,4,0,4,3,5,3,5,4,0,4,7,8,2,3,4,0,3,3,3,5,7,3,0,5,6,3,8,3,5,0]
df = amplpy.DataFrame(('I','J'), 'c')
df.setValues({(I,J): poids[(len(set_K))*i+j]
            for i, J in enumerate(set_K)
            for j, I in enumerate(set_K)})
ampl.setData(df)
ampl.solve()

X = ampl.getVariable('X')
X_val = X.getValues()

Y = ampl.getVariable('Y')
Y_val = Y.getValues()
print(X_val, Y_val)
