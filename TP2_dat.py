import amplpy
import os

class Solver:

    def __init__(self, set_k, larg_on, poids):

        self.set_K = set_k
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
        ampl.read(os.path.join(model_dir, 'TP2_mod1.mod'))

        #----------------------Paramètre----------------------#

        """ Paramètre n """
        df = ampl.getParameter('n')
        df.set(6)

        """ Paramètre m """
        df = ampl.getParameter('m')
        df.set(3)

        """ Paramètre d """
        df = ampl.getParameter('d')
        df.set(12)

        """ Paramètre L """
        df = ampl.getParameter('L')
        df.set(27)

        """ Paramètre Lon_u """
        df = ampl.getParameter('Lon_u')
        df.set(24)

        """ Paramètre Lar_u """
        df = ampl.getParameter('Lar_u')
        df.set(60)

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
                X_val, Y_val, A_val, B_val, dx_val, dy_val)


