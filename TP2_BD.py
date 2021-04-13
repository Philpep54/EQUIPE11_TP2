import sqlite3
import os
import numpy as np

db_path = os.path.normpath('./qc_configs.sqlite')
c = sqlite3.connect(db_path)

#Create Table
c.execute('''CREATE TABLE configs
            (X TEXT,
            Y TEXT,
            Aij TEXT,
            Bij TEXT,
            dx TEXT,
            dy TEXT)''')