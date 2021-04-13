import sqlite3
import os
import numpy as np

db_path = os.path.normpath('/Users/phillipepepin/Documents/UL_2020-2021/Hiver 2021/Environnement de développement de SIAD/SIAD_TP2/TP2_db.db')
c = sqlite3.connect(db_path)

#Create Table
c.execute('''CREATE TABLE configs
            (X TEXT,
            Y TEXT,
            Aij TEXT,
            Bij TEXT,
            dx TEXT,
            dy TEXT)''')