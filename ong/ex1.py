import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

def funcao1():
    label.setText("Botao 1 pressionado")
    label.adjustSize()

def funcao2():
    label.setText("Botao 2 pressionado")
    label.adjustSize()

def funcao3():
    valor_lido = le.text()
    label.setText(valor_lido)
    label.adjustSize()

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(800,600)
janela.setWindowTitle("Ong Amazonia Vivia")

botao1 = QPushButton("Botao 1",janela)
botao1.setGeometry(100,100,150,80)
botao1.setStyleSheet('background-color:red;color:white')
botao1.clicked.connect(funcao1)

botao2 = QPushButton("Botao 2",janela)
botao2.setGeometry(100,300,150,80)
botao2.setStyleSheet('background-color:green;color:white')
botao2.clicked.connect(funcao2)

botao3 = QPushButton("Botao 3",janela)
botao3.setGeometry(100,500,150,80)
botao3.setStyleSheet('background-color:blue;color:white')
botao3.clicked.connect(funcao3)


le = QLineEdit("",janela)
le.setGeometry(500,300,150,40)


label = QLabel("Text teste",janela)
label.move(400,100)
label.setStyleSheet('font-size:30px')
janela.show()

app.exec()
