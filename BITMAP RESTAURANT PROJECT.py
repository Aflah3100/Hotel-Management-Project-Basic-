#****************IMPORT SECTIONS***********************8
from tkinter import *



#*********CREATING WINDOW FOR THE RESTAURANT**************

root=Tk()
root.geometry('1600x800+0+0')
root.title('BITMAP RESTAUTRANT PLAN ')
root.configure(bg="white")


#*******CREATING FRAMES*******************

top_frame=Frame(root,width=1600,height=50,bg='#B2BABB',relief='sunken')
top_frame.pack()

right_frame=Frame(root,width=800,height=700,bg='#48C9B0',relief='sunken')
right_frame.pack()

left_frame=Frame(root,width=300,height=700,bg='#48C9B0',relief='sunken')
left_frame.pack()



#**********CREATING LABEL INFORMATION**************


label_info=Label(top_frame,text='BITMAP HOTEL MANAGEMENT',bd=10,font=('courier new',50,'bold'),anchor='w',fg='#16A085')
label_info.grid(row=0,column=0)

#*****************************MAIN DISPLAY INFORMATION******************













#******************************************************************CALCULATOR AREA********************************













root.mainloop()


