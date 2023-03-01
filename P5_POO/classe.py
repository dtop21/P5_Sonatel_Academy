import csv

t1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
t2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
chiffre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

tableau_valide = []
invalide = []
valideMoy = []

class Etudiant:
    
    def __init__(self,code,numero,nom,prenom,date_naiss,classe,notes,moy_gen):
        
        self.code= code
        self.numero = numero
        self.nom = nom
        self.prenom = prenom
        self.date_naiss = date_naiss
        self.classe = classe
        self.notes = notes
        self.moy_gen = moy_gen
    
    def __str__(self):
        
        return f"{self.code},{self.numero},{self.nom},{self.prenom},{self.date_naiss},{self.classe},{self.notes},{self.moy_gen}"
    
class Etudiants:
    
    def __init__(self, fichier):
        
        self.tab = []
        with open(fichier, encoding='UTF-8') as mon_fichier:
            mon_fichier_reader = csv.reader(mon_fichier, delimiter=',')
            for row in mon_fichier_reader:
                code = row[0]
                numero = row[1]
                nom= row[2]
                prenom = row[3]
                date_naiss = row[4]
                classe= row[5]
                notes = row[6]
                moy_gen = 0
                etudiant = Etudiant(code,numero,nom,prenom,date_naiss,classe,notes,moy_gen)
                self.tab.append(etudiant)
                
    def format_classe(self):
        valideC = []
        ch = ''
        for x in self.tab:
            for y in x.classe:
                if y in t1 or y in t2 or y in chiffre:
                    ch += y
            x.classe = ch
            ch = ''
            if len(x.classe) >= 2:
                if (x.classe[-1] == 'a' or x.classe[-1] == 'A') and x.classe[0] in chiffre[3:7]:
                    x.classe = x.classe[0] + 'em' + 'A'
                    valideC.append(x)
                elif (x.classe[-1] == 'b' or x.classe[-1] == 'B') and x.classe[0] in chiffre[3:7]:
                    x.classe = x.classe[0] + 'em' + 'B'
                    valideC.append(x)
                else:
                    invalide.append(x)
            else:
                invalide.append(x)
                
        return valideC 
   
    def format_date(self):
        valideD =[]
        t = []
        ch = ''
        for x in self.tab:
            for y in x.date_naiss:
                if (y not in chiffre and y not in t1 and y not in [' ','/','-','|',',',':','.','_']) or x.date_naiss[0] in t1 :
                    invalide.append(x)
                    break
        for x in self.tab:
            if x not in invalide:
                t.append(x)
        self.tab = t
        t = []

        for x in self.tab:
            for i in range(len(x.date_naiss)):
                if x.date_naiss[i] == ' ' and x.date_naiss[i+1] == ' ' :
                    continue
                else:
                    ch += x.date_naiss[i]
                if ch[0] == ' ' :
                    s = ch[1:len(ch)]  
                    ch  = s
            x.date_naiss = ch
            ch = ''
                
        for x in self.tab:
            if len(x.date_naiss) >= 7:
                if x.date_naiss[0] in chiffre and x.date_naiss[1] not in chiffre:
                    x.date_naiss = '0'+x.date_naiss[0:-1]+x.date_naiss[-1]
                if x.date_naiss[3] in chiffre and x.date_naiss[4] not in chiffre:
                    x.date_naiss = x.date_naiss[0:3]+'0'+x.date_naiss[3:-1]+x.date_naiss[-1]
                t.append(x)
            else:
                invalide.append(x)
        self.tab = t
        t = []
        for x in self.tab:
            for y in x.date_naiss:
                if y in chiffre or y in t1:
                    ch += y
            x.date_naiss = ch
            ch = ''
        for x in self.tab:
            for y in x.date_naiss :
                if y in t1:
                    ch += y
            for y in x.date_naiss:
                if y in t1 and ch in 'janvier':
                    c = '01'
                    x.date_naiss = x.date_naiss[0:2] + c + x.date_naiss[4:-1] + x.date_naiss[-1]
                elif y in t1 and ch in 'fevrier':
                    c = '02'
                    x.date_naiss = x.date_naiss[0:2] + c + x.date_naiss[4:-1] + x.date_naiss[-1]
                elif y in t1 and ch in 'mars':
                    c = '0'
                    x.date_naiss = x.date_naiss[0:2] + c + x.date_naiss[4:-1] + x.date_naiss[-1]
                elif y in t1 and ch in 'avril':
                    c = '04'
                    x.date_naiss = x.date_naiss[0:2] + c + x.date_naiss[4:-1] + x.date_naiss[-1]
                elif y in t1 and ch in 'mai':
                    c = '05'
                    x.date_naiss = x.date_naiss[0:2] + c + x.date_naiss[4:-1] + x.date_naiss[-1]
                elif y in t1 and ch in 'juin':
                    c = '06'
                    x.date_naiss = x.date_naiss[0:2] + c + x.date_naiss[4:-1] + x.date_naiss[-1]
                elif y in t1 and ch in 'juillet':
                    c = '07'
                    x.date_naiss = x.date_naiss[0:2] + c + x.date_naiss[4:-1] + x.date_naiss[-1]
                elif y in t1 and ch in 'aout':
                    c = '08'
                    x.date_naiss = x.date_naiss[0:2] + c + x.date_naiss[4:-1] + x.date_naiss[-1]
                elif y in t1 and ch in 'septembre':
                    c = '09'
                    x.date_naiss= x.date_naiss[0:2] + c + x.date_naiss[4:-1] + x.date_naiss[-1]
                elif y in t1 and ch in 'octobre':
                    c = '10'
                    x.date_naiss= x.date_naiss[0:2] + c + x.date_naiss[4:-1] + x.date_naiss[-1]
                elif y in t1 and ch in 'novembre':
                    c = '11'
                    x.date_naiss= x.date_naiss[0:2] + c + x.date_naiss[4:-1] + x.date_naiss[-1]
                elif y in t1 and ch in 'decembre':
                    c = '12'
                    x.date_naiss= x.date_naiss[0:2] + c + x.date_naiss[4:-1] + x.date_naiss[-1]
            ch = ''
        for x in self.tab:
            for y in x.date_naiss :
                if y in chiffre:
                    ch += y
            x.date_naiss = ch
            ch = ''
            if len(x.date_naiss [4:-1] + x.date_naiss [-1]) == 2:
                if x.date_naiss [4:-1] + x.date_naiss [-1] <= '23':
                    x.date_naiss  = x.date_naiss [0:4] + '20' + x.date_naiss [4:-1] + x.date_naiss [-1]
                else:
                    x.date_naiss  = x.date_naiss [0:4] + '19' + x.date_naiss [4:-1] + x.date_naiss [-1]
        for x in self.tab:
            x.date_naiss = x.date_naiss [0:2] + '-' + x.date_naiss [2:4] + '-' +x.date_naiss [4:-1] + x.date_naiss [-1]
            jour = x.date_naiss [0:2]
            mois = x.date_naiss [3:5]
            annee = int(x.date_naiss [6:-1] + x.date_naiss [-1])
        
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
    
    def controle_numero(self):
        valideN = []
        ch = ''
        for x in self.tab:
            if len(x.numero) == 7 :
                for y in x.numero:
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
    
    def controle_prenom(self):
        valideP = []
        for x in self.tab:
            if (x.prenom[0] in t1 or x.prenom[0] in t2) and len(x.prenom) > 3 :
                valideP.append(x)
            else:
                invalide.append(x)
                
        return valideP

    def controle_nom(self):
        valideNom = []
        for x in self.tab:
            if (x.nom[0] in t1 or x.nom[0] in t2) and len(x.nom) >= 2 :
                valideNom.append(x)
            else:
                invalide.append(x)
        
        return valideNom

    def calcul_moyenne(self):
        valide = []
        t = []
        for x in self.tab:
            if x.notes[-1] != ']' and x.notes[-1] != '#':
                x.notes += ']' 
        ch = ''
        for x in self.tab:
            for y in x.notes:
                if y != ',':
                    ch += y    
                elif y == ',':
                    y = '.'
                    ch += y
            x.notes = ch
            ch = ''
        result = ''
        for x in self.tab:
            for y in x.notes[-5:-1]:
                ch += y
            if ':' not in ch:
                invalide.append(x)
            ch = ''
        for x in self.tab:
            if x not in invalide:
                t.append(x)
        self.tab = t
        t = []
        for x in self.tab:
            if x.notes[-1] == '#':
                invalide.append(x)
        for x in self.tab:
            if x not in invalide:
                t.append(x)
        self.tab = t
        t = []
        for x in self.tab:
            x.notes = x.notes.split("#")
        for x in self.tab:
            if x.notes[0] == '':
                invalide.append(x)
        for x in self.tab:
            if x not in invalide:
                t.append(x)
        self.tab = t
        t = []
        m = 0
        i = 0
        for x in self.tab :
            for y in x.notes:
                nom_matiere = y.split("[")[0]
                devoirs = [note for note in y.split("[")[1].split(":")[0].split("|")]
                for note in devoirs[-1]:
                    if note == ']':
                        devoirs = devoirs[0:-1]
                devoirs = [float(n) for n in devoirs]
                examen = float(y.split("[")[1].split("]")[0].split(":")[1])
                if examen < 0 or examen > 20:
                    invalide.append(x)
                    break
                moyenne = round((sum(devoirs) / len(devoirs) + 2 * examen) / 3,2)
                m += moyenne
                i += 1
                result +=" "+nom_matiere +" "+str(moyenne)
            x.moy_gen = round(m / i,2)
            x.notes = result 
            valide.append(x)
            result = ''
            m = 0
            i = 0

        return valide

    def affiche_info(self,num):
        bol = False
        for x in self.tab:
            if num == x.numero :
                bol = True
                print('\n')
                print(x)
                print('\n')
        if bol == False:
            print("\n Le numero que vous cherchez n'est pas dans le fichier ")

    def affiche_cinq_premiers(self):
        self.tab.sort(key = lambda s:s.moy_gen ,reverse = True)
        
        choix = (input("choissisez une classe(format : 5emA,5emB,4emA .....) : "))
        
        j = 0
        bol = False
        for x in self.tab :
            if choix == x.classe and j <= 4:
                bol = True
                print(x)
                print('\n') 
                j +=1
        if bol == False :
            print("veuillez entrer une classe valide")   

    def ajouter(self,et):
        self.tab = []
        code = input("Donner le code : ")
        numero = input("Donner le numero : ")
        nom = input("Donner le nom : ")
        prenom = input("Donner le prenom : ")
        date = input("Donner la date de naissance : ")
        classe = input("Donner le classe : ")
        note = input("Donner les notes : ")
        moy_gen = 0
        etudiant = Etudiant(code,numero,nom,prenom,date,classe,note,moy_gen)
        self.tab.append(etudiant)
        self.tab = et.format_date()
        self.tab = et.format_classe()
        self.tab = et.controle_numero()
        self.tab = et.controle_prenom()
        self.tab = et.controle_nom()
        self.tab = et.calcul_moyenne()    
            

etu = Etudiants('Donnees_Projet_Python_DataC5.csv')
tableau_valide = etu.format_classe()
tableau_valide  = etu.format_date()
tableau_valide = etu.controle_numero()
tableau_valide  = etu.controle_prenom()
tableau_valide  = etu.controle_nom()
tableau_valide = etu.calcul_moyenne()
# num = input("NUMERO : ")
# etu.affiche_info(num)
# etu.affiche_cinq_premiers()
# etu.ajouter(etu)
for x in tableau_valide :
    print(x)

# for x in invalide :
#     print(x)


