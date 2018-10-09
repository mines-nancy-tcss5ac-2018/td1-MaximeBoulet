def score(NOM):
    """Entrée: un Nom
    Sortie: son score"""
    score = 0
    reference=' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for lettre in NOM:
        indice = 0
        if lettre in reference:
            while indice < 26 and reference[indice] != lettre :
                indice = indice +1 
        score = score + indice 
    return score

assert score('"COLIN"') == 53

doc = open('p022_names.txt','r')
stock=[]
for ligne in doc:
    stock += ( ligne.split(","))
print(stock)
doc.close()
newstock = sorted(stock)
print(newstock)
scoretot = 0
for i in range(len(newstock)):
    nom = newstock[i]
    scoretot = scoretot + (i+1)*score(nom)

print(scoretot)
    
