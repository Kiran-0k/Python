from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
import tkinter.messagebox

from bs4 import BeautifulSoup
import requests

import smtplib
import time
from datetime import datetime


link = ''
derkprice = ''
title = ''
comp_price = 0.0
UIProd_link = ''
user_price = 0.0
UImail_Id = ''
iterate_rate = 0

#  https://www.flipkart.com/samsung-galaxy-s10-prism-white-128-gb/p/itmfdyp64j3hsfzy
#  https://www.flipkart.com/mi-led-smart-tv-4x-108-cm-43/p/itmab87244d2fead
# https://www.flipkart.com/nikon-d5600-dslr-camera-body-single-lens-af-p-dx-nikkor-18-55-mm-f-3-5-5-6g-vr-16-gb-sd-card/p/itmezvbdzefvjpfn
# https://www.flipkart.com/jbl-t450bt-extra-bass-bluetooth-headset-mic/p/itmf3vhgqqtat2eh
# https://www.flipkart.com/redmi-note-7-pro-space-black-64-gb/p/itmfegkx2gufuzhp
# https://www.flipkart.com/acer-predator-helios-300-core-i5-8th-gen-8-gb-1-tb-hdd-128-gb-ssd-windows-10-home-4-graphics-ph315-51-ph315-51-51v7-ph315-51-55xx-gaming-laptop/p/itm913399b8faf3d


def popup():
	print('Executing popup function')
	global link
	link = UIlink.get()
	print('Getting link data')
	source = requests.get(link).text
	soup = BeautifulSoup(source, 'lxml')
	print('Getting source data')
	global derkprice
	print('Getting Price:')
	price = soup.find('div', class_='_1vC4OE _3qQ9m1').text
	print(price)
	derkprice=str(price)
	global title
	print('Getting Title:')
	title = soup.find('span', class_='_35KyD6').text
	print(title)
	Product_title = Label(frame3, text=f'Product: {title}', font=('normal',16,'bold'))
	Product_title.pack(side=TOP,anchor=W, padx=10)
	Product_price = Label(frame3,text = f'Current Price: {price}',font = ('normal',16,'bold'))
	Product_price.pack(side=TOP,anchor=W, padx=10, pady=10)
	user_info = Label(frame4, text='To Get Notified when the Price Drops ', font=('times',21,'italic'))
	user_info.pack(pady=5, anchor=N)
	Price_prompt = Label(frame4, text='Enter your desired price:', font=('verdana',12,'bold'))
	Price_prompt.pack(side=LEFT, padx=10, pady=10)
	global UIProd_link
	UIProd_link = StringVar()      
	Product_price = ttk.Entry(frame4,textvariable = UIProd_link,font = 14, width=30)
	Product_price.pack(side=LEFT, fill=X, expand=True, padx=100, anchor=CENTER)
	global UImail_Id
	UImail_Id = StringVar()
	notify = Label(frame5,text = 'Enter your Email Id:',font = ('verdana',12,'bold'))
	notify.pack(side=LEFT, padx=10, anchor=NW)
	User_mail_Id = ttk.Entry(frame5,textvariable = UImail_Id,font = 15, width=50)
	User_mail_Id.pack(side=TOP, fill=X, expand=True, padx=100, anchor=CENTER)
	Enter = ttk.Button(frame5,text = 'Notify ME!',command = price_compare)
	Enter.pack(side=BOTTOM, padx=10, pady=15, anchor=CENTER)
	print('Converting price[str to float]')
	temp_price = price[1:8].replace(',','')
	global comp_price
	comp_price = float(temp_price)
	print('Comp Price:' + str(comp_price))
	global iterate_rate
	iterate_rate = IntVar()
	# iterate_rate.set(2)
	opt1 = ttk.Radiobutton(frame6, text='Iterate 5/day',command=radio, variable=iterate_rate, value=1)
	opt1.pack(side=TOP, padx=20, pady=10)
	opt2 = ttk.Radiobutton(frame6, text='Iterate 3/minute(Demo)',command=radio, variable=iterate_rate, value=2)
	opt2.pack(side=BOTTOM, padx=20, pady=10)


def price_compare():
	global UIProd_link
	print('Getting User Price')
	str_price = UIProd_link.get()
	print('User Price:' + str_price)
	global user_price
	user_price = float(str_price)
	print('Comparing User Price')
	if(comp_price >= user_price):
		print(str(comp_price) + ' >= ' + str(user_price))
		tkinter.messagebox.showinfo('Sh!t',f'You will be Notified when the price drops below ₹{str(user_price)}')
	else:
		print(f'Calling mail function: {str(comp_price)} < {str(user_price)}')
		mail()


def mail():
	global UImail_Id
	print('Entering mail function')
	mail_ID = UImail_Id.get()
	print('Getting mailID')
	print(mail_ID)
	server =smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('#email','#password')     #Enter Service Mail_Id and Password
	print('Cooking Subject and Message')
	subject ='Flipkart Price Tracker:Price Drop Alert'
	body =(f'The Price of the product has dropped to INR - {derkprice[1:]}.You can buy it at:\n {link}')
	msg =f"Subject:{subject}\n\n{body}"
	print('Sending Email')
	server.sendmail('#email', mail_ID ,msg)        #Enter Mail_Id again
	tkinter.messagebox.showinfo('Congrats',"The Email has been sent!")
	print("Email has been sent")
	server.quit()

def scrape():
	print('Running Post-Scrape function')
	now = datetime.now()
	print(now)
	source = requests.get(link).text
	soup = BeautifulSoup(source, 'lxml')
	# global price
	price = soup.find('div', class_='_1vC4OE _3qQ9m1').text
	temp_price = price[1:8].replace(',','')
	global comp_price
	comp_price = float(temp_price)
	if(comp_price >= user_price):
		print(f'{str(comp_price)} >= {str(user_price)}')
		print('Product Not yet available')
	else:
		print(f'Calling mail function: {str(comp_price)} < {str(user_price)}')
		mail()


def radio():
	print('Executing Radio function')
	conditn = iterate_rate.get()
	print(conditn)
	if(conditn == 1):
		print('Option 5/day')
		for i in range(0,5):
			scrape()
			time.sleep(60*60*24/5)

	elif(conditn == 2):
		print('Option 3/minute')
		for i in range(0,3):
			scrape()
			time.sleep(20)

 
#UI Elements
GUI = tk.ThemedTk()
GUI.title("Flipkart Product Price")
GUI.geometry("+160+80")
GUI.get_themes()
GUI.set_theme("scidblue")
GUI.maxsize(1000,700)
# GUI.iconbitmap('code.ico')

frame1 = Frame(GUI, relief=GROOVE, bd=10, bg='deepskyblue')
frame1.pack(fill=X)
Welcome_text = Label(frame1, text='Flipkart Product Price', font=('times',30,'underline')
	                    , width=400, bg='steelblue', relief=RIDGE)
Welcome_text.pack(fill=X, side=TOP)

frame2 = Frame(GUI)
frame2.pack(fill=X, anchor=N, padx=5, pady=10)
Link_Prompt = Label(frame2,text = 'Enter Product link:',font = ('verdana',12,'bold'))
Link_Prompt.pack(side=LEFT, anchor=N,pady=4)
UIlink = StringVar()
Product_link = ttk.Entry(frame2, textvariable=UIlink, font=14)
Product_link.pack(side=LEFT, padx=5, fill=X, expand=True)
Status = ttk.Button(frame2,text = 'Get Status!',command = popup)
Status.pack(pady=4)

frame3 = Frame(GUI, bd=5, relief=GROOVE)
frame3.pack(fill=X,pady=10)

frame4 = Frame(GUI)
frame4.pack(fill=X)

frame5 = Frame(GUI)
frame5.pack(fill=X,pady=5)

frame6 = Frame(GUI, background='gainsboro',bd=5, relief=GROOVE)
frame6.pack(fill=X)

GUI.mainloop()
