import tkinter as tk
from tkinter import ttk

import base64

class Spinbox(ttk.Entry):

    def __init__(self, master=None, **kw):

        ttk.Entry.__init__(self, master, "ttk::spinbox", **kw)
    def set(self, value):
        self.tk.call(self._w, "set", value)


class View(object):
    root = None

    edit_var = None
    label_var = None
    doit_button = None

    def __init__(self):
        self.root = tk.Tk()

        self.root.title('Interactive Helloworld')

        x, y, w, h = 500, 200, 700, 100
        self.root.geometry('%sx%s+%s+%s' % (w, h, x, y))

        main_frame = ttk.Frame(self.root)
        main_frame['padding'] = (5, 5)
        main_frame.pack(side='top', fill='both', expand=True)

        label1 = ttk.Label(main_frame, text='Point:')
        label1.grid(row=0, column=0)
        label2 = ttk.Label(main_frame, text='Base:')
        label2.grid(row=1, column=0)

        self.spin1 = Spinbox(main_frame, from_=1, to=100000, wrap=True, width=7)
        self.spin1.grid(row=0, column=1)

        self.spin2 = Spinbox(main_frame, from_=1, to=100000, wrap=True, width=7)
        self.spin2.grid(row=1, column=1)

        label3 = ttk.Label(main_frame, text='Input:')
        label3.grid(row=0, column=2)
        label4 = ttk.Label(main_frame, text='Result:')
        label4.grid(row=1, column=2)

        self.inp_var = tk.IntVar()
        edit1 = ttk.Entry(main_frame, textvariable=self.inp_var)
        edit1.grid(row=0, column=3, sticky="we")
        main_frame.grid_columnconfigure(3, weight=1)

        self.out_var = tk.IntVar()
        edit2 = ttk.Entry(main_frame, textvariable=self.out_var)
        edit2.grid(row=1, column=3, sticky="we")      

        
##        in_frame = tkinter.ttk.Frame(main_frame)
##        in_frame.pack(side='left')
##
##        out_frame = tkinter.ttk.Frame(main_frame)
##        out_frame.pack(side='left')
##
##        self.edit_var = tkinter.StringVar()
##        edit = tkinter.ttk.Entry(main_frame, textvariable=self.edit_var)
##        edit.pack(side='top', fill='x')
##
##        self.label_var = tkinter.StringVar()
##        label = tkinter.ttk.Label(main_frame, textvariable=self.label_var)
##        label.pack(side='top', fill='x')
##
        self.doit_button = ttk.Button(main_frame, text='DO IT')
        self.doit_button.grid(row=2, column=1)

    def close(self):
        self.root.destroy()
        self.root.quit()


class Model(object):
    ui = None

    def __init__(self, view):
        self.ui = view

    def doit(self):
##        word = 'PYTHON'
##        b64 = base64.b64encode(word)
##        print(b64)
        
        point = int(self.ui.spin1.get())
        base = int(self.ui.spin2.get())

        text = str(point/base)
        self.ui.out_var.set(text)


class Ctrl(object):
    view = None
    model = None

    def __init__(self):
        self.view = View()
        self.model = Model(self.view)

        self.bind()

        self.view.root.protocol('WM_DELETE_WINDOW', self.close_handler)
        self.view.root.mainloop()

    def bind(self):
        self.view.doit_button.bind("<Button-1>", self.doit_handler)
        
        self.view.spin1.bind("<<Increment>>", self.doit_handler)
        self.view.spin1.bind("<<Decrement>>", self.doit_handler)

        self.view.spin2.bind("<<Increment>>", self.doit_handler)
        self.view.spin2.bind("<<Decrement>>", self.doit_handler)        
        

    def doit_handler(self, event):
        self.model.doit()

    def close_handler(self):
        self.view.close()


class App(object):
    ctrl = None

    def __init__(self):
        self.ctrl = Ctrl()


if __name__ == '__main__':
    app = App()
