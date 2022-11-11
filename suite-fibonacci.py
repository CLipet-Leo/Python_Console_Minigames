a = 0
b = 1
x = 0

#tant que b est inferieur à 1000
while b < 1000:
    #alors afficher "x a une valeur de " le nombre x
    print("x a une valeur de ", x)
    #x est egal a la valeur de a plus la valeur de b
    x = a + b
    #a prend la valeur de b
    a = b
    #b prend la valeur de x
    b = x

