import tkinter as tk  # name for tkinter shortened as tk
import random

def DiceRoller():
    value = random.randint(1, 6)
    dice.config(text=str(value))
    value = random.randint(1, 6)
    dicey.config(text=str(value))


win = tk.Tk()  # window
win.title("Dice Roller")  # top of window title
ButtonLabel = tk.Label(win, text="Press the button to roll the dice")
ButtonLabel.pack()
dice = tk.Label(win, fg="green")
dice.pack()
dicey = tk.Label(win, fg="blue")
dicey.pack()
DiceButton = tk.Button(win, text="Roll Dice",
                       width=25, command=DiceRoller)
DiceButton.pack()
win.mainloop()  # start of GUI
