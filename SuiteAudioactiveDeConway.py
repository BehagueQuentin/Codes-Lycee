def remplace (série):
    for nombre1 , lettre1 in LIST1:
        if nombre1 in série :
            série = série.replace(nombre1,lettre1)
    for lettre2, nombre2 in LIST2:
        if lettre2 in série :
            série = série.replace(lettre2,nombre2)
    return série


def facteur_M (x,y):
    return len(x)/len(y)


def compteur (chaine):
    compt1 =0
    for lettre in chaine :
        if lettre == "1" :
            compt1 +=1
    return compt1/len(chaine)*100

if __name__ == '__main__' :
    Moyenne =0
    MoyMultip =0
    x=0        
    LIST1 = [("333","a"),("33","b"),("3","c"),("222","d"),("22","e"),("2","f"),("111","g"),("11","h"),("1","i"),("4","o"),("5","j"),("6","k"),("7","l"),("8","m"),("9","n")]
    LIST2 = [("a","33"),("b","23"),("c","13"),("d","32"),("e","22"),("f","12"),("g","31"),("h","21"),("i","11"),("o","14"),("j","15"),("k","16"),("l","17"),("m","18"),("n","19")]
    rep = str(input("Choisissez un nombre entier (entre 1 et 9) :"))
    y = int (input("Choisissez un nombre d'étapes :"))
    while x!=y :
        VAR =  remplace(rep)
        print (VAR)
        rep = VAR
        x+=1
        Moyenne += compteur (VAR)
        MoyMultip += facteur_M (VAR, rep)