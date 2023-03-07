i = 0

saisi = str(input("Saisir une phrase : "))
saisi1 = ''

x = len(saisi) 

for i in range(0,x): 
    
    if saisi[i]== ' ' and saisi[i+1] == ' ' :
        continue
    else :
        saisi1 += saisi[i]
        
        
if saisi1[0] == ' ' :
    s = saisi1[1:len(saisi1)]
    print(s)
else :
        print(saisi1)        