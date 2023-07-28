from tkinter import *

window = Tk()

window.title("Travel-Form")

window.geometry("600x400")
window.config(bg="LightCyan2")

heading = Label(window, text="Travel - Form", font=("Times New Roman", 24, "bold"), bg="LightCyan2", fg="cyan4").grid(column=2, pady=10)

name = Label(window, text="Name ", font=("Times New Roman",20,"bold"), fg="cyan4", bg="LightCyan2", justify=LEFT).grid(row=1, column=1, padx=5)

namevalue = StringVar()

nameentry = Entry(window, textvariable=namevalue).grid(row=1, column=2)


phone = Label(window, text="Phone ", font=("Times New Roman",20,"bold"), fg="cyan4", bg="LightCyan2").grid(row=2, column=1, padx=5)

phonevalue = StringVar()

phoneentry = Entry(window, textvariable=phonevalue).grid(row=2, column=2)



Gender = Label(window, text="Gender ", font=("Times New Roman",20,"bold"), fg="cyan4", bg="LightCyan2").grid(row=3, column=1, padx=5)

gendervalue = StringVar()

genderentry = Entry(window, textvariable=gendervalue).grid(row=3, column=2)



Email = Label(window, text="Email ", font=("Times New Roman",20,"bold"), fg="cyan4", bg="LightCyan2").grid(row=4, column=1, padx=5)

emailvalue = StringVar()

emailentry = Entry(window, textvariable=emailvalue).grid(row=4, column=2)


Emergency_Contact = Label(window, text="Emergency\nContact ", font=("Times New Roman",20,"bold"), fg="cyan4", bg="LightCyan2").grid(row=5, column=1, padx=5)

contactvalue = StringVar()

contactentry = Entry(window, textvariable=contactvalue).grid(row=5, column=2)

checkvalue = IntVar()
checkbox = Checkbutton(window, text="I have read the terms and conditions.",variable=checkvalue,font=("Times New Roman",10,"bold"), fg="cyan4", bg="LightCyan2"  ).grid(row=6, column=1)


def submit():
    f = open("travel-info.txt", "a")
    f.truncate(0)
    f.write(f"The name of passanger is {namevalue.get()}\n")
    f.write(f"The Phone Number of passanger is {phonevalue.get()}\n")
    f.write(f"The gender of passanger is {gendervalue.get()}\n")
    f.write(f"The Email of passanger is {emailvalue.get()}\n")
    f.write(f"The Emergency Contact Number of passanger is {contactvalue.get()}\n")
   

button = Button(window, text="Submit", command=submit).grid(row=7, column=2)


window.mainloop()