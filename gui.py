from tkinter import *

class Window:
    def __init__(self, width, heigth, x=50, y=450, title = "YouTube downloader", background = '#851e3e', resizable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{heigth}+{x}+{y}")
        self.root.resizable(resizable[0], resizable[1])
        self.root['background']= background

        self.label = Label(self.root, text = "I'm label", bg = '#851e3e')

    def draw_widgets(self):
        self.label.pack()



    def run(self):
        self.draw_widgets()
        self.root.mainloop()


window = Window(500,250) #Window size
window.run()
 
