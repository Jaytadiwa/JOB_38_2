import tkinter as tk
from tkinter import messagebox
login_window = tk.Tk()
login_window.title("login form")
login_window.geometry("390x900")
login_window.configure(bg='#333333')
import random
import json
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

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
    main_window.configure(bg='#333333')
    main_window.geometry("590x500")
    frame=tk.Frame(main_window,bg='#333333')
    #create labels
    workout_B= tk.Button(frame,text="calorie tracker",bg="#7F0587",font=("Arial",18), command= lambda: CalorieTracker(main_window))
    workout_C= tk.Button(frame,text="Workout creator",bg="#7F0587",font=("Arial",18), command= lambda: WorkoutTracker(main_window))
    #insatiate button
    workout_B.grid(row=1,column=1,sticky="news")
    workout_C.grid(row=0,column=1,sticky="news")
    frame.pack(expand=True)
def WorkoutBegun(main_window,list_Exercise):
    print(list_Exercise)
    workoutBegun= tk.Toplevel(main_window)
    main_window.withdraw()
    workoutBegun.configure(bg='#333333')
    workoutBegun.geometry("590x500")
    frame=tk.Frame(workoutBegun,bg='#333333')
    frame.pack(expand=True)
    
    CurrentIndex=0
    x=0
    y=0
    def DisplayNext():#connect this to a class to save adds steeze
        x=int(Reps.get())
        y=int(Sets.get())
        if (x < 0 or x > 50) or (y < 0 or y >= 40):
            messagebox.showinfo("Validity",message="put valid entries or to begin workout enter 0 into feilds")
        else:
            nonlocal CurrentIndex
            CurrentW.config(text=f"current workout: {list_Exercise[CurrentIndex]}")
            CurrentIndex= CurrentIndex + 1
            
            print(CurrentIndex)
            return CurrentIndex
    CurrentW= tk.Button(frame,text="Begin first Workout",font=("Arial",19),command= lambda: DisplayNext())
    Reps = tk.Entry(frame)
    Reps_L = tk.Label(frame,text="How many reps were completed",bg='#333333', fg="#FFFFFF",font=("Arial",18))
    Sets = tk.Entry(frame)
    Sets_L= tk.Label(frame,text="How many sets were completed",bg='#333333', fg="#FFFFFF",font=("Arial",18))
    generate_graph = tk.Label(frame,text="Saved data",bg="#C5228F", fg="#FFFFFF",font=("Arial",14))
    Back_button = tk.Button(frame,text="Back to home",bg="#333333", fg="#FFFFFF",font=("Arial",13), command= lambda: create_main_window())
    present_graph= tk.Button(frame,bg="#C5228F")
   
    CurrentW.grid(row=0,column=1,)
    present_graph.grid(row=3,column=1,columnspan=1,pady=40,sticky="ew")
    generate_graph.grid(row=3,column=0,columnspan=1,pady=5,sticky="ew")
    Back_button.grid(row=3,column=3,pady=20)
    Reps_L.grid(row=1,column=0,pady=20)
    Sets_L.grid(row=2,column=0,pady=20)
    Reps.grid(row=1,column=1,pady=20)
    Sets.grid(row=2,column=1,pady=20)
def WorkoutTracker(main_window):
    WorkoutTracker= tk.Toplevel(main_window)
    main_window.withdraw()
    WorkoutTracker.configure(bg='#333333')
    WorkoutTracker.geometry("590x500")
    
    
    frame=tk.Frame(WorkoutTracker,bg='#333333')
    frame.pack(expand=True)
    #Dictionary
    workout = {
    "Beginner":["pushups","squats","pull-ups"],
    "Intermediate" : ["bicep curl","tricep extension","lateral raise"],
    "Advanced": ["shoulder press","lateral pulldown","seated dips"]
    }
    
    difficulty_var = tk.StringVar(value="Beginner")# allows user to select difficulty of workout
    dropdown = tk.OptionMenu(frame, difficulty_var, "Beginner", "Intermediate", "Advanced")
    dropdown.grid(row=2, column=2,pady=0)
    Difficulty_L = tk.Label(frame,text="Select the difficulty of your workouts",font=("Arial",13))
    Difficulty_L.grid(row=2,column=0,columnspan=2)
    btn2 = tk.Button(frame, text="")
    btn2.grid(row=2, column=1)
    btn2.grid_forget() 
    def work():#builds the workout and begins it
        level = difficulty_var.get()
        n=int(No_Workout.get())
        list_Exercise=[]
        for i in range(n):
            excersice= random.choice(workout[level])
            list_Exercise.append(excersice)
        print("hi")
        btn2.config(text= f"start exercise consisting {list_Exercise}",command= lambda:WorkoutBegun(main_window,list_Exercise))  # change text
        btn2.grid()
    No_Workout_L = tk.Label(frame,text="how many workouts do you want to do",font=("Arial",13))
    No_Workout_L.grid(row=0,column=0,columnspan=2)
    No_Workout= tk.Entry(frame)
    No_Workout.grid(row=0,column=2,pady=0)
    gene= tk.Button(frame,text="generate workout",command= lambda:work())
    gene.grid(row=1,column=2)
    Back_button = tk.Button(frame,text="Back to home",bg="#333333", fg="#FFFFFF",font=("Arial",13), command= lambda: create_main_window())
    Back_button.grid(row=3,column=5,pady=20)
    
def CalorieTracker(main_window):
    calorietracker= tk.Toplevel(main_window)
    main_window.withdraw()
    calorietracker.configure(bg='#333333')
    calorietracker.geometry("590x500")
    
    frame=tk.Frame(calorietracker,bg='#333333')
    frame.pack(expand=True)
    
    
    x_entry = tk.Entry(frame,)
    x_label = tk.Label(frame,text="DAY OF MONTH",bg='#333333', fg="#FFFFFF",font=("Arial",18))
    y_entry = tk.Entry(frame)
    y_label = tk.Label(frame,text="Calories intaken",bg='#333333', fg="#FFFFFF",font=("Arial",18))
    generate_graph = tk.Label(frame,text="Generate Graph",bg="#C5228F", fg="#FFFFFF",font=("Arial",14))
    Back_button = tk.Button(frame,text="Back to home",bg="#333333", fg="#FFFFFF",font=("Arial",13), command= lambda: create_main_window())
    
    generate_graph.grid(row=3,column=0,columnspan=1,pady=5,sticky="ew")
    Back_button.grid(row=3,column=3,pady=20)
    x_label.grid(row=1,column=0,pady=20)
    y_label.grid(row=2,column=0,pady=20)
    x_entry.grid(row=1,column=1,pady=20)
    y_entry.grid(row=2,column=1,pady=20)
    y=[0]
    x=[0]
    # show grapgh is up here as you need to make the function come before the button
    def sort_x(x,y):#sorts the entries of the user into a chronological order
        x_list = int(x_entry.get())
        y_list = int(y_entry.get())
        y.append(y_list)
        x.append(x_list)
        temp=""
        n=len(x)
        swapped = True
        while n > 0 and swapped:
             swapped = False
             n = n - 1
             for i in range (0,n):
                if x[i] > x[i+1]:
                     temp = x[i]
                     x[i] = x[i+1]
                     x[i+1]= temp
                     temp_y = y[i]
                     y[i] = y[i+1]
                     y[i+1] = temp_y
                     swapped = True
        return x
        return y
    def show_graph():
            plt.clf()
            plt.plot(x,y, marker="*")
            plt.title("Calories consumed per day")
            plt.xlabel("DAY")
            plt.ylabel("Calories")
            plt.show()
            messagebox.showinfo(title="Days", message=str(x)) 
            #make the sort function connected to a button and maybe take it out of the show grapgh function as it comes to early potentianlyy
            # need to make a sorting algoritham for x (Days)    
    def runboth():
        sort_x(x,y) 
        show_graph()                
    present_graph= tk.Button(frame,bg="#C5228F",command=runboth)
    present_graph.grid(row=3,column=1,columnspan=1,pady=40,sticky="ew")
    

        
    
    
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
