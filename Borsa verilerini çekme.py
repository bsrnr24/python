import requests
from bs4 import BeautifulSoup
import tkinter as tk

url = 'https://uzmanpara.milliyet.com.tr/canli-borsa/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

data1 = soup.find('span', { 'id' : 'usd_header_son_data'}).text
data2 = soup.find('span', { 'id' : 'eur_header_son_data'}).text
data3 = soup.find('span', { 'id' : 'gld_header_son_data'}).text
data4 = soup.find('span', { 'id' : 'petrol_header_son_data'}).text
data5 = soup.find('span', { 'id' : 'btc_header_son_data'}).text

window = tk.Tk()
window.geometry('400x300')
window.title('BORSA')

label =tk.Label(window, text= 'GÜNCEL BORSA VERİLERİ', font= 'arial 20')
label.pack()
label.place(x=10, y=10)

label1 = tk.Label(window, text= {'DOLAR' : data1}, font= 'arial 15')
label1.pack()
label1.place(x=10, y=50)

label2 = tk.Label(window, text= {'EURO' : data2}, font= 'arial 15')
label2.pack()
label2.place(x=10, y=80)

label3 = tk.Label(window, text= {'ALTIN' : data3}, font= 'arial 15')
label3.pack()
label3.place(x=10, y=110)

label4 = tk.Label(window, text= {'PETROL' : data4}, font= 'arial 15')
label4.pack()
label4.place(x=10, y=140)

label5 = tk.Label(window, text= {'BITCOIN' : data5}, font= 'arial 15')
label5.pack()
label5.place(x=10, y=170)

window.mainloop()

yeniListe =['DOLAR :' + data1, 'EURO :' + data2, 'ALTIN :' + data3, 'PETROL :' + data4, 'BITCOIN :' + data5]

print(yeniListe)