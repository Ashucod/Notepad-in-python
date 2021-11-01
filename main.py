from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("500x600")
root.title("My Notepad")

def save_file():
      open_file = filedialog.asksaveasfile(mode='w',defaultextension="*.txt")
      if open_file is None:
            return
      text = str(Entry.get(1.0, END))
      open_file.write(text)
      open_file.close()
def clear():
      Entry.delete(1.0, END)
def open_file():
      file = filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')])
      if file is not None:
            content=file.read()
            Entry.insert(INSERT, content)

b1 = Button(root, text = "Save", command = save_file)
b1.place(x=10, y=10)

b2 = Button(root, text = "Clear all", command = clear)
b2.place(x=50, y=10)

b3 = Button(root, text = "Open", command = open_file)
b3.place(x=108, y=10)

Entry = Text(root, height=33, width=58, wrap=WORD)
Entry.place(x=10, y=50)

root.mainloop()