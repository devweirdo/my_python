import tkinter as tk
class calculator:
    def __init__(self):  #defines
        self.entry = 0
        self.root = tk.Tk()
        self.root.title('Calculator')
        self.user = tk.Frame()
        self.keyboard = tk.Frame()
        self.user_screen = tk.Entry(master=self.user,width=25)
        # self.run()

    def define_buttons(self): #buttons
        self.button_1 = tk.Button(master=self.keyboard,text="1",width=3,command= lambda:self.button_click(1))
        self.button_2 = tk.Button(master=self.keyboard,text="2",width=3,command= lambda:self.button_click(2))
        self.button_3 = tk.Button(master=self.keyboard,text='3',width=3,command= lambda:self.button_click(3))
        self.button_4 = tk.Button(master=self.keyboard,text="4",width=3,command= lambda:self.button_click(4))
        self.button_5 = tk.Button(master=self.keyboard,text="5",width=3,command= lambda:self.button_click(5))
        self.button_6 = tk.Button(master=self.keyboard,text="6",width=3,command= lambda:self.button_click(6))
        self.button_7 = tk.Button(master=self.keyboard,text="7",width=3,command= lambda:self.button_click(7))
        self.button_8 = tk.Button(master=self.keyboard,text="8",width=3,command= lambda:self.button_click(8))
        self.button_9 = tk.Button(master=self.keyboard,text="9",width=3,command= lambda:self.button_click(9))
        self.button_0 = tk.Button(master=self.keyboard,text="0",width=3,command= lambda:self.button_click(0))
        self.button_plus = tk.Button(master=self.keyboard,text="+",width=3,command= lambda:self.button_click("+"))
        self.button_min = tk.Button(master=self.keyboard,text="-",width=3,command= lambda:self.button_click("-"))
        self.button_multi = tk.Button(master=self.keyboard,text="x",width=3,command= lambda:self.button_click("*"))
        self.button_div = tk.Button(master=self.keyboard,text="/",width=3,command= lambda:self.button_click("/"))
        self.button_dot = tk.Button(master=self.keyboard,text=".",width=3,command= lambda:self.button_click("."))
        self.button_equal = tk.Button(master=self.keyboard,text="=",command=self.result)
        self.button_clear = tk.Button(master=self.keyboard,text="clr",width=3,command=self.clear)
        self.button_delete = tk.Button(master=self.keyboard,text="del",width=3,command=self.delete)
        self.prev_ans = tk.Button(master=self.keyboard,text="Ans",width=3,command=lambda:self.button_click("ans"))

    def arrange_buttons(self):
        #arrange buttons
        self.button_1.grid(row=0,column=0)
        self.button_2.grid(row=0,column=1)
        self.button_3.grid(row=0,column=2)
        self.button_4.grid(row=1,column=0)
        self.button_5.grid(row=1,column=1)
        self.button_6.grid(row=1,column=2)
        self.button_7.grid(row=2,column=0)
        self.button_8.grid(row=2,column=1)
        self.button_9.grid(row=2,column=2)
        self.button_0.grid(row=3,column=0)
        self.button_equal.grid(row=3,column=3,columnspan=2,sticky="EW")
        self.button_plus.grid(row=2,column=3)
        self.button_min.grid(row=2,column=4)
        self.button_multi.grid(row=1,column=3)
        self.button_div.grid(row=1,column=4)
        self.button_clear.grid(row=0,column=4)
        self.button_dot.grid(row=3,column=1)
        self.button_delete.grid(row=0,column=3)
        self.prev_ans.grid(row=3,column=2)

    def button_click(self,cmd): #give input
        self.user_screen.insert(tk.END, str(cmd))

    def result(self): #give result
        try:
            ans = self.entry
            self.entry = eval(self.user_screen.get())
            self.user_screen.delete(0, tk.END)
            self.user_screen.insert(0, self.entry)
        except:
            self.user_screen.delete(0, tk.END)
            self.user_screen.insert(0,"error")
        
    def clear(self): #clear screen
        self.user_screen.delete(0, tk.END)
    
    def delete(self):
        self.user_screen.delete(first=len(self.user_screen.get())-1,last=tk.END)
    
    def packing(self):
        self.user_screen.pack() #pack and loop
        self.user.pack()
        self.keyboard.pack()
    
    def run(self):
        self.define_buttons()
        self.arrange_buttons()
        self.packing()



    