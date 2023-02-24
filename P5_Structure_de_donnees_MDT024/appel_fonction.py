from fonction import *
 
format = input("Donner le format du fichier (CSV,JSON ou XML) : ")

tab = format_fichier(format)
tab = format_date(tab)
tab = format_classe(tab)
tab = controle_numero(tab)
tab = controle_prenom(tab)
tab = controle_nom(tab)
tab = calcul_moyenne(tab)

