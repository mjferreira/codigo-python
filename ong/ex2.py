import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QComboBox

def ler_combobox():
    valor = combo.currentText()
    label2.setText(valor)

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(500,500)
janela.setWindowTitle("2 - Ong Amazonia Vivia")

botao = QPushButton("Mostrar OPCAO ", janela)
botao.setGeometry(300,90,130,80)
botao.clicked.connect(ler_combobox)

label = QLabel(janela)
label.move(10,200)
label.setText("Opção Selecionada: ")

label2 = QLabel(janela)
label2.move(150,200)
label2.setText("                          ")

combo = QComboBox(janela)
combo.addItem("Selecione uma liguaguem de programacao")
combo.addItem("Java")
combo.addItem("Python")
combo.addItem("JavaScript")
combo.addItem("Rust")
combo.addItem("C++")
combo.move(20,20)

janela.show()
app.exec()
