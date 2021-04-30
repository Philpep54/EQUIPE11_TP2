
########################################################################
""" 
    Tout les données initiales du problème de même que les emplacements 
    sont créée ici et sont appeler dans les différent script du SIAD 
"""
########################################################################


#-----------------------Emplacement-----------------------#

model = 'TP2_mod1.mod'

emplacement_AMPL = '/Applications/Document/ULaval/AMPL/ampl_macos64'

emplacement_DB = '/Users/phillipepepin/Documents/UL_2020-2021/Hiver 2021/Environnement de développement de SIAD/EQUIPE11_TP2/TP2_db.db'

#-------------------------Données-------------------------#

""" Explication des paramètres et des variables dans TP2_dat.py
    et lors de l'affichage de variables en Array dans TP2_Affichage.py """

cd = 3

n = 6

m = 3

d = 12

lon = [4,3,5,4,6,5,3,8]

L = sum(lon)

lon_u = 24

lar_u = 60

set_K = [1,2,3,4,5,6,7,8]

Xa = [4,3,5,4,6,5,3,8]

Ya = [4,3,5,4,6,5,3,8]

poids = [0,4,5,2,3,6,6,6,4,0,4,3,5,3,3,3,5,4,0,4,7,8,3,3,2,3,4,0,3,3,3,3,3,5,7,3,0,5,5,5,6,3,8,3,5,0,0,0,6,3,8,3,5,0,0,0,6,3,8,3,5,0,0,0]
