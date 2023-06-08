from tkinter import *
from PIL import Image, ImageTk
import sys, os


class ImageViewer:  
    def __init__(self):
        self.image_index = 0
        self.dir = os.path.join(sys.path[0], "images", files[self.image_index])
       
       
        self.root = Tk(className="ImageView")
        self.root.bind("<Configure>", self.resizer)

        self.bw_button = Button(self.root, text="<---", command=self.backward, width=100).pack()
        self.fw_button = Button(self.root, text="--->", command=self.forward, width=100).pack()

        
        self.image = Image.open(self.dir)
        self.image = ImageTk.PhotoImage(self.image)
        
        self.canvas = Canvas(self.root, width=1600, height=900)
        self.canvas.pack(fill="both", expand=True, anchor="nw")
        self.canvas.create_image(0,0, image=self.image, anchor="nw")
        
        self.root.mainloop()
       
        
    def resizer(self, e):
        global new_image
     
        image = Image.open(self.dir)
        resized_image = image.resize((e.width, e.height), Image.LANCZOS)
        new_image = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0,0, image=new_image, anchor="nw")
        
    
    def forward(self):
        global new_image
     
        if self.image_index < len(files)-1:
            self.image_index = self.image_index + 1
        else:
            self.image_index = 0
        self.dir = os.path.join(sys.path[0], "images", files[self.image_index])

        
        image = Image.open(self.dir)
        resized_image = image.resize((self.canvas.winfo_width(), self.canvas.winfo_height()), Image.LANCZOS)
        new_image = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0,0, image=new_image, anchor="nw")    
        
    
    def backward(self):
        global new_image
        
        if self.image_index > 0:
            self.image_index = self.image_index - 1
        else:
            self.image_index = len(files) - 1  
        self.dir = os.path.join(sys.path[0], "images", files[self.image_index])

        
        image = Image.open(self.dir)
        resized_image = image.resize((self.canvas.winfo_width(), self.canvas.winfo_height()), Image.LANCZOS)
        new_image = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0,0, image=new_image, anchor="nw")



def main():
    global files
    files = {}
    for index, name in enumerate(os.listdir(os.path.join(sys.path[0], "images"))):
        files[index] = name
                    
        
    root = ImageViewer()
    root.mainloop()



if __name__ == "__main__":
    main()
