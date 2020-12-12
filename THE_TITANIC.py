from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import pandas as pd
from numpy import *
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

root=Tk()
root.title("THE TITANIC")
root.geometry("800x450+250+100")

render = ImageTk.PhotoImage(Image.open("image.jpg"))

img = Label(root, image=render)
img.place(x=0,y=0)

def click(event):
    global namev
    global genderv
    global bv
    global cv
    global ev
    global dv
    global fv
    df = pd.read_csv('titanic.csv')
    df['male'] = df['Sex'] == 'male'
    x = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
    y = df['Survived'].values
    xtr, xt, ytr, yt = train_test_split(x, y, test_size=0.3, random_state=42)
    model = LogisticRegression()
    model.fit(x, y)
    a1=int(nametext.get())
    b1=int(gendertext.get())
    c1=int(btext.get())
    d1=int(ctext.get())
    e1=int(etext.get())
    f1=float(dtext.get())
    arr = array([[a1,b1,c1,d1,e1,f1]])
    output = model.predict(arr)
    accu = model.score(xt, yt)
    print(accu)
    predict = model.predict_proba(arr)
    predictInPercent=(predict[0,1]*100)//1
    fv.set(f'{predictInPercent} %')

def reset():
    namev.set("")
    genderv.set("")
    bv.set("")
    cv.set("")
    ev.set("")
    dv.set("")


namev=StringVar()
genderv = StringVar()
bv = StringVar()
cv = StringVar()
ev = StringVar()
dv = StringVar()
fv = StringVar()

top = Label(root,text="SURVIVAL ON TITANIC",font=("times new roman",13,"bold"),bg="#087587",fg="white")
top.place(x=20,y=40,width=400,height=40)

name = Label(root, text="Pclass", font=("times new roman", 13, "bold"),bg="#087587",fg="white")
name.place(x=20, y=90,width=80,height=30 )

nametext = ttk.Combobox(root,width=28,textvariable=namev, font=("times new roman", 13, "bold"),state='readonly')
nametext['values']=("1","2","3")
nametext.place(x=100, y=90,width=120,height=30)

gender = Label(root, text="male", font=("times new roman", 13, "bold"),bg="#087587",fg="white")
gender.place(x=20, y=130,width=80,height=30 )

gendertext = ttk.Combobox(root,width=28,textvariable=genderv, font=("times new roman", 13, "bold"),state='readonly')
gendertext['values']=("1","0")
gendertext.place(x=100, y=130,width=120,height=30)

b = Label(root, text="Age", font=("times new roman", 13, "bold"),bg="#087587",fg="white")
b.place(x=20, y=170,width=80,height=30 )

btext=Entry(root,width=30,textvariable=bv,font=("times new roman", 13, "bold"),)
btext.place(x=100, y=170,width=120,height=30 )

c = Label(root, text="Siblings/Spouses", font=("times new roman", 7, "bold"),bg="#087587",fg="white")
c.place(x=20, y=210,width=80,height=30 )

ctext=Entry(root,width=30,textvariable=cv,font=("times new roman", 13, "bold"),)
ctext.place(x=100, y=210,width=120,height=30 )

e = Label(root, text="Parents/Children", font=("times new roman", 7, "bold"),bg="#087587",fg="white")
e.place(x=20, y=250,width=80,height=30 )

etext=Entry(root,width=30,textvariable=ev,font=("times new roman", 13, "bold"),)
etext.place(x=100, y=250,width=120,height=30 )

d = Label(root, text="Fare", font=("times new roman", 13, "bold"),bg="#087587",fg="white")
d.place(x=20, y=290,width=80,height=30 )

dtext=Entry(root,width=30,textvariable=dv,font=("times new roman", 13, "bold"),)
dtext.place(x=100, y=290,width=120,height=30 )

B0 = Button(root,text="Survival Probability",font=("times new roman",13,"bold"),bg="#087587",fg="white")
B0.place(x=20,y=330,width=200,height=30)
B0.bind("<Button-1>",click)

screen=Entry(root,width=30,textvariable=fv,font=("times new roman", 13, "bold"),)
screen.place(x=20, y=370,width=100,height=30 )

B1 = Button(root,text="RESET",command=reset,font=("times new roman",13,"bold"),bg="#087587",fg="white")
B1.place(x=120,y=370,width=100,height=30)

root.mainloop()