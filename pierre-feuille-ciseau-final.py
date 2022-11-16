#DEBUT

#on admet random une fonction qui renvoie une valeur aléatoire entre 1 et 3
#on admet input une fonction qui renvoie la valeur qu'a donner le joueur

#définir une fonction coup() qui définis les valeurs 1, 2 et 3 en chaîne de caractères
    #définir "1" = "pierre"
    #définir "2" = "feuille"
    #définir "3" = "ciseau"


#définir une fonction choixBot()
    #définir une variable randomNb prend pour valeur le retour de l'execution de la fonction random(1, 3)
    #retourner randomNb


#définir une fonction choixJoueur()
    #définir une variable choiceP1 qui prend pour valeur le retour de l'execution de la fonction input(1, 3)
    #retourner la valeur


#définir une fonction resultat()
    #définir coupJoueur une variable qui est égale à la fonction choixJoueur()
    #définir coupBot une variable qui est égale à la fonction choixBot()
    #si choixJoueur == 1 alors
        #si choixBot == 1
            #alors afficher "égalité"
        #si choixBot == 2
            #alors afficher "perdu"
        #si choixBot == 3
            #alors afficher "gagné"
    #si choixJoueur == 2 alors
        #si choixBot == 1
            #alors afficher "gagné"
        #si choixBot == 2
            #alors afficher "égalité"
        #si choixBot == 3
            #alors afficher "perdu"
    #si choixJoueur == 3 alors
        #si choixBot == 1
            #alors afficher "perdu"
        #si choixBot == 2
            #alors afficher "gagné"
        #si choixBot == 3
            #alors afficher "égalité"
    #retourner la valeur

#afficher la fonction resultat()

#FIN