"""On veut avoir un palindrome"""
import string
from unidecode import unidecode

#### Fonction secondaire

def ispalindrome(s):
    """L'objectif est de vérifier si s est un palindrome"""
    s = unidecode(s.replace(" ", "").lower())
    s = s.translate(str.maketrans("", "", string.punctuation))
    return s == s[::-1]

#### Fonction principale

def main():
    # vos appels à la fonction secondaire ici
    """On teste sur des chaînes de caractères la fonction ispalindrome()"""
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
