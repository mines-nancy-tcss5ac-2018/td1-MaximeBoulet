def testpalindrome ( entier ):
    """Entree: un entier
    Sortie: un booleen qui confirme ou non que la chaine est un palindrome"""
    chaine = str(entier)
    n = len(chaine)
    for i in range(n):
        if chaine[i] != chaine[n-i-1]:
            return False
    return True

assert testpalindrome(956359) == False and testpalindrome(736637) == True

def inversion(entier):
    """Entree un entier 
    Sortie l'entier dont les digits sont dans l'ordre inverse"""
    chaine = str(entier)
    res = str()
    for caractere in chaine :
        res = caractere + res 
    return int(res)

print(inversion(656554))

def solve(n):
    """Entree: un entier n
    Sortie: le nombre de nombres de lychrel en deça de n"""
    compteur=0
    for candidat in range (n):
        boucle = 0
        test = candidat
        while boucle <= 50 :
            test = test + inversion(test)
            boucle += 1
            if testpalindrome(test):
                #je précipite la fin de la boucle
                boucle += 60   
        if boucle == 51:
            compteur += 1
    return compteur

print(solve(10000))
        