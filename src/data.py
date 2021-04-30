
##########################################################################
""" 
    Tout les données initiales du problème de même que les emplacements 
    sont créée ici et sont appeler dans les différent script du SIAD 
"""
##########################################################################


#-----------------------Emplacement-----------------------#

model = 'TP2_mod1.mod'

emplacement_AMPL = 'C:/ampl_mswin64'

emplacement_DB = './EQUIPE11_TP2/TP2_db.db'

#-------------------------Données-------------------------#

""" Explication des paramètres et des variables dans TP2_dat.py
    et lors de l'affichage de variables en Array dans TP2_Affichage.py """

cd = 5

n = 8

m = 3

d = 6

lon = [30,5,9,12,12,9,2,11]

L = sum(lon)

lon_u = 43

lar_u = 18

set_K = [1,2,3,4,5,6,7,8]

Xa = [5,41,35,19,33,23,16,14]

Ya = [8,8,4,4,8,8,12,8]

poids = [0,8,6,7,7,3,0,2,8,0,8,7,7,3,0,2,6,8,0,8,8,7,0,0,7,7,8,0,0,9,0,10,7,7,8,0,0,7,0,10,3,3,7,9,7,0,0,10,0,0,0,0,0,0,0,10,2,2,0,10,10,10,10,0]