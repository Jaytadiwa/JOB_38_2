import tkinter as tk
from tkinter import messagebox
login_window = tk.Tk()
login_window.title("login form")
login_window.geometry("390x900")
login_window.configure(bg='#333333')
import json
import os

# Check if file exists
if not os.path.exists("info.json"):
    # Create the file with a default account
    default_info = {"jhon": "1234"}
    with open("info.json", "w") as file:
        json.dump(default_info, file)  # <-- write the dictionary to the file

# Now read the info from the file
with open("info.json", "r") as file:
    info = json.load(file)  # <-- safe now, file exists and has valid JSON

print(info)  # just to check
def MkAcc():
    username=username_entry.get()
    password=password_entry.get()
    info[username]= password
    with open("info.json", "w") as file:
        json.dump(info, file)
    messagebox.showinfo(title="Registration Success" ,message="You have made an account")

def create_main_window():
    main_window= tk.Toplevel()
    login_window.withdraw()
    main_window.configure(bg="#232796")
    main_window.geometry("590x500")
    frame=tk.Frame(main_window)
    #create labels
    workout_B= tk.Button(frame,text="calorie tracker",bg="#333333", command= lambda: CalorieTracker(main_window))
    #insatiate button
    workout_B.grid(row=1,column=1,sticky="news")
    frame.pack()
def CalorieTracker(main_window):
    calorietracker= tk.Toplevel(main_window)
    main_window.withdraw()
    calorietracker.configure(bg="#232796")
    calorietracker.geometry("590x500")
    frame=tk.Frame(calorietracker)

def login():
    username= username_entry.get()
    password = password_entry.get()
    with open("info.json","r") as file:
        data =json.load(file)
    if username in data and password == data[username]:
        messagebox.showinfo(title="Login Success" ,message="You have logged in")
        create_main_window()
    else:
        messagebox.showinfo(title="Not Success", message="You need to try again")

#place everything in a frame and it become abox within the box. a box within the window frame created
frame= tk.Frame(bg="#333333")

#creating labels of login page
username_label = tk.Label(frame,text= "Username",bg='#333333', fg="#FFFFFF",font=("Arial",18))
login_label = tk.Label(frame,text="Login",bg='#333333', fg="#FFFFFF",font=("Arial",18))
username_entry= tk.Entry(frame,)
login_button = tk.Button(frame,text="Login",bg="#C5228F", fg="#FFFFFF",font=("Arial",14), command= login)
password_label =tk.Label(frame,text="Password",bg='#333333', fg="#FFFFFF",font=("Arial",18))
password_entry = tk.Entry(frame, show="*")
register_button = tk.Button(frame,text="register",bg='#333333', fg="#FFFFFF",font=("Arial",14), command= MkAcc)

#instanstiation of the label or entry in the grind
login_label.grid(row=0,column=0,columnspan=2, sticky="news",pady=40)#sticky takes up ass much space in vector north east south and west.)
username_label.grid(row=1, column=0,)
username_entry.grid(row=1,column=1,pady=20)
login_button.grid(row=3,column=0,columnspan=2,)
password_label.grid(row=2,columnspan=1,column=0, pady=20)
password_entry.grid(row=2,column=1)
register_button.grid(row=3,column=2,columnspan=2)

#place frame on screen
frame.pack()



login_window.mainloop()
