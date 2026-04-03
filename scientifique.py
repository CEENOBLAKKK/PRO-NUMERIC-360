import math

def traiter_expression(expression):

    expression = expression.replace('π', str(math.pi))
    expression = expression.replace('e', str(math.e))
    expression = expression.replace('^', '**')
    expression = expression.replace('×', '*')
    expression = expression.replace('÷', '/')

    expression = expression.replace('sin', 'math.sin')
    expression = expression.replace('cos', 'math.cos')
    expression = expression.replace('tan', 'math.tan')
    expression = expression.replace('sqrt', 'math.sqrt')
    expression = expression.replace('log', 'math.log10')
    expression = expression.replace('ln', 'math.log')

    return expression


def calculer(expression):
    try:
        expression = traiter_expression(expression)
        return eval(expression)
    except:
        return "Erreur"


def supprimer(texte):
    return texte[:-1]
