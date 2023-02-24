from appel_fonction import *
from fonction import *


print(28*'*',"MENU",28*'*')
print("* 1.Afficher les informations (Valide ou invalide ) au choix * ")
print("* 2.Afficher une information (par son numéro)                * ")
print("* 3.Afficher les cinq premiers                               * ")
print("* 4.Ajouter une information                                  * ")
print("* 5.Modifier une information invalide                        * ")
print("* 6.Afficher par 5 lignes                                    * ")
print("* 7.Afficher le nombre de lignes choisi par l'utilisateur    * ")
print("* 8.Choix de format de sortie                                * ")
print("* 9.Sortir                                                   * ")
print(62*'*')

print("\n ")
mon_choix = int(input("Choissisez un menu : "))

while mon_choix in [1, 2, 3, 4, 5, 6, 7, 8]:
    if mon_choix == 1:
        affichage(tab)
    elif mon_choix == 2:
        numero = input("Entrer le numero que vous rechercher : ")
        affiche_info(numero,valide)
    elif mon_choix == 3:
        affiche_cinq_premiers(valideMoy)
    elif mon_choix == 6:
        choix = int(input("Donner le numero de la page a afficher : "))
        afficher_par_5(valide,choix)
    elif mon_choix == 7:
        choix = int(input("Donner le numero de la page a afficher : "))
        afficher_par_X(valide,choix)
    elif mon_choix == 8:
        format_sortie(format)
    print("\n ")                                                    
    print(28*'*',"MENU",28*'*')
    print("* 1.Afficher les informations (Valide ou invalide ) au choix * ")
    print("* 2.Afficher une information (par son numéro)                * ")
    print("* 3.Afficher les cinq premiers                               * ")
    print("* 4.Ajouter une information                                  * ")
    print("* 5.Modifier une information invalide                        * ")
    print("* 6.Afficher par 5 lignes                                    * ")
    print("* 7.Afficher le nombre de lignes choisi par l'utilisateur    * ")
    print("* 8.Choix de format de sortie                                * ")
    print("* 9.Sortir                                                   * ")
    print(62*'*')

    print("\n ")     
    mon_choix = int(input("Choissisez un menu : "))

if mon_choix == 9:
    exit()