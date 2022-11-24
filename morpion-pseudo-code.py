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

#BOT

#définir une fonction Bot
#Si choix joueur  est égale à 2 alors:
    #définir une liste place qui va du nombre 0 à 8

    #conditions de victoires
    #si (case[0] est égale à case[1]) ET (case[0] est égale à "O") ET (case[2] n'est pas égale à "X"):
        #alors placer "O" dans la case[2]
    #sinon si (case[2] est égale à case[1]) ET (case[2] est égale à "O") ET (case[0] n'est pas égale à "X"):
        #alors placer "O" dans la case[0]
    #sinon si (case[0] est égale à case[2]) ET (case[0] est égale à "O") ET (case[1] n'est pas égale à "X"):
        #alors placer "O" dans la case[1]
    #sinon si (case[3] est égale à case[4]) ET (case[3] est égale à "O") ET (case[5] n'est pas égale à "X"):
        #alors placer "O" dans la case[5]
    #sinon si (case[5] est égale à case[4]) ET (case[5] est égale à "O") ET (case[3] n'est pas égale à "X"):
        #alors placer "O" dans la case[3]
    #sinon si (case[3] est égale à case[5]) ET (case[5] est égale à "O") ET (case[4] n'est pas égale à "X"):
        #alors placer "O" dans la case[4]
    #sinon si (case[6] est égale à case[7]) ET (case[6] est égale à "O") ET (case[8] n'est pas égale à "X"):
        #alors placer "O" dans la case[8]
    #sinon si (case[8] est égale à case[7]) ET (case[8] est égale à "O") ET (case[6] n'est pas égale à "X"):
        #alors placer "O" dans la case[6]
    #sinon si (case[6] est égale à case[8]) ET (case[6] est égale à "O") ET (case[7] n'est pas égale à "X"):
        #alors placer "O" dans la case[7]
    #sinon si (case[0] est égale à case[3]) ET (case[0] est égale à "O") ET (case[6] n'est pas égale à "X"):
        #alors placer "O" dans la case[6]
    #sinon si (case[3] est égale à case[6]) ET (case[3] est égale à "O") ET (case[0] n'est pas égale à "X"):
        #alors placer "O" dans la case[0]
    #sinon si (case[0] est égale à case[6]) ET (case[0] est égale à "O") ET (case[3] n'est pas égale à "X"):
        #alors placer "O" dans la case[3]
    #sinon si (case[1] est égale à case[4]) ET (case[1] est égale à "O") ET (case[7] n'est pas égale à "X"):
        #alors placer "O" dans la case[7]
    #sinon si (case[4] est égale à case[7]) ET (case[7] est égale à "O") ET (case[1] n'est pas égale à "X"):
        #alors placer "O" dans la case[1]
    #sinon si (case[1] est égale à case[7]) ET (case[7] est égale à "O") ET (case[4] n'est pas égale à "X"):
        #alors placer "O" dans la case[4]
    #sinon si (case[2] est égale à case[5]) ET (case[2] est égale à "O") ET (case[8] n'est pas égale à "X"):
        #alors placer "O" dans la case[8]
    #sinon si (case[8] est égale à case[5]) ET (case[8] est égale à "O") ET (case[2] n'est pas égale à "X"):
        #alors placer "O" dans la case[2]
    #sinon si (case[2] est égale à case[8]) ET (case[2] est égale à "O") ET (case[5] n'est pas égale à "X"):
        #alors placer "O" dans la case[5]
    #sinon si (case[0] est égale à case[4]) ET (case[0] est égale à "O") ET (case[8] n'est pas égale à "X"):
        #alors placer "O" dans la case[8]
    #sinon si (case[4] est égale à case[8]) ET (case[4] est égale à "O") ET (case[0] n'est pas égale à "X"):
        #alors placer "O" dans la case[0]
    #sinon si (case[0] est égale à case[8]) ET (case[0] est égale à "O") ET (case[4] n'est pas égale à "X"):
        #alors placer "O" dans la case[4]
    #sinon si (case[2] est égale à case[4]) ET (case[2] est égale à "O") ET (case[6] n'est pas égale à "X"):
        #alors placer "O" dans la case[6]
    #sinon si (case[6] est égale à case[4]) ET (case[6] est égale à "O") ET (case[2] n'est pas égale à "X"):
        #alors placer "O" dans la case[2]
    #sinon si (case[2] est égale à case[6]) ET (case[2] est égale à "O") ET (case[4] n'est pas égale à "X"):
        #alors placer "O" dans la case[4]

    #conditions de blocages
    #sinon si (grille[0] est égale à grille[1]) ET (grille[0] est égale à "X") ET (grille[2] n'est pas égale à "O"):
        #alors placer "O" dans la case[2]
    #sinon si (grille[2] est égale à grille[1]) ET (grille[2] est égale à "X") ET (grille[0] n'est pas égale à "O"):
        #alors placer "O" dans la case[0]
    #sinon si (grille[0] est égale à grille[2]) ET (grille[0] est égale à "X") ET (grille[1] n'est pas égale à "O"):
        #alors placer "O" dans la case[1]
    #sinon si (grille[3] est égale à grille[4]) ET (grille[3] est égale à "X") ET (grille[5] n'est pas égale à "O"):
        #alors placer "O" dans la case[5]
    #sinon si (grille[5] est égale à grille[4]) ET (grille[5] est égale à "X") ET (grille[3] n'est pas égale à "O"):
        #alors placer "O" dans la case[3]
    #sinon si (grille[3] est égale à grille[5]) ET (grille[5] est égale à "X") ET (grille[4] n'est pas égale à "O"):
        #alors placer "O" dans la case[4]
    #sinon si (grille[6] est égale à grille[7]) ET (grille[6] est égale à "X") ET (grille[8] n'est pas égale à "O"):
        #alors placer "O" dans la case[8]
    #sinon si (grille[8] est égale à grille[7]) ET (grille[8] est égale à "X") ET (grille[6] n'est pas égale à "O"):
        #alors placer "O" dans la case[6]
    #sinon si (grille[6] est égale à grille[8]) ET (grille[6] est égale à "X") ET (grille[7] n'est pas égale à "O"):
        #alors placer "O" dans la case[7]
    #sinon si (grille[0] est égale à grille[3]) ET (grille[0] est égale à "X") ET (grille[6] n'est pas égale à "O"):
        #alors placer "O" dans la case[6]
    #sinon si (grille[3] est égale à grille[6]) ET (grille[3] est égale à "X") ET (grille[0] n'est pas égale à "O"):
        #alors placer "O" dans la case[0]
    #sinon si (grille[0] est égale à grille[6]) ET (grille[0] est égale à "X") ET (grille[3] n'est pas égale à "O"):
        #alors placer "O" dans la case[3]
    #sinon si (grille[1] est égale à grille[4]) ET (grille[1] est égale à "X") ET (grille[7] n'est pas égale à "O"):
        #alors placer "O" dans la case[7]
    #sinon si (grille[4] est égale à grille[7]) ET (grille[7] est égale à "X") ET (grille[1] n'est pas égale à "O"):
        #alors placer "O" dans la case[1]
    #sinon si (grille[1] est égale à grille[7]) ET (grille[7] est égale à "X") ET (grille[4] n'est pas égale à "O"):
        #alors placer "O" dans la case[4]
    #sinon si (grille[2] est égale à grille[5]) ET (grille[2] est égale à "X") ET (grille[8] n'est pas égale à "O"):
        #alors placer "O" dans la case[8]
    #sinon si (grille[8] est égale à grille[5]) ET (grille[8] est égale à "X") ET (grille[2] n'est pas égale à "O"):
        #alors placer "O" dans la case[2]
    #sinon si (grille[2] est égale à grille[8]) ET (grille[2] est égale à "X") ET (grille[5] n'est pas égale à "O"):
        #alors placer "O" dans la case[5]
    #sinon si (grille[0] est égale à grille[4]) ET (grille[0] est égale à "X") ET (grille[8] n'est pas égale à "O"):
        #alors placer "O" dans la case[8]
    #sinon si (grille[4] est égale à grille[8]) ET (grille[4] est égale à "X") ET (grille[0] n'est pas égale à "O"):
        #alors placer "O" dans la case[0]
    #sinon si (grille[0] est égale à grille[8]) ET (grille[0] est égale à "X") ET (grille[4] n'est pas égale à "O"):
        #alors placer "O" dans la case[4]
    #sinon si (grille[2] est égale à grille[4]) ET (grille[2] est égale à "X") ET (grille[6] n'est pas égale à "O"):
        #alors placer "O" dans la case[6]
    #sinon si (grille[6] est égale à grille[4]) ET (grille[6] est égale à "X") ET (grille[2] n'est pas égale à "O"):
        #alors placer "O" dans la case[2]
    #sinon si (grille[2] est égale à grille[6]) ET (grille[2] est égale à "X") ET (grille[4] n'est pas égale à "O"):
        #alors placer "O" dans la case[4]
    
    #blocage coin
    #sinon si (case[0] est égale à case[8]) ET (case[0] est égale à "X") ET (case[4] est égale à "O"):
        #alors placer "O" dans la case[3]
    #sinon si (case[2] est égale à case[6]) ET (case[2] est égale à "X") ET (case[4] est égale à "O"):
        #alors placer "O" dans la case[3]
    #sinon si (case[0] OU case[2] OU case[6] OU case[8]) est égale à "X":
        #alors placer "O" dans la case[4]
    
    #case unique
    #autre:
        #définir une variable choix qui est égale au choix d'un nb aléatoire dans la liste choix
        #tant que la case choisit par le bot est prise par un "X" ou un "O":
            #si la case est prise par un "X":
                #supprime le choix de la liste
                #rechoisit un nombre dans la liste
            #sinon si la case est prise par un "O":
                #supprime le choix de la liste
                #rechoisit un nombre dans la liste
            #sinon si la case est vide:
                #placer un "O" dans la case choisit
                #sortir de la boucle while
