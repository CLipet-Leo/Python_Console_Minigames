#définir une fonction afficher_grille() avec comme paramètre grille
    #afficher le numéro de chaques colonnes
    #afficher la permière ligne
    #afficher le numéro de la première ligne
    #afficher chaques colonnes de la ligne
    #afficher la seconde ligne
    #afficher le numéro de la seconde ligne
    #afficher chaques colonnes de la ligne
    #afficher la troisieme ligne
    #afficher le numéro de la troisième ligne
    #afficher chaques colonnes de la ligne
    #afficher la dernière ligne

#définir une fonction tour() avec comme paramètres grille et joueur
    #afficher "C'est à toi joueur", le numéro du joueur
    #définir la variable colonne comme input qui affiche "Le numero de colonne que tu veux jouer : "
    #définir la variable ligne comme input qui affiche "Et maintenant la ligne : "
    #afficher "OK ! C'est placé dans la case ("+numéro de la colonne+","+numéro de la ligne+")"
    #faire une boucle tant que la case selectionné est prise
        #appeler la fonction afficher_grille(grille)
        #afficher "Cette case est déjà prise >:( selectionne un autre case !"
        #définir la variable colonne comme input qui affiche "Le numero de colonne que tu veux jouer : "
        #définir la variable ligne comme input qui affiche "Et maintenant la ligne : "
        #afficher "OK ! C'est placé dans la case ("+numéro de la colonne+","+numéro de la ligne+")"
    
    #si la variable joueur est égale à 1
        #alors afficher "X" dans la case selectionner
    ##si la variable joueur est égale à 2
        #alors afficher O dans la case selectionner
    #appeler la fonction afficher_grille(grille)

#définir une fonction gagnant() avec comme paramètre grille
    #si case(...) est prise ET case(...) est prise ET case(...) est différente de " "
        #alors retourner la valeur 1
    #repeter la boucle du dessu 8 fois (le nombre de possibilité de gagner au morpion)

#définir une fonction match_nul() avec comme paramètre grille
    #pour i le nombre de case sur la grille allant jusqu'à 9
        #si la valeur grille ayant comme paramètre i est égale à " " (c'est à dire qu'aucune ligne n'a été former par un joueur)
            #alors retourner la valeur 0
    #retourner la valeur 1

#DEBUT

#définir la variable joueur est égale à 1
#afficher "Joueur 1 tu possède les X, Joueur 2 tu possède les O"
#afficher "Que le match COMMENCE !!!"
#définir que les cases de la variable grille sont égale à " "
#appeler la fonction afficher_grille(grille)
#définir la variable gagne égale à 0
#faire un boucle tant que la variable gagne est égale à 0 faire :
    #appeler la fonction tour(grille,joueur)
    #si la fonction gagnant(grille) est vraie
        #alors afficher "Bravo joueur "(la variable joueur)" tu remporte la partie !"
        #la variable gagne est égale à 1
    #sinon:
        #si la fonction match_nul(grille) est vraie
            #alors afficher "Il n'y a plus de place ! C'est donc un match nul !"
            #la variable gagne est égale à 1
    #si la variable joueur est égale à 1:
        #alors elle passe à 2
    #sinon:
        #la variable joueur est égale à 1

#FIN