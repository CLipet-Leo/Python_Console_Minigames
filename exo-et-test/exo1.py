#DEBUT
# def salaireNet(brut, coeff):
    # return brut - brut*  coeff

def salaireParSeconde(salaireHoraire,heureParJourOuvre, jourOuvreParAn):
    #Calculer mon salaire annuel 
    salaireAnnuel = salaireHoraire * heureParJourOuvre * jourOuvreParAn
    #Calculer le nombre de secondes dans une année 
    nbSecondesParAn = 365*24*60*60
    #Je pose et retourne la division  
    return salaireAnnuel / nbSecondesParAn

#Definir une fonction withdrawFees qui retire un pourcentage a un total en fonction d'un total et d'un pourcentage
def withdrawFees(total, percent):
    #Definir fees en fonction d'un total et d'un pourcentage
    fees= total * (percent/100)
    #soustraire fees au total
    result = total - fees
    #retourner la valeur obtenue
    return result
#Definir une fonction qui retourne le salaire net en fonction du salaire brut (float) et du secteur d'activité (isPublic > booleen)
def calculBrutEnNet(salaireBrut, isPublic):
    #Si je suis un travailleur du secteur public
    if isPublic: 
        #Alors je soustrais 15 % de mon salaire Brut a mon salaire brut et je l'assigne a la variable salaireNet
        salaireNet = withdrawFees(salaireBrut, 15)
    #Sinon : Je suis un travailleur du secteur privé
    else:
        #Alors je soustrais 23 % de mon salaire Brut a mon salaire brut et je l'assigne a la variable salaireNet
            salaireNet = withdrawFees(salaireBrut, 23)


    #Retourner salaireNet
    return salaireNet

#FIN




#DEBUT
assertionFinale  = (( (365 * 3) / (24 - (16 - 8)) ) * (rh)  > r) == (e * s  < r)

assertionFinaleDeux = ((365 * 3) / (4 - (12 - 8)) * (rh)  > r) == (e * s  < r)

def retournerSixPlusTrois():
    return 6 + 3
def retournerYPlusX(x, y):
    return y + x

ECRIRE "BONJOUR MONDE"
PRINT "HELLO WORLD"
retournerSixPlusTrois()
retournerSixPlusX(9, 4)
print("Qui vole un " + retournerSixPlusTrois() + " Vole un boeuf ")



#FIN