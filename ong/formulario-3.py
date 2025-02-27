import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMainWindow
from PyQt6.QtGui import QAction
import banco

def gravarDados():
    vnome=lenome.text()
    vrg=lerg.text()
    vcpf=lecpf.text()
    vmae=lemae.text()
    vcpfmae=lecpfmae.text()
    vpai=lepai.text()
    vcpfpai=lecpfpai.text()
    #vsql= "INSERT INTO tb_pessoa (T_NOME, [N_RG], [N_CPF], T_MAE, [N_CPF-MAE], T_PAI, [N_CPF-PAI]) VALUES('"+vnome+"',(vrg),(vcpf),'"+vmae+"',(vcpfmae),'"+vpai+"',(vcpfpai)"
    vsql="INSERT INTO tb_pessoa (T_NOME, T_RG, T_CPF, T_MAE, T_CPFMAE, T_PAI, T_CPFPAI) VALUES ('%s', %s, %s, '%s', %s, '%s', %s)" %(vnome, vrg, vcpf, vmae, vcpfmae, vpai, vcpfpai)
    banco.atualizar(vsql)
    lenome.clear()
    lerg.clear()
    lecpf.clear()
    lemae.clear()
    lecpfmae.clear()
    lepai.clear()
    lecpfpai.clear()


def funcao2():
    label.setText("Botao 2 pressionado")
    label.adjustSize()

def funcao3():
    valor_lido = le.text()
    label.setText(valor_lido)
    label.adjustSize()

class MinhaJanela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600,500)
        self.setWindowTitle("Ong Amazonia Vivia")
        self.setStyleSheet("background-color: lightblue;")
        # Criar a barra de menuInserir
        menu_bar = self.menuBar()
        menu_bar.setStyleSheet("background-color: lightgray; color: black;")
        # Criar um menu "Arquivo"
        menu_arquivo = menu_bar.addMenu("Menu")
        # Criar ações para o menu
        acao_inserir = QAction("Inserir", self)
        acao_consultar = QAction("Consultar", self)
        acao_modificar = QAction("Modificar", self)
        acao_deletar = QAction("Deletar", self)
        acao_sair = QAction("Sair", self)

        # Adicionar ações ao menu
        menu_arquivo.addAction(acao_inserir)
        menu_arquivo.addAction(acao_consultar)
        menu_arquivo.addAction(acao_modificar)
        menu_arquivo.addAction(acao_deletar)
        menu_arquivo.addSeparator()  # Adiciona uma linha separadora
        menu_arquivo.addAction(acao_sair)
        # Conectar a ação "Sair" para fechar a janela
        acao_sair.triggered.connect(self.close)


app = QApplication(sys.argv)
janela = MinhaJanela()

botao1 = QPushButton("Gravar",janela)
botao1.setGeometry(450,400,100,40)
botao1.setStyleSheet('background-color:red;color:white')
botao1.clicked.connect(gravarDados)

botao2 = QPushButton("Voltar",janela)
botao2.setGeometry(250,400,100,40)
botao2.setStyleSheet('background-color:green;color:white')
botao2.clicked.connect(funcao2)

# botao3 = QPushButton("Botao 3",janela)
# botao3.setGeometry(400,700,100,40)
# botao3.setStyleSheet('background-color:blue;color:white')
# botao3.clicked.connect(funcao3)

lnome = QLabel("Nome:",janela)
lnome.move(10,100)
lnome.setStyleSheet('color: red; font-size:18px;')

lenome = QLineEdit("",janela)
lenome.setGeometry(155,100,400,20)

lrg = QLabel("RG:",janela)
lrg.move(10,130)
lrg.setStyleSheet('font-size:16px')
lerg = QLineEdit("",janela)
lerg.setGeometry(155,130,120,20)

lcpf = QLabel("CPF:",janela)
lcpf.move(100,160)
lcpf.setStyleSheet('font-size:16px')
lecpf = QLineEdit("",janela)
lecpf.setGeometry(155,160,150,20)

lmae = QLabel("Mãe:",janela)
lmae.move(100,200)
lmae.setStyleSheet('font-size:16px')
lemae = QLineEdit("",janela)
lemae.setGeometry(180,200,400,20)

lcpfmae = QLabel("CPF Mãe:",janela)
lcpfmae.move(100,230)
lcpfmae.setStyleSheet('font-size:16px')
lecpfmae = QLineEdit("",janela)
lecpfmae.setGeometry(180,230,150,20)

lpai = QLabel("Pai:",janela)
lpai.move(100,270)
lpai.setStyleSheet('font-size:16px')
lepai = QLineEdit("",janela)
lepai.setGeometry(180,270,400,20)

lcpfpai = QLabel("CPF Pai:",janela)
lcpfpai.move(100,300)
lcpfpai.setStyleSheet('font-size:16px')
lecpfpai = QLineEdit("",janela)
lecpfpai.setGeometry(180,300,150,20)

janela.show()

app.exec()
