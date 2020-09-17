import tkinter as tk
from tkinter import *
import os
MAX_WIDTH = 700
MAX_HEIGHT = 700


def make_main_window():
    root = tk.Tk()
    root.title("The best messenger!")
    root.maxsize(MAX_WIDTH, MAX_HEIGHT)
    tk.Grid.rowconfigure(root, 0, weight=1)
    tk.Grid.columnconfigure(root, 0, weight=1)
    root.config(height=MAX_WIDTH, width=MAX_HEIGHT, bg="#263D42")

    return root


def make_main_buttons(root):
    button_height = int(root.winfo_height() / 150)
    button_width = int(root.winfo_width() / 80 * 4)
    registration_button = tk.Button(root, text="Registration",
                                    height=button_height, width=button_width,
                                    fg="#bfb3b3", bg="#263D42", borderwidth=0,
                                    activebackground="#263D42", activeforeground="White")

    enter_button = tk.Button(root, text="Login",
                             height=button_height, width=button_width,
                             fg="#bfb3b3", bg="#263D42", borderwidth=0,
                             activebackground="#263D42", activeforeground="White")
    # registration_button.grid(column=0, row=0, sticky="nsew")
    # enter_button.grid(column=1, row=0, sticky="nsew")
    # registration_button.pack(side=tk.LEFT, padx=[5, 5])
    # enter_button.pack(side=tk.RIGHT, padx=[5, 5])

# class Button:
#     """button1 = Button("Testo", "4ce", 0, 0)"""
#     row = 0
#     column = 0
#     def __init__(self, text, func, image=""):
#         image = tk.PhotoImage(file=image)
#         tk.Grid.rowconfigure(frame, Button.row, wight=1)
#         tk.Grid.columnconfigure(frame, Button.column, weight=1)
#
#         self.button = tk.Button(
#             frame,
#             text=text,
#             image=image,
#             compound=tk.LEFT,
#             command=func)
#         self.button.grid(sticky="nswe")
#         self.button.image = image
#         button.row += 1
#         )
# def make_main_new_buttons(root):



def make_main_frame(root):
    frame = tk.Frame(root, bg="#bfb3b3", image='my_messenger_logo.png')
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    frame.update()
    make_main_buttons(frame)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = make_main_window()
    make_main_frame(root)
    root.mainloop()

