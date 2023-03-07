mat = []
ligne = []
position = ['ADDP', 'EDDP', 'SDP', 'ADDS', 'EDDS', 'SDS']
couleur = ['bleu', 'rouge']

choix_couleur = str(input("Choisissez une couleur. Bleu ou Rouge : "))

while choix_couleur not in couleur:
    choix_couleur = str(input("Choisissez une couleur. Bleu ou Rouge : "))

choix_position = str(input("Choisissez une position. haut ou bas : "))

while choix_position not in position:
    choix_position = str(input("Choisissez une position : "))

ord = int(input("Donner l'ordre de la matrice : "))

while ord < 4:
    ord = int(input("Donner l'ordre de la matrice : "))

b = '\033[0;34m' + 'B' + '\033[0m'
r = '\033[0;31m' + 'R' + '\033[0m'

for i in range((ord)):
    for j in range((ord)):
        if i+j <= ord-2 and choix_position == "ADDS":
            if choix_couleur == "bleu":
                ligne.append(b)
            elif choix_couleur == "rouge":
                ligne.append(r)
        elif i+j >= ord and choix_position == "EDDS":
            if choix_couleur == "bleu":
                ligne.append(b)
            elif choix_couleur == "rouge":
                ligne.append(r)
        elif i < j and choix_position == "ADDP":
            if choix_couleur == "bleu":
                ligne.append(b)
            else:
                ligne.append(r)
        elif i > j and choix_position == "EDDP":
            if choix_couleur == "bleu":
                ligne.append(b)
            elif choix_couleur == "rouge":
                ligne.append(r)
        elif i + j == ord-1 and choix_position == "SDS":
            if choix_couleur == "bleu":
                ligne.append(b)
            elif choix_couleur == "rouge":
                ligne.append(r)
        elif i == j and choix_position == "SDP":
            if choix_couleur == "bleu":
                ligne.append(b)
            elif choix_couleur == "rouge":
                ligne.append(r)
        else:
            ligne.append("*")

    mat.append(ligne)
    ligne = []

for m in mat:
    for i in range(ord):
        print(m[i], end=(5*' '))
    print('\n')
