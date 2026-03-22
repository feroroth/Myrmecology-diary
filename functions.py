import tkinter as tk
from tkinter import ttk

#Function for writting input on canvas
def read_text():

    # new window for function
    ro = tk.Tk()
    ro.title("Ants")
    ro.geometry("250x300")

    # Frame
    frame = tk.Frame(ro)
    frame.pack(fill = "both", expand = True)

    # Scrollbar
    scrollbar = tk.Scrollbar(frame, orient = "vertical")
    scrollbar.pack(side = "right", fill = "y")

    #creatting of canvas
    c = tk.Canvas(ro, width=400, height=400, bg="#4c566a", yscrollcommand=scrollbar.set)
    c.pack(side = "left", fill = "both", expand = True)

    scrollbar.config(command = c.yview)
    c.config(scrollregion=c.bbox("all"))

    y = 150
    with open("text.txt") as file:
        c.delete("all")
        for line in file:
            line = file.read()
            c.create_text(120,y, text = line)
            y += 5


    ro.mainloop()

# Function for writting input into text.txt
def write_text(x, y, z):

    # getting variables from dropdown menu and pole
    text = x.get()
    text_month = str(y.get())
    text_day = str(z.get())
    with open("text.txt", "a", encoding = "utf-8") as file:
        file.write(text+" "+text_day+". "+text_month+". "+"\n")

# Function for cleaning canvas
def clean():
    open("text.txt", "w").close()

# Function for comparing text.txt with database.txt
def compare():

    # new window for function
    ro = tk.Tk()
    ro.title("Comparsion")
    ro.geometry("250x300")

    #creatting of canvas
    c = tk.Canvas(ro, width=250, height=300, bg="#4c566a")
    c.pack()

    # Main code of function
    with open("database.txt") as file:
        with open("text.txt") as f:
            text_data = f.readlines()
            counter2 = 10
            
            for specie in file.readlines():
                specie = specie.strip()
                counter = 0

                for y in text_data:
                    word_specie = specie.lower().split()[:2]
                    words_y = y.strip().lower().split()[:2]

                    if word_specie == words_y:
                        counter += 1

                if counter != 0:
                    c.create_text(75, counter2, text="      " + specie + ": " + str(counter))
                    counter2 += 13

    c.mainloop()
    ro.mainloop()

# Function of clearing window
def reset(y):
    y.delete("all")
    open("text.txt", "w").close()
    
