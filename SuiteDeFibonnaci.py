rep = int ( input ("Nombre d'étapes :"))
x = y = 1
comp = 0
while comp != rep :
    x += y
    nbor = x/y
    print (x,", (rapport =", nbor,")")
    y += x
    nbor = y/x
    print (y,", (rapport =",nbor, ")")
    comp += 1