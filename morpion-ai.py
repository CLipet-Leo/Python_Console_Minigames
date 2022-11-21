def afficher_grille(grille):
    print("     0)  1)  2)")
    print("   -------------")
    print("0)", end='')
    for i in range(3):
        print(" | "+str(grille[i]), end='')
    print(" |")
    print("   -------------")
    print("1)", end='')
    for i in range(3):
        print(" | "+str(grille[i+3]), end='')
    print(" |")
    print("   -------------")
    print("2)", end='')
    for i in range(3):
        print(" | "+str(grille[i+6]), end='')
    print(" |")
    print("   -------------")

def tour(grille,joueur):
    print("C'est à toi joueur "+str(joueur))
    cover = 0
    liver = 0
    while cover == 0 or liver == 0:
        colonne = input("Le numero de colonne que tu veux jouer : ")
        ligne = input("Et maintenant la ligne : ")
        if grille[int(colonne)+int(ligne)*3]!=" ":
            afficher_grille(grille)
            print("Cette case est déjà prise >:( selectionne un autre case !")
        elif colonne >= "3":
            print("ta mère la pute tu sais pas écrire")
            cover = 0
        elif ligne >= "3":
            print("ta mère la pute tu sais pas écrire")
            liver = 0
        else:
            print("OK ! C'est placé dans la case ("+colonne+","+ligne+")")
            cover = 1
            liver = 1
            break
    
    if joueur == 1:
        grille[int(colonne)+int(ligne)*3]="X"
    if joueur == 2:
        grille[int(colonne)+int(ligne)*3]="O"
    afficher_grille(grille)

#définir une fonction gagnant() avec comme paramètre grille
def gagnant(grille):
    #si case(...) est prise ET case(...) est prise ET case(...) est différente de " "
    if (grille[0]==grille[1]) and (grille[0]==grille[2]) and (grille[0]!=" "):
        #alors retourner la valeur 1
        return 1
    #repeter la boucle du dessu 8 fois (le nombre de possibilité de gagner au morpion)
    if (grille[3]==grille[4]) and (grille[3]==grille[5]) and (grille[3]!=" "):
        return 1
    if (grille[6]==grille[7]) and (grille[6]==grille[8]) and (grille[6]!=" "):
        return 1
    if (grille[0]==grille[3]) and (grille[0]==grille[6]) and (grille[0]!=" "):
        return 1
    if (grille[1]==grille[4]) and (grille[1]==grille[7]) and (grille[1]!=" "):
        return 1
    if (grille[2]==grille[5]) and (grille[2]==grille[8]) and (grille[2]!=" "):
        return 1
    if (grille[0]==grille[4]) and (grille[0]==grille[8]) and (grille[0]!=" "):
        return 1
    if (grille[2]==grille[4]) and (grille[2]==grille[6]) and (grille[2]!=" "):
        return 1

#définir une fonction match_nul() avec comme paramètre grille
def match_nul(grille):
    #pour i le nombre de case sur la grille allant jusqu'à 9
    for i in range(9):
        #si la valeur grille ayant comme paramètre i est égale à " " (c'est à dire qu'aucune ligne n'a été former par un joueur)
        if grille[i]==" ":
            #alors retourner la valeur 0
            return 0
    #retourner la valeur 1
    return 1


#DEBUT

#définir la variable joueur est égale à 1
joueur = 1
#afficher "Joueur 1 tu possède les X, Joueur 2 tu possède les O"
print("Joueur 1 tu possède les X, Joueur 2 tu possède les O")
#afficher "Que le match COMMENCE !!!"
print("Que le match COMMENCE !!!")
#définir que les cases de la variable grille sont égale à " "
grille=[" "," "," "," "," "," "," "," "," "]
#appeler la fonction afficher_grille(grille)
afficher_grille(grille)
#définir la variable gagne égale à 0
gagne = 0
#faire un boucle tant que la variable gagne est égale à 0 faire :
while gagne == 0:
    #appeler la fonction tour(grille,joueur)
    tour(grille,joueur)
    #si la fonction gagnant(grille) est vraie
    if gagnant(grille):
        #alors afficher "Bravo joueur "(la variable joueur)" tu remporte la partie !"
        print("Bravo joueur "+str(joueur)+" tu remporte la partie !")
        #la variable gagne est égale à 1
        gagne = 1
    #sinon:
    else:
        #si la fonction match_nul(grille) est vraie
        if match_nul(grille):
            #alors afficher "Il n'y a plus de place ! C'est donc un match nul !"
            print("Il n'y a plus de place ! C'est donc un match nul !")
            #la variable gagne est égale à 1
            gagne = 1
    #si la variable joueur est égale à 1:
    if joueur == 1:
        #alors elle passe à 2
        joueur = 2
    #sinon:
    else:
        #la variable joueur est égale à 1
        joueur = 1

#FIN