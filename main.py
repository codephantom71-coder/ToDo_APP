# Import tkinter 
from tkinter import *
from tkinter import font

# Add task function
def add_task(event, paned_W, fenetre, bar):
    # Get the value of Entry, store in a variable and after delete the text to input some new task 
    def get_text_bar(bar):
        print("get_text_bar function is running")
        txt = bar.get()
        print(result)
        bar.delete(0, END)
        return txt 
    result = get_text_bar(bar)
    print("Add boutton")
    paned_W.add(Checkbutton(fenetre, text='test',))
    result = bar.get()
    print(result)
    bar.delete(0, END)


# Get the position of the mouse
def get_position(event):
    print(event.x, event.y)




#Main function 
def main():
# Creation of the window 
    fenetre = Tk()
    fenetre.title("ToDo")
    fenetre.geometry("800x600")
    fenetre.configure(bg = "ivory")


    # Window configure
    fenetre.rowconfigure(1, weight =1)
    fenetre.columnconfigure(0, weight =1)

    # Creation of add Button
    bouton = Button(fenetre, text = "Add", width= 10, height=3 )

    

    # bar d'écriture 
    bar_write = Entry(fenetre, font=("mononoki 30"), border= 1, highlightthickness = 2, highlightbackground ="#262626", )
    
    # PanedWindow
    p = PanedWindow(fenetre, orient='vertical')
    p.add(Label(p, text = "Essaie"))


    
    # Add widgets
    bar_write.grid(row = 0, column = 0, sticky="ew", padx = 5, pady= 10)
    bouton.grid(row = 0, column = 1, padx = 10)
    p.grid(row = 1, column=0,columnspan = 2, sticky= 'ewns', padx = 5)

    # Bind function with 'add buton'
    bouton.bind("<Button-1>", lambda event: add_task(event, p, fenetre, bar_write))

    # Bind function with 'bar_write'
    bar_write.bind("<Return>", lambda event: get_text_bar(event, bar_write))


    # Loop
    fenetre.mainloop()


#Usin main function
main()