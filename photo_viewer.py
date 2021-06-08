import tkinter as tk
from PIL import ImageTk, Image

class img_viewer:
    def __init__(self):
        self.count=0
        self.root = tk.Tk()
        self.root.title("Image Viewer")
        self.photo_frame = tk.Frame()
        self.button_frame = tk.Frame()
        self.img_no_1 = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\DesktopGoose v0.3\Assets\Images\Memes\Meme1.png"))
        self.img_no_2 = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\DesktopGoose v0.3\Assets\Images\Memes\Meme2.png"))
        self.img_no_3 = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\DesktopGoose v0.3\Assets\Images\Memes\Meme3.png"))
        self.img_no_4 = ImageTk.PhotoImage(Image.open(r"C:\Users\Admin\Desktop\DesktopGoose v0.3\Assets\Images\Memes\Meme4.png"))
        self.img_list = [self.img_no_1,self.img_no_2,self.img_no_3,self.img_no_4]
        self.photo = tk.Label(self.photo_frame,image=self.img_list[self.count])
        
    def back(self):
        pass
    
    def forward(self,no):
            self.photo.grid_forget()
            self.count+=1
            self.photo = tk.Label(self.photo_frame,image=self.img_list[self.count])
            self.photo.grid(row=0,column=0,columnspan=3)

    def def_buttons(self):
        self.button_back = tk.Button(self.button_frame,text="Back",command=self.back)
        self.button_forward = tk.Button(self.button_frame,text="Forward",command=lambda:self.forward(0))
        self.button_quit = tk.Button(self.button_frame,text="Quit",command=self.root.quit)
        self.button_back.grid(row=0,column=0)
        self.button_quit.grid(row=0,column=1)
        self.button_forward.grid(row=0,column=2)
        for y in range(3):    
            self.button_frame.columnconfigure(y, weight=1)
    

    def packing(self):
        self.photo.grid(row=0,column=0,columnspan=3)
        self.def_buttons()
        self.photo_frame.pack()
        self.button_frame.pack(expand=True,fill="both",side=tk.BOTTOM)
        self.root.mainloop()

photo1= img_viewer()
photo1.packing()