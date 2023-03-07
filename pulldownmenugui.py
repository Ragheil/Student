from tkinter import *

root = Tk()
root.title('MENU WITH SQLITE')

root.configure(bg='orange')
from tkinter.filedialog import asksaveasfile, askopenfilename


def OpeningFile():
    root.destroy()
    import pass2



# Creating Menubar
menubar = Menu(root)

# Adding File Menu and commands
# Adding File Menu and commands

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='Exit', command=root.destroy)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Select All', command=None)
edit.add_separator()
edit.add_command(label='Find ...', command=None)
edit.add_command(label='Delete...', command=None)

# Adding Option Menu
option = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Option', menu=option)
option.add_command(label='Log-in Account', command=OpeningFile)



# Adding Help Menu
help_ = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help_)


mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=100, padx=100)

# Create a Tkinter variable
tkvar = StringVar(root)
text="MUSICIAN IDENTIFIER\n",

# display Menu
root.config(menu=menubar)
root.configure(bg='#CCCCCC')
root.geometry('400x250')

root.mainloop()
