import tkinter as tk
from tkinter import *
from tkinter import ttk
from selenium import webdriver

root=tk.Tk()
#tkinter ekranını oluşturdum.
root.geometry('300x200')
#tkinter ekran boyutunu ayarladım.
root.title('Instagram Bilgileri')
#tkinter ekranının ismini oluşturdum.

frame=tk.Frame(root)
frame.pack()
#ekranda çerçeve oluşturdum.


follower=''
#fonksiyon içerisinde kullanabilmek için global değişken tanımlaması yaptım.

def followerCount():
    global follower
    #global değişkeni fonksiyon içerisinde aktif hale getirdim.Bu sayede kullanıcı adını yazdığım hesabın takipçi sayısını almış olacağım.
    Username=inputusername.get()
    #tkinter ekranına yazılacak olan kullanıcı adını çağırıp aktif hale getirdim.
    driver=webdriver.Chrome()
    #tarayıcı açtım.
    driver.get('https://www.instagram.com/{}'.format(Username))
    #tarayıcıda instagram sayfasında girilen kullanıcı adına göre hesabı açmayı ve chrome yolunu belirttim.
    label2=tk.Label(frame,text='Takipçi Sayısı: {}'.format(follower))
    #almış olduğum takipçi sayısını yeni bir etiket olarak tkinter ekranında yazdırdım.
    label2.pack(padx=10,pady=1)
    #takipçi sayısının yazacağı etiketin boyutlarını ayarladım.
    
inputusername= StringVar()
#değişken her değiştiğinde otomatik olarak güncellenebilmesini sağladım.

label1=tk.Label(frame, text='KULLANICI ADI', font= ('Arial',15))
#ilk etiket için yazıyı, yazı tipi ve büyüklüğünü belirttim.
label1.pack(padx=10, pady=10)
#etiketin alanını büyüklük olarak belirledim.

entry=tk.Entry(frame, textvariable=inputusername)
#kullanıcı adı girişindeki metin değişkenini belirttim.
entry.pack(padx=5,pady=10)
#kullanıcı adı girilecek alanın büyüklüğünü oluşturdum.
entry.pack()

button=tk.Button(frame, text='TAKİPÇİ SAYISINI ÖĞREN', command=followerCount)
#buton oluşturup ne yazacağını tanımladım, butona tıkladıktan sonra yukarıda belirttiğim fonksiyona yönlendirdim.
button.pack(padx=15, pady=10)
#buton boyutunu oluşturdum.

root.mainloop()
