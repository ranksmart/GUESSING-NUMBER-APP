import tkinter as tk

import random

computer_guess=random.randint(1,20)



APP= tk.Tk()
APP.geometry("350x190")

#crerating a title of window
APP.title("Guessing Game")

def check():
    
            
    try:
        user_guess=int(text.get())

        if user_guess==computer_guess:
            msg="Corect! well done!!"
            label3.configure(fg="blue")
        elif user_guess>computer_guess:
            msg="you guessed high!" 
            label3.configure(fg="green")
        elif user_guess < computer_guess:
            msg="you guessed low!"
            label3.configure(fg="green")
    except:
        msg="invalid guess!"
        label3.configure(fg="red")  

    label3["text"] =msg 
    text.delete(0,10)
        
        
def reset():
    global computer_guess
    computer_guess=random.randint(1,20)
    label3["text"]="Game is reset! play again"
    text.delete(0,10)

    
#creating a label
label=tk.Label(APP,text='WELCOME TO GUESSING GAME',fg="green",bg="white")
label.pack()
label2=tk.Label(APP,text='guess the number between 1 to 20',fg="red")
label2.pack()

text=tk.Entry(width=10,border="4")
text.focus()
text.pack()


label3=tk.Label(APP,text="Good luck!!",fg="#500")
label3.pack()




#creating  a check button to check a your guess
check_btn=tk.Button(APP,text="check",fg="black", bg="orange",command=check,border="5")
check_btn.pack()
#reset button
reset_btn=tk.Button(APP,text="Reset",fg="red",bg="yellow",command=reset,border="5")
reset_btn.pack()

label4=tk.Label(APP,text=" Remember: You have 5 chance to guess ",fg="#900")
label4.pack(side="left")




APP.configure(bg="white",border=0)

APP.mainloop()
