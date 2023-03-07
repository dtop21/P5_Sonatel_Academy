def saisi(mat):
    nb_operateurs = int(
        input("Donner le nombre d'opérateurs : "))
    for i in range(nb_operateurs):
        operateur = input("Saisir un opérateur : ")
        mat.append(operateur)

    nb_clients = int(input("Donner le nombre de clients : "))
    for i in range(nb_clients):
        nom = input("le nom du client : ")
        prenom = input("le prénom du client : ")
        numero = input("le numéro de téléphone du client : ")
        booleen = controle_numero(numero)
        while booleen == False:
            numero = input("Veuillez saisir un bon numero : ")
            booleen = controle_numero(numero)
        mat.append([nom, prenom, numero])


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


def affichage_complet(mat):
    for op in mat:
        if op == 'orange':
            print(op)
            for cl in mat:
                for j in cl:
                    if len(j) == 9 and j[0] == '7' and j[1] == '7':
                        for i in range(len(cl)):
                            print(cl[i], end=(5*' '))
                        print("\n")
        elif op == 'tigo':
            print(op)
            for cl in mat:
                for j in cl:
                    if len(j) == 9 and j[0] == '7' and j[1] == '6':
                        for i in range(len(cl)):
                            print(cl[i], end=(5*' '))
                        print("\n")
        elif op == 'expresso':
            print(op)
            for cl in mat:
                for j in cl:
                    if len(j) == 9 and j[0] == '7' and j[1] == '0':
                        for i in range(len(cl)):
                            print(cl[i], end=(5*' '))
                        print("\n")


def affiche_client(x, mat):
    print(x)
    if x == 'orange':
        for cl in mat:
            for j in cl:
                if len(j) == 9 and j[0] == '7' and j[1] == '7':
                    for i in range(len(cl)):
                        print(cl[i], end=(5*' '))
                    print("\n")
    elif x == 'tigo':
        for cl in mat:
            for j in cl:
                if len(j) == 9 and j[0] == '7' and j[1] == '6':
                    for i in range(len(cl)):
                        print(cl[i], end=(5*' '))
                    print("\n")
    elif x == 'expresso':
        for cl in mat:
            for j in cl:
                if len(j) == 9 and j[0] == '7' and j[1] == '0':
                    for i in range(len(cl)):
                        print(cl[i], end=(5*' '))
                    print("\n")


def affiche_numero(prenom, nom, mat):
    print("les numeros de : ", prenom, " ", nom)
    for cl in mat:
        if prenom in cl and nom in cl:
            print(cl[2], end=' ')
    print("\n")


def modifier_numero(prenom, nom, mat):
    choix = input("Voulez-vous modifier ou ajouter un numero : ")
    if choix == 'ajouter':
        nom = nom
        prenom = prenom
        numero = input("Ajout numero pour le client : ")
        booleen = controle_numero(numero)
        while booleen == False:
            numero = input("Veuillez saisir un bon numero : ")
            booleen = controle_numero(numero)
        mat.append([nom, prenom, numero])
    else:
        i = 0
        for cl in mat:
            if prenom in cl and nom in cl and i < 1:
                numero = input("Entrer le nouveau numero pour le client : ")
                booleen = controle_numero(numero)
                while booleen == False:
                    numero = input("Veuillez saisir un bon numero : ")
                    booleen = controle_numero(numero)
                cl[2] = numero
                i += 1
            elif prenom in cl and nom in cl and i >= 1:
                choix = input("Voulez-vous modifier l'autre numero O/N : ")
                if choix == 'O':
                    numero = input(
                        "Entrer le nouveau numero pour le client : ")
                    booleen = controle_numero(numero)
                    while booleen == False:
                        numero = input("Veuillez saisir un bon numero : ")
                        booleen = controle_numero(numero)
                    cl[2] = numero
                    i += 1
                else:
                    break
