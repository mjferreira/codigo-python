import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QHBoxLayout, QMessageBox, QTableWidget
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtGui import QAction
import banco

class MinhaJanela(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.resize(600,500)
        self.setGeometry(10, 500, 800, 600)
        self.setWindowTitle("Ong Amazonia Vivia")
        self.setStyleSheet("background-color: lightblue; color: black;")

        # Criando um widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Criar a barra de menuInserir
        menu_bar = self.menuBar()
        menu_bar.setStyleSheet("background-color: lightgray; color: black;")
        # Criar um menu "Arquivo"
        menu_form = menu_bar.addMenu("Formulario")
        # Criar ações para o menu
        acao_inserir = QAction("Inserir", self)
        acao_inserir.triggered.connect(self.inserir)
        acao_consultar = QAction("Consultar", self)
        acao_consultar.triggered.connect(self.consultar)
        acao_sair = QAction("Sair", self)

        # Adicionar ações ao menu
        menu_form.addAction(acao_inserir)
        menu_form.addAction(acao_consultar)
        menu_form.addSeparator()  # Adiciona uma linha separadora
        menu_form.addAction(acao_sair)
        # Conectar a ação "Sair" para fechar a janela
        acao_sair.triggered.connect(self.close)


        menu_sobre = menu_bar.addMenu("Sobre")
        # Criar ações para o menu
        acao_mostrar = QAction("Versão", self)
        acao_mostrar.triggered.connect(self.mostrar_mensagem_sobre)
        # Adicionar ações ao menu
        menu_sobre.addAction(acao_mostrar)

        # Criando um label e botão para a mensagem de versão (inicialmente ocultos)
        self.label_versao = QLabel("Versão 1.0.0", self.central_widget)
        self.label_versao.move(150, 250)
        self.label_versao.setVisible(False)
        self.label_versao.setStyleSheet('background-color:green;color:white')


        self.botao_ok = QPushButton("OK", self.central_widget)
        self.botao_ok.move(200, 280)
        self.botao_ok.setFixedSize(80, 30)
        self.botao_ok.setVisible(False)
        self.botao_ok.setStyleSheet('background-color:blue;color:white')
        self.botao_ok.clicked.connect(self.ocultar_mensagem_versao)


        self.botao1 = QPushButton("Gravar", self.central_widget)
        self.botao1.setFixedSize(80, 30)
        self.botao1.move(400,400)
        self.botao1.setVisible(False)
        self.botao1.setStyleSheet('background-color:red;color:white')
        self.botao1.clicked.connect(self.gravarDados)

        self.botao2 = QPushButton("Voltar", self.central_widget)
        self.botao2.setFixedSize(80,30)
        self.botao2.move(10,400)
        self.botao2.setVisible(False)
        self.botao2.setStyleSheet('background-color:green;color:white')
        self.botao2.clicked.connect(self.ocultar)

        self.lnome = QLabel("Nome:", self.central_widget)
        self.lnome.move(10,10)
        self.lnome.setStyleSheet('color: black; font-size:18px;')
        self.lnome.setVisible(False)

        self.lenome = QLineEdit("", self.central_widget)
        self.lenome.setGeometry(80,10,400,25)
        self.lenome.setStyleSheet('background: white; color: black; font-size:18px;')
        self.lenome.setVisible(False)

        self.lrg = QLabel("RG:", self.central_widget)
        self.lrg.move(10,40)
        self.lrg.setStyleSheet('color: black; font-size:16px;')
        self.lrg.setVisible(False)

        self.lerg = QLineEdit("", self.central_widget)
        self.lerg.setGeometry(80,40,120,25)
        self.lerg.setStyleSheet('background: white; color: black; font-size:18px;')
        self.lerg.setVisible(False)

        self.lcpf = QLabel("CPF:",self.central_widget)
        self.lcpf.move(10,70)
        self.lcpf.setStyleSheet('color: black; font-size:16px')
        self.lecpf = QLineEdit("",self.central_widget)
        self.lecpf.setStyleSheet('background: white; color: black; font-size:18px;')
        self.lecpf.setGeometry(80,70,150,25)

        # self.linhacpf = QLabel("________Dados Pessoais_____________________",self.central_widget)
        # self.linhacpf.move(10,90)
        # self.linhacpf.setStyleSheet('color: black; font-size:16px')

        self.lmae = QLabel("Mãe:",self.central_widget)
        self.lmae.move(10,120)
        self.lmae.setStyleSheet('color: black; font-size:18px;')
        self.lemae = QLineEdit("",self.central_widget)
        self.lemae.setStyleSheet('background: white; color: black; font-size:18px;')
        self.lemae.setGeometry(80,120,400,25)

        self.lcpfmae = QLabel("CPF:",self.central_widget)
        self.lcpfmae.move(10,150)
        self.lcpfmae.setStyleSheet('color: black; font-size:18px')
        self.lecpfmae = QLineEdit("",self.central_widget)
        self.lecpfmae.setStyleSheet('background: white; color: black; font-size:18px;')
        self.lecpfmae.setGeometry(80,150,150,25)

        self.lpai = QLabel("Pai:",self.central_widget)
        self.lpai.move(10,180)
        self.lpai.setStyleSheet('color: black; font-size:18px;')
        self.lepai = QLineEdit("",self.central_widget)
        self.lepai.setStyleSheet('background: white; color: black; font-size:18px;')
        self.lepai.setGeometry(80,180,400,25)

        self.lcpfpai = QLabel("CPF:",self.central_widget)
        self.lcpfpai.move(10,210)
        self.lcpfpai.setStyleSheet('color: black; font-size:18px;')
        self.lecpfpai = QLineEdit("",self.central_widget)
        self.lecpfpai.setStyleSheet('background: white; color: black; font-size:18px;')
        self.lecpfpai.setGeometry(80,210,150,25)

        self.lcpf.setVisible(False)
        self.lmae.setVisible(False)
        self.lcpfmae.setVisible(False)
        self.lpai.setVisible(False)
        self.lcpfpai.setVisible(False)
        self.lecpf.setVisible(False)
        self.lemae.setVisible(False)
        self.lecpfmae.setVisible(False)
        self.lepai.setVisible(False)
        self.lecpfpai.setVisible(False)
        # self.linhacpf.setVisible(False)

        # Layout principal
        layout = QVBoxLayout(self.central_widget)
        self.tabela = QTableWidget()
        layout.addWidget(self.tabela)
        self.tabela.setStyleSheet("background-color: lightblue; color: black")
        self.tabela.setVisible(False)
        # Criar Botão para Alternar Visibilidade
        self.botao_toggle = QPushButton("Voltar")
        self.botao_toggle.clicked.connect(self.ocultar)
        self.botao_toggle.setStyleSheet("background-color: green; color: white;")
        self.botao_toggle.setFixedSize(80, 30)
        layout.addWidget(self.botao_toggle)
        self.botao_toggle.setVisible(False)
        # self.tabela.setStyleSheet("QTableWidget { background-color: lightblue; color: black; }")  # Define a cor do texto para azul


    def carregar_dados(self):

        vsql = "SELECT N_ID, T_NOME, T_CPF FROM tb_pessoa order by T_NOME"
        dados = banco.consultar(vsql)

        self.tabela.setRowCount(len(dados))
        self.tabela.setColumnCount(5)  # ID, Nome, Idade, Ações
        self.tabela.setColumnWidth(0, 10)   # Coluna 0 com 50 pixels
        self.tabela.setColumnWidth(1, 400)  # Coluna 1 com 150 pixels
        self.tabela.setColumnWidth(2, 100)  # Coluna 2 com 100 pixels
        self.tabela.setHorizontalHeaderLabels(["ID", "Nome", "CPF", "Ações", ""])

        for linha_idx, linha in enumerate(dados):
            for col_idx, valor in enumerate(linha):
                self.tabela.setItem(linha_idx, col_idx, QTableWidgetItem(str(valor)))

            # Botão Editar
            botao_editar = QPushButton("Editar")
            botao_editar.setStyleSheet("background-color: green; color white;")
            botao_editar.clicked.connect(lambda _, row=linha[0]: self.editar_registro(row))
            self.tabela.setCellWidget(linha_idx, 3, botao_editar)

            # Botão Excluir
            botao_excluir = QPushButton("Excluir")
            botao_excluir.setStyleSheet("background-color: red; color white;")
            botao_excluir.clicked.connect(lambda _, row=linha[0]: self.excluir_registro(row))
            self.tabela.setCellWidget(linha_idx, 4, botao_excluir)



    def editar_registro(self, id_registro):
        """Simula edição de um registro"""
        QMessageBox.information(self, "Editar", f"Editar formulário de {id_registro}")

    def excluir_registro(self, id_registro):
        """Exclui um registro do banco de dados"""
        resposta = QMessageBox.question(self, "Excluir", f"Tem certeza que deseja excluir o {id_registro}?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if resposta == QMessageBox.StandardButton.Yes:
            vsql = "DELETE FROM tb_pessoa WHERE N_ID = "+ str(id_registro)
            banco.atualizar(vsql)
            self.carregar_dados()  # Recarregar os dados após a exclusão

    def inserir(self):
        self.ocultar()
        self.botao1.setVisible(True)
        self.botao2.setVisible(True)
        self.lnome.setVisible(True)
        self.lenome.setVisible(True)
        self.lrg.setVisible(True)
        self.lerg.setVisible(True)
        self.lcpf.setVisible(True)
        self.lmae.setVisible(True)
        self.lcpfmae.setVisible(True)
        self.lpai.setVisible(True)
        self.lcpfpai.setVisible(True)
        self.lecpf.setVisible(True)
        self.lemae.setVisible(True)
        self.lecpfmae.setVisible(True)
        self.lepai.setVisible(True)
        self.lecpfpai.setVisible(True)
        # self.linhacpf.setVisible(True)

    def consultar(self):
        self.carregar_dados()
        self.tabela.setVisible(True)
        self.botao_toggle.setVisible(True)

    def ocultar(self):
        self.botao_toggle.setVisible(False)
        self.tabela.setVisible(False)
        self.botao1.setVisible(False)
        self.botao2.setVisible(False)
        self.lnome.setVisible(False)
        self.lenome.setVisible(False)
        self.lrg.setVisible(False)
        self.lerg.setVisible(False)
        self.lcpf.setVisible(False)
        self.lmae.setVisible(False)
        self.lcpfmae.setVisible(False)
        self.lpai.setVisible(False)
        self.lcpfpai.setVisible(False)
        self.lecpf.setVisible(False)
        self.lemae.setVisible(False)
        self.lecpfmae.setVisible(False)
        self.lepai.setVisible(False)
        self.lecpfpai.setVisible(False)

    def gravarDados(self):
        vnome=self.lenome.text()
        vrg=self.lerg.text()
        vcpf=self.lecpf.text()
        vmae=self.lemae.text()
        vcpfmae=self.lecpfmae.text()
        vpai=self.lepai.text()
        vcpfpai=self.lecpfpai.text()
        #vsql= "INSERT INTO tb_pessoa (T_NOME, [N_RG], [N_CPF], T_MAE, [N_CPF-MAE], T_PAI, [N_CPF-PAI]) VALUES('"+vnome+"',(vrg),(vcpf),'"+vmae+"',(vcpfmae),'"+vpai+"',(vcpfpai)"
        vsql="INSERT INTO tb_pessoa (T_NOME, T_RG, T_CPF, T_MAE, T_CPFMAE, T_PAI, T_CPFPAI) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(vnome, vrg, vcpf, vmae, vcpfmae, vpai, vcpfpai)
        print(vsql)
        banco.atualizar(vsql)
        print("Aqui.....")
        self.lenome.clear()
        self.lerg.clear()
        self.lecpf.clear()
        self.lemae.clear()
        self.lecpfmae.clear()
        self.lepai.clear()
        self.lecpfpai.clear()

    def mostrar(self):
        self.label_versao.setVisible(True)
        self.botao_ok.setVisible(True)

    def ocultar_mensagem_versao(self):
        self.label_versao.setVisible(False)
        self.botao_ok.setVisible(False)

    def mostrar_mensagem_sobre(self):
        mensagem = QMessageBox(self)
        mensagem.setWindowTitle("Sobre")
        mensagem.setStyleSheet('background: lightgray; color: black; font-size:18px;')
        mensagem.setText("""
Controle de Formulários
ONG Amazonia Viva
Versão: 1.0.0
Autor: Marcelo Ferreira
            """)
        mensagem.setStandardButtons(QMessageBox.StandardButton.Ok)
        mensagem.exec()

app = QApplication(sys.argv)
janela = MinhaJanela()
janela.show()
app.exec()
