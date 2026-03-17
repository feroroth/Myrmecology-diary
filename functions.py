import tkinter as tk

#Function for writting input on canvas
def read_text(y):
    with open("text.txt") as file:
        textt = file.read()
    y.create_text(50,30, text=textt)

# Function for writting input into text.txt
def write_text(x):
    text = x.get()
    with open("text.txt", "a", encoding = "utf-8") as file:
        file.write(text+"\n")

# Function for cleaning text.txt
def clean():
    open("text.txt", "w", encoding = "utf-8")

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
            for druh in file.readlines():
                druh = druh.strip()
                counter = 0
                for y in text_data:
                    if str(druh.lower().replace(" ", "")) == str(y.strip().lower().replace(" ", "")):
                        counter += 1
                if counter != 0:
                    c.create_text(75, counter2, text = "      "+druh+": "+str(counter))
                    counter2 += 13

    c.mainloop()
    ro.mainloop()

# Function of clearing window
def reset(y):
    y.delete("all")
    y.create_text(150, 10, text="Entomology diary")
