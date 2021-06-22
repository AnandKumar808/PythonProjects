from tkinter import*
from tkinter import messagebox
import random
# Importing random,tkinter and messagebox


random_num=random.randint(0,100)   #Generating a random number 
attempts=8

def help_me():
    # Don't get panic when seeing the lower line
    messagebox.showinfo("Help","1.Guess the number between 0 to 100 \n2.Defaultly your game is in easy mode and you have 8 attempts \n3.In medium mode you get 6 attempts\n4.In hard mode you not get hint and you get 8 attempts")

def medium():
    global attempts
    attempts=6
    hint_button.pack()

def hard():
    global attempts
    attempts=8
    hint_button.pack_forget()

def hintbutton():
    if random_num>=0 and random_num<=25:
        messagebox.showinfo("Hint","Hint:Guess number between 0 to 25")
    elif random_num>25 and random_num<=50:
         messagebox.showinfo("Hint","Hint:Guess number between 26 to 50")
    elif random_num>50 and random_num<=90:
         messagebox.showinfo("Hint","Hint:Guess number between 51 to 77")
    else:
        messagebox.showinfo("Hint","Hint:Guess number between 78 to 100")







#Defining the function and Validating the answer
def check():
    global attempts
    attempts-=1
    your_ans= int(input_area.get())
    if random_num==your_ans:
        messagebox.showinfo("Congrats","You are Right")
        checkbutton.pack_forget()
    elif attempts==0:
        checkbutton.pack_forget()
        messagebox.showinfo("Game Over",f"Your Attempts are over.The number was {random_num}.Start a new game")
    elif random_num<your_ans:
        messagebox.showinfo("Wrong",f"Guess a smaller number.{attempts} attempts left")
    else:
        messagebox.showinfo("Wrong",f"Guess a larger number.{attempts} attempts left")
       
   

#defining the quit button
def quit1():
    quit()

# Creating and packing the widgets
root=Tk()

root.title("Guess the number between 0 to 100")
root.geometry("400x400")

    
text=Label(root,text="Guess the number",fg="blue",font=('bold','15'))
text.pack(pady=10)

input_area=Entry(root,width=40,borderwidth=2)
input_area.pack(pady=10)




checkbutton=Button(text="Check your Answer",fg='white',bg='green',width=20,command=check)
checkbutton.pack(pady=10)

helpdesk=Button(text="Help Me",fg='white',bg='orange',width=20,command=help_me)
helpdesk.pack()

quitbutton=Button(text="Quit the Game",fg='white',bg='red',width=20,command=quit1)
quitbutton.pack(pady=10)

medmode=Button(text="Medium Mode",fg='black',bg='cyan',width=20,command=medium)
medmode.pack()

hardmode=Button(text="Hard Mode",fg='white',bg='purple',width=20,command=hard)
hardmode.pack(pady=10)

hint_button=Button(text="Hint",fg='black',bg='yellow',width=20,command=hintbutton)
hint_button.pack()

root.mainloop()
