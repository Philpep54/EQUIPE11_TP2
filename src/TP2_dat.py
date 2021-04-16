import amplpy
from data import model, emplacement_AMPL
import os

class Solver:

    def __init__(self, n, m, d, L, lon_u, lar_u, set_K, lon, poids):

        self.n = n
        self.m = m
        self.d = d
        self.L = L
        self.lon_u = lon_u
        self.lar_u = lar_u
        self.set_K = set_K
        self.lon = lon
        self.poids = poids

    def solve(self):

        # ampl_path => L'emplacement de AMPL et nos dossiers .mod
        # ampl_env => l'environnement AMPL dans Python
        # ampl => notre traducteur, permet de lire les models

        # model et emplacement_AMPL se trouv dans data.py

        ampl_env = amplpy.Environment()
        ampl_path = os.path.normpath(emplacement_AMPL)
        ampl_env = amplpy.Environment(ampl_path)
        ampl = amplpy.AMPL(ampl_env)

        #--------------------Configuration--------------------#

        ampl.setOption('solver', 'gurobi')

        #-------------------Lecture du .mod-------------------#

        model_dir = os.path.normpath(emplacement_AMPL)
        ampl.read(os.path.join(model_dir, model))

        #----------------------Paramètre----------------------#

        """ Param n: Nombre de département """
        df = ampl.getParameter('n')
        df.set(self.n)

        """ Param m: Nombre maximal de rangée """
        df = ampl.getParameter('m')
        df.set(self.m)

        """ Param d: Largeur des rangées """
        df = ampl.getParameter('d')
        df.set(self.d)

        """ Param L: Somme des longueurs de tous les département """
        df = ampl.getParameter('L')
        df.set(self.L)

        """ Param Lon_u: Longueur MAX de l'usine """
        df = ampl.getParameter('Lon_u')
        df.set(self.lon_u)

        """ Param Lar_u: Largeur MAX de l'usine """
        df = ampl.getParameter('Lar_u')
        df.set(self.lar_u)

        """ Set K: Ensemble des département """
        df = amplpy.DataFrame('K')
        df.setColumn('K', self.set_K)
        ampl.setData(df, 'K')

        """ Param lon: Longueur du département k """
        df = amplpy.DataFrame("K", "lon")
        df.setValues({I: self.lon[i]
                        for i, I in enumerate(self.set_K)})
        ampl.setData(df)

        """ Param c: Coût du déplacement de i => j """
        df = amplpy.DataFrame(('I','J'), 'c')
        df.setValues({(I,J): self.poids[(len(self.set_K))*i+j]
                    for i, I in enumerate(self.set_K)
                    for j, J in enumerate(self.set_K)})
        ampl.setData(df)
        ampl.solve()

        #----------------------Variables----------------------#

        """ Var X: Position horizontale du département i """
        X = ampl.getVariable('X')
        X_val = X.getValues()
        X_val_dic = X_val.toDict()

        """ Var Y: Position verticale du département i """
        Y = ampl.getVariable('Y')
        Y_val = Y.getValues()
        Y_val_dic = Y_val.toDict()

        """ Var Aij: Position relative; =1 si i est dans 
            la même rangée à la gauche de j, 0 sinon """
        A = ampl.getVariable('Aij')
        A_val = A.getValues()
        A_val_dic = A_val.toDict()

        """ Var Bij: Position relative; =1 si i et j ne sont pas dans 
            la même rangée et que i est en dessous de j, 0 sinon """
        B = ampl.getVariable('Bij')
        B_val = B.getValues()
        B_val_dic = B_val.toDict()

        """ Var dx: Distance horizontale entre i et j """
        dx = ampl.getVariable('dx')
        dx_val = dx.getValues()
        dx_val_dic = dx_val.toDict()

        """ Var dy: Distance verticale entre i et j """
        dy = ampl.getVariable('dy')
        dy_val = dy.getValues()
        dy_val_dic = dy_val.toDict()

        return (X_val_dic, Y_val_dic, A_val_dic, B_val_dic, dx_val_dic, dy_val_dic,
                X_val, Y_val, A_val, B_val, dx_val, dy_val, model)


