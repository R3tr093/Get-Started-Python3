# Voici un exemple d'une condition en Python


a = -5

# On écrit if suivi de la condition et on ferme avec :

# Ensuite on passe à la ligne, on décale de 4 espaces, et on écris les instructions.

if a > 0 : # Si a est supérieur à 0
    print (" a est positif. " )


elif a < 0 : # si est inférieur à O.
    print (" a est négatif.")


# Si on veut ajouter une close else, elle dois ce situer au même niveau d'indentation, suivi d'un :

else :
    print (" a est nul, a vaut 0")

# Les opérateurs de comparaison 

# Les conditions doivent nécessairement introduire de nouveaux opérateurs, dit opérateurs de comparaison.

# Nous allons faire un petit tour rapide de ceux-ci.

# > et <, si est inférieur ou supérieur


# ==, si est égal à

# >= si est supérieur ou égal à

# <= si est inférieur ou égal à

# != si est différent de 


age = 18


if age >= 18 :
    print (" Vous avez la majorité dans votre pays de résidence et le droit d'entrer sur notre site web.")

elif  age <= 16 : 
    print (" Vous n'avez pas encore la majorité et ne pouvez accéder qu'a une portion du site web.")

elif age <= 12 :
    print ("Désolé, vous n'avez pas le droit d'accéder à notre site web.")

else : 
    print ("Veuillez définir un nombre positif.")

  # La condition qui suis un else, elif ou if est appelée prédicat.

  # Elle retourne toujours un booléen donc la valeur est sois True sois False.

  # Il est important de retenir que True ou False s'écrive toujours avec la première lettre en majuscule.

print ("Saviez vous qu'une condition retourne toujours un booléen donc la valeur retourne True ou False ?")

# Les mots clé and, or,not

# Il existe également les mots clé and, or, not il permette de rendre vos conditions plus efficace, courte et concise.


b = 101

if b > 0 and b < 100 : 
    print ("b est compris entre 0 et 100.")

else :
    print ("b n'est pas compris dans l'intervalle entre 0 et 100.")






