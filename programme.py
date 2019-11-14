import xlrd
import matplotlib.pyplot as plt
document = xlrd.open_workbook("statistiques.xls")
print("Nombre de feuilles: "+str(document.nsheets))
print("Noms des feuilles: "+str(document.sheet_names()))
 
feuille_1 = document.sheet_by_index(0)
feuille_1 = document.sheet_by_name("Données")
 
print("Format de la feuille 1:")
print("Nom: "+str(feuille_1.name))
print("Nombre de lignes: "+str(feuille_1.nrows))
print("Nombre de colonnes: "+str(feuille_1.ncols))
 
cols = feuille_1.ncols
rows = feuille_1.nrows
 
X = []
Y= []
 
for r in range(1, rows):
    X += [feuille_1.cell_value(rowx=r, colx=0)]
    Y += [feuille_1.cell_value(rowx=r, colx=1)]
 
plt.plot(X, Y)
plt.show()