Mariam, tu devras modifier ce fichier en écrivant ton code ici, pour ce faire, tu vas cliquer sur le petit crayon, supprimer ce message d'information et ensuite y mettre ton code et valider les modifs


from tkinter import *


def bouton(txt, row, col, colspan=1, bg='#bdc3c7', fg='#2c3e50'):
    Button(window ,text=txt ,font=('Arial', 14, 'bold') ,bg=bg ,fg=fg  ).grid(row=row , column=col, columnspan=colspan, sticky='nsew')


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
bouton('sin(', 1, 0)
bouton('cos(', 1, 1)
bouton('tan(', 1, 2)
bouton('log10(', 1, 3)
bouton('ln(', 1, 4)
bouton('sqrt(', 1, 5)

bouton('(', 2, 0)
bouton(')', 2, 1)
bouton('π', 2, 2)
bouton('e', 2, 3)
bouton('x²', 2, 4)
bouton('n!', 2, 5)

# Nombres a gauche
bouton('7', 3, 0)
bouton('8', 3, 1)
bouton('9', 3, 2)
bouton('4', 4, 0)
bouton('5', 4, 1)
bouton('6', 4, 2)
bouton('1', 5, 0)
bouton('2', 5, 1)
bouton('3', 5, 2)
bouton('0', 6, 0, colspan=2)
bouton('.', 6, 2)

# Operations a droite
bouton('AC', 3, 3, bg='#3498db', fg='white')
bouton('Inv', 3, 4, bg='#3498db', fg='white')
bouton('%', 3, 5, bg='#3498db', fg='white')
bouton('÷', 4, 3, bg='#3498db', fg='white')
bouton('×', 4, 4, bg='#3498db', fg='white')
bouton('^', 4, 5, bg='#3498db', fg='white')
bouton('+', 5, 3, bg='#3498db', fg='white')
bouton('-', 5, 4, bg='#3498db', fg='white')
bouton('/', 5, 5, bg='#3498db', fg='white')
bouton('=', 6, 3, colspan=3, bg='#16a085', fg='white')

window.mainloop()
