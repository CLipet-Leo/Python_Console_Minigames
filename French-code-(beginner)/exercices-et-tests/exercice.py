def calculSalaireParSeconde(salaireHoraire, heureParJourOuvrable, jourOuvrable):
    # Assigner a salaireAnnuel, le nombre d'heure travaillées en un an
    salaireAnnuel = salaireHoraire * heureParJourOuvrable * jourOuvrable
    #Calculer, puis assigner a nombreDeSecondeParAn, le nombre de seconde dans une année non-bisextile
    nombreDeSecondeParAn = 60 * 60 * 24 * 365
    #Retourner le salaire Annuel divisé par le nombre de seconde par an
    return salaireAnnuel / nombreDeSecondeParAn


def calculSalaireNet(salaireBrut, coeff): 
    #Assigner SalaireNet, SalairBrut*coeff
    SalaireNet = salaireBrut*(1-coeff)
    #return SalaireNet
    return SalaireNet

def withdrawFees(total, percent):
    #Caclul du montant des taxes a retirer : 
    fees = total * (percent / 100)
    #Retourner la valeur totale moins les taxes 
    return total - fees

def calculSalaireNet(salaireBrut, public):
    # #Calculer et retourner le Salaire Net a partir du salaire brut
    # return withdrawFees(salaireBrut, coeff)

    #Si j'occupe un poste de la fonction publique
    if public:
        #alors je retourne le salaire brut - 15% de taxes
        return withdrawFees(salaireBrut, 15)
    # Sinon ? C'est que je suis travailleur dans le secteur privé, alors je retourne le salaire brut - 23% de douille a l'ancienne 
    else:
        return withdrawFees(salaireBrut, 23)

#Definir une fonction qui divise x par y et retourne le resultat 
def divide(x,y):
    #Si y est egale a0 
    if y == 0:
            
        #Alors ecrire un message d'erreur
        print("ERREUR : Cannot divide by 0")
        #retourner vide
        return
    #sinon
    else:
        #Alors retourner x / y 
        return x / y


# def input():
    #Renvoie un caractere de type string au hasard

#Exercice:
    #Faire un mini jeu qui affiche un message lorsque input renvoie le bon caractere
    # le caractere doit etre parametrable
#je definis un mini jeux
def miniJeux(x):
    #compteur à 0
    compteur = 0
    #je definiq une variable y 
    y=input("Devinez")
    #Tant que y est différent de x 
    while y!=x :
        #ajouter 1 au compteur
        compteur = compteur + 1
        #afficher le compteur
        print(compteur)
        #Alors j'appelle un nouvelle y 
        y=input("Devinez")
    #lorsque la variable y est égale a la variable x alors 
    print("réussi")


prenom = "Alexandre"
nom = "Delaistre"
identite = nom + prenom # retourne "DelaistreAlexandre"

identite = nom + ' ' + prenom #retourne "Delaistre Alexandre"

integerValue = 342 #Retourne 342
stringIntegerValue = str(342)# retourne "342"


tableau = [0,10,15,5,1]
#Pour Recuperer 15 je prends dans tableau l'index 2

print(tableau[2]) # Affiche 15

len(tableau) #Renvoie la longueur de tableau renvoie 5 


#Exercice 1  
#Faire une fonction qui concatene 2 chaines de caractere, les séparants par une virgule
def concatWithComma(strA, strB): 
    #Je m'assure que strA soit bien de type str
    stringifiedA = str(strA)
    #Je m'assure que strB soit bien un str
    stringifiedB = str(strB)
    #Retourne stra + ',' + strb 
    return strA + ", " + strB

concatWithComma(23, "toto") #retourne "23, toto"
#Exercice 2
#Faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractere
#avec l'ensembles des occurences d'un chiffre e.g.:
#Pour tableau = [0,1,1,1,0,1,1,0,1]
#la fonction(tableau, 0) doit renvoyer "0, 4, 7" n'hesitez pas a implementer la premiere fonction ;)


tableau = [0,1,1,1,0,1,1,0,1]
#Definir la fonction findIndex qui itere sur tableau, cherchant l'index
#des differentes occurences de x
def findIndex(tableau, x):
    #definir i un index de depart
    i = 0
    #definir chaineRetour telle qu'une chaine de caractere vide
    chaineRetour = ''
    #Tant que i est different du nombre d'elt dans le tableau
    while i != len(tableau):
        #Alors j'attribue a une variable la valeur de tableau a l'index i
        selected = tableau[i]
        #Je defini un boolen tel que firstTurn est true
        #Si selected est egal a x ET que firstTurn est true
            #Alors on assigne a chaineRetour le retour de str(i)
            #changer la valeur de firstTurn a false
        #Sinon si selected est egal a x 
            #Alors j'assigne le retour de concatWithComma tel que : concatWithComma(chaineRetour, i) à chaineRetour
        chaineRetour = concatWithComma(chaineRetour, i)
        #j'incremente i de 1
        i = i + 1
    #Retourne la chaine retour
    return chaineRetour








#Definir mon index
i = 0 
while (i != len(tableau)): 
    selected = tableau[i]
    i = i + 1
#Exercice 3
# Renvoyer / Afficher un message
