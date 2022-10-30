import sys

#Afficher le menu :
user_input = ""
liste = []




while user_input != "5":

#Afficher le menu
    user_input = input("""
    ---------------------------------------------------------------------
Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément à la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
Votre choix : """)

#Ajouter un élément à la liste
    if not (user_input.isdigit() and 1 <= int(user_input) <= 5):
        print("Choix inconnue: Veuillez entre un nombre en 1 et 5")
        continue


    elif user_input == "1":
        ajouter = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        liste.append(ajouter)
        print(f"L'élément {ajouter} a bien été ajouté à la liste")
        

#Retirer un element à la liste
    elif user_input == "2":
        retirer = input("Entrez le nom d'un élément à retirer de la liste de course : ")
        if retirer in liste:
            liste.remove(retirer)
        else:
            print(f"L'élement {retirer} n'est pas dans la liste.")
            
    


#Afficher la liste
    elif user_input == "3":
        print(f"Voici le contenu de votre liste : ")
        for i, element in enumerate(liste):
            print(f"{i+1}. {element}")


    
#Vider la liste
    elif user_input == "4":
        liste.clear() 
        print("La liste a été vidé")

#Quitter la liste
    elif user_input == "5":
       sys.exit()









