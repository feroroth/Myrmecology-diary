import tkinter as tk

#Funkcia na načítanie textu z textového súboru
def read_text(y):
    with open("text.txt") as file:
        text = file.read()
    y.create_text(50,30, text=text)

# Funkcia na zapísanie inputu z pola
def write_text(x):
    text = x.get()
    with open("text.txt", "a", encoding = "utf-8") as file:
        file.write(text+"\n")

# Funkcia na vyčistenie súboru
def clean():
    open("text.txt", "w", encoding = "utf-8")

# Funkcia na porovnanie text.txt s databázou
def compare():

    # Nové okno pre funkciu
    ro = tk.Tk()
    ro.title("Comparsion")
    ro.geometry("250x300")

    # vytvoríme canvas
    c = tk.Canvas(ro, width=250, height=300, bg="#4c566a")
    c.pack()

    # Hlavný kód funkcie
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

# Funkcia na vyčistenie plátna
def reset(y):
    y.delete("all")
    y.create_text(150, 10, text="Entomology diary")
