t1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
t2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
point = ['.','?','!']
espace = ' '
i = 0
booleen = True

s = ''

while booleen :
    chaine = str(input("entrer les phrases : "))
    if chaine[0] in t2 :
        s+= chaine[0]
        for i in range(1,len(chaine)):
            if chaine[i] in t1 or chaine[i] == espace :
                if(chaine[i] == espace and chaine[i+1] == espace) :
                    continue
                else :
                    s+= chaine[i]
            elif (chaine[i] in point and chaine[i+1] in t2) :
                if(i >= 25 ):
                    s+= chaine[i]
                    s+= chaine[i+1]
                    continue
                else:
                    booleen = True
                    break
            elif chaine[i] in point and chaine[i+1] == '/':
                s+= chaine[i]
                booleen = False
                
                
print(s)