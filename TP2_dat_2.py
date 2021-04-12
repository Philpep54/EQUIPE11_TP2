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

set_I = [1,2,3,4,5,6]

set_J = [0,4,5,9,2,6,4,0,4,3,5,3,5,4,0,4,7,8,2,3,4,0,3,3,3,5,7,3,0,5,6,3,8,3,5,0]

C = []
for i in range(len(set_I)):
    for j in range(len(set_I)):
        C.append([set_I[j], set_I[i], set_J[(len(set_I))*i+j]])



print(C)


