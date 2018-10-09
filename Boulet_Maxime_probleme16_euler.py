def solve(n) : 
    """Entree: un entier n
    Sortie: la somme des digits de 2**n"""
    somme = 0
    objet = str(2**n)
    for digit in objet :
        somme += int(digit)
    return somme

assert solve(15) == 26

print(solve(1000))