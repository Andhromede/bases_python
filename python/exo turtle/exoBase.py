# PART 1

# ------------------------------------------------------------
# # EXO 1 :
# miles = input("Entrez les nombre de miles que vous souhaitez convertir svp : ")
# print(str(miles) + " miles équivalent à " + str(int(miles) * 1.60934) + "km" )

# ------------------------------------------------------------
# # EXO 2 :
# var1 = "Variable 1"
# var2 = "Variable 2"
# var1,var2 = var2,var1           #Inversion de variables





# ------------------------------------------------------------
# PART 2
# ------------------------------------------------------------
# # EXO 1 :

# nb = input("Entrez un nombre svp : ")

# if int(nb)%2:
#     print("Votre nombre est impaire !")
# else:
#     print("Votre nombre est paire !")

# ------------------------------------------------------------
# # EXO 2 :

# i = 1
# result = 0

# while i <= 3:
#     i+=1
#     nb = (int(input("Veuillez entrez le nombre svp : ")))
#     if result<nb :
#         result = nb

# print("le plus grand nombre est le : " + str(result))


# ------------------------------------------------------------
# PART 3
# ------------------------------------------------------------
# # EXO 1 :

# def nbrPairOuImpair(nbr):
#     if nbr % 2 == 0:
#         print("le nombre est paire")
#     else:
#         print("Le nombre est impaire")

# nbrPairOuImpair(int(input("entrez un nombre svp : ")))

# ------------------------------------------------------------
# # EXO 2 :

# def est_pair(nbr):
#     if nbr % 2 == 0:
#         print("true")
#     else:
#         print("false")

# est_pair(int(input("entrez un nombre svp : ")))


# ------------------------------------------------------------
# # EXO 3 :

# i = 1
# tab = []

# while i <= 3:
#     nb = (int(input("Veuillez entrez le nombre svp : ")))
#     tab.append(nb)
#     # tab += nb1, nb2, nb3
#     i+=1

# def nb(tab):
#     # tab.sort()
#     tab.sort(reverse = True)
#     return tab[0]

# print(nb(tab))


# ------------------------------------------------------------
# # EXO 4 :

# def decrementation(a, b):
#     """Decremente un nombre s'il est inferieur a 0"""
#     if a<0: -a
#     if b<0: -b
#     print(decrementation.__doc__)
#     return a*b

# print(decrementation(5,2))
    

# ------------------------------------------------------------
# # EXO 5 :
# def moyenne(nb1, nb2, nb3):
#     moyenneNote = (nb1+nb2+nb3)/3
#     return moyenneNote

# print(str(moyenne(5,9,3)))



# ------------------------------------------------------------
# PART 4
# ------------------------------------------------------------
# # EXO 1 :
nb = int(input("Entrez un nombre svp : "))

for i in range (nb):
    i+=1
    ligne = ""
    for j in range (i):
        j+=1
        ligne+="#"
    print(ligne)   
        






