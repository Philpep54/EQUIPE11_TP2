import sqlite3
import os
from data import emplacement_DB
import numpy as np

db_path = os.path.normpath(emplacement_DB)
c = sqlite3.connect(db_path)

#Create Table
c.execute('''CREATE TABLE configs
            (X TEXT,
            Y TEXT,
            Aij TEXT,
            Bij TEXT,
            dx TEXT,
            dy TEXT,
            ddx TEXT,
            ddy TEXT)''')

