# Pour gérer les évenements on dispose d'outils tels que les conditions, les boucles

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



#Voici un exemple de l'utilisation de and.

b = 101

if b > 0 and b < 100 : 
    print ("b est compris entre 0 et 100.")

else :
    print ("b n'est pas compris dans l'intervalle entre 0 et 100.")



# Voici un exemple de l'utilisation de or.

c = 50

if c > 50 or c < 45 :
    print (" la variable c à une valeur supérieur à 50 ou inférieur à 45")
else:
    print (" La variable c a une valeur comprise entre 45 et 50 ") 



# Voici un exemple de l'utilisation de not.


password = False

if password is not True : 
    print (" Mot de passe valide ! ")


else :

    print("Mot de passe invalide !") 
#Le mot clé break permet de sortir d'une boucle


d = 0
while d < 100:
    d = d + 1
    print(str(d))
    if d > 20:
        break

# Le mot clé continue permet de continuer une boucle en revenant au début.

p = 1

while p < 20 :
    if p % 3 == 0:
        p += 4
        print(" On incrémente p de 4. p est maintenant égal à : " + str(p))
        continue
    print(" La variable p = ", str(p))
    p += 1


print( "Vous remarquez qu'avec le mot clé continue chaque fois que p est divisble par 3, on l'incrémente de 4 et on reviens au début de la boucle sans la termine. c'est à dire sans incrémenter p de 1 ")
