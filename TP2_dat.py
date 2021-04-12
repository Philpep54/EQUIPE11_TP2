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
ampl.setOption('cplex_options', 'timelim 600 outlev 1')

#-------------------Lecture du .mod-------------------#

model_dir = os.path.normpath('/Applications/Document/ULaval/AMPL/ampl_macos64')
ampl.read(os.path.join(model_dir, 'TP2_mod1.mod'))

#----------------------Paramètre----------------------#

df = ampl.getParameter('n')
df.set(6)

df = ampl.getParameter('m')
df.set(3)

df = ampl.getParameter('d')
df.set(12)

df = ampl.getParameter('L')
df.set(27)

df = ampl.getParameter('Lu')
df.set(24)

set_I = [1,2,3,4,5,6]
df = amplpy.DataFrame('I')
df.setColumn('I', set_I)
ampl.setData(df, 'I')

set_J = [1,2,3,4,5,6]
df = amplpy.DataFrame('J')
df.setColumn('J', set_J)
ampl.setData(df, 'J')

set_K = [1,2,3,4,5,6]
df = amplpy.DataFrame('K')
df.setColumn('K', set_K)
ampl.setData(df, 'K')

c = []
poids = [0,4,5,9,2,6,4,0,4,3,5,3,5,4,0,4,7,8,2,3,4,0,3,3,3,5,7,3,0,5,6,3,8,3,5,0]
for i in range(len(set_I)):
    for j in range(len(set_I)):
        c.append([set_I[j], set_I[i], poids[(len(set_I))*i+j]])

df = ampl.getParameter('c')
df.set(c)


for i in c:
    print(i)


