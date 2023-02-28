import csv

class Etudiant:
    
    def __init__(self,code,numero,nom,prenom,date_naiss,classe,notes):
        
        self.code= code
        self.numero = numero
        self.nom = nom
        self.prenom = prenom
        self.date_naiss = date_naiss
        self.classe = classe
        self.notes = notes
    
    def __str__(self):
        
        return f"{self.code},{self.numero},{self.nom},{self.prenom},{self.date_naiss},{self.classe},{self.notes}"
    
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
                etudiant = Etudiant(code,numero,nom,prenom,date_naiss,classe,notes)
                self.tab.append(etudiant)
    
   
    def afficher(self):
        
        for x in self.tab:
            print(x)   
    
    
etu = Etudiants('Donnees_Projet_Python_DataC5.csv')

etu.afficher()
