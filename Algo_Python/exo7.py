caractere = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
            ,'n','o','p','q','r','s','t','u','v','w','x','y','z',' '
            ,'A','B','C','D','E','F','G','H','I','J','K','L','M'
            ,'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            ,'0','1','2','3','4','5','6','7','8','9']
correspondant = ['2','22','222','3','33','333','4','44','444','5','55','555','6'
            ,'66','666','7','77','777','7777','8','88','888','9','99','999','9999','00'
            ,'2','22','222','3','33','333','4','44','444','5','55','555','6'
            ,'66','666','7','77','777','7777','8','88','888','9','99','999','9999'
            ,'a','b','c','d','e','f','g','h','i','j']

phrase = str(input("Entrer la phrase : "))
chaine = []
s = []

for j in range(len(phrase)):
    for i in range(len(caractere)):
        if phrase[j] == caractere[i]:
            chaine.append(correspondant[i])
    if phrase[j] not in caractere :
        chaine.append(phrase[j])
            
s.append(chaine[0])
for i in range(1,len(chaine)) :  
    a = chaine[i]
    b = chaine[i-1]    
    if a[0]== b[len(b) - 1] :
        s.append('0')  
    s.append(chaine[i])
        
for l in s :
    print(l,end='')