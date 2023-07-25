import tkinter
import socket
from tkinter import *
from threading import Thread


window = Tk()
window.title("Chat Room Application")
window.config(bg="blue")

message_frame = Frame(window, height=100, width=100, bg="green")
message_frame.pack()

my_msg = StringVar()
my_msg.set("")

scroll_bar = Scrollbar(message_frame)
msg_list = Listbox(message_frame, height=15, width=100, bg="light green", yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()


mainloop()