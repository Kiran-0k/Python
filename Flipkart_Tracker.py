import time
import smtplib
import requests
from bs4 import BeautifulSoup
import tkinter.messagebox
from ttkthemes import themed_tk as tk
from tkinter import ttk, Label, TOP, N, LEFT, StringVar, CENTER, BOTTOM, IntVar, Frame, X, W, NW, GROOVE, RIDGE


# ///Demo Links///

# https://www.flipkart.com/samsung-galaxy-s10-prism-white-128-gb/p/itmfdyp64j3hsfzy
# https://www.flipkart.com/mi-led-smart-tv-4x-108-cm-43/p/itmab87244d2fead
# https://www.flipkart.com/jbl-t450bt-extra-bass-bluetooth-headset-mic/p/itmf3vhgqqtat2eh
# https://www.flipkart.com/redmi-note-7-pro-space-black-64-gb/p/itmfegkx2gufuzhp

def popup():
    global link
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    }
    link = UIlink.get()
    source = requests.get(link, headers=head)
    soup = BeautifulSoup(source.content, 'html.parser')
    soup.encode('utf-8')
    global derkprice
    price = soup.find('div', class_='_1vC4OE _3qQ9m1').text
    derkprice = str(price)
    global title
    title = soup.find('span', class_='_35KyD6').text
    Product_title = Label(
        frame3, text=f'Product: {title}', font=('normal', 16, 'bold'))
    Product_title.pack(side=TOP, anchor=W, padx=10)
    Product_price = Label(
        frame3, text=f'Current Price: {price}',
        font=('normal', 16, 'bold'))
    Product_price.pack(side=TOP, anchor=W, padx=10, pady=10)
    user_info = Label(frame4, text='To Get Notified when the Price Drops ', font=(
        'times', 21, 'italic'))
    user_info.pack(pady=5, anchor=N)
    Price_prompt = Label(
        frame4, text='Enter your desired price:',
        font=('verdana', 12, 'bold'))
    Price_prompt.pack(side=LEFT, padx=10, pady=10)
    global UIProd_link
    UIProd_link = StringVar()
    Product_price = ttk.Entry(
        frame4, textvariable=UIProd_link, font=14, width=30)
    Product_price.pack(side=LEFT, fill=X, expand=True,
                       padx=100, anchor=CENTER)
    global UImail_Id
    UImail_Id = StringVar()
    notify = Label(frame5, text='Enter your Email Id:',
                   font=('verdana', 12, 'bold'))
    notify.pack(side=LEFT, padx=10, anchor=NW)
    User_mail_Id = ttk.Entry(
        frame5, textvariable=UImail_Id, font=15, width=50)
    User_mail_Id.pack(side=TOP, fill=X, expand=True,
                      padx=100, anchor=CENTER)
    Enter = ttk.Button(frame5, text='Notify ME!',
                       command=price_compare)
    Enter.pack(side=BOTTOM, padx=10, pady=15, anchor=CENTER)
    temp_price = price[1:8].replace(',', '')
    global comp_price
    comp_price = float(temp_price)
    global iterate_rate
    iterate_rate = IntVar()
    # Default:1.Set to 5 per day 2.Demo 3 per minute
    iterate_rate.set(1)
    opt1 = ttk.Radiobutton(
        frame6, text='Iterate 5/day', command=radio,
        variable=iterate_rate, value=1)
    opt1.pack(side=TOP, padx=20, pady=10)
    opt2 = ttk.Radiobutton(
        frame6, text='Iterate 3/minute(Demo)', command=radio,
        variable=iterate_rate, value=2)
    opt2.pack(side=BOTTOM, padx=20, pady=10)


def price_compare():
    global UIProd_link
    str_price = UIProd_link.get()
    global user_price
    user_price = float(str_price.replace(',', ''))
    if(comp_price >= user_price):
        tkinter.messagebox.showinfo(
            'Sh!t', f'You will be Notified when the price drops below ₹{str_price}')
    else:
        mail()


def mail():
    global UImail_Id
    mail_ID = UImail_Id.get()
    if '@' not in mail_ID:
        tkinter.messagebox.showerror(
            'Invalid Mail_Id', 'Please Enter a valid Email_ID')
    else:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        # Enter Service Mail_Id and Password
        server.login('#email', '#password')
        subject = 'Flipkart Price Tracker:Price Drop Alert'
        body = (f'The Price of the product has dropped to INR - {derkprice[1:]}\
         .You can buy it at:\n {link}')
        msg = f"Subject:{subject}\n\n{body}"
        # Enter Mail_Id again
        server.sendmail('#email', mail_ID, msg)
        tkinter.messagebox.showinfo('Congrats', "The Email has been sent!")
        server.quit()


def scrape():
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')
    price = soup.find('div', class_='_1vC4OE _3qQ9m1').text
    temp_price = price[1:8].replace(',', '')
    global comp_price
    comp_price = float(temp_price)
    if(comp_price >= user_price):
        tkinter.messagebox.showinfo('Info', 'Product Not yet available')
    else:
        mail()


def radio():
    conditn = iterate_rate.get()
    if(conditn == 1):
        for i in range(0, 5):
            scrape()
            time.sleep(60*60*24/5)

    elif(conditn == 2):
        for i in range(0, 3):
            scrape()
            time.sleep(20)


# UI Elements
GUI = tk.ThemedTk()
GUI.title("Flipkart Product Price Tracker")
GUI.geometry("+160+80")
GUI.get_themes()
GUI.set_theme("scidblue")
GUI.maxsize(1000, 700)

# Add your Program Icon here
# GUI.iconbitmap('code.ico')

frame1 = Frame(GUI, relief=GROOVE, bd=10, bg='deepskyblue')
frame1.pack(fill=X)
Welcome_text = Label(frame1, text='Flipkart Product Price Tracker', font=(
    'times', 30, 'underline'), width=400, bg='steelblue', relief=RIDGE)
Welcome_text.pack(fill=X, side=TOP)

frame2 = Frame(GUI)
frame2.pack(fill=X, anchor=N, padx=5, pady=10)
Link_Prompt = Label(frame2, text='Enter Product link:',
                    font=('verdana', 12, 'bold'))
Link_Prompt.pack(side=LEFT, anchor=N, pady=4)
UIlink = StringVar()
Product_link = ttk.Entry(frame2, textvariable=UIlink, font=14)
Product_link.pack(side=LEFT, padx=5, fill=X, expand=True)
Status = ttk.Button(frame2, text='Get Status!', command=popup)
Status.pack(pady=4)

frame3 = Frame(GUI, bd=5, relief=GROOVE)
frame3.pack(fill=X, pady=10)

frame4 = Frame(GUI)
frame4.pack(fill=X)

frame5 = Frame(GUI)
frame5.pack(fill=X, pady=5)

frame6 = Frame(GUI, background='gainsboro', bd=5, relief=GROOVE)
frame6.pack(fill=X)

GUI.mainloop()
