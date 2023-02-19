from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import requests
import json
import time

c1 = "white"
c2 = "black"

window = Tk()
window.title('')
window.geometry('320x150')
window.configure(bg=c1)


def btc():
    api = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=BTC,USD"
    res = requests.get(api)
    data = res.json()

    usd_price = float(data["USD"])
    usd_formatted_price = "${:,.3f}".format(usd_price)
    usd["text"] = usd_formatted_price
    body.after(1000, btc)


head_frame = Frame(window, width=320, height=50, bg=c1)
head_frame.grid(row=1, column=0)

body = Frame(window, width=320, height=300, bg="grey")
body.grid(row=2, column=0)

img1 = Image.open('images/bit.png')
img1 = img1.resize((30, 30))
img1 = ImageTk.PhotoImage(img1)

icon1 = Label(head_frame, padx=0, image=img1, bg=c1)
icon1.place(x=10, y=10)

title = Label(head_frame, padx=0, text="Bitcoin Price", bg=c1, fg=c2, width=16, height=1, anchor="w",
              font='Poppins 20')
title.place(x=50, y=11)

usd = Label(body, bg="grey", pady=0, fg=c1, text="$223", width=14, height=1, anchor="w", font='Poppins 30')
usd.place(x=0, y=30)

btc()

window.mainloop()
