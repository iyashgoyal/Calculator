#calculator script
import tkinter
from tkinter import *
from tkinter import messagebox

#BACKEND

val=''
A=0
operator=''

def btn1_isclicked():
    global val
    val=val+'1'
    data.set(val)

def btn2_isclicked():
    global val
    val=val+'2'
    data.set(val)

def btn3_isclickd():
    global val
    val=val+'3'
    data.set(val)

def btn4_isclicked():
    global val
    val=val+'4'
    data.set(val)

def btn5_isclicked():
    global val
    val=val+'5'
    data.set(val)

def btn6_isclicked():
    global val
    val=val+'6'
    data.set(val)

def btn7_isclicked():
    global val
    val=val+'7'
    data.set(val)

def btn8_isclicked():
    global val
    val=val+'8'
    data.set(val)

def btn9_isclicked():
    global val
    val=val+'9'
    data.set(val)

def btn0_isclicked():
    global val
    val=val+'0'
    data.set(val)

def btndot_isclicked():
    global val
    val=val+'.'
    data.set(val)

def btnplus_isclicked():
    global A
    global operator
    global val
    A=int(val)
    operator='+'
    val=val+'+'
    data.set(val)

def btnminus_isclicked():
    global A
    global operator
    global val
    A=int(val)
    operator='-'
    val=val+'-'
    data.set(val)

def btnmultipy_isclicked():
    global A
    global operator
    global val
    A=int(val)
    operator='x'
    val=val+'x'
    data.set(val)

def btndivide_isclicked():
    global A
    global operator
    global val
    A=int(val)
    operator='/'
    val=val+'/'
    data.set(val)

def btnc_isclicked():
    global A
    global operator
    global val
    val=''
    A=0
    operator=''
    data.set(val)

def btnequal_isclicked():
    global A
    global val
    global operator
    val2= val
    x= int(val2.split(operator)[1])
    if operator=='+':
        c=A+x
        data.set(c)
        val=str(c)
    elif operator=='-':
        c=A-x
        data.set(c)
        val=str(c)
    elif operator=='x':
        c=A*x
        data.set(c)
        val=str(c)
    elif operator=='/':
        if x==0:
            messagebox.showerror('Error','division by 0 not possible')
            A=''
            val=''
            data.set(val)
        else:
            c=int(A/x)
            data,set(c)
            val=str(c)


#FRONTEND
root=tkinter.Tk()
root.geometry('250x400+300+300')
root.resizable(0,0)
root.title('Calculator')

data=StringVar()
#LABEL
lbl=Label(
    root,
    text='Label',
    anchor=SE,
    font=('verdana',20),
    textvariable=data,
    background='#ffffff',
    fg='#000000'
)
lbl.pack(expand=True,fill='both',)


#ROWS
row1=Frame(root)
row1.pack(expand=True,fill='both',)

row2= Frame(root)
row2.pack(expand=True,fill='both',)

row3=Frame(root)
row3.pack(expand=True,fill='both',)

row4=Frame(root)
row4.pack(expand=True,fill='both')

row5=Frame(root)
row5.pack(expand=True,fill='both')

#BUTTONS

#ROW 1

btn7= Button(
    row1,
    text='7',
    font=('Verdana',22),
    relief=GROOVE,
    border=0,
    command=btn7_isclicked,
)
btn7.pack(side=LEFT,expand= True,fill='both')

btn8= Button(
    row1,
    text='8',
    font=('Verdana',22),
    relief=GROOVE,
    border=0,
    command=btn8_isclicked

)
btn8.pack(side=LEFT,expand= True,fill='both')

btn9= Button(
    row1,
    text='9',
    font=('Verdana',22),
    relief=GROOVE,
    border=0,
    command=btn9_isclicked

)
btn9.pack(side=LEFT,expand= True,fill='both')

btnmultiply= Button(
    row1,
    text='X',
    font=('Verdana',22),
    relief=GROOVE,
    border=0,
    command=btnmultipy_isclicked

)
btnmultiply.pack(side=LEFT,expand= True,fill='both')

#ROW2

btn4= Button(
    row2,
    text='4',
    font=('Verdana',22),
    relief=GROOVE,
    border=0,
    command=btn4_isclicked

)
btn4.pack(side=LEFT,expand= True,fill='both')

btn5= Button(
    row2,
    text='5',
    font=('Verdana',22),
    relief=GROOVE,
    border=0,
    command=btn5_isclicked

)
btn5.pack(side=LEFT,expand= True,fill='both')

btn6= Button(
    row2,
    text='6',
    font=('Verdana',22),
    relief=GROOVE,
    border=0,
    command=btn6_isclicked

)
btn6.pack(side=LEFT,expand= True,fill='both')

btnminus= Button(
    row2,
    text='-',
    font=('Verdana',22),
    relief=GROOVE,
    border=0,
    command=btnminus_isclicked

)
btnminus.pack(side=LEFT,expand= True,fill='both')


#ROW3

btn1= Button(
    row3,
    text='1',
    font=('Verdana',22),
    relief=GROOVE,
    border=0,
    command=btn1_isclicked
)
btn1.pack(side=LEFT,expand= True,fill='both')

btn2= Button(
    row3,
    text='2',
    font=('Verdana',22),
    relief=GROOVE,
    border=0,
    command=btn2_isclicked
)
btn2.pack(side=LEFT,expand= True,fill='both')

btn3= Button(
    row3,
    text='3',
    font=('Verdana',22),
    relief=GROOVE,
    border=0,
    command=btn3_isclickd
)
btn3.pack(side=LEFT,expand= True,fill='both')

btnplus= Button(
    row3,
    text='+',
    font=('Verdana',22),
    relief=GROOVE,
    border=0,
    command=btnplus_isclicked

)
btnplus.pack(side=LEFT,expand= True,fill='both')


#ROW4

btnc=Button(
    row4,
    text='C',
    font=('Verdana',24),
    relief=GROOVE,
    border=0,
    command=btnc_isclicked
)
btnc.pack(side=LEFT,expand=True,fill='both')

btn0= Button(
    row4,
    text='0',
    font=('Verdana',22),
    relief=GROOVE,
    border=0,
    command=btn0_isclicked,
)
btn0.pack(side=LEFT,expand= True,fill='both')

# btndot= Button(
#     row4,
#     text='.',
#     font=('Verdana',22),
#     relief=GROOVE,
#     border=0,
#     command=btndot_isclicked
#
# )
# btndot.pack(side=LEFT,expand= True,fill='both')

btndivide= Button(
    row4,
    text='/',
    font=('Verdana',22),
    relief=GROOVE,
    border=0,
    command=btndivide_isclicked
)
btndivide.pack(side=LEFT,expand= True,fill='both')


#ROW5

btnequal= Button(
    row5,
    text='=',
    font=('Verdana',22),
    relief=GROOVE,
    border=0,
    command=btnequal_isclicked

)
btnequal.pack(side=LEFT,expand= True,fill='both')
root.mainloop()