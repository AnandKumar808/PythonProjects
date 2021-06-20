from tkinter import *
from tkinter import messagebox
# Importing tkinter and messagebox

# you can increase the number of entry fields and can design on your choice


root=Tk()

root.geometry("500x300")   #Giving a size to our GUI
root.title("Your Result")   #Giving a title


def checkresult():    #defining the function when button get clicked
    
    # using int() and get() to get the integer value from entry
    total=int(computer.get())+int(physics.get())+int(maths.get())
    percent=total/300*100

    if total>300:
        messagebox.showinfo("Error","Please write number below 100 in each field")
    
    # valdating the marks system 

    if percent>=80 and percent<=100:
        messagebox.showinfo("Excellent", f"Your marks is {total}.Your percentange is {percent}%.Your grade is A and you are pass.")
    elif percent>=60 and percent<80:
        messagebox.showinfo("Great", f"Your marks is {total}.Your percentange is {percent}%.Your grade is B and you are pass.")
    elif percent>=40 and percent<60:
        messagebox.showinfo("Good! Improve more ", f"Your marks is {total}.Your percentange is {percent}%.Your grade is C and you are pass.")
    else:
        messagebox.showinfo("Focus on Study ", f"Your marks is {total}.Your percentange is {percent}%.Your are not graded and you are fail!.")







# Creating and packing the widgets

text=Label(text="Your Result",fg="green",font=('bold','15'))
text.pack(pady=15)

comp=Label(text="Computer")
comp.pack()
computer=Entry(fg="blue")
computer.pack()

phys=Label(text="Physics")
phys.pack()
physics=Entry(fg="blue")
physics.pack()

math=Label(text="Maths")
math.pack()
maths=Entry(fg="blue")
maths.pack()






b=Button(text="Check Result",command=checkresult,bg="green",fg="white")
b.pack(pady=10)







root.mainloop()
