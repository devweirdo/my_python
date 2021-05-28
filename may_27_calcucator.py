import tkinter as tk

root = tk.Tk()
root.title('Calculator')

entry = 0
user = tk.Frame()
keyboard = tk.Frame()

user_screen = tk.Entry(master=user)
user_screen.pack()

def button_click(cmd):
    #user_screen.delete(0, tk.END)
    user_screen.insert(tk.END, str(cmd))

def result():
    try:
        global entry
        entry = eval(user_screen.get())
        user_screen.delete(0, tk.END)
        user_screen.insert(0,entry)
    except:
        user_screen.delete(0, tk.END)
        user_screen.insert(0,"error")
        
def clear():
    user_screen.delete(0, tk.END)

#define buttons
button_1 = tk.Button(master=keyboard,text="1",width=3,command= lambda:button_click(1))
button_2 = tk.Button(master=keyboard,text="2",width=3,command= lambda:button_click(2))
button_3 = tk.Button(master=keyboard,text='3',width=3,command= lambda:button_click(3))
button_4 = tk.Button(master=keyboard,text="4",width=3,command= lambda:button_click(4))
button_5 = tk.Button(master=keyboard,text="5",width=3,command= lambda:button_click(5))
button_6 = tk.Button(master=keyboard,text="6",width=3,command= lambda:button_click(6))
button_7 = tk.Button(master=keyboard,text="7",width=3,command= lambda:button_click(7))
button_8 = tk.Button(master=keyboard,text="8",width=3,command= lambda:button_click(8))
button_9 = tk.Button(master=keyboard,text="9",width=3,command= lambda:button_click(9))
button_0 = tk.Button(master=keyboard,text="0",width=3,command= lambda:button_click(0))
button_plus = tk.Button(master=keyboard,text="+",width=3,command= lambda:button_click("+"))
button_minus = tk.Button(master=keyboard,text="-",width=3,command= lambda:button_click("-"))
button_multi = tk.Button(master=keyboard,text="x",width=3,command= lambda:button_click("*"))
button_div = tk.Button(master=keyboard,text="/",width=3,command= lambda:button_click("/"))
button_equal = tk.Button(master=keyboard,text="=",width=3,command=result)
button_clr = tk.Button(master=keyboard,text="clr",width=3,command=clear)

#arrange buttons
button_1.grid(row=0,column=0)
button_2.grid(row=0,column=1)
button_3.grid(row=0,column=2)
button_4.grid(row=1,column=0)
button_5.grid(row=1,column=1)
button_6.grid(row=1,column=2)
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_0.grid(row=3,column=0)
button_equal.grid(row=3,column=2)
button_plus.grid(row=0,column=3)
button_minus.grid(row=1,column=3)
button_multi.grid(row=2,column=3)
button_div.grid(row=3,column=3)
button_clr.grid(row=3,column=1)


user.pack()
keyboard.pack()

root.mainloop()