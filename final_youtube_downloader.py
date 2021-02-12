import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()



root = tk.Tk()
app = Application(master = root)
app.mainloop()