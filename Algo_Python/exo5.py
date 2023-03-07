mat = []

b = '\033[0;34m' + 'B' + '\033[0m'
r = '\033[0;31m' + 'R' + '\033[0m'

choix_couleur = input("choisir une couleur : ")
choix_position = input("choisir la position : ")
ord = int(input("Donner l'ordre de la matrice"))

for i in range(ord):
    lign = []
    for j in range(ord):
        if choix_position == 'haut' and i < j :
            if choix_couleur == 'bleu':
                lign.append(b)
            else:
                lign.append(r)
        elif choix_position == 'bas' and i > j :
            if choix_couleur == 'bleu':
                lign.append(b)
            else:
                lign.append(r)
        else:
            lign+= '0'
    mat.append(lign)

for lign in mat :
    for l in lign :
        print(l,end=(5*' '))
    print("\n")