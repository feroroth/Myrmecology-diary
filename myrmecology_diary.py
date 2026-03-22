import tkinter as tk
from PIL import Image, ImageTk
import functions

# Creatting Window
window = tk.Tk()
window.title("Myrmecology diary")
window.geometry("350x300")
window.configure(bg = "#4c566a", highlightbackground = "#4c566a")

# Creatting icon
img = Image.open("icon.png")
ikona = ImageTk.PhotoImage(img)
window.iconphoto(True, ikona)

pole=tk.Entry()
pole.config(bg = "#4c566a" , fg = "white", highlightbackground = "#3b4252", width = 40)
pole.pack()

# list of variables for Dropdown menu
days = [i + 1 for i in range(31)]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "Septeber", "October", "November", "December"]

# Setting variables
opt1 = tk.StringVar(value = "January")
opt2 = tk.IntVar(value = 1)

# Dropdown menu
option1 = tk.OptionMenu(window, opt1, *months)
option1.config(bg = "#4c566a" , fg = "white", highlightbackground = "#3b4252")
option1.place(x = 75, y = 30)
option2 = tk.OptionMenu(window, opt2, *days)
option2.config(bg = "#4c566a" , fg = "white", highlightbackground = "#3b4252")
option2.place(x = 15, y = 30)

# Button for writting text
button = tk.Button(text = "Ants", bg = "#4c566a", highlightbackground = "#3b4252",  command= lambda:  functions.read_text())
button.place(x = 35, y = 250)

# Button for adding text into text.txt
button1 = tk.Button(text = "Upload", bg = "#4c566a", highlightbackground = "#3b4252", command= lambda: functions.write_text(pole, opt1, opt2))
button1.place(x = 100, y = 250)

# Button for clearing text.txt
button_clean = tk.Button(text = "clean", bg = "#4c566a", highlightbackground = "#3b4252", command = functions.clean)
button_clean.place(x = 180, y = 250)

# Button for counting a species
button_counter = tk.Button(text= "counter", bg = "#4c566a", highlightbackground = "#3b4252" , command = lambda: functions.compare())
button_counter.place(x = 250, y = 250)

window.mainloop()
