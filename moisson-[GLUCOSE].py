#coding utf-8

import csv
import requests
from bs4 import BeautifulSoup

url = "https://ici.radio-canada.ca/actualite/decouverte/dossiers/63_montignac/pop_tableau_03.html"
entetes = { 
    "User-Agent":"Thomas Litalien",
    "From":"thomas.litalien@gmail.com"
}

#Êtes-vous du type à surveiller ce que vous manger? Vous sentez-vous balloné lorsqu'il y a trop de glucides dans vos aliments? N'ayez crainte! Voici un guide qui vous aidera.
#Première étape, j'ai défini ce qu'est les glucides, grâce à la fonction "def"
#Deuxième étape, je vous demande offre un choix selon la liste établie par mon url de Radio-Canada. 
#Troisième étape. Pour chacune des catégories, je fais la liste des aliments qui y sont. Les aliments se trouvent dans des balises "td" dans l'url, donc je les classe ainsi grâce à la fonctoin "next". La première réponse n'avait aucun espace avant son texte, comme les éléments suivants dans la liste. C'est pourquoi j'ai ajouté les "       ".
#Vous pouvez choisir une quantité de glucides, et on vous donnera une liste d'aliments qui se trouve dans cette tranche. 

contenu = requests.get(url,headers=entetes)
page = BeautifulSoup(contenu.text,"html.parser")

def glucide():
    menuChoix()
    
def menuChoix():
    valide = ['10','15','20','22','30','35','40','45','50','65','70','75','80','85','90','95','100','110']
    choixIndex = str(input('Veuillez entrer un index glycemique parmis les suivants: 10, 15, 20, 22, 30, 35, 40, 45, 50, 65, 70, 75, 80, 90, 95, 100 ou 110 :'))
    if choixIndex in valide:
        reponseValide(choixIndex)
    else:
        print("Votre index glycemique est invalide.")
        menuChoix()
        
def reponseValide(choixIndex):
    print("Vous avez choisi l'index glycemique",choixIndex)
    choixIndex = choixIndex
    if choixIndex == "10":
        print("Voici les aliments trouvés:")
        for i in page.find_all("td"):
            if i.text.strip() == "10":
                print("     ",i.find_next("td").text.strip())
                continuer = str(input('Voulez-vous choisir un autre index?'))
                if continuer == "oui":
                    menuChoix()
                if continuer == "non":
                    print("Fin du programme")
                else:
                    print("ce n'est pas une réponse valide!")
                    continuer = str(input('Voulez-vous choisir un autre index?'))
    if choixIndex == "15":
        print("Voici les aliments trouvés:")
        for i in page.find_all("td"):
            if i.text.strip() == "15":
                print("     ",i.find_next("td").text.strip())
                continuer = str(input('Voulez-vous choisir un autre index?'))
                if continuer == "oui":
                    menuChoix()
                if continuer == "non":
                    print("Fin du programme")
                else:
                    print("ce n'est pas une réponse valide!")
                    continuer = str(input('Voulez-vous choisir un autre index?'))
    if choixIndex == "20":
        print("Voici les aliments trouvés:")
        for i in page.find_all("td"):
            if i.text.strip() == "20":
                print("     ",i.find_next("td").text.strip())
                continuer = str(input('Voulez-vous choisir un autre index?'))
                if continuer == "oui":
                    menuChoix()
                if continuer == "non":
                    print("Fin du programme")
                else:
                    print("ce n'est pas une réponse valide!")
                    continuer = str(input('Voulez-vous choisir un autre index?'))
    if choixIndex == "22":
        print("Voici les aliments trouvés:")
        for i in page.find_all("td"):
            if i.text.strip() == "22":
                print("     ",i.find_next("td").text.strip())
                continuer = str(input('Voulez-vous choisir un autre index?'))
                if continuer == "oui":
                    menuChoix()
                if continuer == "non":
                    print("Fin du programme")
                else:
                    print("ce n'est pas une réponse valide!")
                    continuer = str(input('Voulez-vous choisir un autre index?'))
    if choixIndex == "30":
        print("Voici les aliments trouvés:")
        for i in page.find_all("td"):
            if i.text.strip() == "30":
                print("     ",i.find_next("td").text.strip())
                continuer = str(input('Voulez-vous choisir un autre index?'))
                if continuer == "oui":
                    menuChoix()
                if continuer == "non":
                    print("Fin du programme")
                else:
                    print("ce n'est pas une réponse valide!")
                    continuer = str(input('Voulez-vous choisir un autre index?'))
    if choixIndex == "35":
        print("Voici les aliments trouvés:")
        for i in page.find_all("td"):
            if i.text.strip() == "35":
                print("     ",i.find_next("td").text.strip())
                continuer = str(input('Voulez-vous choisir un autre index?'))
                if continuer == "oui":
                    menuChoix()
                if continuer == "non":
                    print("Fin du programme")
                else:
                    print("ce n'est pas une réponse valide!")
                    continuer = str(input('Voulez-vous choisir un autre index?'))
    if choixIndex == "40":
        print("Voici les aliments trouvés:")
        for i in page.find_all("td"):
            if i.text.strip() == "40":
                print("     ",i.find_next("td").text.strip())
                continuer = str(input('Voulez-vous choisir un autre index?'))
                if continuer == "oui":
                    menuChoix()
                if continuer == "non":
                    print("Fin du programme")
                else:
                    print("ce n'est pas une réponse valide!")
                    continuer = str(input('Voulez-vous choisir un autre index?'))
    if choixIndex == "45":
        print("Voici les aliments trouvés:")
        for i in page.find_all("td"):
            if i.text.strip() == "45":
                print("     ",i.find_next("td").text.strip())
                continuer = str(input('Voulez-vous choisir un autre index?'))
                if continuer == "oui":
                    menuChoix()
                if continuer == "non":
                    print("Fin du programme")
                else:
                    print("ce n'est pas une réponse valide!")
                    continuer = str(input('Voulez-vous choisir un autre index?'))
    if choixIndex == "50":
        print("Voici les aliments trouvés:")
        for i in page.find_all("td"):
            if i.text.strip() == "50":
                print("     ",i.find_next("td").text.strip())
                continuer = str(input('Voulez-vous choisir un autre index?'))
                if continuer == "oui":
                    menuChoix()
                if continuer == "non":
                    print("Fin du programme")
                else:
                    print("ce n'est pas une réponse valide!")
                    continuer = str(input('Voulez-vous choisir un autre index?'))
    if choixIndex == "65":
        print("Voici les aliments trouvés:")
        for i in page.find_all("td"):
            if i.text.strip() == "65":
                print("     ",i.find_next("td").text.strip())
                continuer = str(input('Voulez-vous choisir un autre index?'))
                if continuer == "oui":
                    menuChoix()
                if continuer == "non":
                    print("Fin du programme")
                else:
                    print("ce n'est pas une réponse valide!")
                    continuer = str(input('Voulez-vous choisir un autre index?'))
    if choixIndex == "70":
        print("Voici les aliments trouvés:")
        for i in page.find_all("td"):
            if i.text.strip() == "70":
                print("     ",i.find_next("td").text.strip())
                continuer = str(input('Voulez-vous choisir un autre index?'))
                if continuer == "oui":
                    menuChoix()
                if continuer == "non":
                    print("Fin du programme")
                else:
                    print("ce n'est pas une réponse valide!")
                    continuer = str(input('Voulez-vous choisir un autre index?'))
    if choixIndex == "75":
        print("Voici les aliments trouvés:")
        for i in page.find_all("td"):
            if i.text.strip() == "75":
                print("     ",i.find_next("td").text.strip())
                continuer = str(input('Voulez-vous choisir un autre index?'))
                if continuer == "oui":
                    menuChoix()
                if continuer == "non":
                    print("Fin du programme")
                else:
                    print("ce n'est pas une réponse valide!")
                    continuer = str(input('Voulez-vous choisir un autre index?'))
    if choixIndex == "80":
        print("Voici les aliments trouvés:")
        for i in page.find_all("td"):
            if i.text.strip() == "80":
                print("     ",i.find_next("td").text.strip())
                continuer = str(input('Voulez-vous choisir un autre index?'))
                if continuer == "oui":
                    menuChoix()
                if continuer == "non":
                    print("Fin du programme")
                else:
                    print("ce n'est pas une réponse valide!")
                    continuer = str(input('Voulez-vous choisir un autre index?'))
    if choixIndex == "85":
        print("Voici les aliments trouvés:")
        for i in page.find_all("td"):
            if i.text.strip() == "85":
                print("     ",i.find_next("td").text.strip())
                continuer = str(input('Voulez-vous choisir un autre index?'))
                if continuer == "oui":
                    menuChoix()
                if continuer == "non":
                    print("Fin du programme")
                else:
                    print("ce n'est pas une réponse valide!")
                    continuer = str(input('Voulez-vous choisir un autre index?'))
    if choixIndex == "90":
        print("Voici les aliments trouvés:")
        for i in page.find_all("td"):
            if i.text.strip() == "90":
                print("     ",i.find_next("td").text.strip())
                continuer = str(input('Voulez-vous choisir un autre index?'))
                if continuer == "oui":
                    menuChoix()
                if continuer == "non":
                    print("Fin du programme")
                else:
                    print("ce n'est pas une réponse valide!")
                    continuer = str(input('Voulez-vous choisir un autre index?'))
    if choixIndex == "95":
        print("Voici les aliments trouvés:")
        for i in page.find_all("td"):
            if i.text.strip() == "95":
                print("     ",i.find_next("td").text.strip())
                continuer = str(input('Voulez-vous choisir un autre index?'))
                if continuer == "oui":
                    menuChoix()
                if continuer == "non":
                    print("Fin du programme")
                else:
                    print("ce n'est pas une réponse valide!")
                    continuer = str(input('Voulez-vous choisir un autre index?'))
    if choixIndex == "100":
        print("Voici les aliments trouvés:")
        for i in page.find_all("td"):
            if i.text.strip() == "100":
                print("     ",i.find_next("td").text.strip())
                continuer = str(input('Voulez-vous choisir un autre index?'))
                if continuer == "oui":
                    menuChoix()
                if continuer == "non":
                    print("Fin du programme")
                else:
                    print("ce n'est pas une réponse valide!")
                    continuer = str(input('Voulez-vous choisir un autre index?'))
    if choixIndex == "110":
        print("Voici les aliments trouvés:")
        for i in page.find_all("td"):
            if i.text.strip() == "110":
                print("     ",i.find_next("td").text.strip())
                continuer = str(input('Voulez-vous choisir un autre index?'))
                if continuer == "oui":
                    menuChoix()
                if continuer == "non":
                    print("Fin du programme")
                else:
                    print("ce n'est pas une réponse valide!")
                    continuer = str(input('Voulez-vous choisir un autre index?'))
        
glucide()
