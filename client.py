import tkinter
import socket
from tkinter import *
from threading import Thread


window = Tk()
window.title("Chat Room Application")
window.config(bg="light blue")

message_frame = Frame(window, height=100, width=100, bg="green")
message_frame.pack()

my_msg = StringVar()
my_msg.set("")

scroll_bar = Scrollbar(message_frame)
msg_list = Listbox(message_frame, height=15, width=100, bg="light green", yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()

label = Label(window, text="Enter your message", fg="light blue", font="Arial", bg="blue")
label.pack()

entry_field = Entry(window, textvariable=my_msg, fg="white", width=800)
entry_field.pack()

send_button = Button(window, text="Send", font="Arial", fg="white", command=send)
send_button.pack()

quit_button = Button(window, text="Quit", font="Arial", fg="white", command=on_closing)
quit_button.pack()


host = "127.0.0.1"
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

receive_thread = Thread(target=receive)
receive_thread.start()

mainloop()