from tkinter import *
from tkinter .filedialog import askopenfilename, asksaveasfilename

window=Tk()
window.title("Text Editor")
window.gemetry('600x500')
window.rowconfigure(0, minisize = 800, width=1)
window.columnconfigure(1, minisize=800, width=-1)
def open_file():
    filepath = askopenfilename(
        filetypes=[("TextFiles", "*.txt"), ("All Files", "**.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0 , END)
    
    with open(filepath, "r")as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
    window.title("Text Editor - {filepath}")
def save_files():
    filepath = askopenfilename(
        defaulttextension= "txt",
    filetype=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
        window.title("Codingals Text Editor - {filepath}")
        
txt_edit = Text(window)
fr_buttons = Frame(window,relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text = "Save as....."command=save_files)

btn_open.grid(row=0, column = 0, sticky = "ew", padx = 5, pady = 5)
btn_save.grid(row=1, column = 0, sticky = "ew", padx = 5)

fr_buttons.grid(row = 0, column = 0, stick="ew")
txt_edit.grid(row = 0, column = 1, stick = "ew")

window.mainloop()