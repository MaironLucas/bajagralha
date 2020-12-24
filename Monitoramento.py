from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from random import randint
from datetime import datetime as data
velocidade = 0
CVT = 28
oleo = 30
rpm = 0
diesel= 100
mes = data.today().month
ano = data.today().year
dia = data.today().day

def funcao_principal():
    bajapp.pushButton.clicked.connect(disparaTimer)
    bajapp.pushButton_2.clicked.connect(paraTimer)

def disparaTimer():
    timer.timeout.connect(funcao_de_random)
    timer.start(1000)

def paraTimer():
    timer.stop()

def funcao_de_random():
    velocimetro()
    tempCVT()
    tempOleo()
    rotacoes()
    combustivel()
    armazenar()


def velocimetro():
    global velocidade
    cont = randint(1,3)
    r=randint(1,10)
    if velocidade >=72:
        if cont ==1 or cont==2:
            r = (r/10) - 1
            velocidade +=r
        else:
            r = r/10
            velocidade +=r
    else:
        r = randint(1, 5)
        velocidade += r
    bajapp.lcdNumber.display(velocidade)


def tempCVT():
    global CVT
    if CVT > 75:
        r = randint(1, 10)
        cont = randint(1, 3)
        if cont==1 or cont==2:
            r = (r/10) -1
            CVT += r
        else:
            r= r/10
            CVT += r
    else:
        r = (randint(1,10)/10)
        CVT +=r
    bajapp.lcdNumber_2.display(CVT)


def tempOleo():
    global oleo
    if oleo > 85:
        r = randint(1, 10)
        cont = randint(1, 4)
        if cont == 1 or cont == 2 or cont==3:
            r = (r / 10) - 1
            oleo += r
        else:
            r = r / 10
            oleo += r
    else:
        r = (randint(1, 10) / 10)
        oleo += r
    bajapp.lcdNumber_3.display(oleo)


def rotacoes():
    global rpm
    if rpm<7000:
        r = randint(500, 1500)
        rpm +=r
    else:
        r=randint(500, 1000)
        cont = randint(1,4)
        if cont==1 or cont==2 or cont==3:
            rpm -= r
        else:
            rpm += r
    bajapp.lcdNumber_4.display(rpm)


def combustivel():
    global diesel
    cont = randint(1,15)
    if cont == 5:
        r = (randint(1,10)/10)
        diesel -= r
    bajapp.lcdNumber_5.display(diesel)


def armazenar():
    hora = data.today().hour
    min = data.today().minute
    seg = data.today().second
    temp = int(velocidade)
    arq= open("../Logs/{}-{}-{}.txt".format(dia, mes, ano), "a")
    arq.write(f"{hora}:{min}:{seg:2}-> VELOCIDADE: {temp:2}     CVT: {CVT:.1f}     OLEO: {oleo:.1f}     RPM: {rpm:4}     DIESEL: {diesel:.1f}\n")
    arq.close()

app= QtWidgets.QApplication([])
bajapp = uic.loadUi("interface.ui")
bajapp.setWindowIcon(QIcon("icon.png"))
timer = QTimer(bajapp)
funcao_principal()
bajapp.show()
app.exec()