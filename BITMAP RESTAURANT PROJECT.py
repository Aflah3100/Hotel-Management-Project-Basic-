#****************IMPORT SECTIONS***********************8
from tkinter import *



#*********CREATING WINDOW FOR THE RESTAURANT**************

root=Tk()
root.geometry('1600x800+0+0')
root.title('BITMAP RESTAUTRANT PLAN ')
root.configure(bg="white")


#*******CREATING FRAMES*******************

top_frame=Frame(root,width=1600,height=50,bg='#B2BABB',relief='sunken')
top_frame.pack(side=TOP)

left_frame=Frame(root,width=800,height=700,bg='#48C9B0',relief='sunken')
left_frame.pack(side=LEFT)

right_frame=Frame(root,width=300,height=700,bg='#48C9B0',relief='sunken')
right_frame.pack(side=RIGHT)



#**********CREATING LABEL INFORMATION**************


label_info=Label(top_frame,text='BITMAP HOTEL MANAGEMENT',bd=10,font=('courier new',50,'bold'),anchor='w',fg='#16A085')
label_info.grid(row=0,column=0)

#*****************************MAIN DISPLAY INFORMATION******************













#******************************************************************CALCULATOR AREA*******************************************************************

#CALCULATOR FUNCTIONS
def press():
    pass
def equalpress():
    pass
def clearpress():
    pass




#TO CREATE DISPLAY FOR THE CALCULATOR

equation=StringVar

text_display=Entry(right_frame,textvariable=equation,justify='right',insertwidth=4,font=('arial',20,'bold'),bd=30,bg='#16A085',)
text_display.grid(row=0,column=0,columnspan=4)


#******TO CREATE BUTTONS FOR CALCULATOR*********************

button_1=Button(right_frame,text='1',font=('arial',20,'bold'),bg='#48C9B0',bd=8,padx=16,pady=16,fg='black',command=lambda:press(1))
button_1.grid(row=1,column=0)

button_2=Button(right_frame,text='2',font=('arial',20,'bold'),bg='#48C9B0',bd=8,padx=16,pady=16,fg='black',command=lambda:press(2))
button_2.grid(row=1,column=1)

button_3=Button(right_frame,text='3',font=('arial',20,'bold'),bg='#48C9B0',bd=8,padx=16,pady=16,fg='black',command=lambda:press(3))
button_3.grid(row=1,column=2)

button_4=Button(right_frame,text='4',font=('arial',20,'bold'),bg='#48C9B0',bd=8,padx=16,pady=16,fg='black',command=lambda:press(4))
button_4.grid(row=2,column=0)

button_5=Button(right_frame,text='5',font=('arial',20,'bold'),bg='#48C9B0',bd=8,padx=16,pady=16,fg='black',command=lambda:press(5))
button_5.grid(row=2,column=1)

button_6=Button(right_frame,text='6',font=('arial',20,'bold'),bg='#48C9B0',bd=8,padx=16,pady=16,fg='black',command=lambda:press(6))
button_6.grid(row=2,column=2)

button_7=Button(right_frame,text='7',font=('arial',20,'bold'),bg='#48C9B0',bd=8,padx=16,pady=16,fg='black',command=lambda:press(7))
button_7.grid(row=3,column=0)

button_8=Button(right_frame,text='8',font=('arial',20,'bold'),bg='#48C9B0',bd=8,padx=16,pady=16,fg='black',command=lambda:press(8))
button_8.grid(row=3,column=1)

button_9=Button(right_frame,text='9',font=('arial',20,'bold'),bg='#48C9B0',bd=8,padx=16,pady=16,fg='black',command=lambda:press(9))
button_9.grid(row=3,column=2)

button_0=Button(right_frame,text='0',font=('arial',20,'bold'),bg='#48C9B0',bd=8,padx=16,pady=16,fg='black',command=lambda:press(0))
button_0.grid(row=4,column=0)

decimal=Button(right_frame,text='.',font=('arial',20,'bold'),bg='#48C9B0',bd=8,padx=16,pady=16,fg='black',command=lambda:press('.'))
decimal.grid(row=4,column=1)

equal=Button(right_frame,text='=',font=('arial',20,'bold'),bg='#48C9B0',bd=8,padx=16,pady=16,fg='black',command=lambda:equalpress())
equal.grid(row=5,column=0)

cancel_button=Button(right_frame,text='C',font=('arial',20,'bold'),bg='#48C9B0',bd=8,padx=16,pady=16,fg='black',command=lambda:clearpress())
cancel_button.grid(row=4,column=2)

#CREATING EQUATOR BUTTONS

add=Button(right_frame,text='+',font=('arial',20,'bold'),bg='#48C9B0',bd=8,padx=16,pady=16,fg='black',command=lambda:press('+'))
add.grid(row=1,column=3)

subtract=Button(right_frame,text='-',font=('arial',20,'bold'),bg='#48C9B0',bd=8,padx=16,pady=16,fg='black',command=lambda:press('-'))
subtract.grid(row=2,column=3)

multiply=Button(right_frame,text='*',font=('arial',20,'bold'),bg='#48C9B0',bd=8,padx=16,pady=16,fg='black',command=lambda:press('*'))
multiply.grid(row=3,column=3)

divide=Button(right_frame,text='/',font=('arial',20,'bold'),bg='#48C9B0',bd=8,padx=16,pady=16,fg='black',command=lambda:press('/'))
divide.grid(row=4,column=3)



























root.mainloop()


