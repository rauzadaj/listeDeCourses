import sys

option1 = "1: Ajouter"
option2 = "2: Retirer"
option3 = "3: Afficher"
option4 = "4: Vider"
option5 = "5: Quitter"
choix = ""
i = 0
liste = []

while choix != "5":
    print("Choisissez parmi les 5 options suivantes")
    choix = input(
       option1 + "\n" + option2 + "\n" + option3 + "\n" + option4 + "\n" + option5 + "\n" + "Votre choix : ")
    if choix == "1":
        liste.append( input(" Entrer le nom d'un element a ajouter a la liste de courses : "))
    elif choix == "2":
        if liste:
            for i, element in enumerate(liste):
                print(i, element)
            liste.remove(input("Entrer le nom du produit a supprimer : "))
        else:
            print("La liste est vide")
    elif choix == "3":
        for i, element in enumerate(liste):
            print(i, element)
    elif choix == "4":
        liste.clear()
    elif choix == "5":
        sys.exit()



