#DEBUT

#on admet random une fonction qui renvoie une valeur aléatoire entre 1 et 3
import random
#on admet input une fonction qui renvoie la valeur qu'a donner le joueur

#définir une fonction coup() qui définis les valeurs 1, 2 et 3 en chaîne de caractères
def coup(num):
    if num == "1":
        #définir 1 = pierre
        return "pierre"
    if num == "2":
        #définir 2 = feuille
        return "feuille"
    if num == "3":
        #définir 3 = ciseau
        return "ciseau"

#définir une fonction choixBot
def choixBot():
    #définir une variable randomNb prend pour valeur le retour de l'execution de la fonction random(1, 3)
    randomNb = random.randint(1, 3)
    str(randomNb)
    #retourner randomNb
    return randomNb

#définir une fonction choixJoueur
def choixJoueur():
    #définir une variable choiceP1 qui prend pour valeur le retour de l'execution de la fonction input(1, 3)
    choiceP1 = input("Quel coup veut-tu jouer : Pierre 1, Feuille 2 ou Ciseau 3 ? ")
    if choiceP1 == "1" or "2" or "3":
        #retourner la valeur
        return choiceP1
    else:
        print("La valeur n'est pas valide, veullez entrer 1, 2 ou 3")
    


#définir une fonction resultat
def resultat():
    result = ""
    #définir coupJoueur une variable qui est égale à la fonction choixJoueur()
    coupJoueur = choixJoueur()
    turnJoueur = coup(coupJoueur)
    print("Tu as joué ", coupJoueur, ", c'est à dire : ", turnJoueur)
    #définir coupBot une variable qui est égale à la fonction choixBot()
    coupBot = choixBot()
    turnBot = coup(coupBot)
    print("Le bot a joué ", coupBot, ", c'est à dire : ", turnBot)
    #si choixJoueur == 1 alors
    if coupJoueur == "1":
        #si choixBot == 1
        if coupBot == "1":
            #alors afficher "égalité"
            result = "Egalité"
        #si choixBot == 2
        elif coupBot == "2":
            #alors afficher "perdu"
            result = "Perdu"
        #si choixBot == 3
        else:
            #alors afficher "gagné"
            result = "Gagné"
    #si choixJoueur == 2 alors
    elif coupJoueur == "2":
        #si choixBot == 1
        if coupBot == "1":
            #alors afficher "gagné"
            result = "Gagné"
        #si choixBot == 2
        elif coupBot == "2":
            #alors afficher "égalité"
            result = "Egalité"
        #si choixBot == 3
        else:
            #alors afficher "perdu"
            result = "Perdu"
    #si choixJoueur == 3 alors
    elif coupJoueur == "3":
        #si choixBot == 1
        if coupBot == "1":
            #alors afficher "perdu"
            result = "Perdu"
        #si choixBot == 2
        elif coupBot == "2":
            #alors afficher "gagné"
            result = "Gagné"
        #si choixBot == 3
        else:
            #alors afficher "égalité"
            result = "Egalité"
    #retourner la valeur
    return result

#afficher la fonction resultat()
print(resultat())

#FIN