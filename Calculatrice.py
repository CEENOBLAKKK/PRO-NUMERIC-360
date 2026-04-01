from tkinter import *


def affichage(valeur):
    entree.insert(END , valeur)


def bouton(txt, row, col, command ,  colspan=1, bg='#bdc3c7', fg='#2c3e50'):
    Button(window ,text=txt ,font=('Arial', 14, 'bold') ,bg=bg ,fg=fg, command=command ).grid(row=row , column=col, columnspan=colspan, sticky='nsew')


window = Tk()
window.title('Calculatrice Scientifique')
window.geometry('900x620')
window.config(bg='#ecf0f1')

for i in range(6):
    window.columnconfigure(i, weight=1, minsize=80)

for i in range(8):
    window.rowconfigure(i, weight=1, minsize=70)

entree = Entry(window, font=('helvetica', 20, 'bold'), justify='right')
entree.grid(row=0, column=0, columnspan=6, sticky='nsew')

# Fonctions en haut
bouton('sin(', 1, 0, lambda: affichage('sin('))
bouton('cos(', 1, 1, lambda: affichage('cos('))
bouton('tan(', 1, 2, lambda: affichage('tan('))
bouton('log10(', 1, 3, lambda: affichage('log10('))
bouton('ln(', 1, 4, lambda: affichage('ln('))
bouton('sqrt(', 1, 5, lambda: affichage('sqrt('))

bouton('(', 2, 0, lambda: affichage('('))
bouton(')', 2, 1, lambda: affichage(')'))
bouton('π', 2, 2, lambda: affichage('π'))
bouton('e', 2, 3, lambda: affichage('e'))
bouton('x²', 2, 4, lambda: affichage('x²'))
bouton('n!', 2, 5, lambda: affichage('n!'))

# Nombres a gauche
bouton('7', 3, 0, lambda: affichage('7'))
bouton('8', 3, 1, lambda: affichage('8'))
bouton('9', 3, 2, lambda: affichage('9'))
bouton('4', 4, 0, lambda: affichage('4'))
bouton('5', 4, 1, lambda: affichage('5'))
bouton('6', 4, 2, lambda: affichage('6'))
bouton('1', 5, 0, lambda: affichage('1'))
bouton('2', 5, 1, lambda: affichage('2'))
bouton('3', 5, 2, lambda: affichage('3'))
bouton('0', 6, 0, lambda: affichage('0'), colspan=2)
bouton('.', 6, 2, lambda: affichage('.'))

# Operations a droite
bouton('AC', 3, 3, lambda:affichage("AC") ,  bg='#3498db', fg='white')
bouton('Inv', 3, 4,lambda:affichage("INV") , bg='#3498db', fg='white')
bouton('%', 3, 5, lambda: affichage('%'), bg='#3498db', fg='white')
bouton('÷', 4, 3, lambda: affichage('/'), bg='#3498db', fg='white')
bouton('×', 4, 4, lambda: affichage('*'), bg='#3498db', fg='white')
bouton('^', 4, 5, lambda: affichage('^'), bg='#3498db', fg='white')
bouton('+', 5, 3, lambda: affichage('+'), bg='#3498db', fg='white')
bouton('-', 5, 4, lambda: affichage('-'), bg='#3498db', fg='white')
bouton('/', 5, 5, lambda: affichage('/'), bg='#3498db', fg='white')
bouton('=', 6, 3, lambda:affichage("=") , colspan=3, bg='#16a085', fg='white')

window.mainloop()
