import amplpy
import os

class Solver:

    def __init__(self, n, m, d, L, lon_u, lar_u, set_K, larg_on, poids):

        self.n = n
        self.m = m
        self.d = d
        self.L = L
        self.lon_u = lon_u
        self.lar_u = lar_u
        self.set_K = set_K
        self.larg_on = larg_on
        self.poids = poids

    def solve(self):

        # ampl_path => L'emplacement de AMPL et nos dossiers .mod
        # ampl_env => l'environnement AMPL dans Python
        # ampl => notre traducteur, permet de lire les models

        ampl_env = amplpy.Environment()
        ampl_path = os.path.normpath('/Applications/Document/ULaval/AMPL/ampl_macos64')
        ampl_env = amplpy.Environment(ampl_path)
        ampl = amplpy.AMPL(ampl_env)

        #--------------------Configuration--------------------#

        ampl.setOption('solver', 'gurobi')

        #-------------------Lecture du .mod-------------------#

        model_dir = os.path.normpath('/Applications/Document/ULaval/AMPL/ampl_macos64')
        model = 'TP2_mod2.mod'
        ampl.read(os.path.join(model_dir, model))

        #----------------------Paramètre----------------------#

        """ Paramètre n """
        df = ampl.getParameter('n')
        df.set(self.n)

        """ Paramètre m """
        df = ampl.getParameter('m')
        df.set(self.m)

        """ Paramètre d """
        df = ampl.getParameter('d')
        df.set(self.d)

        """ Paramètre L """
        df = ampl.getParameter('L')
        df.set(self.L)

        """ Paramètre Lon_u """
        df = ampl.getParameter('Lon_u')
        df.set(self.lon_u)

        """ Paramètre Lar_u """
        df = ampl.getParameter('Lar_u')
        df.set(self.lar_u)

        """ Set K """
        df = amplpy.DataFrame('K')
        df.setColumn('K', self.set_K)
        ampl.setData(df, 'K')

        """ Paramètre lon """
        df = amplpy.DataFrame("K", "lon")
        df.setValues({I: self.larg_on[i]
                        for i, I in enumerate(self.set_K)})
        ampl.setData(df)

        """ Paramètre c """
        df = amplpy.DataFrame(('I','J'), 'c')
        df.setValues({(I,J): self.poids[(len(self.set_K))*i+j]
                    for i, J in enumerate(self.set_K)
                    for j, I in enumerate(self.set_K)})
        ampl.setData(df)
        ampl.solve()

        #----------------------Affichage----------------------#

        X = ampl.getVariable('X')
        X_val = X.getValues()
        X_val_dic = X_val.toDict()

        Y = ampl.getVariable('Y')
        Y_val = Y.getValues()
        Y_val_dic = Y_val.toDict()

        A = ampl.getVariable('Aij')
        A_val = A.getValues()
        A_val_dic = A_val.toDict()

        B = ampl.getVariable('Bij')
        B_val = B.getValues()
        B_val_dic = B_val.toDict()

        dx = ampl.getVariable('dx')
        dx_val = dx.getValues()
        dx_val_dic = dx_val.toDict()

        dy = ampl.getVariable('dy')
        dy_val = dy.getValues()
        dy_val_dic = dy_val.toDict()

        return (X_val_dic, Y_val_dic, A_val_dic, B_val_dic, dx_val_dic, dy_val_dic,
                X_val, Y_val, A_val, B_val, dx_val, dy_val, model)


