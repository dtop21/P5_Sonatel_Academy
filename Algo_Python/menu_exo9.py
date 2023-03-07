from exo91 import *
mat = []

print(15*' ', "Menu", 15*' ')
print("1.Saisi operateurs et clients")
print("2.Afficher les clients de la matrice par opérateurs")
print("3.Afficher les clients d’un opérateur")
print("4.Afficher les numéros téléphone d’un client")
print("5.Modifier ou ajouter un numero telephone pour un client")
print("6.Sortir")

choix = int(input("Choissisez un menu : "))

while choix in [1, 2, 3, 4, 5]:
    if choix == 1:
        saisi(mat)
    elif choix == 2:
        affichage_complet(mat)
    elif choix == 3:
        x = input("donner l'operateur : ")
        affiche_client(x, mat)
    elif choix == 4:
        prenom = input("Donner le prenom : ")
        nom = input("Donner le nom : ")
        affiche_numero(prenom, nom, mat)
    elif choix == 5:
        prenom = input("Donner le prenom : ")
        nom = input("Donner le nom : ")
        modifier_numero(prenom, nom, mat)

    print(15*' ', "Menu", 15*' ')
    print("1.Saisi operateurs et clients")
    print("2.Afficher les clients de la matrice par opérateurs")
    print("3.Afficher les clients d’un opérateur")
    print("4.Afficher les numéros téléphone d’un client")
    print("5.Modifier ou ajouter un numero telephone pour un client")
    print("6.Sortir")

    choix = int(input("Choissisez un menu : "))

if choix == 6:
    exit()
