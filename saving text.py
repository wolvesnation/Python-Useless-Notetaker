from tkinter import *
window = Tk()
window.title("Twitch Notes")
window.configure(background='grey')
lbl = Label(window, text="Stream Idea:")
lbl.grid(column=0, row=0)
txt = Entry(window,width=35)
txt.grid(column=1, row=0)


def clicked():
    inputt = "" + txt.get()
    with open("Ideas.txt", "a") as text_file:
        text_file.write(inputt+'\n')
btn = Button(window, text="Write", command=clicked)
btn.grid(column=2, row=0)
def wiped():
    with open("Ideas.txt", "w"): pass
tup = Button(window, text="Wipe File", command=wiped)
tup.grid(column=1, row=1)
window.mainloop()
