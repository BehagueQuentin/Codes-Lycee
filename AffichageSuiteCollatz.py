import matplotlib.pyplot as plt

def Syracusse (nb):
    Maxi = 0
    liste = []
    while nb != 1:
        liste.append (nb)
        if nb%2 ==0:
            nb =nb/2
        else :
            nb=3*nb+1
        if Maxi < nb :
            Maxi = nb
    liste.append (Maxi)
    return liste

if __name__ == '__main__' :
    rep = 1
    while rep > 0 :
        rep = int(input("Choisissez un nombre : "))
        Abcisse = Syracusse (rep)
        Ordonnées = []
        for nb in range (0, len(Abcisse)-1):
            Ordonnées.append(int(nb))
        print( "Altitude maximale =", Abcisse[-1])
        del Abcisse[-1]
        print ('temps de vol =',len(Abcisse))
        plt.plot(Ordonnées,Abcisse,color="green")
        plt.grid()
        plt.show()