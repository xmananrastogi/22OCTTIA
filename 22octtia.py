import tkinter as tk
from tkinter import messagebox

def move_no_button():
    x = no_button.winfo_x()
    y = no_button.winfo_y()
    new_x = (x + 50) % 300
    new_y = (y + 50) % 200
    no_button.place(x=new_x, y=new_y)

def yes_clicked():
    messagebox.showinfo("Hurrayyyy!!", "Hurrayyyy!!")
    root.destroy()

root = tk.Tk()
root.title("CAN I BE YOUR BOYFRIEND or WILL YOU BE MY GIRLFRIEND ?")
root.geometry("400x300")
root.configure(bg="#BDE17A")

header = tk.Label(root, text="CAN I BE YOUR BOYFRIEND or\nWILL YOU BE MY GIRLFRIEND ?",
                  font=("Nunito", 16, "bold"), bg="#BDE17A", fg="white")
header.pack(pady=20)

subtext = tk.Label(root, text="obv you wanna be my girlfriend shutup",
                   font=("Nunito", 12), bg="#BDE17A", fg="white")
subtext.pack()

yes_button = tk.Button(root, text="Yes", command=yes_clicked,
                       bg="white", fg="#E93030", font=("Nunito", 12),
                       padx=15, pady=10, borderwidth=0, relief="flat")
yes_button.place(x=100, y=150)

no_button = tk.Button(root, text="No", command=move_no_button,
                      bg="white", fg="#E93030", font=("Nunito", 12),
                      padx=15, pady=10, borderwidth=0, relief="flat")
no_button.place(x=250, y=150)

root.mainloop()
