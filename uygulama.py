# -'- coding:cp1254 -'-

from Tkinter import *
import sqlite3
import tkMessageBox





import time
from sinchsms import SinchSMS





def listele():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM kampanyalar")
        data = cursor.fetchall()  # gelen verileri data değişkenine atar.
        return data


def sepete_ekle():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        data=listele()
        cursor.execute("INSERT INTO sepet(urun_id,urun_adi,urun_markasi,urun_fiyat) VALUES(?,?,?,?)",(data[0][0],data[0][1],data[0][2],data[0][3]))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Bilgilendirme","Eklendi!")

def sepete_ekle1():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        data = listele()
        cursor.execute("INSERT INTO sepet(urun_id,urun_adi,urun_markasi,urun_fiyat) VALUES(?,?,?,?)",(data[1][0], data[1][1], data[1][2], data[1][3]))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Bilgilendirme", "Eklendi!")

def sepete_ekle2():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        data = listele()
        cursor.execute("INSERT INTO sepet(urun_id,urun_adi,urun_markasi,urun_fiyat) VALUES(?,?,?,?)",(data[2][0], data[2][1], data[2][2], data[2][3]))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Bilgilendirme", "Eklendi!")

def sepete_ekle3():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        data = listele()
        cursor.execute("INSERT INTO sepet(urun_id,urun_adi,urun_markasi,urun_fiyat) VALUES(?,?,?,?)",(data[3][0], data[3][1], data[3][2], data[3][3]))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Bilgilendirme", "Eklendi!")

def sepete_ekle4():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        data = listele()
        cursor.execute("INSERT INTO sepet(urun_id,urun_adi,urun_markasi,urun_fiyat) VALUES(?,?,?,?)",(data[4][0], data[4][1], data[4][2], data[4][3]))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Bilgilendirme", "Eklendi!")




def kampanyalar():
        yazi2.destroy()
        yazi3.destroy()
        yazi4.destroy()
        yazi5.destroy()
        yazi6.destroy()
        yazi7.destroy()
        yazi8.destroy()
        ktu.destroy()
        kutu.destroy()
        kutu2.destroy()
        buton.destroy()
        buton1.destroy()
        buton2.destroy()
        buton3.destroy()
        buton4.destroy()
        buton5.destroy()
        buton31.destroy()
        buton34.destroy()
        buton35.destroy()
        buton36.destroy()
        buton41.destroy()

        data=listele()

        yazi9 = Label()
        yazi9.config(text=str(data[0]).strip(" ,;()[]u'"), font=("", "12", ""),fg="green")
        yazi9.pack()


        buton6 = Button()
        buton6.config(text="Sepete Ekle", width=20, height=2,command=sepete_ekle)
        buton6.pack()

        yazi10 = Label()
        yazi10.config(text=str(data[1]).strip(" ,;()[]u'"), font=("", "12", ""),fg="green")
        yazi10.pack()

        buton7 = Button()
        buton7.config(text="Sepete Ekle", width=20, height=2,command=sepete_ekle1)
        buton7.pack()

        yazi11 = Label()
        yazi11.config(text=str(data[2]).strip(" ,;()[]u'"), font=("", "12", ""),fg="green")
        yazi11.pack()

        buton8 = Button()
        buton8.config(text="Sepete Ekle", width=20, height=2,command=sepete_ekle2)
        buton8.pack()

        yazi12 = Label()
        yazi12.config(text=str(data[3]).strip(" ,;()[]u'"), font=("", "12", ""),fg="green")
        yazi12.pack()

        buton9 = Button()
        buton9.config(text="Sepete Ekle", width=20, height=2,command=sepete_ekle3)
        buton9.pack()

        yazi13 = Label()
        yazi13.config(text=str(data[4]).strip(" ,;()[]u'"), font=("", "12", ""),fg="green")
        yazi13.pack()

        buton10 = Button()
        buton10.config(text="Sepete Ekle", width=20, height=2,command=sepete_ekle4)
        buton10.pack()







def listele2():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM gunun_firsatlari")
        dt = cursor.fetchall()  # gelen verileri data değişkenine atar.
        return dt


def sepete_ekle5():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        dt=listele2()
        cursor.execute("INSERT INTO sepet(urun_id,urun_adi,urun_markasi,urun_fiyat) VALUES(?,?,?,?)",(dt[0][0],dt[0][1],dt[0][2],dt[0][3]))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Bilgilendirme","Eklendi!")

def sepete_ekle6():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        dt = listele2()
        cursor.execute("INSERT INTO sepet(urun_id,urun_adi,urun_markasi,urun_fiyat) VALUES(?,?,?,?)",(dt[1][0], dt[1][1], dt[1][2], dt[1][3]))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Bilgilendirme", "Eklendi!")

def sepete_ekle7():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        dt = listele2()
        cursor.execute("INSERT INTO sepet(urun_id,urun_adi,urun_markasi,urun_fiyat) VALUES(?,?,?,?)",(dt[2][0], dt[2][1], dt[2][2], dt[2][3]))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Bilgilendirme", "Eklendi!")

def sepete_ekle8():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        dt = listele2()
        cursor.execute("INSERT INTO sepet(urun_id,urun_adi,urun_markasi,urun_fiyat) VALUES(?,?,?,?)",(dt[3][0], dt[3][1], dt[3][2], dt[3][3]))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Bilgilendirme", "Eklendi!")

def sepete_ekle9():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        dt = listele2()
        cursor.execute("INSERT INTO sepet(urun_id,urun_adi,urun_markasi,urun_fiyat) VALUES(?,?,?,?)",(dt[4][0], dt[4][1], dt[4][2], dt[4][3]))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Bilgilendirme", "Eklendi!")






def gunun_firsatlari():
        yazi2.destroy()
        yazi3.destroy()
        yazi4.destroy()
        yazi5.destroy()
        yazi6.destroy()
        yazi7.destroy()
        yazi8.destroy()
        ktu.destroy()
        kutu.destroy()
        kutu2.destroy()
        buton.destroy()
        buton1.destroy()
        buton2.destroy()
        buton3.destroy()
        buton4.destroy()
        buton5.destroy()
        buton31.destroy()
        buton34.destroy()
        buton35.destroy()
        buton36.destroy()
        buton41.destroy()
        dt=listele2()
        yazi14 = Label()
        yazi14.config(text=str(dt[0]).strip(" ,;()[]u'"), font=("", "12", ""), fg="green")
        yazi14.pack()

        buton11 = Button()
        buton11.config(text="Sepete Ekle", width=20, height=2,command=sepete_ekle5)
        buton11.pack()

        yazi15 = Label()
        yazi15.config(text=str(dt[1]).strip(" ,;()[]u'"), font=("", "12", ""), fg="green")
        yazi15.pack()

        buton12 = Button()
        buton12.config(text="Sepete Ekle", width=20, height=2,command=sepete_ekle6)
        buton12.pack()

        yazi16 = Label()
        yazi16.config(text=str(dt[2]).strip(" ,;()[]u'"), font=("", "12", ""), fg="green")
        yazi16.pack()

        buton13 = Button()
        buton13.config(text="Sepete Ekle", width=20, height=2,command=sepete_ekle7)
        buton13.pack()

        yazi17 = Label()
        yazi17.config(text=str(dt[3]).strip(" ,;()[]u'"), font=("", "12", ""), fg="green")
        yazi17.pack()

        buton14 = Button()
        buton14.config(text="Sepete Ekle", width=20, height=2,command=sepete_ekle8)
        buton14.pack()

        yazi18 = Label()
        yazi18.config(text=str(dt[4]).strip(" ,;()[]u'"), font=("", "12", ""), fg="green")
        yazi18.pack()

        buton15 = Button()
        buton15.config(text="Sepete Ekle", width=20, height=2,command=sepete_ekle9)
        buton15.pack()





def UyeOl():
        kdi=kadi.get()
        sfre=sifre.get()
        cnsyt=vr.get()
        epsta=eposta.get()
        tl=tel.get()
        krt_no=kart_no.get()
        Cvc=cvc.get()
        Son=son_kullanma.get()
        adrs=adres.get()

        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        cursor.execute("INSERT INTO uyeler(Kullanici_adi,Sifre,Cinsiyet,Eposta,Telefon,Kart_numarasi,Cvc,Son_kullanma_tarihi,il_ilce) VALUES(?,?,?,?,?,?,?,?,?)",(kdi,sfre,cnsyt,epsta,tl,krt_no,Cvc,Son,adrs))
        con.commit()
        con.close()
        tkMessageBox.showinfo(u"Bilgilendirme", u"Üye Olma İşlemi Başarılı!")



def uye_ol():
        yazi2.destroy()
        yazi3.destroy()
        yazi4.destroy()
        yazi5.destroy()
        yazi6.destroy()
        yazi7.destroy()
        yazi8.destroy()
        ktu.destroy()
        kutu.destroy()
        kutu2.destroy()
        buton.destroy()
        buton1.destroy()
        buton2.destroy()
        buton3.destroy()
        buton4.destroy()
        buton5.destroy()
        buton31.destroy()
        buton34.destroy()
        buton35.destroy()
        buton36.destroy()
        buton41.destroy()

        yazi19 = Label()
        yazi19.config(text=u"Kullanıcı Adı:", font=("", "12", ""))
        yazi19.pack()

        global kadi
        kadi = Entry()
        kadi.pack()

        yazi20 = Label()
        yazi20.config(text=u"Şifre:",font=("","12",""))
        yazi20.pack()

        global sifre
        sifre=Entry(show="*")
        sifre.pack()

        yazi21 = Label()
        yazi21.config(text=u"Cinsiyet:", font=("", "12", ""))
        yazi21.pack()

        global vr
        vr = IntVar()
        Radio1 = Radiobutton(text=u"Erkek", font=("", "12", ""), value=1, variable=vr)
        Radio1.pack()

        Radio2 = Radiobutton(text=u"Kadın", font=("", "12", ""), value=0, variable=vr)
        Radio2.pack()

        yazi22 = Label()
        yazi22.config(text=u"Eposta:", font=("", "12", ""))
        yazi22.pack()

        global eposta
        eposta = Entry()
        eposta.pack()

        yazi23 = Label()
        yazi23.config(text=u"Telefon:", font=("", "12", ""))
        yazi23.pack()

        global tel
        tel = Entry()
        tel.pack()

        yazi24 = Label()
        yazi24.config(text=u"Kart Numarası:", font=("", "12", ""))
        yazi24.pack()

        global kart_no
        kart_no = Entry()
        kart_no.pack()

        yazi25 = Label()
        yazi25.config(text=u"Cvc:", font=("", "12", ""))
        yazi25.pack()

        global cvc
        cvc = Entry()
        cvc.pack()

        yazi26 = Label()
        yazi26.config(text=u"Son Kullanma Tarihi:", font=("", "12", ""))
        yazi26.pack()

        global son_kullanma
        son_kullanma = Entry()
        son_kullanma.pack()

        yazi27 = Label()
        yazi27.config(text=u"İl-ilçe:", font=("", "12", ""))
        yazi27.pack()

        global adres
        adres = Entry()
        adres.pack()

        buton16 = Button()
        buton16.config(text="Üye Ol", width=20, height=2, command=UyeOl)
        buton16.pack()



def Sorgu():

        urunn=urun.get()
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        cursor.execute('SELECT * FROM urunler WHERE urun_adi = ? OR urun_markasi = ?', (urunn,urunn))
        global dataa
        dataa=cursor.fetchall()
        yazi33.config(text=str(dataa[0]).strip(" ,;[]()'u"),font=("","12",""),fg="brown")
        con.close()




def sepete_ekle10():
        dt=kimlik()
        dta=dt[0][0]
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        cursor.execute("INSERT INTO sepetim(urun_id,urun_adi,urun_markasi,fiyat,kullanici) VALUES(?,?,?,?,?)",(dataa[0][0], dataa[0][1], dataa[0][2], dataa[0][3],dta))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Bilgilendirme", "Eklendi!")





def listele3():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM kampanyalar")
        data = cursor.fetchall()  # gelen verileri data değişkenine atar.
        return data

def kimlik():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        kadi=kdi
        sifre=sfre
        cursor.execute('SELECT * FROM uyeler WHERE Kullanici_adi = ? AND Sifre = ?', (kadi, sifre))
        data = cursor.fetchall()
        con.close()
        return data

def sepete_ekle11():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        data=listele3()
        dta=kimlik()
        cursor.execute("INSERT INTO sepetim(urun_id,urun_adi,urun_markasi,fiyat,kullanici) VALUES(?,?,?,?,?)",(data[0][0], data[0][1], data[0][2], data[0][3], dta[0][0]))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Bilgilendirme", "Eklendi!")


def sepete_ekle12():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        data = listele3()
        dta=kimlik()
        cursor.execute("INSERT INTO sepetim(urun_id,urun_adi,urun_markasi,fiyat,kullanici) VALUES(?,?,?,?,?)",(data[1][0], data[1][1], data[1][2], data[1][3],dta[0][0]))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Bilgilendirme", "Eklendi!")


def sepete_ekle13():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        data = listele3()
        dta=kimlik()
        cursor.execute("INSERT INTO sepetim(urun_id,urun_adi,urun_markasi,fiyat,kullanici) VALUES(?,?,?,?,?)",(data[2][0], data[2][1], data[2][2], data[2][3],dta[0][0]))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Bilgilendirme", "Eklendi!")


def sepete_ekle14():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        data = listele3()
        dta=kimlik()
        cursor.execute("INSERT INTO sepetim(urun_id,urun_adi,urun_markasi,fiyat,kullanici) VALUES(?,?,?,?,?)",(data[3][0], data[3][1], data[3][2], data[3][3],dta[0][0]))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Bilgilendirme", "Eklendi!")


def sepete_ekle15():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        data = listele3()
        dta=kimlik()
        cursor.execute("INSERT INTO sepetim(urun_id,urun_adi,urun_markasi,fiyat,kullanici) VALUES(?,?,?,?,?)",(data[4][0], data[4][1], data[4][2], data[4][3],dta[0][0]))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Bilgilendirme", "Eklendi!")


def kampanya():
        yazi31.destroy()
        yazi32.destroy()
        yazi33.destroy()
        buton18.destroy()
        buton19.destroy()

        buton21.destroy()
        urun.destroy()
        buton22.destroy()
        buton23.destroy()
        dataaa=listele3()

        yazi34=Label()
        yazi34.config(text=str(dataaa[0]).strip(" ,;[]()'u"),font=("","12",""),fg="green")
        yazi34.pack()

        buton24=Button()
        buton24.config(text=u"Sepete Ekle",width=15,height=2,command=sepete_ekle11)
        buton24.pack()


        yazi35 = Label()
        yazi35.config(text=str(dataaa[1]).strip(" ,;[]()'u"),font=("","12",""),fg="green")
        yazi35.pack()

        buton25 = Button()
        buton25.config(text=u"Sepete Ekle", width=15, height=2,command=sepete_ekle12)
        buton25.pack()


        yazi36 = Label()
        yazi36.config(text=str(dataaa[2]).strip(" ,;[]()'u"),font=("","12",""),fg="green")
        yazi36.pack()

        buton26 = Button()
        buton26.config(text=u"Sepete Ekle", width=15, height=2,command=sepete_ekle13)
        buton26.pack()


        yazi37 = Label()
        yazi37.config(text=str(dataaa[3]).strip(" ,;[]()'u"),font=("","12",""),fg="green")
        yazi37.pack()

        buton27 = Button()
        buton27.config(text=u"Sepete Ekle", width=15, height=2,command=sepete_ekle14)
        buton27.pack()


        yazi38 = Label()
        yazi38.config(text=str(dataaa[4]).strip(" ,;[]()'u"),font=("","12",""),fg="green")
        yazi38.pack()

        buton28 = Button()
        buton28.config(text=u"Sepete Ekle", width=15, height=2,command=sepete_ekle15)
        buton28.pack()



def Satin_aldiklarim():
        yazi31.destroy()
        yazi32.destroy()
        yazi33.destroy()
        buton18.destroy()
        buton19.destroy()

        buton21.destroy()
        urun.destroy()
        buton22.destroy()
        buton23.destroy()

        dt=kimlik()
        dta=dt[0][0]
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        cursor.execute("SELECT urun_adi,SUM(toplam_fiyat),SUM(adet) FROM Odeme WHERE kullanici=? GROUP BY urun_adi",(dta,))
        data = cursor.fetchall()

        yazi39 = Label()
        yazi39.config(text=u"Satın Aldığım Ürünler Toplam Fiyat ve Adeti:", font=("", "12", ""))
        yazi39.pack()

        yazi40 = Label()
        yazi40.config(text=str(data[0]).strip(" ,;[]()'u"), font=("", "12", ""))
        yazi40.pack()

        yazi41 = Label()
        yazi41.config(text=str().strip(" ,;[]()'u"), font=("", "12", ""))
        yazi41.pack()
        con.close()

        yazi42 = Label()
        yazi42.config(text=str().strip(" ,;[]()'u"), font=("", "12", ""))
        yazi42.pack()

        yazi43 = Label()
        yazi43.config(text=str().strip(" ,;[]()'u"), font=("", "12", ""))
        yazi43.pack()


def Odeme():
        dt=kimlik()
        dtaa=dt[0][0]
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        cursor.execute("SELECT urun_adi,sum(fiyat),count(urun_adi) FROM sepetim WHERE kullanici=? GROUP BY urun_adi",(dtaa,))
        data=cursor.fetchall()

        for index in range(len(data)):
           cursor.execute("INSERT INTO Odeme(urun_adi,toplam_fiyat,adet,kullanici) VALUES(?,?,?,?)",(data[index][0], data[index][1],data[index][2],dtaa))
           con.commit()
        con.close()
        tkMessageBox.showinfo("Bilgilendirme", u"Satın Alındı!")
        yazi47.config(text=u"Satın alındı!",font=("","12",""),fg="green")




def Sepetim():
        yazi31.destroy()
        yazi32.destroy()
        yazi33.destroy()
        buton18.destroy()
        buton19.destroy()

        buton21.destroy()
        urun.destroy()
        buton22.destroy()
        buton23.destroy()

        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        dt=kimlik()
        dtt=dt[0][0]
        cursor.execute("SELECT urun_adi,SUM(fiyat),COUNT(urun_adi) FROM sepetim WHERE kullanici=? GROUP BY urun_adi",(dtt,))
        data = cursor.fetchall()


        yazi44 = Label()
        yazi44.config(text=u"Sepetimdeki Ürünler ve Toplam fiyat", font=("", "12", ""), fg="brown")
        yazi44.pack()

        for index in range(len(data)):

                yazi45 = Label()
                yazi45.config(text=str(data[index][0]).strip(" ,;()[]'u")+"  ", font=("", "12", ""), fg="brown")
                yazi45.pack()

        for index in range(len(data)):
                yazi46 = Label()
                yazi46.config(text=str(data[index][1]).strip(" ,;()[]'u")+"  ", font=("", "12", ""), fg="brown")
                yazi46.pack()

        for index in range(len(data)):
                yazi53 = Label()
                yazi53.config(text=str(data[index][2]).strip(" ,;()[]'u") + "  ", font=("", "12", ""), fg="brown")
                yazi53.pack()

        con.close()
        buton29 = Button()
        buton29.config(text=u"SATIN AL", width=15, height=2, command=Odeme)
        buton29.pack()

        global yazi47
        yazi47 = Label()
        yazi47.config(text=u"Satın Alınmadı!", font=("", "12", ""), fg="red")
        yazi47.pack()


def hesabimi_duzenle():
        pass


def hesabimi_sil():
        pass


def urun_cikar():
        pass


def mesajlarim():
        pass


def favorilerim():
        pass

def cikis():
        pass



def GirisYap():
        global kdi
        kdi=kadii.get()
        global sfre
        sfre=sifree.get()

        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        cursor.execute('SELECT * FROM uyeler WHERE Kullanici_adi = ? AND Sifre = ?', (kdi, sfre))

        if cursor.fetchall():
                con.close()
                yazi1.config(text=u"Sisteme Hoşgeldiniz!",font=("","12",""),fg="green")
                yazi28.destroy()
                kadii.destroy()
                yazi29.destroy()
                sifree.destroy()
                buton17.destroy()

                con = sqlite3.connect("Eticaret.db")
                cursor = con.cursor()
                cursor.execute('SELECT * FROM uyeler WHERE Kullanici_adi = ? AND Sifre = ?', (kdi, sfre))
                data=cursor.fetchall()
                yazi30=Label()
                yazi30.config(text=u"Sayın "+str(data[0][0]).strip(" ,;[]()u'"),font=("","12",""),fg="brown")
                yazi30.pack()
                con.close()

                global yazi31
                yazi31 = Label()
                yazi31.config(text=u"Seçenekler:", font=("", "10", ""), fg="green")
                yazi31.pack()
                global buton18
                buton18 = Button()
                buton18.config(text=u"Sepetim",width=20,height=2,command=Sepetim)
                buton18.pack()

                global buton19
                buton19 = Button()
                buton19.config(text=u"Satın Aldıklarım",width=20,height=2,command=Satin_aldiklarim)
                buton19.pack()


                global buton21
                buton21 = Button()
                buton21.config(text=u"Kampanyalar",width=20,height=2,command=kampanya)
                buton21.pack()

                buton37 = Button()
                buton37.config(text=u"Hesabımı Düzenle", width=20, height=2,command=hesabimi_duzenle)
                buton37.pack()

                buton38 = Button()
                buton38.config(text=u"Hesabımı Sil", width=20, height=2,command=hesabimi_sil)
                buton38.pack()

                buton39 = Button()
                buton39.config(text=u"Ürün Çıkar", width=20, height=2,command=urun_cikar)
                buton39.pack()

                buton40 = Button()
                buton40.config(text=u"Mesajlarım", width=20, height=2,command=mesajlarim)
                buton40.pack()

                buton42 = Button()
                buton42.config(text=u"Favorilerim", width=20, height=2,command=favorilerim)
                buton42.pack()

                buton43 = Button()
                buton43.config(text=u"Çıkış Yap", width=20, height=2,command=cikis)
                buton43.pack()

                global yazi32
                yazi32 = Label()
                yazi32.config(text=u"Ürün İle İlgili:", font=("", "10", ""), fg="green")
                yazi32.pack()

                global urun
                urun=Entry(width=50)
                urun.pack()

                global buton22
                buton22=Button()
                buton22.config(text=u"Sorgula",width=20,height=2,command=Sorgu)
                buton22.pack()

                global yazi33
                yazi33 = Label()
                yazi33.config(text=u"Ürün bilgisi listelenmedi!", font=("", "12", ""), fg="red")
                yazi33.pack()

                global buton23
                buton23 = Button()
                buton23.config(text=u"Sepete Ekle", width=15, height=2, command=sepete_ekle10)
                buton23.pack()




        else:
                tkMessageBox.showerror("Hata!",u"Kullanıcı adı veya şifrenizi doğru giriniz!")




def giris_yap():
        yazi1.config(text=u"Lütfen kullanıcı adı ve şifrenizi giriniz!",font=("","12",""),fg="brown")
        yazi2.destroy()
        yazi3.destroy()
        yazi4.destroy()
        yazi5.destroy()
        yazi6.destroy()
        yazi7.destroy()
        yazi8.destroy()
        ktu.destroy()
        kutu.destroy()
        kutu2.destroy()
        buton.destroy()
        buton1.destroy()
        buton2.destroy()
        buton3.destroy()
        buton4.destroy()
        buton5.destroy()
        buton31.destroy()
        buton34.destroy()
        buton35.destroy()
        buton36.destroy()
        buton41.destroy()

        global yazi28
        yazi28 = Label()
        yazi28.config(text=u"Kullanıcı Adı:", font=("", "12", ""))
        yazi28.pack()

        global kadii
        kadii = Entry()
        kadii.pack()

        global yazi29
        yazi29 = Label()
        yazi29.config(text=u"Şifre:", font=("", "12", ""))
        yazi29.pack()

        global sifree
        sifree = Entry(show="*")
        sifree.pack()

        global buton17
        buton17 = Button()
        buton17.config(text=u"Giriş Yap", width=20, height=2, command=GirisYap)
        buton17.pack()


def odeme():
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        cursor.execute("SELECT urun_adi,sum(urun_fiyat),count(urun_adi) FROM sepet GROUP BY urun_adi")
        dataaaa = cursor.fetchall()

        for index in range(len(dataaaa)):
                cursor.execute("INSERT INTO odeme_yap(urun_adi,adet,fiyat) VALUES(?,?,?)",(dataaaa[index][0], dataaaa[index][1], dataaaa[index][2]))
                con.commit()
        con.close()
        tkMessageBox.showinfo("Bilgilendirme", u"Satın Alındı!")
        yazi52.config(text=u"Satın alındı!", font=("", "12", ""), fg="green")


def alisveris_yap():
        yazi2.destroy()
        yazi3.destroy()
        yazi4.destroy()
        yazi5.destroy()
        yazi6.destroy()
        yazi7.destroy()
        yazi8.destroy()
        ktu.destroy()
        kutu.destroy()
        kutu2.destroy()
        buton.destroy()
        buton1.destroy()
        buton2.destroy()
        buton3.destroy()
        buton4.destroy()
        buton5.destroy()
        buton31.destroy()
        buton34.destroy()
        buton35.destroy()
        buton36.destroy()
        buton41.destroy()

        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        cursor.execute("SELECT urun_adi,SUM(urun_fiyat),COUNT(urun_adi) FROM sepet GROUP BY urun_adi")
        data = cursor.fetchall()


        yazi48=Label()
        yazi48.config(text=u"Sepetimdeki Ürünler ve Toplam Fiyat ve Adet",font=("","12",""),fg="brown")
        yazi48.pack()

        for index in range(len(data)):
                yazi49=Label()
                yazi49.config(text=str(data[index][0]).strip(" ,;()[]'u")+"  ",font=("","12",""),fg="green")
                yazi49.pack()

        for index in range(len(data)):

                yazi50= Label()
                yazi50.config(text=str(data[index][1]).strip(" ,;()[]'u")+"  ", font=("", "12", ""), fg="green")
                yazi50.pack()


        for index in range(len(data)):

                yazi51 = Label()
                yazi51.config(text=str(data[index][2]).strip(" ,;()[]'u")+"  ", font=("", "12", ""), fg="green")
                yazi51.pack()

        con.close()

        buton30 = Button()
        buton30.config(text=u"SATIN AL", width=15, height=2, command=odeme)
        buton30.pack()
        global yazi52
        yazi52 = Label()
        yazi52.config(text=u"Satın Alınmadı!", font=("", "12", ""), fg="red")
        yazi52.pack()


def ksorgula():
        kkadi=kadigiris.get()
        con = sqlite3.connect("Eticaret.db")
        cursor = con.cursor()
        cursor.execute("SELECT DISTINCT urun_adi FROM Odeme WHERE kullanici=?",(kkadi,))
        data = cursor.fetchall()

        yazi55.config(text=str(data[0]).strip(" ,;!()[]'u"), font=("", "14", ""), fg="brown")

        yazi56.config(text=str(data[1]).strip(" ,;()[]'u"), font=("", "14", ""), fg="brown")

        con.close()





def sikayett():

        number = '+5422781674'
        message = 'Hello from Sinch!'

        client = SinchSMS("c8f9cbf7-4709-4c5f-ad57-e71d9dfabc3b", "zfEITUhnP0WCTl4nTENiZw==")

        print("Sending '%s' to %s" % (message, number))
        response = client.send_message(number, message)
        message_id = response['messageId']

        response = client.check_status(message_id)
        while response['status'] != 'Successful':
                print(response['status'])
                time.sleep(1)
                response = client.check_status(message_id)
        print(response['status'])












def urun_sikayet():
        yazi2.destroy()
        yazi3.destroy()
        yazi4.destroy()
        yazi5.destroy()
        yazi6.destroy()
        yazi7.destroy()
        yazi8.destroy()
        ktu.destroy()
        kutu.destroy()
        kutu2.destroy()
        buton.destroy()
        buton1.destroy()
        buton2.destroy()
        buton3.destroy()
        buton4.destroy()
        buton5.destroy()
        buton31.destroy()
        buton34.destroy()
        buton35.destroy()
        buton36.destroy()
        buton41.destroy()

        yazi53=Label()
        yazi53.config(text=u"Kullanıcı Adı:",font=("","12",""),fg="brown")
        yazi53.pack()

        global kadigiris
        kadigiris=Entry(width=40)
        kadigiris.pack()

        buton32=Button()
        buton32.config(text=u"Sorgula",width=20,height=2,command=ksorgula)
        buton32.pack()

        yazi54 = Label()
        yazi54.config(text=u"Ürünler Listeleniyor...", font=("", "14", ""), fg="green")
        yazi54.pack()

        global yazi55
        yazi55 = Label()
        yazi55.config(text=u"Ürün Listelenmedi!", font=("", "14", ""), fg="red")
        yazi55.pack()

        global yazi56
        yazi56 = Label()
        yazi56.config(text=u"Ürün Listelenmedi!", font=("", "14", ""), fg="red")
        yazi56.pack()

        global yazi57
        yazi57 = Label()
        yazi57.config(text=u"Ürün Listelenmedi!", font=("", "14", ""), fg="red")
        yazi57.pack()

        yazi58 = Label()
        yazi58.config(text=u"Ürün Hakkında Şikayetiniz:", font=("", "12", ""), fg="brown")
        yazi58.pack()

        sikayet = Text(pencere, height=10, width=40)
        sikayet.pack()

        yazi59 = Label()
        yazi59.config(text=u"Telefon:", font=("", "12", ""), fg="brown")
        yazi59.pack()

        tel=Entry(width=40)
        tel.pack()

        buton33=Button()
        buton33.config(text=u"Gönder",width=20,height=2,command=sikayett)
        buton33.pack()


def yardim_destek():
        pass


def bize_sorun():
        pass


def encok():
        pass

def sifremi_unuttum():
        pass



def Sorgula():
        con = sqlite3.connect("Eticaret.db")
        ifade1=ktu.get()
        ifade2=kutu.get()
        ifade3=kutu2.get()
        liste = [ifade1, ifade2, ifade3]
        yeni = ["", "", ""]
        say = 0
        sy = 0
        konum = ["", "", ""]
        for i in liste:
                sy += 1
                if i != "":
                        yeni[say] = i
                        konum[say] = sy
                        say += 1

        sorgu="SELECT * FROM urunler WHERE"
        deger=""
        for j in konum:
                if j==1:
                        sorgu=sorgu+" urun_adi=? AND"
                        deger=deger+"ifade1,"
                if j==2:
                        sorgu=sorgu+" urun_markasi=? AND"
                        deger=deger+"ifade2,"
                if j==3:
                        sorgu=sorgu+" fiyat=? AND"
                        deger=deger+"ifade3,"



        if sorgu[-3:]=="AND":
                sorgu=sorgu[:-4]



        deger=deger[:-1]

        cursor = con.cursor()
      #  cursor.execute('SELECT * FROM urunler WHERE urun_adi = ? OR urun_markasi = ? OR fiyat= ?',(ifade1,ifade2,ifade3))
      #  eval stringin içindekileri değer olarak algılar.
        cursor.execute(sorgu,(eval(deger)))
        data = cursor.fetchall()  # gelen verileri data değişkenine atar.
        if len(data)>0:
                yazi5.config(text=u"Ürünün Adı: "+str(data[0][1]).strip(" ,;()[]u"))
                yazi6.config(text=u"Ürününü Markası: "+str(data[0][2]).strip(" ,;()[]u"))
                yazi7.config(text=u"Ürünün Fiyatı: "+str(data[0][3]).strip(" ,;()[]u"))
                yazi8.config(text=u"Ürünün Adeti: "+str(data[0][4]).strip(" ,;()[]u"))
        else:
                yazi5.config(text=u"Ürünün adı bilgisi bulunamadı!")
                yazi6.config(text=u"Ürününü markası bilgisi bulunamadı!")
                yazi7.config(text=u"Ürünün fiyatı bilgisi bulunamadı!")
                yazi8.config(text=u"Ürünün adeti bilgisi bulunamadı!")


pencere=Tk() #pencereyi oluşturduk

pencere.title(u"E-TİCARET SİSTEMİ!")
pencere.geometry("800x900+300+10") #yukardan 100 aşağıdan 100 800-600 boyut olacaktır.


yazi1=Label(pencere)
yazi1.config(text=u"Hoşgeldiniz!",font=("","15",""))
yazi1.pack()

yazi2=Label(pencere)
yazi2.config(text=u"Ürün Adı:",font=("","12",""))
yazi2.pack()

ktu=Entry(pencere)
ktu.pack()

yazi3=Label(pencere)
yazi3.config(text=u"Ürün Markası:", font=("","12",""))
yazi3.pack()

kutu=Entry(pencere)
kutu.pack()

yazi4=Label(pencere)
yazi4.config(text=u"Fiyatı:",font=("","12",""))
yazi4.pack()

kutu2=Entry(pencere)
kutu2.pack()

buton=Button(pencere)
buton.config(text="Ara",command=Sorgula,width=20,height=2)
buton.pack()


yazi5=Label(pencere)
yazi5.config(text=u"Ürün bilgisi listelenmedi!\n",font=("","12",""),fg="red")
yazi5.pack()

yazi6=Label(pencere)
yazi6.config(text=u"Ürün bilgisi listelenmedi!\n",font=("","12",""),fg="red")
yazi6.pack()

yazi7=Label(pencere)
yazi7.config(text=u"Ürün bilgisi listelenmedi!\n",font=("","12",""),fg="red")
yazi7.pack()

yazi8=Label(pencere)
yazi8.config(text=u"Ürün bilgisi listelenmedi!\n",font=("","12",""),fg="red")
yazi8.pack()


buton1=Button(pencere)
buton1.config(text=u"Kampanyalar",width=20,height=1,command=kampanyalar)
buton1.pack()


buton2=Button(pencere)
buton2.config(text=u"Günün Fırsatları",width=20,height=1,command=gunun_firsatlari)
buton2.pack()


buton3=Button(pencere)
buton3.config(text=u"Üye Ol",width=20,height=1,command=uye_ol)
buton3.pack()


buton4=Button(pencere)
buton4.config(text=u"Giriş Yap",width=20,height=1,command=giris_yap)
buton4.pack()


buton5=Button(pencere)
buton5.config(text=u"Alışveriş Yap",width=20,height=1,command=alisveris_yap)
buton5.pack()


buton31=Button(pencere)
buton31.config(text=u"Ürün Şikayet Sistemi",width=20,height=1,command=urun_sikayet)
buton31.pack()

buton34=Button(pencere)
buton34.config(text=u"Yardım ve Destek",width=20,height=1,command=yardim_destek)
buton34.pack()

buton35=Button(pencere)
buton35.config(text=u"Bize Sorun",width=20,height=1,command=bize_sorun)
buton35.pack()

buton36=Button(pencere)
buton36.config(text=u"Ençok Satan,Endüşük Fiyatlı",width=20,height=1,command=encok)
buton36.pack()

buton41=Button(pencere)
buton41.config(text=u"Şifremi Unuttum",width=20,height=1,command=sifremi_unuttum)
buton41.pack()

mainloop()



