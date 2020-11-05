#****************IMPORT SECTIONS***********************8
from tkinter import *



#*********CREATING WINDOW FOR THE RESTAURANT**************

root=Tk()
root.geometry('1600x800+0+0')
root.title('BITMAP RESTAUTRANT PLAN ')
root.configure(bg="white")


#*******CREATING FRAMES*******************

top_frame=Frame(root,width=1600,height=50,bg='#48C9B0',relief='sunken')
top_frame.pack(side=TOP)

left_frame=Frame(root,width=800,height=700,relief='sunken')
left_frame.pack(side=LEFT)

right_frame=Frame(root,width=300,height=700,bg='#48C9B0',relief='sunken')
right_frame.pack(side=RIGHT)



#**********CREATING LABEL INFORMATION**************


label_info=Label(top_frame,text='BITMAP HOTEL MANAGEMENT',bd=10,font=('courier new',50,'bold'),anchor='w',fg='#229954')
label_info.grid(row=0,column=0)

#*****************************MAIN DISPLAY INFORMATION******************

mainequation=StringVar()
main_display=Entry(top_frame,textvariable=mainequation,justify='right',width=55,bg='#48C9B0',bd=15,fg='#17202A',font=('arial',20,'bold'))
main_display.grid(row=2,column=0)












#******************************************************************CALCULATOR AREA*******************************************************************

#CALCULATOR FUNCTIONS
expression=""
def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)

def equalpress():
   try:
       global expression
       total=str(eval(expression))
       equation.set(total)
       expression=""
   except:
       ZeroDivisionError
       equation.set("ERROR!!!")

def clearpress():
    global expression
    equation.set('0')
    expression=""


def pressoff():
    global expression
    mainequation.set(" POWERED OFF!!! ")
    expression=""

def presscloss():
    global expression
    mainequation.set("SHOP CLOSED! THANK YOU!!!!!!!!")
    expression=""

def presscash():
    global expression
    mainequation.set("CASHIER OPENED AND RECORDED")
    expression=""







#TO CREATE DISPLAY FOR THE CALCULATOR

equation=StringVar()

text_display=Entry(right_frame,textvariable=equation,justify='right',insertwidth=4,font=('arial',20,'bold'),bd=30,bg='#16A085',)
text_display.grid(row=0,column=0,columnspan=4)


#******TO CREATE BUTTONS FOR CALCULATOR*********************

button_1=Button(right_frame,text='1',font=('arial',20,'bold'),bg='#48C9B0',bd=8,padx=16,pady=16,fg='black',command=lambda :press(1))
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

#CREATE OTHER FUNCTION BUTTONS

off_button=Button(right_frame,text='Off!',font=('verdana',12,'bold'),bg='#48C9B0',bd=8,padx=10,pady=19,fg='black',command=lambda:pressoff())
off_button.grid(row=5,column=1)

close_button=Button(right_frame,text='Close',font=('verdana',12,'bold'),bg='#48C9B0',bd=8,padx=10,pady=19,fg='black',command=lambda:presscloss())
close_button.grid(row=5,column=2)

cashier_button=Button(right_frame,text='Cash',font=('verdana',12,'bold'),bg='#48C9B0',bd=8,padx=10,pady=19,fg='black',command=lambda:presscash())
cashier_button.grid(row=5,column=3)










#***********RESTAURANT INFORMATION(1) FOR FFRAME(1)***************************


label_refer=Label(left_frame,text='Reference',font=('arial',16,'bold'),bd=16,anchor='w',)
label_refer.grid(row=0,column=0)

disp=StringVar()
text_refr=Entry(left_frame,font=('arial',16,'bold'),bd=16,textvariable=disp,insertwidth=4,bg='#16A085',justify='right')
text_refr.grid(row=0,column=1)

meal1_refer=Label(left_frame,text='Meal 1: ',font=('arial',16,'bold'),bd=16,anchor='w',)
meal1_refer.grid(row=1,column=0)

disp1=StringVar()
textmeal1_refr=Entry(left_frame,font=('arial',16,'bold'),bd=16,textvariable=disp,insertwidth=4,bg='#16A085',justify='right')
textmeal1_refr.grid(row=1,column=1)

meal2_refer=Label(left_frame,text='Meal 2: ',font=('arial',16,'bold'),bd=16,anchor='w',)
meal2_refer.grid(row=2,column=0)

disp2=StringVar()
textmeal2_refr=Entry(left_frame,font=('arial',16,'bold'),bd=16,textvariable=disp,insertwidth=4,bg='#16A085',justify='right')
textmeal2_refr.grid(row=2,column=1)

meal3_refer=Label(left_frame,text='Meal 3: ',font=('arial',16,'bold'),bd=16,anchor='w',)
meal3_refer.grid(row=3,column=0)

disp3=StringVar()
textmeal3_refr=Entry(left_frame,font=('arial',16,'bold'),bd=16,textvariable=disp,insertwidth=4,bg='#16A085',justify='right')
textmeal3_refr.grid(row=3,column=1)

meal4_refer=Label(left_frame,text='Meal 4: ',font=('arial',16,'bold'),bd=16,anchor='w',)
meal4_refer.grid(row=4,column=0)

disp4=StringVar()
textmeal4_refr=Entry(left_frame,font=('arial',16,'bold'),bd=16,textvariable=disp,insertwidth=4,bg='#16A085',justify='right')
textmeal4_refr.grid(row=4,column=1)

meal5_refer=Label(left_frame,text='Meal 5: ',font=('arial',16,'bold'),bd=16,anchor='w',)
meal5_refer.grid(row=5,column=0)

disp5=StringVar()
textmeal5_refr=Entry(left_frame,font=('ariall',16,'bold'),bd=16,textvariable=disp,insertwidth=4,bg='#16A085',justify='right')
textmeal5_refr.grid(row=5,column=1)



#**********RESTAURANT INFORMATION(2) FOR FRAME(1)***********************************************


drinks_refer=Label(left_frame,text='DRINKS',font=('arial',16,'bold'),bd=16,anchor='w',)
drinks_refer.grid(row=0,column=2)

disp7=StringVar()
drinks_refr=Entry(left_frame,font=('arial',16,'bold'),bd=16,textvariable=disp,insertwidth=4,bg='#16A085',justify='right')
drinks_refr.grid(row=0,column=3)

mealcost_refer=Label(left_frame,text='Meal Cost (T)',font=('arial',16,'bold'),bd=16,anchor='w',)
mealcost_refer.grid(row=1,column=2)

disp8=StringVar()
mealcost_refr=Entry(left_frame,font=('arial',16,'bold'),bd=16,textvariable=disp,insertwidth=4,bg='#16A085',justify='right')
mealcost_refr.grid(row=1,column=3)


servcharge_refer=Label(left_frame,text='Service Charge: ',font=('arial',16,'bold'),bd=16,anchor='w',)
servcharge_refer.grid(row=2,column=2)

disp9=StringVar()
servcharge_refr=Entry(left_frame,font=('arial',16,'bold'),bd=16,textvariable=disp,insertwidth=4,bg='#16A085',justify='right')
servcharge_refr.grid(row=2,column=3)

tax_refer=Label(left_frame,text='State Tax: ',font=('arial',16,'bold'),bd=16,anchor='w',)
tax_refer.grid(row=3,column=2)

disp10=StringVar()
tax_refr=Entry(left_frame,font=('arial',16,'bold'),bd=16,textvariable=disp,insertwidth=4,bg='#16A085',justify='right')
tax_refr.grid(row=3,column=3)

subt_refer=Label(left_frame,text='Sub Total: ',font=('arial',16,'bold'),bd=16,anchor='w',)
subt_refer.grid(row=4,column=2)

disp11=StringVar()
subt_refr=Entry(left_frame,font=('arial',16,'bold'),bd=16,textvariable=disp,insertwidth=4,bg='#16A085',justify='right')
subt_refr.grid(row=4,column=3)

total_refer=Label(left_frame,text='Total Cost: ',font=('verdana',16,'bold'),bd=16,anchor='w',)
total_refer.grid(row=5,column=2)

disp12=StringVar()
total_refr=Entry(left_frame,font=('arial',16,'bold'),bd=16,textvariable=disp,insertwidth=4,bg='#16A085',justify='right')
total_refr.grid(row=5,column=3)


#*********UTILITY BUTTONS*****************************



































root.mainloop()


