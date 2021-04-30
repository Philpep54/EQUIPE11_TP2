
##########################################################
"""
    Le script main.py sert à afficher le résultat issue
    de TP2_affichage dans le terminal et publie ceux-ci
    dans la base de données à l'aide de TP2_pytosql
"""
##########################################################


from data import *
from TP2_pytosql import requete, bd_data, cursor
from TP2_Affichage import pr_ar


#########################################################
#   S'assurer d'initialiser la base de données dans     #
#   TP2_BD avant de publier le résultat dans celle-ci   #
#                                                       #
#   Choisir le model entre:     TP2_mod1.mod            #
#                               TP2_mod2.mod            #
#                               TP2_mod3.mod            #
#                                                       #         
#   Situé dans le fichier data.py                       #
#########################################################

#########################################################
#   Si une erreur du genre survient lors de             #
#   l'exécution du script dans VSCode:                  #
#       reportMissingImports                            #
#                                                       #
#   S'assurer d'avoir dans votre settings.json les      #
#   réglages suivant:                                   #
#                                                       #
#   "python.languageServer": "Pylance"                  #
#                                                       #
#   "python.analysis.diagnosticSeverityOverrides": {    #
#       "reportMissingImports": "none"                  #
#########################################################


""" Afficher le résultat dans le terminal """
pr_ar()

""" Publier les résultat dans la base de données """
cursor.execute(requete, (bd_data))
cursor.execute("COMMIT")
cursor.close()
