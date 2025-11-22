from tkinter import *

def main():
# Création du fenêtre 
    fenetre = Tk()
    fenetre.title("ToDo")
    fenetre.geometry("800x600")
    fenetre.configure(bg = "ivory")


    #keys configure
    # print(fenetre.configure().keys())

    fenetre.rowconfigure(1, weight =1)
    fenetre.columnconfigure(0, weight =1)


    bouton = Button(fenetre, text = "Add")
    label = Label(fenetre, text = "Hello World", bg='black', )
    

    # canvas = Canvas(fenetre, width= 850 , height = 850, background= 'ivory')
    # canvas.grid(row = 1, column = 3, pady = 6)

    # liste de case à cocher dans laquelle un seul élément peut être choisi 
    # bouton2 = tkinter.Radiobutton(fenetre, text="Non", variable=tkinter.StringVar(), value=2)
    # bouton2.pack()

    # bar d'écriture 
    bar_write = Entry(fenetre, font=("Calibiri 10") )
    bar_write

    # print(Entry().keys())

    bar_write.grid(row = 0, column = 0, sticky="ew", padx = 10, pady= 20)
    bouton.grid(row = 0, column = 3, padx = 5)
    # label.grid()



    # Loop
    fenetre.mainloop()

main()