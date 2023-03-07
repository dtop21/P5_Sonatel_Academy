def saisi(tab):
    tel = input("Numero telephone : ")
    booleen = controle_numero(tel)
    while booleen == False:
        tel = input("Veuillez saisir un bon numero : ")
        booleen = controle_numero(tel)
    nom = input("Nom : ")
    prenom = input("Prenom : ")
    classe = input("Classe : ")
    devoir = float(input("Note de devoir : "))
    while devoir < 0 or devoir > 20:
        devoir = float(input("Veuillez saisir une bonne note : "))
    projet = float(input("Note de projet : "))
    while projet < 0 or projet > 20:
        projet = float(input("Veuillez saisir une bonne note : "))
    examen = float(input("Note d'examen : "))
    while examen < 0 or examen > 20:
        examen = float(input("Veuillez saisir une bonne note : "))
    moyenne = round(calcul_moyenne(devoir, projet, examen), 2)

    tab.append([prenom, nom, tel, classe, devoir, projet, examen, moyenne])
    choix = input("Desirez-vous continuer O/N : ")

    while choix == 'O':
        tel = input("Numero telephone : ")
        booleen = controle_numero(tel)
        while booleen == False:
            tel = input("Veuillez saisir un bon numero : ")
            booleen = controle_numero(tel)
        nom = input("Nom : ")
        prenom = input("Prenom : ")
        classe = input("Classe : ")
        devoir = float(input("Note de devoir : "))
        while devoir < 0 or devoir > 20:
            devoir = float(input("Veuillez saisir une bonne note : "))
        projet = float(input("Note de projet : "))
        while projet < 0 or projet > 20:
            projet = float(input("Veuillez saisir une bonne note : "))
        examen = float(input("Note d'examen : "))
        while examen < 0 or examen > 20:
            examen = float(input("Veuillez saisir une bonne note : "))
        moyenne = round(calcul_moyenne(devoir, projet, examen), 2)

        tab.append([prenom, nom, tel, classe, devoir, projet, examen, moyenne])
        choix = input("Desirez-vous continuer O/N : ")


def controle_numero(x):
    chiffre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    commencement = ['0', '5', '6', '7', '8']
    numeros = []
    chaine = ''

    for i in range(len(x)):
        if x[i] in chiffre:
            chaine += x[i]

    numeros.append(chaine)

    for numero in numeros:
        if len(numero) > 9 or len(numero) < 9 or numero[0] != '7' or numero[1] not in commencement:
            return False
        else:
            return True


def calcul_moyenne(x, y, z):
    moyenne = (x+y+z) / 3
    return moyenne


def affiche(tab):
    print(120 * '*')
    for etudiant in tab:
        for j in range(len(etudiant)):
            print("| ", etudiant[j], end=(
                12 - len(str(etudiant[j]))) * ' ')
        print('\n')
    print(120 * '*')


def recherche(x, tab):
    booleen = False
    for etudiant in tab:
        if x in etudiant:
            booleen = True
            for j in range(len(etudiant)):
                print("| ", etudiant[j], end=(
                    12 - len(str(etudiant[j]))) * ' ')
            print('\n')
    if booleen == False:
        print("l'etudiant n'est pas sur la liste")


def modif_note(x, tab):
    booleen = False
    for etudiant in tab:
        if x == etudiant[2]:
            booleen = True
            devoir = float(input("Note de devoir : "))
            while devoir < 0 or devoir > 20:
                devoir = float(input("Veuillez saisir une bonne note : "))
            projet = float(input("Note de projet : "))
            while projet < 0 or projet > 20:
                projet = float(input("Veuillez saisir une bonne note : "))
            examen = float(input("Note d'examen : "))
            while examen < 0 or examen > 20:
                examen = float(input("Veuillez saisir une bonne note : "))
            moyenne = round(calcul_moyenne(devoir, projet, examen), 2)
            etudiant[4] = devoir
            etudiant[5] = projet
            etudiant[6] = examen
            etudiant[7] = moyenne
            for j in range(len(etudiant)):
                print("| ", etudiant[j], end=(
                    12 - len(str(etudiant[j]))) * ' ')
            print('\n')
    if booleen == False:
        print("le numero que vous avez donné n'est pas sur la liste")


def trier(tab):
    for i in range(2, len(tab)):
        k = tab[i]
        j = i-1
        a = tab[j]
        m = k[len(k)-1]
        n = a[len(a)-1]
        while j >= 1 and m > n:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = k
    print("le tableau trié  \n")
    affiche(tab)
