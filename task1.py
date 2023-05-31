#RANDOM PASSWORD GENERATOR
import random
import string
from tkinter import *

def gen_pass():
    length = int(length_entry.get())
    
    symbol = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + symbol 
    
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    
    pass_label.config(text=password)

page = Tk()
page.geometry("200x150")
page.title("Password Generator")

bg_color = "#374259"
btn_color = "#545B77"
text_color = "#F2D8D8"
page.configure(bg=bg_color)

length_label = Label(page, text="Password Length:", bg=bg_color, fg=text_color)
length_label.pack()
length_entry = Entry(page)
length_entry.pack()

gen_btn = Button(page, text="Generate", command=gen_pass, bg=btn_color,fg=text_color )
gen_btn.pack()

pass_label = Label(page, text="", bg=bg_color, fg=text_color)
pass_label.pack()

page.mainloop()
