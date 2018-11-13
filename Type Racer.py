'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Tommy Ramsey IV
Typer Racer?
'''

from tkinter import ttk
from tkinter import *
import random
import time

root = Tk()

root.title("Type Racer")

root.geometry("375x200")

words = ['this','is', 'a', 'string', 'with', 'words', 'wait', 'speak', 'Monday', 'Tuesday', 'able', 'Friday', 'Acid', 'Angry', 'Automatic', 'Awake', 'Bent', 'Natural', 'Clean', 'Chemical', 'Common', 'Cruel', 'Dark', 'Dependent', 'Early', 'Loose', 'Important', 'Great']

score = 0

timeleft = 30


def clickMe():
    print('Welcome ' + nameEntered.get())

def account1():
    gh = Tk()
    gh.title("Username")
    global nameEntered

    Label(gh, text="Enter a name:").grid(column=0, row=0)
    name = StringVar()
    nameEntered = Entry(gh, width=12, textvariable=name)
    nameEntered.grid(column=0, row=1)

    Button(gh, text='Submit', command=clickMe).grid(column=2, row=12, sticky=E)

    with open('Output.txt', "w"):
        file = open("Output.txt", "a+")
        file.write(name.get())
        file.close()



def startGame(event):
    if timeleft == 30:
        global pb
        pb = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
        pb.pack()
        pb.start()

        countdown()
    nextword()


def nextword():
    global score
    global timeleft

    if timeleft > 0:

        e.focus_set()

        if e.get() == words[0]:
            score += 1

            sentence = Label(root, text=" ")
            sentence.config(text=" " + str(e.get()))
            sentence.pack()

        e.delete(0, END)

        random.shuffle(words)

        label.config(text=str(words[0]))

        scoreLabel.config(text="Score: " + str(score))

    if timeleft == 0:
        pb.stop()
        gameover = Tk()
        gameover.title("Race Results")
        scorego = Label(gameover, text="Score: " + str(score)).pack()

def countdown():
    global timeleft
    global pb

    if timeleft > 0:
        timeleft -= 1


        timeLabel.config(text="Time left: " + str(timeleft))

        timeLabel.after(1000, countdown)


def instructions():
    master = Tk()
    master.title("About")

    Label(master, text=('''.Type Racer is a game that helps you practice your typing speed and accuracy.
To play, type in the sentence that is displayed above the entry box, your goal is to try and beat your high score''')).pack()



scoreLabel = Label(root, text='Press "Enter" to begin.')
scoreLabel.pack()

timeLabel = Label(root, text="Time left: " + str(timeleft))

timeLabel.pack()

# add a label for displaying the words
label = Label(root)
label.pack()

# add a text entry box for
# typing in words
e = Entry(root)

# start the 'startGame' function
root.bind('<Return>', startGame)
e.pack()

# set focus on the entry box
e.focus_set()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Login", command=account1)
filemenu.add_separator()
filemenu.add_command(label="Sign up", command=account1)
menubar.add_cascade(label="Account", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Instructions", command=instructions)
menubar.add_cascade(label="About", menu=editmenu)

root.config(menu=menubar)

root.mainloop()
