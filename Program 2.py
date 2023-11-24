import tkinter
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import PhotoImage


def enter():
    try:
        total_amount_of_money = float(amount_of_money.get())
        price_of_apples = float(price_of_apple.get())
        buyer_name_output= buyer_name.get()

        number_of_apples = total_amount_of_money//price_of_apples
        amount_needed_to_pay=number_of_apples*price_of_apples
        change=int(total_amount_of_money)-(amount_needed_to_pay) 

        #new window
        result_window = tkinter.Tk()
        result_window.title("TUTOY'S ONLINE STORE")
        result_window.geometry('925x500+300+200')
        result_window.configure(bg='#00CED1')
        result_window.wm_resizable(False,False)

        result_frame=tkinter.Frame(result_window,width=600,height=400,bg='#97FFFF')
        result_frame.place(x=190,y=50)
       

        greetings = "Hello" +" "+ buyer_name_output
        welcome=tkinter.Label(result_frame,text=greetings, fg="#000000",bg='#97FFFF',font=('Arial',25,'bold'))
        welcome.place(x=40,y=20)

        #number of apples
        number_of_apples_label=tkinter.Label(result_frame,text="Number of Apples:",fg="#000000",bg='#97FFFF',font=('Georgia',16))
        number_of_apples_label.place(x=30,y=80)
        number_of_apples_output=tkinter.Label(result_frame,text=number_of_apples,fg="#000000",bg='#97FFFF',font=('Georgia',20,'bold'))
        number_of_apples_output.place(x=190,y=110)

        #need to pay
        amount_needed_to_pay_label=tkinter.Label(result_frame,text="Amount to pay:",fg="#000000",bg='#97FFFF',font=('Georgia',16))
        amount_needed_to_pay_label.place(x=30,y=160)
        amount_to_pay_output=tkinter.Label(result_frame,text=amount_needed_to_pay, fg="#000000",bg='#97FFFF',font=('Georgia',20,'bold'))
        amount_to_pay_output.place(x=200,y=190)

        #change
        amount_of_change_label=tkinter.Label(result_frame,text="Change:",fg="#000000",bg='#97FFFF',font=('Georgia',16))
        amount_of_change_label.place(x=30,y=240)
        amount_of_change=tkinter.Label(result_frame,text=change, fg="#000000",bg='#97FFFF',font=('Georgia',20,'bold'))
        amount_of_change.place(x=200,y=270)



    except ValueError:
        messagebox.showwarning("Error", "Please enter a valid number.")

    


    
window = tkinter.Tk()
window.title("TUTOY'S ONLINE STORE")
window.geometry('925x500+300+200')
window.wm_resizable(False,False)

image_path=PhotoImage(file=r"C:\Users\jhobert\Pictures\images.png")
bg_image=tkinter.Label(window,image=image_path)
bg_image.place(relheight=1, relwidth=1)

#Logo
logo_img=PhotoImage(file=r"C:\Users\jhobert\Pictures\tutoy’s.png")
tkinter.Label(window,image=logo_img,border=0,bg='white').place(x=0,y=0)

frame=tkinter.Frame(window,width=400,height=400,bg='#97FFFF')
frame.place(x=490,y=50)

#heading
heading=tkinter.Label(frame,text="Welcome to Tutoy's Online Store", fg="#000000",bg='#97FFFF',font=('Georgia',16,'bold'))
heading.place(x=20,y=20)

#buyer name
def on_enter(e):
    buyer_name.delete(0,'end')
def on_leave(e):
    if buyer_name.get()=='':
        buyer_name.insert(0,'Name')

buyer_name = tkinter.Entry(frame,width=30,fg='black',border=0,bg='#97FFFF',font=('Microsoft Yahei UI Light',15))
buyer_name.place(x=30,y=80)
buyer_name.insert(0,  'Name')
buyer_name.bind("<FocusIn>",on_enter)
buyer_name.bind("<FocusOut>",on_leave)

tkinter.Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#amount of money
def on_enter(e):
    amount_of_money.delete(0,'end')
def on_leave(e):
    if amount_of_money.get()=='':
        amount_of_money.insert(0,'Amount of Money')

amount_of_money = tkinter.Entry(frame,width=30,fg='black',border=0,bg='#97FFFF',font=('Microsoft Yahei UI Light',15))
amount_of_money.place(x=30,y=150)
amount_of_money.insert(0,  'Amount of Money')
amount_of_money.bind("<FocusIn>",on_enter)
amount_of_money.bind("<FocusOut>",on_leave)

tkinter.Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#price of apple
def on_enter(e):
    price_of_apple.delete(0,'end')
def on_leave(e):
    if price_of_apple.get()=='':
        price_of_apple.insert(0,'Price of Apple')

price_of_apple = tkinter.Entry(frame,width=30,fg='black',border=0,bg='#97FFFF',font=('Microsoft Yahei UI Light',15))
price_of_apple.place(x=30,y=220)
price_of_apple.insert(0,  'Price of Apple')
price_of_apple.bind("<FocusIn>",on_enter)
price_of_apple.bind("<FocusOut>",on_leave)

tkinter.Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

#button
tkinter.Button(frame,width=35,pady=7,text='Enter',command=enter,bg='#F0FFFF',fg='#000000',border=0,font=('Microsoft Yahei UI Light',12,'bold')).place(x=25,y=280)

window.mainloop()