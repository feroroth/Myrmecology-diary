import tkinter as tk
from PIL import Image, ImageTk
import funkcie

# Vytvoríme okno
window = tk.Tk()
window.title("Entomologický denník") # Popis okna
window.geometry("350x350")
window.configure(bg = "#4c566a", highlightbackground = "#4c566a")

# Načítanie obrázka a vytvorenie ikony
img = Image.open("Gemini_Generated_Image_fky97fky97fky97f.png")
ikona = ImageTk.PhotoImage(img)
window.iconphoto(True, ikona)

pole=tk.Entry()
pole.configure(bg = "#4c566a" , fg = "white", highlightbackground = "#3b4252", width = 40)
pole.pack()

# Tlačidlo na vypísanie textu
button = tk.Button(text="Načítaj", bg = "#4c566a", highlightbackground = "#3b4252",  command= lambda:  funkcie.read_text(canvas))
button.place(x = 30, y = 250)

# Tlačidlo na zapísanie textu do text.txt
button1 = tk.Button(text = "Zapíš", bg = "#4c566a", highlightbackground = "#3b4252", command= lambda: funkcie.write_text(pole))
button1.place(x = 110, y = 250)

# Tlačidlo na vyčistenie text.txt
button_clean = tk.Button(text = "clean", bg = "#4c566a", highlightbackground = "#3b4252", command = funkcie.clean)
button_clean.place(x = 180, y = 250)

# ťlačidlo na spočítanie počtu druhov
button_counter = tk.Button(text= "counter", bg = "#4c566a", highlightbackground = "#3b4252" , command = lambda: funkcie.compare())
button_counter.place(x = 250, y = 250)


button_reset = tk.Button(text = "reset", bg = "#3b4252", highlightbackground = "#3b4252", command = lambda: funkcie.reset(canvas))
button_reset.place(x = 150, y = 290)

# Vytvoríme Canvas
canvas = tk.Canvas(window, width=300, height=150, bg = "#4c566a", highlightbackground = "#4c566a")
canvas.pack(pady=20)

canvas.create_text(150,10, text="Ahoj")

window.mainloop()
canvas.mainloop()