from tkinter import Tk,messagebox,simpledialog
messagebox.showinfo("To the people" ,"hello world")
userInput= simpledialog.askstring("","what is your favorite board game?")
if userInput=="snakes and latters ":
    messagebox.showinfo("board game","Hey, me too!!!!")
else:
    messagebox.showinfo("board game","that is cool")
