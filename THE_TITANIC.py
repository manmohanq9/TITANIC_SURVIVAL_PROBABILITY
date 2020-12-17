from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import pandas as pd
from numpy import *
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
import tkinter.messagebox as tmsg

root=Tk()
root.title("THE TITANIC")
root.geometry("800x450+250+100")

render = ImageTk.PhotoImage(Image.open("image.jpg"))

img = Label(root, image=render)
img.place(x=0,y=0)

def check_Dtype(x):
    try:
        return int(x)
    except ValueError :
        tmsg.showinfo("Survival Probability", "INVALID NUMBERS")

def click(event):
    global pclassv
    global genderv
    global agev
    global siblingsv
    global parentsv
    global farev
    global displayv

    df = pd.read_csv('titanic.csv')
    df['male'] = df['Sex'] == 'male'

    x = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
    y = df['Survived'].values

    xtr, xt, ytr, yt = train_test_split(x, y, test_size=0.3, random_state=42)
    
    from sklearn.model_selection import StratifiedKFold
    kf = StratifiedKFold(n_splits=50)

    for ti, tti in kf.split(x, y):
        xtr, xt, ytr, yt = x[ti], x[tti], y[ti], y[tti]

    model = LogisticRegression()
    model.fit(x, y)

    a1=int(pclasstext.get())
    b1=gendertext.get()
    if gendertext.get() == 'MALE':
        b1=1
    else:
        b1=0
    c1=check_Dtype(agetext.get())
    d1=check_Dtype(siblingsext.get())
    e1=check_Dtype(parentstext.get())
    f1=check_Dtype(faretext.get())

    input_val = array([[a1,b1,c1,d1,e1,f1]])
    output = model.predict(input_val)
    accuracy = model.score(xt, yt)
    print(accuracy)

    predict_y = model.predict_proba(input_val)
    predictInPercent=(predict_y[0,1]*100)//1
    displayv.set(f'{predictInPercent} %')
    tmsg.showinfo("Survival Probability",f"Probability of surviving is {predictInPercent} %")

def reset():
    pclassv.set("")
    genderv.set("")
    agev.set("")
    siblingsv.set("")
    parentsv.set("")
    farev.set("")
    displayv.set("")


pclassv=StringVar()
genderv = StringVar()
agev = StringVar()
siblingsv = StringVar()
parentsv = StringVar()
farev = StringVar()
displayv = StringVar()

top = Label(root,text="SURVIVAL ON TITANIC",font=("times new roman",13,"bold"),bg="#087587",fg="white")
top.place(x=20,y=40,width=400,height=40)

pclass = Label(root, text="Pclass", font=("times new roman", 13, "bold"),bg="#087587",fg="white")
pclass.place(x=20, y=90,width=80,height=30 )

pclasstext = ttk.Combobox(root,width=28,textvariable=pclass, font=("times new roman", 13, "bold"),state='readonly')
pclasstext['values']=("1","2","3")
pclasstext.place(x=100, y=90,width=120,height=30)

gender = Label(root, text="GENDER", font=("times new roman", 10, "bold"),bg="#087587",fg="white")
gender.place(x=20, y=130,width=80,height=30 )

gendertext = ttk.Combobox(root,width=28,textvariable=genderv, font=("times new roman", 13, "bold"),state='readonly')
gendertext['values']=("MALE","FEMALE")
gendertext.place(x=100, y=130,width=120,height=30)

age = Label(root, text="Age", font=("times new roman", 13, "bold"),bg="#087587",fg="white")
age.place(x=20, y=170,width=80,height=30 )

agetext=Entry(root,width=30,textvariable=agev,font=("times new roman", 13, "bold"),)
agetext.place(x=100, y=170,width=120,height=30 )

siblings= Label(root, text="Siblings/Spouses", font=("times new roman", 7, "bold"),bg="#087587",fg="white")
siblings.place(x=20, y=210,width=80,height=30 )

siblingsext=Entry(root,width=30,textvariable=siblingsv,font=("times new roman", 13, "bold"),)
siblingsext.place(x=100, y=210,width=120,height=30 )

parents = Label(root, text="Parents/Children", font=("times new roman", 7, "bold"),bg="#087587",fg="white")
parents.place(x=20, y=250,width=80,height=30 )

parentstext=Entry(root,width=30,textvariable=parentsv,font=("times new roman", 13, "bold"),)
parentstext.place(x=100, y=250,width=120,height=30 )

fare = Label(root, text="Fare", font=("times new roman", 13, "bold"),bg="#087587",fg="white")
fare.place(x=20, y=290,width=80,height=30 )

faretext=Entry(root,width=30,textvariable=farev,font=("times new roman", 13, "bold"),)
faretext.place(x=100, y=290,width=120,height=30 )

Button1 = Button(root,text="Survival Probability",font=("times new roman",13,"bold"),bg="#087587",fg="white")
Button1.place(x=20,y=330,width=200,height=30)
Button1.bind("<Button-1>",click)

screen=Entry(root,width=30,textvariable=displayv,font=("times new roman", 13, "bold"),)
screen.place(x=20, y=370,width=100,height=30 )

reset_button = Button(root,text="RESET",command=reset,font=("times new roman",13,"bold"),bg="#087587",fg="white")
reset_button.place(x=120,y=370,width=100,height=30)

root.mainloop()
