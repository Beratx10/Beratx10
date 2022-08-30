from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton,QLineEdit
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
import sys



class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,100,500,500)
        self.setWindowTitle("Net Hesaplama")
        self.setStyleSheet("background:beige")
        self.pencereler = []
        self.sınavlar()

    def sınavlar(self):

        self.tyt = QtWidgets.QPushButton("TYT")
        self.tyt.setFont(QFont("Arial",23))
        self.tyt.setStyleSheet("background:grey")
        self.ayt = QtWidgets.QPushButton("AYT")
        self.ayt.setFont(QFont("Arial",23))
        self.ayt.setStyleSheet("background:grey")
        self.dgs = QtWidgets.QPushButton("DGS")
        self.dgs.setFont(QFont("Arial",23))
        self.dgs.setStyleSheet("background:grey")


        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.tyt)
        v_box.addStretch()
        v_box.addWidget(self.ayt)
        v_box.addStretch()
        v_box.addWidget(self.dgs)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        

        self.setLayout(h_box)

        self.tyt.clicked.connect(self.tytt)
        self.ayt.clicked.connect(self.aytt)
        self.dgs.clicked.connect(self.dgss)

        


    def tytt(self):
        pencere2 = Pencere2()
        self.pencereler.append(pencere2)
    
    
    def aytt(self):
        pencere3 = Pencere3()
        self.pencereler.append(pencere3)
    
    
    def dgss(self):
        pencere4 = Pencere4()
        self.pencereler.append(pencere4)


class Pencere2(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.tyt()
        
        


    def tyt(self):


        self.dogru = QtWidgets.QLabel(self)
        self.dogru.setText("Doğru")
        self.dogru.setFont(QFont("Arial",15))
        self.dogru.setGeometry(280,2,80,40)

        self.yanlış = QtWidgets.QLabel(self)
        self.yanlış.setText("Yanlış")
        self.yanlış.setFont(QFont("Arial",15))
        self.yanlış.setGeometry(400,2,80,40)



        self.türkçe = QtWidgets.QLabel(self)
        self.türkçe.setText("Türkçe / 40")
        self.türkçe.setGeometry(60,20,200,80)
        self.türkçe.setFont(QFont("Arial",17))

        self.türkçe_dogru = QtWidgets.QLineEdit(self)
        self.türkçe_dogru.setMaxLength(2)
        self.türkçe_dogru.setGeometry(270,50,80,30)
        self.türkçe_dogru.setFont(QFont("Arial",17))
        self.türkçe_yanlış = QtWidgets.QLineEdit(self)
        self.türkçe_yanlış.setMaxLength(2)
        self.türkçe_yanlış.setGeometry(390,50,80,30)
        self.türkçe_yanlış.setFont(QFont("Arial",17))
        

        

        self.sosyal = QtWidgets.QLabel(self)
        self.sosyal.setText("Sosyal Bilimler / 20")
        self.sosyal.setGeometry(60,90,200,80)
        self.sosyal.setFont(QFont("Arial",17))

        self.sosyal_dogru = QtWidgets.QLineEdit(self)
        self.sosyal_dogru.setMaxLength(2)
        self.sosyal_dogru.setGeometry(270,115,80,30)
        self.sosyal_dogru.setFont(QFont("Arial",17))
        self.sosyal_yanlış = QtWidgets.QLineEdit(self)
        self.sosyal_yanlış.setMaxLength(2)
        self.sosyal_yanlış.setGeometry(390,115,80,30)
        self.sosyal_yanlış.setFont(QFont("Arial",17))


        self.matematik = QtWidgets.QLabel(self)
        self.matematik.setText("Matematik / 40")
        self.matematik.setGeometry(60,170,200,80)
        self.matematik.setFont(QFont("Arial",17))

        self.mat_dogru = QtWidgets.QLineEdit(self)
        self.mat_dogru.setMaxLength(2)
        self.mat_dogru.setGeometry(270,195,80,30)
        self.mat_dogru.setFont(QFont("Arial",17))
        self.mat_yanlış = QtWidgets.QLineEdit(self)
        self.mat_yanlış.setMaxLength(2)
        self.mat_yanlış.setGeometry(390,195,80,30)
        self.mat_yanlış.setFont(QFont("Arial",17))



        self.fen = QtWidgets.QLabel(self)
        self.fen.setText("Fen Bilimleri / 20")
        self.fen.setGeometry(60,250,200,80)
        self.fen.setFont(QFont("Arial",17))

        self.fen_dogru = QtWidgets.QLineEdit(self)
        self.fen_dogru.setMaxLength(2)
        self.fen_dogru.setGeometry(270,275,80,30)
        self.fen_dogru.setFont(QFont("Arial",17))
        self.fen_yanlış = QtWidgets.QLineEdit(self)
        self.fen_yanlış.setMaxLength(2)
        self.fen_yanlış.setGeometry(390,275,80,30)
        self.fen_yanlış.setFont(QFont("Arial",17))


        self.net = QtWidgets.QLabel(self)
        self.net.setText("Toplam Net")
        self.net.setGeometry(60,330,200,80)
        self.net.setFont(QFont("Arial",17))

        self.net_hesap = QtWidgets.QLineEdit(self)
        self.net_hesap.setGeometry(200,350,80,40)
        self.net_hesap.setFont(QFont("Arial",17))

        self.puan = QtWidgets.QLabel(self)
        self.puan.setText("Puan")
        self.puan.setGeometry(300,330,200,80)
        self.puan.setFont(QFont("Arial",17))

        self.puan_hesap = QtWidgets.QLineEdit(self)
        self.puan_hesap.setMaxLength(5)
        self.puan_hesap.setGeometry(370,350,80,40)
        self.puan_hesap.setFont(QFont("Arial",17))




        self.hesapla = QtWidgets.QPushButton(self)
        self.hesapla.setText("Hesapla")
        self.hesapla.setGeometry(310,420,100,50)
        self.hesapla.setFont(QFont("Arial",17))
        self.hesapla.clicked.connect(self.hesaplaa)

        self.temizle = QtWidgets.QPushButton(self)
        self.temizle.setText("Temizle")
        self.temizle.setGeometry(90,420,100,50)
        self.temizle.setFont(QFont("Arial",17))
        self.temizle.clicked.connect(self.clear)

        self.setGeometry(400,100,500,500)
        self.setWindowTitle("TYT Net Hesaplama")
        self.setStyleSheet("background:beige")
        self.show()
    
    def hesaplaa(self):

        türkçe = int(self.türkçe_dogru.text())
        türkçee = int(self.türkçe_yanlış.text())
        sosyal = int(self.sosyal_dogru.text())
        sosyall = int(self.sosyal_yanlış.text())
        mat = int(self.mat_dogru.text())
        matt = int(self.mat_yanlış.text())
        fen = int(self.fen_dogru.text())
        fenn = int(self.fen_yanlış.text())

        net = (türkçe-(türkçee/4)+(sosyal-(sosyall/4)+(mat-(matt/4)+(fen-(fenn/4)))))
        puan = net*4.5

        self.net_hesap.setText(str(net))
        self.puan_hesap.setText(str(puan))
        
        self.show()




    
    def clear(self):
        self.türkçe_dogru.clear()
        self.türkçe_yanlış.clear()
        self.mat_dogru.clear()
        self.mat_yanlış.clear()
        self.fen_dogru.clear()
        self.fen_yanlış.clear()
        self.sosyal_dogru.clear()
        self.sosyal_yanlış.clear()
        


        


class Pencere3(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.ayt()
        
        


    def ayt(self):


        self.dogru = QtWidgets.QLabel(self)
        self.dogru.setText("Doğru")
        self.dogru.setFont(QFont("Arial",15))
        self.dogru.setGeometry(280,2,80,40)

        self.yanlış = QtWidgets.QLabel(self)
        self.yanlış.setText("Yanlış")
        self.yanlış.setFont(QFont("Arial",15))
        self.yanlış.setGeometry(400,2,80,40)



        self.türkçe = QtWidgets.QLabel(self)
        self.türkçe.setText("T.Dili Edebiyatı / 24")
        self.türkçe.setGeometry(60,20,200,80)
        self.türkçe.setFont(QFont("Arial",17))

        self.türkçe_dogru = QtWidgets.QLineEdit(self)
        self.türkçe_dogru.setMaxLength(2)
        self.türkçe_dogru.setGeometry(270,50,80,30)
        self.türkçe_dogru.setFont(QFont("Arial",17))
        self.türkçe_yanlış = QtWidgets.QLineEdit(self)
        self.türkçe_yanlış.setMaxLength(2)
        self.türkçe_yanlış.setGeometry(390,50,80,30)
        self.türkçe_yanlış.setFont(QFont("Arial",17))
        

        

        self.sosyal = QtWidgets.QLabel(self)
        self.sosyal.setText("Tarih-1 / 10")
        self.sosyal.setGeometry(60,90,200,80)
        self.sosyal.setFont(QFont("Arial",17))

        self.sosyal_dogru = QtWidgets.QLineEdit(self)
        self.sosyal_dogru.setMaxLength(2)
        self.sosyal_dogru.setGeometry(270,115,80,30)
        self.sosyal_dogru.setFont(QFont("Arial",17))
        self.sosyal_yanlış = QtWidgets.QLineEdit(self)
        self.sosyal_yanlış.setMaxLength(2)
        self.sosyal_yanlış.setGeometry(390,115,80,30)
        self.sosyal_yanlış.setFont(QFont("Arial",17))


        self.matematik = QtWidgets.QLabel(self)
        self.matematik.setText("Coğrafya-1 / 6")
        self.matematik.setGeometry(60,170,200,80)
        self.matematik.setFont(QFont("Arial",17))

        self.mat_dogru = QtWidgets.QLineEdit(self)
        self.mat_dogru.setMaxLength(2)
        self.mat_dogru.setGeometry(270,195,80,30)
        self.mat_dogru.setFont(QFont("Arial",17))
        self.mat_yanlış = QtWidgets.QLineEdit(self)
        self.mat_yanlış.setMaxLength(2)
        self.mat_yanlış.setGeometry(390,195,80,30)
        self.mat_yanlış.setFont(QFont("Arial",17))



        self.fen = QtWidgets.QLabel(self)
        self.fen.setText("Tarih-2 / 11")
        self.fen.setGeometry(60,250,200,80)
        self.fen.setFont(QFont("Arial",17))

        self.fen_dogru = QtWidgets.QLineEdit(self)
        self.fen_dogru.setMaxLength(2)
        self.fen_dogru.setGeometry(270,275,80,30)
        self.fen_dogru.setFont(QFont("Arial",17))
        self.fen_yanlış = QtWidgets.QLineEdit(self)
        self.fen_yanlış.setMaxLength(2)
        self.fen_yanlış.setGeometry(390,275,80,30)
        self.fen_yanlış.setFont(QFont("Arial",17))


        self.net = QtWidgets.QLabel(self)
        self.net.setText("Toplam Net")
        self.net.setGeometry(60,330,200,80)
        self.net.setFont(QFont("Arial",17))

        self.net_hesap = QtWidgets.QLineEdit(self)
        self.net_hesap.setGeometry(200,350,80,40)
        self.net_hesap.setFont(QFont("Arial",17))

        self.puan = QtWidgets.QLabel(self)
        self.puan.setText("Puan")
        self.puan.setGeometry(300,330,200,80)
        self.puan.setFont(QFont("Arial",17))

        self.puan_hesap = QtWidgets.QLineEdit(self)
        self.puan_hesap.setMaxLength(5)
        self.puan_hesap.setGeometry(370,350,80,40)
        self.puan_hesap.setFont(QFont("Arial",17))




        self.hesapla = QtWidgets.QPushButton(self)
        self.hesapla.setText("Hesapla")
        self.hesapla.setGeometry(310,600,100,50)
        self.hesapla.setFont(QFont("Arial",17))
        self.hesapla.clicked.connect(self.hesaplaa)

        self.temizle = QtWidgets.QPushButton(self)
        self.temizle.setText("Temizle")
        self.temizle.setGeometry(90,600,100,50)
        self.temizle.setFont(QFont("Arial",17))
        self.temizle.clicked.connect(self.clear)

        self.setGeometry(400,25,500,700)
        self.setWindowTitle("AYT Net Hesaplama")
        self.setStyleSheet("background:beige")
        self.show()
    
    def hesaplaa(self):

        türkçe = int(self.türkçe_dogru.text())
        türkçee = int(self.türkçe_yanlış.text())
        sosyal = int(self.sosyal_dogru.text())
        sosyall = int(self.sosyal_yanlış.text())
        mat = int(self.mat_dogru.text())
        matt = int(self.mat_yanlış.text())
        fen = int(self.fen_dogru.text())
        fenn = int(self.fen_yanlış.text())

        net = (türkçe-(türkçee/4)+(sosyal-(sosyall/4)+(mat-(matt/4)+(fen-(fenn/4)))))
        puan = net*4.5

        self.net_hesap.setText(str(net))
        self.puan_hesap.setText(str(puan))
        
        self.show()




    
    def clear(self):
        self.türkçe_dogru.clear()
        self.türkçe_yanlış.clear()
        self.mat_dogru.clear()
        self.mat_yanlış.clear()
        self.fen_dogru.clear()
        self.fen_yanlış.clear()
        self.sosyal_dogru.clear()
        self.sosyal_yanlış.clear()
    








class Pencere4(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.dgs()
        
        


    def dgs(self):


        self.dogru = QtWidgets.QLabel(self)
        self.dogru.setText("Doğru")
        self.dogru.setFont(QFont("Arial",15))
        self.dogru.setGeometry(280,2,80,40)

        self.yanlış = QtWidgets.QLabel(self)
        self.yanlış.setText("Yanlış")
        self.yanlış.setFont(QFont("Arial",15))
        self.yanlış.setGeometry(400,2,80,40)



        self.sayısal = QtWidgets.QLabel(self)
        self.sayısal.setText("Sayısal / 60")
        self.sayısal.setGeometry(60,20,200,80)
        self.sayısal.setFont(QFont("Arial",17))

        self.sayısal_dogru = QtWidgets.QLineEdit(self)
        self.sayısal_dogru.setMaxLength(2)
        self.sayısal_dogru.setGeometry(270,50,80,30)
        self.sayısal_dogru.setFont(QFont("Arial",17))
        self.sayısal_yanlış = QtWidgets.QLineEdit(self)
        self.sayısal_yanlış.setMaxLength(2)
        self.sayısal_yanlış.setGeometry(390,50,80,30)
        self.sayısal_yanlış.setFont(QFont("Arial",17))

        

        self.sözel = QtWidgets.QLabel(self)
        self.sözel.setText("Sözel / 60")
        self.sözel.setGeometry(60,90,200,80)
        self.sözel.setFont(QFont("Arial",17))

        self.sözel_dogru = QtWidgets.QLineEdit(self)
        self.sözel_dogru.setMaxLength(2)
        self.sözel_dogru.setGeometry(270,115,80,30)
        self.sözel_dogru.setFont(QFont("Arial",17))
        self.sözel_yanlış = QtWidgets.QLineEdit(self)
        self.sözel_yanlış.setMaxLength(2)
        self.sözel_yanlış.setGeometry(390,115,80,30)
        self.sözel_yanlış.setFont(QFont("Arial",17))




        self.net = QtWidgets.QLabel(self)
        self.net.setText("Toplam Net")
        self.net.setGeometry(60,330,200,80)
        self.net.setFont(QFont("Arial",17))

        self.net_hesap = QtWidgets.QLineEdit(self)
        self.net_hesap.setGeometry(200,350,80,40)
        self.net_hesap.setFont(QFont("Arial",17))

        self.puan = QtWidgets.QLabel(self)
        self.puan.setText("Puan")
        self.puan.setGeometry(300,330,200,80)
        self.puan.setFont(QFont("Arial",17))

        self.puan_hesap = QtWidgets.QLineEdit(self)
        self.puan_hesap.setMaxLength(5)
        self.puan_hesap.setGeometry(370,350,80,40)
        self.puan_hesap.setFont(QFont("Arial",17))




        self.hesapla = QtWidgets.QPushButton(self)
        self.hesapla.setText("Hesapla")
        self.hesapla.setGeometry(310,420,100,50)
        self.hesapla.setFont(QFont("Arial",17))
        self.hesapla.clicked.connect(self.hesaplaa)

        self.temizle = QtWidgets.QPushButton(self)
        self.temizle.setText("Temizle")
        self.temizle.setGeometry(90,420,100,50)
        self.temizle.setFont(QFont("Arial",17))
        self.temizle.clicked.connect(self.clear)

        self.setGeometry(400,100,500,500)
        self.setWindowTitle("DGS Net Hesaplama")
        self.setStyleSheet("background:beige")
        self.show()
    
    def hesaplaa(self):

        sayısal = int(self.sayısal_dogru.text())
        sayısall = int(self.sayısal_yanlış.text())
        sözel = int(self.sözel_dogru.text())
        sözell = int(self.sözel_yanlış.text())
        

        net = (sayısal-(sayısall/4)+(sözel-(sözell/4)))
        puan = net*2.87

        self.net_hesap.setText(str(net))
        self.puan_hesap.setText(str(puan))
        
        self.show()




    
    def clear(self):
        self.sayısal_dogru.clear()
        self.sayısal_yanlış.clear()
        self.sözel_dogru.clear()
        self.sözel_yanlış.clear()
        
        

  


app = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
sys.exit(app.exec_())