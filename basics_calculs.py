
resultat = 0
saisie_en_cours = ""


def supprimer_dernier_chiffre():
    global saisie_en_cours
    saisie_en_cours = saisie_en_cours[:-1]
    if saisie_en_cours == "":
        saisie_en_cours = "0"
    return saisie_en_cours

def ajouter_chiffre(chiffre):
    global saisie_en_cours
    if saisie_en_cours == "0":
        saisie_en_cours = str(chiffre)
    else:
        saisie_en_cours = saisie_en_cours + str(chiffre)
    return saisie_en_cours

def lire_saisie():
    global saisie_en_cours
    if saisie_en_cours == "" or saisie_en_cours == "0":
        return 0
    return float(saisie_en_cours)

def effacer():
    global resultat, saisie_en_cours
    resultat = 0
    saisie_en_cours = "0"
    return resultat

def egal(premier, operation, deuxieme):
    global resultat
    premier = float(premier)
    deuxieme = float(deuxieme)

    if operation == "+":
        resultat = premier + deuxieme

    elif operation == "-":
        resultat = premier - deuxieme

    elif operation in ["*", "×"]:
        resultat = premier * deuxieme

    elif operation in ["/", "÷"]:
        if deuxieme == 0:
            return "Erreur : division par zéro impossible !"
        resultat = premier / deuxieme

    else:
        return "Erreur : opération non reconnue"

    return formater(resultat)

def formater(nombre):
    if isinstance(nombre, str):
        return nombre
    if nombre % 1 == 0:
        return int(nombre)
    return nombre
