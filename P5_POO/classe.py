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
    

class Etudiants:
    def __init__(self, fichier):
        tab = []
        with open(fichier, encoding='UTF-8') as mon_fichier:
            mon_fichier_reader = csv.reader(mon_fichier, delimiter=',')
            for row in mon_fichier_reader:
                self.code = row[0]
                self.numero = row[1]
                self.nom= row[2]
                self.prenom = row[3]
                self.date_naiss = row[4]
                self.classe= row[5]
                notes = row[6]
                etudiant = Etudiant(code,numero,nom,prenom,date_naiss,classe,notes)
                self.tab.append(etudiant)
    
    def afficher():
        for x in tab:
            print(x)
    
etu = Etudiants('Donnees_Projet_Python_DataC5.csv')
etu.afficher()

