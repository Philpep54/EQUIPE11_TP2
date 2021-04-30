
####################################################
""" 
    Ici on initiallise notre base de données à son 
    emplacement qu'on récupère du script data.py 
"""
####################################################


import sqlite3
import os
from data import emplacement_DB


#-----------------------Emplacement-----------------------#
db_path = os.path.normpath(emplacement_DB)
c = sqlite3.connect(db_path)


#-------------------------Création------------------------#
c.execute('''CREATE TABLE configs
            (X TEXT,
            Y TEXT,
            Aij TEXT,
            Bij TEXT,
            dx TEXT,
            dy TEXT,
            ddx TEXT,
            ddy TEXT)''')

