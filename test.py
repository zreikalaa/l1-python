def carre_croissant(n) :
    liste2 = []
    for i in range(1,n+1):
        liste = []
        for j in range(i,i+n):
            liste.append(j)
        liste2.append(liste)
    return liste2
print (carre_croissant(5))