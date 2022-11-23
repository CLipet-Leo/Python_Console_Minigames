# DEBUT

# on admet random une fonction qui renvoie une valeur aléatoire entre 1 et 3
import random
# on admet input une fonction qui renvoie la valeur qu'a donner le joueur

# définir une fonction coup() qui définis les valeurs 1, 2 et 3 en chaîne de caractères
def coup(num):
    if num == 1:
        # définir 1 = pierre
        return "pierre"
    elif num == 2:
        # définir 2 = feuille
        return "feuille"
    elif num == 3:
        # définir 3 = ciseau
        return "ciseau"
    else:
        return "Mauvaise saisie"

def contreBot():
    scoreP = 0
    scoreB = 0
    while scoreP or scoreB < 3:
        # définir coupJoueur une variable qui est égale à la fonction choixJoueur()
        coupJoueur = int(input("Quel coup veut-tu jouer : Pierre 1, Feuille 2 ou Ciseau 3 ? ", ))
        turnJoueur = coup(coupJoueur)
        print("Tu as joué ", turnJoueur)
        # définir coupBot une variable qui est égale à la fonction choixBot()
        coupBot = random.randint(1, 3)
        turnBot = coup(coupBot)
        print("Le bot a joué ", turnBot)
        # si choixJoueur == 1 alors
        if coupJoueur == 1:
            # si choixBot == 1
            if coupBot == 1:
                # alors afficher "égalité"
                print("Egalité")
            # si choixBot == 2
            elif coupBot == 2:
                # alors afficher "perdu"
                print("Perdu")
                scoreB = scoreB + 1
            # si choixBot == 3
            else:
                # alors afficher "gagné"
                print("Gagné")
                scoreP = scoreP + 1
        # si choixJoueur == 2 alors
        elif coupJoueur == 2:
            # si choixBot == 1
            if coupBot == 1:
                # alors afficher "gagné"
                print("Gagné")
                scoreP = scoreP + 1
            # si choixBot == 2
            elif coupBot == 2:
                # alors afficher "égalité"
                print("Egalité")
            # si choixBot == 3
            else:
                # alors afficher "perdu"
                print("Perdu")
                scoreB = scoreB + 1
        # si choixJoueur == 3 alors
        elif coupJoueur == 3:
            # si choixBot == 1
            if coupBot == 1:
                # alors afficher "perdu"
                print("Perdu")
                scoreB = scoreB + 1
            # si choixBot == 2
            elif coupBot == 2:
                # alors afficher "gagné"
                print("Gagné")
                scoreP = scoreP + 1
            # si choixBot == 3
            else:
                # alors afficher "égalité"
                print("Egalité")
        else:
            print("Votre choix n'est pas correct, vérifiez la valeur")
        
        print("Ton résultat est de : ", scoreP)
        print("Le résultat du BOT est de : ", scoreB)
        if scoreP == 3:
            print("Victoire du Joueur")
            break
        elif scoreB == 3:
            print("Victoire du Bot !!!! T nul")
            break

def contreJ():
    scoreP = 0
    scoreB = 0
    while scoreP or scoreB < 3:
        # définir coupJoueur une variable qui est égale à la fonction choixJoueur()
        coupJoueur1 = int(input("Quel coup veut-tu jouer joueur1 : Pierre 1, Feuille 2 ou Ciseau 3 ? ", ))
        turnJoueur1 = coup(coupJoueur1)
        print("Joueur 1 tu as joué ", turnJoueur1)
        # définir coupBot une variable qui est égale à la fonction choixBot()
        coupJoueur2 = int(input("Quel coup veut-tu jouer joueur2 : Pierre 1, Feuille 2 ou Ciseau 3 ? ", ))
        turnJoueur2 = coup(coupJoueur2)
        print("Joueur 2 tu as joué ", turnJoueur2)
        # si choixJoueur == 1 alors
        if coupJoueur1 == 1:
            # si choixBot == 1
            if coupJoueur2 == 1:
                # alors afficher "égalité"
                print("Egalité")
            # si choixBot == 2
            elif coupJoueur2 == 2:
                # alors afficher "perdu"
                scoreB = scoreB + 1
            # si choixBot == 3
            else:
                # alors afficher "gagné"
                scoreP = scoreP + 1
        # si choixJoueur == 2 alors
        elif coupJoueur1 == 2:
            # si choixBot == 1
            if coupJoueur2 == 1:
                # alors afficher "gagné"
                scoreP = scoreP + 1
            # si choixBot == 2
            elif coupJoueur2 == 2:
                # alors afficher "égalité"
                print("Egalité")
            # si choixBot == 3
            else:
                # alors afficher "perdu"
                scoreB = scoreB + 1
        # si choixJoueur == 3 alors
        elif coupJoueur1 == 3:
            # si choixBot == 1
            if coupJoueur2 == 1:
                # alors afficher "perdu"
                scoreB = scoreB + 1
            # si choixBot == 2
            elif coupJoueur2 == 2:
                # alors afficher "gagné"
                scoreP = scoreP + 1
            # si choixBot == 3
            else:
                # alors afficher "égalité"
                print("Egalité")
        else:
            print("Votre choix n'est pas correct, vérifiez la valeur")
        
        print("Score du joueur 1 : ", scoreP)
        print("Score du joueur 2 : ", scoreB)
        if scoreP == 3:
            print("Victoire du Joueur 1")
            break
        elif scoreB == 3:
            print("Victoire du Joueur 2")
            break

# appeler la fonction resultat
r=0
while r==0:
    modeDeJeu=int(input("Veut-tu jouer contre un Bot ?(entre 1) ou contre un humain ?(entre 2) : "))
    if modeDeJeu == 1:
        contreBot()
        r=r+1
        break
    elif modeDeJeu == 2:
        contreJ()
        r=r+1
        break
    else:
        print("valeur incorrecte")

# FIN