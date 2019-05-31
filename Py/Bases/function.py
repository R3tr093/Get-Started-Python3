# Ici nous allons voir comment utiliser des fonctions en python


# La syntaxe d'une fonction est la suivante

# On déclare une fonction à l'aide du mot clé def

# Viens ensuite le nom de la fonction

# Ensuite on ouvre des parenthése dans lesquelles ont peut placer des paramètres, séparés par des virgules.


i = 25
b = 9




def hello (param, param2):
    name = input(str(param) + str(param2) + "Entrez votre nom")
    print("Bonjour," + str(name))

hello(i,b)



# Voici une fonction qui indique une table de multiplication jusqu'a une limite définie par un paramètre.





def table ():
    value = input(" Entrez un nombre à multiplier :  ")
    range = input(" Définir la range : ")
    value = int(value)
    range = int(range)

    i=0
    while i < range:
        print(str(i + 1) + " * " + str(value) + " = " + str((i+1) * value))
        i = i + 1

table()        



# on peut notamment définir une valeur par défaut au paramètres

def world (param="world"):
    """ la fonction world à un paramétre qui prend la valeur world par défaut """
    print ("hello" + param)

# ici le parametre aura pour valeur world qui est assigné par défaut;
world()

name = input(" Entrez votre pseudo : " )
name : str(name)

# Ici le paramètre est une réponse de l'utilisateur.
world(name)


# Dans la fonction world on retrouve une docstring, une docstring est une chaines de caractères ouverte par trois guillements double qui permet d'utiliser la commande help(mafunction) pour donner des indicatives concernant vos fonctions.
help(world)


# En python la signature d'une fonction ou d'une variable est tout simplement son nom, aussi si vous créez une nouvelle fonction portant le même nom qu'une fonction existante, la fonction existante est écrasée pour faire place à la nouvelle;

def maFonction():
    print(" ceci est ma fonction version 1")

maFonction()

def maFonction():
    print(" Ceci est ma fonction version 2")


maFonction()

# Notons donc également qu'il n'est pas possible de surcharger une fonction en Python.


# L'instruction return, elle renvoye une valeur et met fin à l'exécution de la fonction.

def square ():
    a = 2 * 2
    b = 3 * 3
    return b
    print(" Je m'execute après le mot clé return ?")
           


square()
print(square())

#Il est possible d'utiliser les fonctions lambdas en python, une fonction lambda est une fonction composé d'une seule instruction voir ci- dessous.

f = lambda x : print(str(x * x))

print (" Retour de la fonction lambda f : " )

f(25)

# Une fonction lambda peut cependant avoir plusieurs paramètres.

g = lambda x, z: print(str(x * z))

print(" Retour de la fonction lambda g : ")

g(6,8)


        # END 
