def countAndSay(n):
    sequence = [1]
    for _ in range (n-1):
        suivant = []
        for num in sequence:
            if not suivant or suivant[-1] != num:
                suivant += [1, num]
            else:
                suivant [-2] += 1
        sequence = suivant
    return "".join(map(str,sequence))

for n in range(1,11):
    print(countAndSay(n))