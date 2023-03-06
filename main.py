from PyQt5 import QtCore, QtGui, QtWidgets
from flask import Flask, render_template, jsonify, request, redirect
import cx_Oracle
from datetime import datetime, date, timedelta


app = Flask(__name__)
with open(app.root_path + '\config.cfg', 'r') as f:
    app.config['ORACLE_URI'] = f.readline()

try:
    dsn_tsn = cx_Oracle.makedsn('bd-dc.cs.tuiasi.ro', 1539, 'orcl')
    con = cx_Oracle.connect("bd074", "bd074", dsn=dsn_tsn)
except cx_Oracle.DatabaseError as er:
    print(er)

class Ui_errorTrain(object):
    def setupUi(self, errorTrain):
        errorTrain.setObjectName("errorTrain")
        errorTrain.resize(428, 104)
        self.label = QtWidgets.QLabel(errorTrain)
        self.label.setGeometry(QtCore.QRect(10, 20, 151, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("kisspng-fitness-centre-exercise-physical-fitness-personal-gym-fitness-5b5d24a07ff459.6187679415328308805241.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(errorTrain)
        self.label_2.setGeometry(QtCore.QRect(170, 40, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(errorTrain)
        QtCore.QMetaObject.connectSlotsByName(errorTrain)

    def retranslateUi(self, errorTrain):
        _translate = QtCore.QCoreApplication.translate
        errorTrain.setWindowTitle(_translate("errorTrain", "Dialog"))
        self.label_2.setText(_translate("errorTrain", "Antrenor ocupat!"))

class Ui_ErrAntrenor(object):
    def setupUi(self, ErrAntrenor):
        ErrAntrenor.setObjectName("ErrAntrenor")
        ErrAntrenor.resize(492, 129)
        font = QtGui.QFont()
        font.setPointSize(14)
        ErrAntrenor.setFont(font)
        self.label = QtWidgets.QLabel(ErrAntrenor)
        self.label.setGeometry(QtCore.QRect(370, 0, 111, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Bugs-Bunny-No-Transparent-File.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(ErrAntrenor)
        self.label_3.setGeometry(QtCore.QRect(100, 30, 261, 61))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(ErrAntrenor)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 81, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("pngegg(1).png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(ErrAntrenor)
        QtCore.QMetaObject.connectSlotsByName(ErrAntrenor)

    def retranslateUi(self, ErrAntrenor):
        _translate = QtCore.QCoreApplication.translate
        ErrAntrenor.setWindowTitle(_translate("ErrAntrenor", "Dialog"))
        self.label_3.setText(_translate("ErrAntrenor", "Program antrenor incalcat!"))

class Ui_constrErr(object):
    def setupUi(self, constrErr):
        constrErr.setObjectName("constrErr")
        constrErr.resize(521, 141)
        self.label = QtWidgets.QLabel(constrErr)
        self.label.setGeometry(QtCore.QRect(20, 30, 111, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("database-error-icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(constrErr)
        self.label_2.setGeometry(QtCore.QRect(130, 30, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(constrErr)
        self.label_3.setGeometry(QtCore.QRect(410, 0, 211, 161))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("er.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(constrErr)
        QtCore.QMetaObject.connectSlotsByName(constrErr)

    def retranslateUi(self, constrErr):
        _translate = QtCore.QCoreApplication.translate
        constrErr.setWindowTitle(_translate("constrErr", "Dialog"))
        self.label_2.setText(_translate("constrErr", "Constrangeri incalcate!"))

class Ui_noFound(object):
    def setupUi(self, noFound):
        noFound.setObjectName("noFound")
        noFound.resize(513, 106)
        self.label = QtWidgets.QLabel(noFound)
        self.label.setGeometry(QtCore.QRect(0, 10, 371, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pngegg.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(noFound)
        self.label_2.setGeometry(QtCore.QRect(380, 0, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(noFound)
        self.label_3.setGeometry(QtCore.QRect(420, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(noFound)
        QtCore.QMetaObject.connectSlotsByName(noFound)

    def retranslateUi(self, noFound):
        _translate = QtCore.QCoreApplication.translate
        noFound.setWindowTitle(_translate("noFound", "Dialog"))
        self.label_2.setText(_translate("noFound", "Informatii"))
        self.label_3.setText(_translate("noFound", "invalide!"))

class Ui_expiratAbonament(object):
    def setupUi(self, expiratAbonament):
        expiratAbonament.setObjectName("expiratAbonament")
        expiratAbonament.resize(420, 118)
        self.label = QtWidgets.QLabel(expiratAbonament)
        self.label.setGeometry(QtCore.QRect(10, 20, 131, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("date-expired-icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(expiratAbonament)
        self.label_2.setGeometry(QtCore.QRect(180, 20, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(expiratAbonament)
        self.label_3.setGeometry(QtCore.QRect(230, 60, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(expiratAbonament)
        QtCore.QMetaObject.connectSlotsByName(expiratAbonament)

    def retranslateUi(self, expiratAbonament):
        _translate = QtCore.QCoreApplication.translate
        expiratAbonament.setWindowTitle(_translate("expiratAbonament", "Dialog"))
        self.label_2.setText(_translate("expiratAbonament", "ABONAMENT"))
        self.label_3.setText(_translate("expiratAbonament", "EXPIRAT!"))


def pushClienti(v):

    cur = con.cursor()
    cur.execute('select * from client')
    row = cur.fetchall()
    v.textView.insertPlainText('ID\tNUME\tSTART\t\t    END\t\t   TIPC  TIPA   TELEFON\n\n')
    for i in row:
            #print(i)
        for j in i:
            v.textView.insertPlainText(str(j)+'    ')
        v.textView.insertPlainText('\n\n')

    cur.close()

def pushAntrenori(v):

    cur = con.cursor()
    cur.execute('select id_antrenor, name_antrenor ,to_char(start_program, \'hh24:mi\'),to_char(end_program, \'hh24:mi\' )from antrenor')
    row = cur.fetchall()
    v.textView.insertPlainText('ID    NUME\t     START     END\t\n\n')
    for i in row:
            #print(i)
        for j in i:
            v.textView.insertPlainText(str(j)+'    ')
        v.textView.insertPlainText('\n\n')

    cur.close()

def pushProgramari(v):
    cur = con.cursor()
    cur.execute('select c.name_client, a.name_antrenor, p.programare_start from client c, antrenor a, programari '
                    'p where c.id_client = p.id_client and  a.id_antrenor = p.id_antrenor')
    row = cur.fetchall()
    v.textView.insertPlainText('NUME\t   ANTRENOR\t   START\n\n')
    for i in row:
        for j in i:
            v.textView.insertPlainText(str(j)+'  ')
        v.textView.insertPlainText('\n\n')
    cur.close()


def pushCost(v):
    cur = con.cursor()
    cur.execute('select c.name_client ,a.cost_abonament - r.reducere*a.cost_abonament, a.cost_abonament, r.reducere'
                ' from client c, tip_antrenament a, reduceri r, tip_client cc '
                ' where c.id_tclient = cc.id_tclient and '
                'cc.id_reducere = r.id_reducere and c.id_type = a.id_type ')
    row = cur.fetchall()
    v.textView.insertPlainText('NUME\t   PRET  PRET-I REDUCERE\n\n')
    for i in row:
        for j in i:
            v.textView.insertPlainText(str(j)+'     ')
        v.textView.insertPlainText('\n\n')
    cur.close()




def editareProgramare(name, oldData, newData):
    cur = con.cursor()
    start = datetime.strptime(oldData, '%m/%d/%Y %H:%M:%S')
    new = datetime.strptime(newData,'%m/%d/%Y %H:%M:%S' )
    stop = new+ timedelta(hours=1)

    str2 = 'select id_client from client where name_client = :TAG'
    cur.execute(str2, TAG=name)
    id_client = cur.fetchall()

    str1='select id_programare from programari where programare_start = :TOLD and id_client = :TNAME'
    cur.execute(str1, TOLD = start, TNAME=id_client[0][0])
    id_prog = cur.fetchall()
    str2='update programari set programare_start = :TNEW, programare_end = :TSTOP where id_programare = :TID '
    cur.execute(str2, TNEW=new, TSTOP=stop ,TID=int(id_prog[0][0]))
    cur.execute('commit')
    cur.close()

class Ui_MainWindow(object):

    def openInreg(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_inregistrareWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openProg(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_programareWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openView(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_viewWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inregistrareButt = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openInreg() )
        self.inregistrareButt.setGeometry(QtCore.QRect(530, 130, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.inregistrareButt.setFont(font)
        self.inregistrareButt.setObjectName("inregistrareButt")
        self.programareButt = QtWidgets.QPushButton(self.centralwidget,  clicked = lambda: self.openProg())
        self.programareButt.setGeometry(QtCore.QRect(530, 200, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.programareButt.setFont(font)
        self.programareButt.setObjectName("programareButt")
        self.viewButt = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openView())
        self.viewButt.setGeometry(QtCore.QRect(530, 270, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.viewButt.setFont(font)
        self.viewButt.setObjectName("viewButt")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 30, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 70, 421, 391))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Gym-Silhoutte-PNG-Photo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inregistrareButt.setText(_translate("MainWindow", "Inregistrare"))
        self.programareButt.setText(_translate("MainWindow", "Programare"))
        self.viewButt.setText(_translate("MainWindow", "Vizualizare"))
        self.label.setText(_translate("MainWindow", "Bine ati venit!"))

class Ui_inregistrareWindow(object):

    def pushOK(self):
        name = self.numeI.text()
        telefon = self.tipClient.text()
        tipClient =self.telefon.text()
        tipAnt = self.tipAnt.text()
        #pushInregistrare(nume, telefon,tipAnt , tipClient)
        try:
            cur = con.cursor()
            str1 = 'select id_type from tip_antrenament where name_antrenament = :TAG'
            cur.execute(str1, TAG=tipAnt.capitalize())
            id_tipA = cur.fetchone()

            str2 = 'select id_tclient from tip_client where name_tclient= :TAG1'

            cur.execute(str2, TAG1=tipClient.capitalize())
            id_tipC = cur.fetchone()

            today = date.today()
            nextDate = today + timedelta(days=30)
            #print(nextDate)
            str3 = 'insert into client(name_client, telefon, id_tclient, id_type, start_time, end_time)  values( :Tname, :Ttelefon ,  :Tid_tipC, :Tid_tipA, :Tdate, :Tend)'
            cur.execute(str3, Tname=name, Ttelefon=telefon, Tid_tipC=int(id_tipC[0]), Tid_tipA=int(id_tipA[0]), Tdate=today,
                        Tend=nextDate)
            cur.execute('commit')
            cur.close()
        except:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_constrErr()
            self.ui.setupUi(self.window)
            self.window.show()

    def plata(self):
        name = self.numeI.text()
        try:
            cur = con.cursor()
            today = date.today()
            nextDate = today + timedelta(days=30)
            str='update client set start_time = :TNEW, end_time = :TSTOP where name_client = :TID  '
            cur.execute(str, TNEW= today, TSTOP=nextDate, TID = name)
            cur.execute('commit')
            cur.close()
        except:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_constrErr()
            self.ui.setupUi(self.window)
            self.window.show()

    def anulareAb(self):
        name = self.numeI.text()
        try:
            cur = con.cursor()

            str = 'delete from client  where name_client = :TID  '
            cur.execute(str,  TID=name)
            cur.execute('commit')
            cur.close()
        except:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_constrErr()
            self.ui.setupUi(self.window)
            self.window.show()
    def setupUi(self, inregistrareWindow):
        inregistrareWindow.setObjectName("inregistrareWindow")
        inregistrareWindow.resize(524, 356)
        self.centralwidget = QtWidgets.QWidget(inregistrareWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 180, 171, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pngwing.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 241, 51))

        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.numeI = QtWidgets.QLineEdit(self.centralwidget)
        self.numeI.setGeometry(QtCore.QRect(280, 100, 151, 21))
        self.numeI.setObjectName("numeI")
        self.tipClient = QtWidgets.QLineEdit(self.centralwidget)
        self.tipClient.setGeometry(QtCore.QRect(280, 140, 151, 21))

        self.tipClient.setObjectName("tipClient")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 100, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 140, 61, 16))

        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.telefon = QtWidgets.QLineEdit(self.centralwidget)
        self.telefon.setGeometry(QtCore.QRect(280, 180, 151, 21))
        self.telefon.setObjectName("telefon")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(210, 180, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.inregistrareOk = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pushOK())
        self.inregistrareOk.setGeometry(QtCore.QRect(420, 280, 75, 23))
        self.inregistrareOk.setObjectName("inregistrareOk")
        self.plataAbonament = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.plata())
        self.plataAbonament.setGeometry(QtCore.QRect(300, 280, 111, 21))
        self.plataAbonament.setObjectName("plataAbonament")
        self.anulareAbonament = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.anulareAb())
        self.anulareAbonament.setGeometry(QtCore.QRect(300, 250, 111, 21))
        self.anulareAbonament.setObjectName("anulareAbonament")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(180, 210, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.tipAnt = QtWidgets.QLineEdit(self.centralwidget)
        self.tipAnt.setGeometry(QtCore.QRect(280, 210, 151, 21))
        self.tipAnt.setObjectName("tipAnt")
        inregistrareWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(inregistrareWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 524, 21))
        self.menubar.setObjectName("menubar")
        inregistrareWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(inregistrareWindow)
        self.statusbar.setObjectName("statusbar")
        inregistrareWindow.setStatusBar(self.statusbar)

        self.retranslateUi(inregistrareWindow)
        QtCore.QMetaObject.connectSlotsByName(inregistrareWindow)

    def retranslateUi(self, inregistrareWindow):
        _translate = QtCore.QCoreApplication.translate
        inregistrareWindow.setWindowTitle(_translate("inregistrareWindow", "MainWindow"))
        self.label_2.setText(_translate("inregistrareWindow", "Inregistrare"))
        self.label_3.setText(_translate("inregistrareWindow", "Name:"))
        self.label_4.setText(_translate("inregistrareWindow", "Telefon:"))
        self.label_5.setText(_translate("inregistrareWindow", "Tip Client:"))
        self.inregistrareOk.setText(_translate("inregistrareWindow", "OK"))
        self.label_6.setText(_translate("inregistrareWindow", "Tip Antrenor:"))
        self.plataAbonament.setText(_translate("inregistrareWindow", "Plata Abonament"))
        self.anulareAbonament.setText(_translate("inregistrareWindow", "Anulare Abonament"))


class Ui_programareWindow(object):
    def pushOK(self):
        nume = self.nameP.text()
        antrenor = self.antrenorP.text()
        data = self.dataProg.text()
        #programareOK(nume, antrenor, data)
        cur = con.cursor()
        str1 = 'select id_client from client where name_client = :TAG'
        cur.execute(str1, TAG=nume)
        id_client = cur.fetchall()
        str1 = 'select end_time from client where name_client = :TAG'
        cur.execute(str1, TAG=nume)
        sfAbonament = cur.fetchall()
        str2 = 'select id_antrenor from antrenor where name_antrenor = :TAG1'
        cur.execute(str2, TAG1=antrenor)
        id_antrenor = cur.fetchall()
        if (id_client  and id_antrenor ):
            start = datetime.strptime(data, '%m/%d/%Y %H:%M:%S')
            #sfAb = datetime.strptime(str(sfAbonament[0][0]), '%Y/%m/%d %H:%M:%S')
           # print(type(sfAbonament[0][0]))
            if(sfAbonament[0][0] > start):
                strVerificare = 'select to_char(start_program, \'hh24:mi\') from antrenor where name_antrenor = :TNAMEA'
                cur.execute(strVerificare, TNAMEA=antrenor)
                startA = cur.fetchall()
                strVerificare = 'select to_char(end_program, \'hh24:mi\') from antrenor where name_antrenor = :TNAMEA'
                cur.execute(strVerificare, TNAMEA=antrenor)
                endA = cur.fetchall()
            # print(startA[0][0]+'  '+endA[0][0])

                startP = datetime.strptime(startA[0][0], '%H:%M')
                endP = datetime.strptime(endA[0][0], '%H:%M')

                stop = start + timedelta(hours=1)
            # print(id_antrenor[0][0]+' '+id_client[0][0])
                if (start.hour >= startP.hour and start.hour < endP.hour):
                    str3 = 'insert into programari(id_client, id_antrenor, programare_start, programare_end) values(:TIDC, :TIDA, :TPS, :TPE)'
                    try:
                        cur.execute(str3, TIDC=int(id_client[0][0]), TIDA=int(id_antrenor[0][0]), TPS=start, TPE=stop)
                        #print('Success')
                        cur.execute('commit')
                        cur.close()
                    except:
                        self.window = QtWidgets.QMainWindow()
                        self.ui = Ui_errorTrain()
                        self.ui.setupUi(self.window)
                        self.window.show()

                else:
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Ui_ErrAntrenor()
                    self.ui.setupUi(self.window)
                    self.window.show()
            else:
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_expiratAbonament()
                self.ui.setupUi(self.window)
                self.window.show()

        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_noFound()
            self.ui.setupUi(self.window)
            self.window.show()



    def pushEdit(self):
        name = self.nameP.text()
        oldData = self.dataVeche.text()
        newData = self.dataProg.text()
        antrenor = self.antrenorP.text()
        #editareProgramare(nume, data, oldData)
        cur = con.cursor()

        str2 = 'select id_client from client where name_client = :TAG'
        cur.execute(str2, TAG=name)
        id_client = cur.fetchall()

        str2 = 'select id_antrenor from antrenor where name_antrenor = :TAG1'
        cur.execute(str2, TAG1=antrenor)
        id_antrenor = cur.fetchall()
        if (id_client and id_antrenor):
            str1 = 'select end_time from client where name_client = :TAG'
            cur.execute(str1, TAG=name)
            sfAbonament = cur.fetchall()
            new = datetime.strptime(newData, '%m/%d/%Y %H:%M:%S')
            # sfAb = datetime.strptime(str(sfAbonament[0][0]), '%Y/%m/%d %H:%M:%S')
            # print(type(sfAbonament[0][0]))
            if (sfAbonament[0][0] > new):
                start = datetime.strptime(oldData, '%m/%d/%Y %H:%M:%S')

                stop = new + timedelta(hours=1)

                strVerificare = 'select to_char(start_program, \'hh24:mi\') from antrenor where name_antrenor = :TNAMEA'
                cur.execute(strVerificare, TNAMEA=antrenor)
                startA = cur.fetchall()
                strVerificare = 'select to_char(end_program, \'hh24:mi\') from antrenor where name_antrenor = :TNAMEA'
                cur.execute(strVerificare, TNAMEA=antrenor)
                endA = cur.fetchall()
            # print(startA[0][0]+'  '+endA[0][0])

                startP = datetime.strptime(startA[0][0], '%H:%M')
                endP = datetime.strptime(endA[0][0], '%H:%M')
                if (new.hour >= startP.hour and new.hour < endP.hour):


                    str1 = 'select id_programare from programari where programare_start = :TOLD and id_client = :TNAME'
                    cur.execute(str1, TOLD=start, TNAME=id_client[0][0])
                    id_prog = cur.fetchall()
                    try:
                        str2 = 'update programari set programare_start = :TNEW, programare_end = :TSTOP where id_programare = :TID '
                        cur.execute(str2, TNEW=new, TSTOP=stop, TID=int(id_prog[0][0]))
                        cur.execute('commit')
                        cur.close()
                    except:
                        self.window = QtWidgets.QMainWindow()
                        self.ui = Ui_errorTrain()
                        self.ui.setupUi(self.window)
                        self.window.show()

                else:
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Ui_ErrAntrenor()
                    self.ui.setupUi(self.window)
                    self.window.show()
            else:
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_expiratAbonament()
                self.ui.setupUi(self.window)
                self.window.show()
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_noFound()
            self.ui.setupUi(self.window)
            self.window.show()

    def setupUi(self, programareWindow):
        programareWindow.setObjectName("programareWindow")
        programareWindow.resize(630, 327)
        self.centralwidget = QtWidgets.QWidget(programareWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.nameP = QtWidgets.QLineEdit(self.centralwidget)
        self.nameP.setGeometry(QtCore.QRect(160, 130, 131, 21))
        self.nameP.setObjectName("nameP")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 130, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.antrenorP = QtWidgets.QLineEdit(self.centralwidget)
        self.antrenorP.setGeometry(QtCore.QRect(160, 160, 131, 21))
        self.antrenorP.setObjectName("antrenorP")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 160, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 190, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.dataProg = QtWidgets.QLineEdit(self.centralwidget)
        self.dataProg.setGeometry(QtCore.QRect(160, 190, 131, 21))
        self.dataProg.setObjectName("dataProg")
        self.dataVeche = QtWidgets.QLineEdit(self.centralwidget)
        self.dataVeche.setGeometry(QtCore.QRect(160, 220, 131, 21))
        self.dataVeche.setObjectName("dataVeche")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(320, 0, 312, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.okProg = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pushOK())
        self.okProg.setGeometry(QtCore.QRect(510, 250, 91, 31))
        self.okProg.setObjectName("okProg")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 220, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.editProg = QtWidgets.QPushButton(self.centralwidget, clicked = lambda :self.pushEdit())
        self.editProg.setGeometry(QtCore.QRect(510, 210, 91, 31))
        self.editProg.setObjectName("editProg")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 10, 91, 91))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("pngfind.com-calendar-icon-png-537550.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        programareWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(programareWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 21))
        self.menubar.setObjectName("menubar")
        programareWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(programareWindow)
        self.statusbar.setObjectName("statusbar")
        programareWindow.setStatusBar(self.statusbar)

        self.retranslateUi(programareWindow)
        QtCore.QMetaObject.connectSlotsByName(programareWindow)

    def retranslateUi(self, programareWindow):
        _translate = QtCore.QCoreApplication.translate
        programareWindow.setWindowTitle(_translate("programareWindow", "MainWindow"))
        self.label.setText(_translate("programareWindow", "Programare"))
        self.label_2.setText(_translate("programareWindow", "Nume:"))
        self.label_3.setText(_translate("programareWindow", "Antrenor:"))
        self.label_4.setText(_translate("programareWindow", "Data:"))
        self.okProg.setText(_translate("programareWindow", "OK"))
        self.label_5.setText(_translate("programareWindow", "Data veche:"))
        self.editProg.setText(_translate("programareWindow", "Editare"))

class Ui_viewWindow(object):


    def setupUi(self, viewWindow):
        viewWindow.setObjectName("viewWindow")
        viewWindow.resize(877, 588)
        font = QtGui.QFont()
        font.setPointSize(10)
        viewWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(viewWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 73, 47, 20))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.clientVi = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: pushClienti(self))
        self.clientVi.setGeometry(QtCore.QRect(150, 20, 111, 31))
        self.clientVi.setObjectName("clientVi")
        self.programariVi = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:  pushProgramari(self))
        self.programariVi.setGeometry(QtCore.QRect(280, 20, 111, 31))
        self.programariVi.setObjectName("programariVi")
        self.costVi = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: pushCost(self))
        self.costVi.setGeometry(QtCore.QRect(410, 20, 111, 31))
        self.costVi.setObjectName("costVi")
        self.textView = QtWidgets.QTextBrowser(self.centralwidget)
        self.textView.setGeometry(QtCore.QRect(10, 60, 861, 501))
        self.textView.setObjectName("textView")
        self.antrenori = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: pushAntrenori(self))
        self.antrenori.setGeometry(QtCore.QRect(540, 20, 111, 31))
        self.antrenori.setObjectName("antrenori")

        viewWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(viewWindow)
        self.statusbar.setObjectName("statusbar")
        viewWindow.setStatusBar(self.statusbar)

        self.retranslateUi(viewWindow)
        QtCore.QMetaObject.connectSlotsByName(viewWindow)

    def retranslateUi(self, viewWindow):
        _translate = QtCore.QCoreApplication.translate
        viewWindow.setWindowTitle(_translate("viewWindow", "MainWindow"))
        self.label_2.setText(_translate("viewWindow", "View"))
        self.clientVi.setText(_translate("viewWindow", "Clienti"))
        self.programariVi.setText(_translate("viewWindow", "Programari"))
        self.costVi.setText(_translate("viewWindow", "Cost"))
        self.antrenori.setText(_translate("viewWindow", "Antrenori"))


if __name__ == "__main__":
    import sys
    ap = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(ap.exec_())

