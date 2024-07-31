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
            print("Trop court !")
            cover = 0
        elif ligne >= "3":
            print("Trop long !")
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

def gagnant(grille):
    if (grille[0]==grille[1]) and (grille[0]==grille[2]) and (grille[0]!=" "):
        return 1
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

def match_nul(grille):
    for i in range(9):
        if grille[i]==" ":
            return 0
    return 1


#DEBUT

joueur = 1
print("Joueur 1 tu possède les X, Joueur 2 tu possède les O")
print("Que le match COMMENCE !!!")
grille=[" "," "," "," "," "," "," "," "," "]
afficher_grille(grille)
gagne = 0
while gagne == 0:
    tour(grille,joueur)
    if gagnant(grille):
        print("Bravo joueur "+str(joueur)+" tu remporte la partie !")
        gagne = 1
    else:
        if match_nul(grille):
            print("Il n'y a plus de place ! C'est donc un match nul !")
            gagne = 1
    if joueur == 1:
        joueur = 2
    else:
        joueur = 1

#FIN