import csv,json,xml.etree.ElementTree as ET

t1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
t2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
chiffre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

valide = []
invalide = []
valideMoy = []

def format_fichier(format):
    tab = []
    if format == 'CSV':
        with open('Donnees_Projet_Python_DataC5.csv', encoding='UTF-8') as mon_fichier:
            mon_fichier_reader = csv.reader(mon_fichier, delimiter=',')
            for row in mon_fichier_reader:
                tab.append(row)
                
    elif format == 'JSON':
        with open('Donnees_Projet_Python_DataC5.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                tab.append(row)
        with open('Donnees_Projet_Python_DataC5.json', 'w') as jsonfile:
            json.dump(tab, jsonfile)
    elif format == 'XML':
        with open('Donnees_Projet_Python_DataC5.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                tab.append(row)
        eleves = ET.Element("eleves")
        for x in tab:
            eleve = ET.SubElement(eleves, "eleve") 
            numero = ET.SubElement(eleve, "numero")
            numero.text = x[1] 
            nom = ET.SubElement(eleve,"nom")
            nom.text = x[2]
            prenom = ET.SubElement(eleve,"prenom")
            prenom.text = x[3]
            date_naiss = ET.SubElement(eleve,"date_naiss")
            date_naiss.text = x[4]
            classe = ET.SubElement(eleve,"classe")
            classe.text = x[5]
            note = ET.SubElement(eleve,"note")
            note.text = x[6]
            
        tree = ET.ElementTree(eleves)
        tree.write("Donnees_Projet_Python_DataC5.xml",encoding="UTF-8", xml_declaration=True)
    else:
        print("Enter un bon format (CSV, JSON ou XML)")
        return None
    
    return tab

def format_classe(tab):
    valideC = []
    ch = ''
    for x in tab:
        for y in x[5]:
            if y in t1 or y in t2 or y in chiffre:
                ch += y
        x[5] = ch
        ch = ''
        if len(x[5]) >= 2:
            if (x[5][-1] == 'a' or x[5][-1] == 'A') and x[5][0] in chiffre[3:7]:
                x[5] = x[5][0] + 'em' + 'A'
                valideC.append(x)
            elif (x[5][-1] == 'b' or x[5][-1] == 'B') and x[5][0] in chiffre[3:7]:
                x[5] = x[5][0] + 'em' + 'B'
                valideC.append(x)
            else:
                invalide.append(x)
        else:
            invalide.append(x)
            
    return valideC

def format_date(tab):
    valideD =[]
    t = []
    ch = ''
    for x in tab:
        for y in x[4]:
            if (y not in chiffre and y not in t1 and y not in [' ','/','-','|',',',':','.','_']) or x[4][0] in t1 :
                invalide.append(x)
                break
    for x in tab:
        if x not in invalide:
            t.append(x)
    tab = t
    t = []

    for x in tab:
        for i in range(len(x[4])):
            if x[4][i] == ' ' and x[4][i+1] == ' ' :
                continue
            else:
                ch += x[4][i]
            if ch[0] == ' ' :
                s = ch[1:len(ch)]  
                ch  = s
        x[4] = ch
        ch = ''
            
    for x in tab:
        if len(x[4]) >= 7:
            if x[4][0] in chiffre and x[4][1] not in chiffre:
                x[4] = '0'+x[4][0:-1]+x[4][-1]
            if x[4][3] in chiffre and x[4][4] not in chiffre:
                x[4] = x[4][0:3]+'0'+x[4][3:-1]+x[4][-1]
            t.append(x)
        else:
            invalide.append(x)
    tab = t
    t = []
    for x in tab:
        for y in x[4]:
            if y in chiffre or y in t1:
                ch += y
        x[4] = ch
        ch = ''
    for x in tab:
        for y in x[4]:
            if y in t1:
                ch += y
        for y in x[4]:
            if y in t1 and ch in 'janvier':
                c = '01'
                x[4] = x[4][0:2] + c + x[4][4:-1] + x[4][-1]
            elif y in t1 and ch in 'fevrier':
                c = '02'
                x[4] = x[4][0:2] + c + x[4][4:-1] + x[4][-1]
            elif y in t1 and ch in 'mars':
                c = '0'
                x[4] = x[4][0:2] + c + x[4][4:-1] + x[4][-1]
            elif y in t1 and ch in 'avril':
                c = '04'
                x[4] = x[4][0:2] + c + x[4][4:-1] + x[4][-1]
            elif y in t1 and ch in 'mai':
                c = '05'
                x[4] = x[4][0:2] + c + x[4][4:-1] + x[4][-1]
            elif y in t1 and ch in 'juin':
                c = '06'
                x[4] = x[4][0:2] + c + x[4][4:-1] + x[4][-1]
            elif y in t1 and ch in 'juillet':
                c = '07'
                x[4] = x[4][0:2] + c + x[4][4:-1] + x[4][-1]
            elif y in t1 and ch in 'aout':
                c = '08'
                x[4] = x[4][0:2] + c + x[4][4:-1] + x[4][-1]
            elif y in t1 and ch in 'septembre':
                c = '09'
                x[4] = x[4][0:2] + c + x[4][4:-1] + x[4][-1]
            elif y in t1 and ch in 'octobre':
                c = '10'
                x[4] = x[4][0:2] + c + x[4][4:-1] + x[4][-1]
            elif y in t1 and ch in 'novembre':
                c = '11'
                x[4] = x[4][0:2] + c + x[4][4:-1] + x[4][-1]
            elif y in t1 and ch in 'decembre':
                c = '12'
                x[4] = x[4][0:2] + c + x[4][4:-1] + x[4][-1]
        ch = ''
    for x in tab:
        for y in x[4]:
            if y in chiffre:
                ch += y
        x[4] = ch
        ch = ''
        if len(x[4][4:-1] + x[4][-1]) == 2:
            if x[4][4:-1] + x[4][-1] <= '23':
                x[4] = x[4][0:4] + '20' + x[4][4:-1] + x[4][-1]
            else:
                x[4] = x[4][0:4] + '19' + x[4][4:-1] + x[4][-1]
    for x in tab:
        x[4] = x[4][0:2] + '-' + x[4][2:4] + '-' + x[4][4:-1] + x[4][-1]
        jour = x[4][0:2]
        mois = x[4][3:5]
        annee = int(x[4][6:-1] + x[4][-1])
    
        if mois in ['01','03','05','07','08','10','12']:
            if jour >= '01' and jour <= '31':
                valideD.append(x)
            else:
                invalide.append(x)
        elif mois in ['04','06','09','11']:
            if jour >= '01' and jour <= '30':
                valideD.append(x)
            else:
                invalide.append(x)
        elif mois == '02':
            if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0) :
                if jour >= '01' and jour <= '29':
                    valideD.append(x)
                else:
                    invalide.append(x)
            else:
                if jour >= '01' and jour <= '28':
                    valideD.append(x)
                else:
                    invalide.append(x)
        else:
            invalide.append(x)
    
    return valideD

def controle_numero(tab):
    valideN = []
    ch = ''
    for x in tab:
        if len(x[1]) == 7 :
            for y in x[1]:
                if y in t2 or y in chiffre:
                    ch += y
            if len(ch) == 7:
                for y in ch:
                    if y in t1:
                        invalide.append(x)
                        break
                if x not in invalide:
                    valideN.append(x)
            else:
                invalide.append(x)
        else:
            invalide.append(x)
        ch = ''
        
    return valideN

def controle_prenom(tab):
    valideP = []
    for x in tab:
        if (x[3][0] in t1 or x[3][0] in t2) and len(x[3]) > 3 :
            valideP.append(x)
        else:
            invalide.append(x)
            
    return valideP

def controle_nom(tab):
    valideNom = []
    for x in tab:
        if (x[2][0] in t1 or x[2][0] in t2) and len(x[2]) >= 2 :
            valideNom.append(x)
        else:
            invalide.append(x)
    
    return valideNom

def calcul_moyenne(tab):
    t = []
    for x in tab:
        if x[6][-1] != ']' and x[6][-1] != '#':
            x[6] += ']' 
    ch = ''
    for x in tab:
        for y in x[6]:
            if y != ',':
                ch += y    
            elif y == ',':
                y = '.'
                ch += y
        x[6] = ch
        ch = ''
    result = ''
    for x in tab:
        for y in x[6][-5:-1]:
            ch += y
        if ':' not in ch:
            invalide.append(x)
        ch = ''
    for x in tab:
        if x not in invalide:
            t.append(x)
    tab = t
    t = []
    for x in tab:
        if x[6][-1] == '#':
            invalide.append(x)
    for x in tab:
        if x not in invalide:
            t.append(x)
    tab = t
    t = []
    for x in tab:
        x[6] = x[6].split("#")
    for x in tab:
        if x[6][0] == '':
            invalide.append(x)
    for x in tab:
        if x not in invalide:
            t.append(x)
    tab = t
    t = []
    m = 0
    i = 0
    moy_general = 0
    for x in tab :
        for y in x[6]:
            nom_matiere = y.split("[")[0]
            devoirs = [note for note in y.split("[")[1].split(":")[0].split("|")]
            for notes in devoirs[-1]:
                if notes == ']':
                    devoirs = devoirs[0:-1]
            devoirs = [float(note) for note in devoirs]
            examen = float(y.split("[")[1].split("]")[0].split(":")[1])
            if examen < 0 or examen > 20:
                invalide.append(x)
                break
            moyenne = round((sum(devoirs) / len(devoirs) + 2 * examen) / 3,2)
            m += moyenne
            i += 1
            result +=" "+nom_matiere +" "+str(moyenne)
        moy_general = round(m / i,2)
        x[6] = result 
        valide.append(x)
        moy_general = str(moy_general)
        valideMoy.append([x,moy_general])
        result = ''
        m = 0
        i = 0

    return valide

def affichage(tab):
    choix = input("Quelles infos voulez vous afficher: valide ou invalide :")
    if choix == 'valide':
        for x in tab:
            for i in range(len(x[1:7])):
                print("|",x[1:7][i],end=(13-len(x[1:7][i]))*' ')
            print('\n')
    else:
        for x in invalide:
            for i in range(len(x[1:7])):
                print(x[1:7][i],end=(13-len(x[1:7][i]))*' ')
            print('\n')    
def affiche_info(num,tab):
    bol = False
    for x in tab:
        if num in x:
            bol = True
            print('\n')
            for i in range(len(x)):
                print(x[i],end=(15-len(x))*' ')
            print('\n')
    if bol == False:
        print("\n Le numero que vous cherchez n'est pas dans le fichier ")
    
def affiche_cinq_premiers(tab):
    tab.sort(key = lambda s:s[1] ,reverse = True)
    
    choix = (input("choissisez une classe(format : 5emA,5emB,4emA .....) : "))
    
    j = 0
    bol = False
    for x in tab :
        if choix in x[0] and j <= 4:
            bol = True
            for i in range(2):
                print(x[i],end=(150-len(str(x[i])))*' ')
            print('\n') 
            j +=1
    if bol == False :
        print("veuillez entrer une classe valide")   
        
def ajouter():
    tab = []
    code = input("Donner le code : ")
    numero = input("Donner le numero : ")
    nom = input("Donner le nom : ")
    prenom = input("Donner le prenom : ")
    date = input("Donner la date de naissance : ")
    classe = input("Donner le classe : ")
    note = input("Donner les notes : ")
    tab.append([code,numero,nom,prenom,date,classe,note])
    tab = format_date(tab)
    tab = format_classe(tab)
    tab = controle_numero(tab)
    tab = controle_prenom(tab)
    tab = controle_nom(tab)
    tab = calcul_moyenne(tab)    
    
def format_sortie(format):
    if format == 'CSV':
        choix = input("Choisissez le format de fichier pour les données valides (JSON,XML) : ")
        if choix == 'JSON':
            jsonString = json.dumps(valide)
            jsonFile = open("donnees_valides.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
            
            eleves = ET.Element("eleves")
            for x in invalide:
                eleve = ET.SubElement(eleves, "eleve") 
                numero = ET.SubElement(eleve, "numero")
                numero.text = x[1] 
                nom = ET.SubElement(eleve,"nom")
                nom.text = x[2]
                prenom = ET.SubElement(eleve,"prenom")
                prenom.text = x[3]
                date_naiss = ET.SubElement(eleve,"date_naiss")
                date_naiss.text = x[4]
                classe = ET.SubElement(eleve,"classe")
                classe.text = x[5]
                note = ET.SubElement(eleve,"note")
                note.text = x[6]
            tree = ET.ElementTree(eleves)
            tree.write("donnees_invalides.xml", encoding="UTF-8", xml_declaration=True)
            print("Le données valides sont enregistrées dans un fichier donnees_valides.JSON \net les données invalides dans un fichier donnees_invalides.XML ")
        elif choix == 'XML':
            eleves = ET.Element("eleves")
            for x in valide:
                eleve = ET.SubElement(eleves, "eleve") 
                numero = ET.SubElement(eleve, "numero")
                numero.text = x[1] 
                nom = ET.SubElement(eleve,"nom")
                nom.text = x[2]
                prenom = ET.SubElement(eleve,"prenom")
                prenom.text = x[3]
                date_naiss = ET.SubElement(eleve,"date_naiss")
                date_naiss.text = x[4]
                classe = ET.SubElement(eleve,"classe")
                classe.text = x[5]
                note = ET.SubElement(eleve,"note")
                note.text = x[6]  
            tree = ET.ElementTree(eleves)
            tree.write("donnees_valides.xml", encoding="UTF-8", xml_declaration=True)
            
            jsonString = json.dumps(invalide)
            jsonFile = open("donnees_invalides.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
            print("Le données valides sont enregistrées dans un fichier donnees_valides.XML \net les données invalides dans un fichier donnees_invalides.JSON ")
        else:
            print("Entrer un bon format ")
    elif format == 'JSON':
        choix = input("Choisissez le format de fichier pour les données valides (CSV,XML) : ")
        if choix == 'CSV':
            with open('donnees_valides.csv', 'w', newline='') as file:
                donnee = csv.writer(file,delimiter=',')
                donnee.writerows(valide)
                
            eleves = ET.Element("eleves")
            for x in invalide:
                eleve = ET.SubElement(eleves, "eleve") 
                numero = ET.SubElement(eleve, "numero")
                numero.text = x[1] 
                nom = ET.SubElement(eleve,"nom")
                nom.text = x[2]
                prenom = ET.SubElement(eleve,"prenom")
                prenom.text = x[3]
                date_naiss = ET.SubElement(eleve,"date_naiss")
                date_naiss.text = x[4]
                classe = ET.SubElement(eleve,"classe")
                classe.text = x[5]
                note = ET.SubElement(eleve,"note")
                note.text = x[6]
            tree = ET.ElementTree(eleves)
            tree.write("donnees_invalides.xml", encoding="UTF-8", xml_declaration=True)
            print("Le données valides sont enregistrées dans un fichier donnees_valides.CSV \net les données invalides dans un fichier donnees_invalides.XML ")
        elif choix == 'XML':
            eleves = ET.Element("eleves")
            for x in valide:
                eleve = ET.SubElement(eleves, "eleve") 
                numero = ET.SubElement(eleve, "numero")
                numero.text = x[1] 
                nom = ET.SubElement(eleve,"nom")
                nom.text = x[2]
                prenom = ET.SubElement(eleve,"prenom")
                prenom.text = x[3]
                date_naiss = ET.SubElement(eleve,"date_naiss")
                date_naiss.text = x[4]
                classe = ET.SubElement(eleve,"classe")
                classe.text = x[5]
                note = ET.SubElement(eleve,"note")
                note.text = x[6]
            tree = ET.ElementTree(eleves)
            tree.write("donnees_valides.xml", encoding="UTF-8", xml_declaration=True)
            
            with open('donnees_invalides.csv', 'w', newline='') as file:
                donnee = csv.writer(file,delimiter=',')
                donnee.writerows(invalide)
            print("Le données valides sont enregistrées dans un fichier donnees_valides.XML \net les données invalides dans un fichier donnees_invalides.CSV ")
        else:
            print("Entrer un bon format ")
    else:
        choix = input("Choisissez le format de fichier pour les données valides (CSV,JSON) : ")
        if choix == 'CSV':
            with open('donnees_valides.csv', 'w', newline='') as file:
                donnee = csv.writer(file,delimiter=',')
                donnee.writerows(valide)
                
            jsonString = json.dumps(invalide)
            jsonFile = open("donnees_invalides.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
            print("Le données valides sont enregistrées dans un fichier donnees_valides.CSV \net les données invalides dans un fichier donnees_invalides.JSON ")
        elif choix == 'JSON':
            jsonString = json.dumps(valide)
            jsonFile = open("donnees_valides.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
            
            with open('donnees_invalides.csv', 'w', newline='') as file:
                donnee = csv.writer(file,delimiter=',')
                donnee.writerows(invalide)
            print("Le données valides sont enregistrées dans un fichier donnees_valides.JSON \net les données invalides dans un fichier donnees_invalides.CSV ")
        else:
            print("Entrer un bon format ")
        
        
def afficher_par_5(tab, page):
    elements_par_page = 5
    d = (page - 1) * elements_par_page
    f = d + elements_par_page
    for e in tab[d:f]:
        print(e)
def afficher_par_X(tab, page):
    elements_par_page = int(input("\nDonner le nombre de lignes que vous voulez aficher : "))
    d = (page - 1) * elements_par_page
    f = d + elements_par_page
    for e in tab[d:f]:
        print(e)
