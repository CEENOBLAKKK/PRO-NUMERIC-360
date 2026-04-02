from tkinter import *

window = Tk()
window.title("PRO NUMERIC 360")
window.geometry("620x500")  
window.configure(bg="#e6dbdb")  

def affichage(valeur):
    if valeur == "AC":
        entree.delete(0, END)
        entree.insert(END, "0")
    elif valeur == "DEL":
        actuel = entree.get()
        entree.delete(0, END)
        entree.insert(END, actuel[:-1] if len(actuel) > 1 else "0")
    else:
        actuel = entree.get()
        if actuel == "0":
            entree.delete(0, END)
        entree.insert(END, valeur)

def bouton(txt, row, col, command, colspan=1, rowspan=1,
           bg='#ecf0f1', fg='#2d3436', font_size=11):
    btn = Button(window, text=txt, font=('Arial', font_size, 'bold'),
                 bg=bg, fg=fg, command=command, relief='flat', bd=0)
    btn.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan,
             sticky='nsew', padx=2, pady=2)
    return btn

entree = Entry(window, font=('Courier', 22, 'bold'),
               bg='#a8e6cf', fg='#1e272e',
               justify='right', bd=10, relief='flat')
entree.grid(row=0, column=0, columnspan=6, sticky='nsew', padx=10, pady=10)
entree.insert(END, "0")

scientific_buttons = [
    ('sin', 'sin('), ('cos', 'cos('), ('tan', 'tan('),
    ('x²', '^2'), ('x³', '^3'), ('xⁿ', '^'),
    ('√x', 'sqrt('), ('³√x', 'cbrt('), ('|x|', 'abs('),
    ('log', 'log('), ('ln', 'ln('), ('eˣ', 'exp('),
    ('10ˣ', '10^'), ('π', 'π'), ('e', 'e'),
    ('n!', '!'), ('1/x', '1/'), ('EXP', 'EXP')
]
row, col = 1, 0
for txt, val in scientific_buttons:
    bouton(txt, row, col, lambda v=val: affichage(v),
           bg='#6c5ce7', fg='white', font_size=10)
    col += 1
    if col > 5:  
        col = 0
        row += 1

bouton('7', 4, 0, lambda: affichage('7'), font_size=14)
bouton('8', 4, 1, lambda: affichage('8'), font_size=14)
bouton('9', 4, 2, lambda: affichage('9'), font_size=14)
bouton('DEL', 4, 3, lambda: affichage('DEL'), bg='#e74c3c', fg='white')
bouton('AC', 4, 4, lambda: affichage('AC'), bg='#27ae60', fg='white', colspan=2)

bouton('4', 5, 0, lambda: affichage('4'), font_size=14)
bouton('5', 5, 1, lambda: affichage('5'), font_size=14)
bouton('6', 5, 2, lambda: affichage('6'), font_size=14)
bouton('×', 5, 3, lambda: affichage('×'), bg='#00cec9', fg='white')
bouton('÷', 5, 4, lambda: affichage('÷'), bg='#00cec9', fg='white')
bouton('^', 5, 5, lambda: affichage('^'), bg='#00cec9', fg='white')

bouton('1', 6, 0, lambda: affichage('1'), font_size=14)
bouton('2', 6, 1, lambda: affichage('2'), font_size=14)
bouton('3', 6, 2, lambda: affichage('3'), font_size=14)
bouton('+', 6, 3, lambda: affichage('+'), bg='#00cec9', fg='white')
bouton('-', 6, 4, lambda: affichage('-'), bg='#00cec9', fg='white')
bouton('Ans', 6, 5, lambda: affichage('Ans'), bg='#00cec9', fg='white')

bouton('0', 7, 0, lambda: affichage('0'), colspan=2, font_size=14)
bouton('.', 7, 2, lambda: affichage('.'), font_size=14)
bouton('=', 7, 3, lambda: affichage('='), colspan=3, bg='#0984e3', fg='white', font_size=14)

for i in range(6): window.columnconfigure(i, weight=1)
for i in range(8): window.rowconfigure(i, weight=1)

window.mainloop()
