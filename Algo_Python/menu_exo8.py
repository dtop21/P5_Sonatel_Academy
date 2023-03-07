from exo8 import *

tab = [['Prenom', 'Nom', 'Telephone', 'Classe',
        'Devoir', 'Projet', 'Examen', 'Moyenne']]

print(15*' ', "Menu", 15*' ')
print("1.Ajouter")
print("2.Afficher")
print("3.Trier")
print("4.Rechercher")
print("5.Modifier")
print("6.Sortir")

choix = int(input("Choissisez un menu : "))

while choix in [1, 2, 3, 4, 5]:
    if choix == 1:
        saisi(tab)
    elif choix == 2:
        affiche(tab)
    elif choix == 3:
        trier(tab)
    elif choix == 4:
        x = input("recherche : ")
        recherche(x, tab)
    elif choix == 5:
        x = input("recherche : ")
        modif_note(x, tab)

    print(15*' ', "Menu", 15*' ')
    print("1.Ajouter")
    print("2.Afficher")
    print("3.Trier")
    print("4.Rechercher")
    print("5.Modifier")
    print("6.Sortir")

    choix = int(input("Choissisez un menu : "))

if choix == 6:
    exit()
