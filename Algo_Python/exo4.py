chiffre = ['0','1','2','3','4','5','6','7','8','9']
commencement = ['7','8','6','0','5']

num = str(input("Donner les numeros : "))
num_valide = []
num_invalide = []
c = ''
s = []
orange = 0
expresso = 0
tigo = 0
promobile = 0

for i in range(len(num)):
    if num[i] in chiffre :
        c+=num[i]
    else:
        s.append(c)
        c = ''
        
        
for numero in s:
    i = numero[0] + numero[1]
    if len(numero) < 9 or len(numero) > 9 or (numero[0]!= '7' and numero[1] not in commencement):
        num_invalide.append(numero)
    else:
        num_valide.append(numero)
        
for numero in num_valide :
    i = numero[0] + numero[1]
    if i == '77' or i == '78':
        orange+=1
    elif i == '76':
        tigo+=1
    elif i == '70':
        expresso+=1
    else:
        promobile+=1
        

print(num_valide)
print("\t")
print(num_invalide)
print("\n")
print("ORANGE    : ",orange)
print("TIGO      : ",tigo)
print("EXPRESSO  : ",expresso)
print("PROMOBILE : ",promobile)
