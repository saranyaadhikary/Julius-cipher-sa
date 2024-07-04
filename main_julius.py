from tkinter import *
from tkinter import messagebox
import base64
import os

screen = Tk()
screen.title("Julius say something")
screen.configure(background="grey")
screen.geometry("420x420")


# ALL THE FUNCTIONS HERE

#encryption function named encrypt_julius
def encrypt_julius():
    password = code.get()
    if password =="1234":
        screen1=Toplevel(screen)
        screen1.title("Encryption window")
        screen1.geometry("400x250")
        screen1.configure(bg="pink")


        message = text_box_var.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1,text="Here is your encrypted message").place(x=5,y=6)
        text_box_var_encrypt_box = Text(screen1,font="3",bd=2,wrap=WORD)
        text_box_var_encrypt_box.place(x=2,y=25,width=390,height=180)
        text_box_var_encrypt_box.insert(END,encrypt)

    elif (password == ""):
        messagebox.showerror("Error","Please enter the secret key")

    elif (password != "1234"):
        messagebox.showerror("Wrong password","Invalid secret key")




#decryption function named encrypt_julius
def decrypt_julius():
    password = code.get()
    if password =="1234":
        screen2=Toplevel(screen)
        screen2.title("Decryption window")
        screen2.geometry("400x250")
        screen2.configure(bg="yellow")


        message = text_box_var.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen2,text="Here is your encrypted message").place(x=5,y=6)
        text_box_var_encrypt_box = Text(screen2,font="3",bd=2,wrap=WORD)
        text_box_var_encrypt_box.place(x=2,y=25,width=390,height=180)
        text_box_var_encrypt_box.insert(END,encrypt)

    elif (password == ""):
        messagebox.showerror("Error","Please enter the secret key")

    elif (password != "1234"):
        messagebox.showerror("Wrong password","Invalid secret key")





#reset function named reset_julius
def reset_julius():
    text_box_var.delete(1.0,END)
    code.set("")


#label for text to encrypted or decrypted
Label(screen,text="Enter the text for encryption and decryption",font="impack 14 bold",bg="grey").place(x=5,y=5)

#text 
text_box_var = Text(screen,font="20",bd=9)
text_box_var.place(x=2,y=45,width=420,height=120)

#label for secret key 
Label(screen,text="Enter your secret key").place(x=145,y=200)

#entry widgets for secret key
code = StringVar()
Entry(textvariable=code,bd=4,font = "20",show="*").place(x=90,y=220)

#buttons
Button(screen,text="Encrypt",font="arial 15 bold",bg="green",fg="white",command=encrypt_julius).place(x=25,y=280,width=180)
Button(screen,text="Decrypt",font="arial 15 bold",bg="Red",fg="white",command=decrypt_julius).place(x=215,y=280,width=180)
Button(screen,text="Reset",font="arial 15 bold",bg="purple",command=reset_julius).place(x=120,y=350,width=180)
mainloop()





