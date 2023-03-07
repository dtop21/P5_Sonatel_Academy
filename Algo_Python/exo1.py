t1 = ['Janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet  ','Aout  ','Septembre','Octobre','Novembre','Decembre']
t2 = ['January','February','March  ','April','May  ','Jun  ','July  ','August','September','October','November','December']
i = 0 
j = 0
booleen = True

while(booleen) :
    print("1. Mois en francais")
    print("2. Mois en anglais")
    print("3. Quitter")

    choix = int(input("Entrer votre choix : " ))

    print("\n")
    
    if(choix == 1 or choix == 2 or choix == 3) :
        booleen =False


if choix == 1 or choix == 2 : 
    if choix == 1 :
        t = t1
    else :
        t = t2
        
    for j in range(3) :
            for i in range(j,12,3) :
                if len(t[i]) < 10 :
                    t[i] += (10 - len(t[i])) * ' '
                print(t[i],end=' | ')
            print("\n")

else :
    exit()