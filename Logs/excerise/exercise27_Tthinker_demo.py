__author__ = 'k22li'

########################################################################################################################
# am trying to delete text inside a text box after waiting 5 seconds, but instead the program wont run and does sleep
# over everything else.
# Also is there a way for me to just make my textbox sleep so i can run other code while the text is frozen?
########################################################################################################################

from time import time, sleep
from Tkinter import *

def empty_textbox():
    textbox.insert(END, 'This is a test')
    sleep(15)
    textbox.delete("1.0", END)

root = Tk()

frame = Frame(root, width=300, height=100)
textbox = Text(frame)

frame.pack_propagate(0)
frame.pack()
textbox.pack()

empty_textbox()

root.mainloop()


########################################################################################################################
# You really should be using something like the Tkinter after method rather than time.sleep(...).
# There's an example of using the after method at this other stackoverflow question.
# Here's a modified version of your script that uses the after method:
########################################################################################################################
from time import time, sleep
from Tkinter import *

def empty_textbox():
    textbox.delete("1.0", END)

root = Tk()

frame = Frame(root, width=300, height=100)
textbox = Text(frame)

frame.pack_propagate(0)
frame.pack()
textbox.pack()

textbox.insert(END, 'Kevin & Cathy')
textbox.after(5000, empty_textbox)

root.mainloop()