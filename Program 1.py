import tkinter
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import PhotoImage

def is_valid_name(entry_text):
    return all(char.isalpha() or char.isspace() for char in entry_text)

def start_buying():
    buyer_name_output = buyer_name.get()
    apples_number__output = apples_number.get()
    orange_number_output = orange_number.get()

    if not all(is_valid_name(entry_text) for entry_text in (buyer_name_output)):
            messagebox.showwarning("Invalid Input", "Please enter a name using LETTERS ONLY.")
            return
    
    if buyer_name_output and apples_number__output and orange_number_output:
        buyer_name_output = buyer_name.get()
        apples_number__output = apples_number.get()
        orange_number_output = orange_number.get()

        number_of_apples = int(apples_number.get())
        number_of_orange = int(orange_number.get())

        apple_price= 20*number_of_apples
        orange_price = 25*number_of_orange

        total_price_of_apple = apple_price
        total_price_of_orange= orange_price

        total_amount_to_pay=(total_price_of_apple) + (total_price_of_orange)

        #new window
        result_window = tkinter.Tk()
        result_window.title("TUTOY'S ONLINE STORE")
        result_window.geometry('925x500+300+200')
        result_window.configure(bg='#00CED1')
        result_window.wm_resizable(False,False)

        result_frame=tkinter.Frame(result_window,width=400,height=400,bg='#97FFFF')
        result_frame.place(x=290,y=50)
       

        greetings = "Hello" +" "+ buyer_name_output
        welcome=tkinter.Label(result_frame,text=greetings, fg="#000000",bg='#97FFFF',font=('Arial',25,'bold'))
        welcome.place(x=40,y=20)

        amount_of_apple = f"₱ {total_price_of_apple}.00"
        amount_of_orange = f"₱ {total_price_of_orange}.00"

        #total price of apple
        apple_result_label=tkinter.Label(result_frame,text="Amount of Apple:",fg="#000000",bg='#97FFFF',font=('Georgia',16))
        apple_result_label.place(x=30,y=80)
        apple_result=tkinter.Label(result_frame,text=amount_of_apple, fg="#000000",bg='#97FFFF',font=('Georgia',20,'bold'))
        apple_result.place(x=200,y=110)

        #total price of orange
        orange_result_label=tkinter.Label(result_frame,text="Amount of Orange:",fg="#000000",bg='#97FFFF',font=('Georgia',16))
        orange_result_label.place(x=30,y=160)
        orange_result=tkinter.Label(result_frame,text=amount_of_orange, fg="#000000",bg='#97FFFF',font=('Georgia',20,'bold'))
        orange_result.place(x=200,y=190)

        #total price of orange
        total_amount= f"₱ {total_amount_to_pay}.00"
        need_to_pay_label=tkinter.Label(result_frame,text="Total Amount:",fg="#000000",bg='#97FFFF',font=('Georgia',16))
        need_to_pay_label.place(x=30,y=240)
        need_to_pay=tkinter.Label(result_frame,text=total_amount,fg="#000000",bg='#97FFFF',font=('Georgia',20,'bold'))
        need_to_pay.place(x=200,y=270)

        

    else:
        tkinter.messagebox.showwarning(title="Error", message="Complete information is required")


    
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

#number of apples
def on_enter(e):
    apples_number.delete(0,'end')
def on_leave(e):
    if apples_number.get()=='':
        apples_number.insert(0,'Number of Apples')

price_of_apples_label=tkinter.Label(frame,text="PRICE OF APPLE: ₱20.00",fg="#000000",bg='#97FFFF',font=('Arial',12,'bold'))
price_of_apples_label.place(x=30,y=130)

apples_number = tkinter.Spinbox(frame,from_=0, to=1000,width=30,fg='black',border=0,bg='#97FFFF',font=('Microsoft Yahei UI Light',15))
apples_number.place(x=30,y=163)
apples_number.insert(0,  'Number of Apples')
apples_number.bind("<FocusIn>",on_enter)
apples_number.bind("<FocusOut>",on_leave)

tkinter.Frame(frame,width=295,height=2,bg='black').place(x=25,y=190)

#number of orange
def on_enter(e):
    orange_number.delete(0,'end')
def on_leave(e):
    if orange_number.get()=='':
        orange_number.insert(0,'Number of Orange')

price_of_orange_label=tkinter.Label(frame,text="PRICE OF ORANGE: ₱25.00",fg="#000000",bg='#97FFFF',font=('Arial',12,'bold'))
price_of_orange_label.place(x=30,y=215)

orange_number = tkinter.Spinbox(frame,from_=0, to=1000,width=30,fg='black',border=0,bg='#97FFFF',font=('Microsoft Yahei UI Light',15))
orange_number.place(x=30,y=245)
orange_number.insert(0,  'Number of Orange')
orange_number.bind("<FocusIn>",on_enter)
orange_number.bind("<FocusOut>",on_leave)

tkinter.Frame(frame,width=295,height=2,bg='black').place(x=25,y=270)

#button
tkinter.Button(frame,width=35,pady=7,text='Start Buying',command=start_buying,bg='#F0FFFF',fg='#000000',border=0,font=('Microsoft Yahei UI Light',12,'bold')).place(x=25,y=320)

window.mainloop()