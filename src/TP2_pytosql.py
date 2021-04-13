import sqlite3
import TP2_dat

n = 6
m = 3
d = 12
L = 27
lon_u = 24
lar_u = 60
set_K = [1,2,3,4,5,6]
larg_on = [4,3,5,4,6,5]
poids = [0,4,5,2,3,6,4,0,4,3,5,3,5,4,0,4,7,8,2,3,4,0,3,3,3,5,7,3,0,5,6,3,8,3,5,0]

simulation1 = TP2_dat.Solver(n, m, d, L, lon_u, lar_u, set_K, larg_on, poids)

list_data = simulation1.solve()

x = list_data[0]
X = str(x)

y = list_data[1]
Y = str(y)

aij = list_data[2]
Aij = str(aij)

bij = list_data[3]
Bij = str(bij)

dx = list_data[4]
Dx = str(dx)

dy = list_data[5]
Dy = str(y)

bd_data = [X, Y, Aij, Bij, Dx, Dy]


connexion = sqlite3.connect('/Users/phillipepepin/Documents/UL_2020-2021/Hiver 2021/Environnement de développement de SIAD/SIAD_TP2/TP2_db.db')

cursor = connexion.cursor()

requete = ('''INSERT INTO configs (X, Y, Aij, Bij, dx, dy)
            VALUES (?, ?, ?, ?, ?, ?)''')

cursor.execute(requete, (bd_data))
cursor.execute("COMMIT")
cursor.close()

list_of_dict = []
list_of_dict = [{}, {}, {}, {}, {}, {}]

