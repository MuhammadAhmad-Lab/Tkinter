from tkinter import *

screen = Tk()
screen.title("Inches -- CM")
lbl1 = Label(text = "Inches to Cm")
lbl2 = Label(text = "Enter Inches")
input2 = Entry()

def math():
    sum2 = input2.get()
    sum2 = float(sum2)
    sum2 =  sum2 * 2.54
    textbox.insert(END, sum2)
    
textbox = Text(heigh=1)
button = Button(text="Convert", command=math)

lbl1.pack()   
lbl2.pack() 
input2.pack()
button.pack()
textbox.pack()        

screen.mainloop()