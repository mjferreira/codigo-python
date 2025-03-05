import sys, re
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QHBoxLayout, QMessageBox, QTableWidget
from PyQt6.QtWidgets import QTableWidgetItem, QComboBox, QSizePolicy
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import QSize
import banco

class MinhaJanela(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.resize(600,500)
        self.setGeometry(500, 200, 850, 800)
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
        self.botao1 = QPushButton("Gravar", self.central_widget)
        self.botao1.setFixedSize(80, 30)
        self.botao1.move(750,700)
        self.botao1.setStyleSheet('background-color:red;color:white')
        self.botao1.clicked.connect(self.inserir_registro)

        self.botao2 = QPushButton("Voltar", self.central_widget)
        self.botao2.setFixedSize(80,30)
        self.botao2.move(600,700)
        self.botao2.setStyleSheet('background-color:green;color:white')
        self.botao2.clicked.connect(self.ocultar_itens)

        self.botao3 = QPushButton("Atualizar", self.central_widget)
        self.botao3.setFixedSize(80, 30)
        self.botao3.move(750,700)
        self.botao3.setStyleSheet('background-color:red;color:white')
        self.botao3.clicked.connect(self.atualizar_dados)

        self.botao4 = QPushButton("Voltar Consulta", self.central_widget)
        self.botao4.setFixedSize(120,30)
        self.botao4.move(600,700)
        self.botao4.setStyleSheet('background-color:green;color:white')
        self.botao4.clicked.connect(self.consultar)

        linha=10
        self.linhaiden = QLabel("_________________________________ IDENTIFICAÇÃO __________________________________",self.central_widget)
        self.linhaiden.move(80,linha)
        self.linhaiden.setStyleSheet('color: blue; font-size:14px')
        self.linhaiden.adjustSize()
        linha=linha+20

        self.lnome = QLabel("Nome:", self.central_widget)
        self.lnome.move(10,linha)
        self.lnome.setStyleSheet('color: black; font-size:18px;')
        self.lenome = QLineEdit("", self.central_widget)
        self.lenome.setGeometry(80,linha,400,25)
        self.lenome.setStyleSheet('background: white; color: black; font-size:18px;')

        self.lcpf = QLabel("CPF:",self.central_widget)
        self.lcpf.move(500,linha)
        self.lcpf.setStyleSheet('color: red; font-size:16px')
        self.lecpf = QLineEdit("",self.central_widget)
        self.lecpf.setStyleSheet('background: white; color: black; font-size:18px;')
        self.lecpf.setGeometry(570,linha,140,25)
        self.lecpf.setInputMask("999.999.999-99")  # Apenas números e "-" fixo

        linha=linha+30
        self.lrg = QLabel("RG:", self.central_widget)
        self.lrg.move(10,linha)
        self.lrg.setStyleSheet('color: black; font-size:16px;')
        self.lerg = QLineEdit("", self.central_widget)
        self.lerg.setGeometry(80,linha,140,25)
        self.lerg.setStyleSheet('background: white; color: black; font-size:18px;')
        self.lerg.setInputMask("99999999999")

        self.lnis = QLabel("NIS:",self.central_widget)
        self.lnis.move(500,linha)
        self.lnis.setStyleSheet('color: red; font-size:16px')
        self.lenis = QLineEdit("",self.central_widget)
        self.lenis.setStyleSheet('background: white; color: black; font-size:18px;')
        self.lenis.setGeometry(570,linha,140,25)
        self.lenis.setInputMask("999.999.999-99")  # Apenas números e "-" fixo

        linha=linha+30
        self.lfone = QLabel("Fone:", self.central_widget)
        self.lfone.move(10,linha)
        self.lfone.setStyleSheet('color: black; font-size:16px;')
        self.lefone = QLineEdit("", self.central_widget)
        #                           col, linha, larg, altura
        self.lefone.setGeometry(80,linha,160,25)
        self.lefone.setStyleSheet('background: white; color: black; font-size:18px;')
        self.lefone.setInputMask("99(99)99999-9999")

        self.lcep = QLabel("CEP:", self.central_widget)
        self.lcep.move(540,linha)
        self.lcep.setStyleSheet('color: black; font-size:16px;')
        self.lecep = QLineEdit("", self.central_widget)
        self.lecep.setGeometry(610,linha,100,25)
        self.lecep.setStyleSheet('background: white; color: black; font-size:18px;')
        self.lecep.setInputMask("99999-999")

        linha=linha+30
    # Rótulo para a zona
        self.l_end = QLabel("ENDEREÇO", self.central_widget)
        self.l_end.move(10,linha)
        self.l_end.setStyleSheet('color: red; font-size:16px;')

        self.l_zona = QLabel("Zona:", self.central_widget)
        self.l_zona.move(120,linha)
        self.l_zona.setStyleSheet('color: red; font-size:16px;')

        # ComboBox para zonas
        self.combo_zona = QComboBox(self.central_widget)
        # self.combo_zona.move(300,100)
        #                           col, linha, larg, altura
        self.combo_zona.setGeometry(180,linha,160,25)
        self.combo_zona.currentIndexChanged.connect(self.atualizar_bairros)

        # Rótulo para o bairro
        self.l_bairro = QLabel("Bairro:", self.central_widget)
        self.l_bairro.move(400,linha)
        self.l_bairro.setStyleSheet('color: red; font-size:16px')
        # ComboBox para bairros
        self.combo_bairro = QComboBox(self.central_widget)
        self.combo_bairro.setGeometry(480,linha,230,25)

        # Carregar dados do banco
        self.carregar_zonas()

        linha=linha+30
        self.lmae = QLabel("Mãe:",self.central_widget)
        self.lmae.move(10,linha)
        self.lmae.setStyleSheet('color: black; font-size:16px;')
        self.lemae = QLineEdit("",self.central_widget)
        self.lemae.setStyleSheet('background: white; color: black; font-size:18px;')
        self.lemae.setGeometry(80,linha,400,25)

        self.lcpfmae = QLabel("CPF:",self.central_widget)
        self.lcpfmae.move(500,linha)
        self.lcpfmae.setStyleSheet('color: black; font-size:16px')
        self.lecpfmae = QLineEdit("",self.central_widget)
        self.lecpfmae.setStyleSheet('background: white; color: black; font-size:18px;')
        self.lecpfmae.setGeometry(570,linha,140,25)
        self.lecpfmae.setInputMask("999.999.999-99")  # Apenas números e "-" fixo

        linha=linha+30
        self.lpai = QLabel("Pai:",self.central_widget)
        self.lpai.move(10,linha)
        self.lpai.setStyleSheet('color: black; font-size:16px;')
        self.lepai = QLineEdit("",self.central_widget)
        self.lepai.setStyleSheet('background: white; color: black; font-size:18px;')
        self.lepai.setGeometry(80,linha,400,25)

        self.lcpfpai = QLabel("CPF:",self.central_widget)
        self.lcpfpai.move(500,linha)
        self.lcpfpai.setStyleSheet('color: black; font-size:16px;')
        self.lecpfpai = QLineEdit("",self.central_widget)
        self.lecpfpai.setStyleSheet('background: white; color: black; font-size:18px;')
        self.lecpfpai.setGeometry(570,linha,140,25)
        self.lecpfpai.setInputMask("999.999.999-99")  # Apenas números e "-" fixo

        linha=linha+25
        self.linhaescolaridade = QLabel("_________________________________ ESCOLARIDADE __________________________________",self.central_widget)
        self.linhaescolaridade.move(80,linha)
        self.linhaescolaridade.setStyleSheet('color: blue; font-size:14px')
        self.linhaescolaridade.adjustSize()

        linha=linha+30
        self.lgrau = QLabel("Grau de Ensino:", self.central_widget)
        self.lgrau.move(10,linha)
        self.lgrau.setStyleSheet('color: black; font-size:16px')
        self.lgrau.adjustSize()
        # ComboBox para Grau de Escolaridade
        self.combo_grau = QComboBox(self.central_widget)
        self.combo_grau.setGeometry(180,linha,230,25)
        self.combo_grau.addItems(["Analfabeto", "Fundamental", "Médio", "Superior"])

        linha=linha+30
        self.lescola = QLabel("Em caso de estudande       Escola:", self.central_widget)
        self.lescola.move(10,linha)
        self.lescola.setStyleSheet('color: black; font-size:18px;')
        self.lescola.adjustSize()
        self.leescola = QLineEdit("", self.central_widget)
        self.leescola.setGeometry(310,linha,400,25)
        self.leescola.setStyleSheet('background: white; color: black; font-size:18px;')

        linha=linha+30
        self.lescola_ano = QLabel("Série/Ano:",self.central_widget)
        self.lescola_ano.move(215,linha)
        self.lescola_ano.setStyleSheet('color: black; font-size:16px')
        self.combo_escola_ano = QComboBox(self.central_widget)
        self.combo_escola_ano.setGeometry(310,linha,200,25)
        self.combo_escola_ano.addItems(["","1º Ano Fund.", "2º Ano Fund.", "3º Ano Fund.", "4º Ano Fund.", "5º Ano Fund.","6º Ano Fund.","7º Ano Fund.","8º Ano Fund.","9º Ano Fund.","1º Ano Médio.","2º Ano Médio","3º Ano Médio"])

        linha=linha+25
        self.linhaerenda = QLabel("_____________________________________ RENDA ______________________________________",self.central_widget)
        self.linhaerenda.move(80,linha)
        self.linhaerenda.setStyleSheet('color: blue; font-size:14px')
        self.linhaerenda.adjustSize()

        linha=linha+30
        self.ltrabalha = QLabel("Trabalha:",self.central_widget)
        self.ltrabalha.move(10,linha)
        self.ltrabalha.setStyleSheet('color: black; font-size:16px')
        self.combo_trabalha = QComboBox(self.central_widget)
        self.combo_trabalha.setGeometry(160,linha,60,25)
        self.combo_trabalha.addItems(["SIM", "NAO"])

        self.lrenda = QLabel("Renda Familiar: R$",self.central_widget)
        self.lrenda.move(300,linha)
        self.lrenda.setStyleSheet('color: black; font-size:16px')
        self.lrenda.adjustSize()
        self.lerenda = QLineEdit("", self.central_widget)
        self.lerenda.setGeometry(450,linha,90,25)
        self.lerenda.setStyleSheet('background: white; color: black; font-size:18px;')
        self.lerenda.setInputMask("99.999,00")  # Apenas números e "-" fixo

        linha=linha+30
        self.lrecbenefinicio = QLabel("Recebe Benefício:",self.central_widget)
        self.lrecbenefinicio.move(10,linha)
        self.lrecbenefinicio.setStyleSheet('color: black; font-size:16px')
        self.lrecbenefinicio.adjustSize()
        self.combo_recbeneficio = QComboBox(self.central_widget)
        self.combo_recbeneficio.setGeometry(160,linha,60,25)
        self.combo_recbeneficio.addItems(["SIM", "NAO"])
        self.combo_recbeneficio.currentIndexChanged.connect(self.verificar_beneficio)

        self.lnomebenefinicio = QLabel("Se sim, qual:",self.central_widget)
        self.lnomebenefinicio.move(300,linha)
        self.lnomebenefinicio.setStyleSheet('color: black; font-size:16px')
        self.combo_nomebeneficio = QComboBox(self.central_widget)
        self.combo_nomebeneficio.setGeometry(450,linha,200,25)
        self.combo_nomebeneficio.addItems(["BPC","Bolsa Família", "Aponsentadoria", "Outros"])
        self.combo_nomebeneficio.currentIndexChanged.connect(self.verificar_nomedobeneficio)

        linha=linha+30
        self.loutrobeneficio = QLabel("OUTROS:",self.central_widget)
        self.loutrobeneficio.move(10,linha)
        self.loutrobeneficio.setStyleSheet('color: red; font-size:16px')
        self.leoutrobeneficio = QLineEdit("", self.central_widget)
        self.leoutrobeneficio.setGeometry(100,linha,200,25)
        self.leoutrobeneficio.setStyleSheet('background: white; color: black; font-size:18px;')

        linha=linha+25
        self.linhainfpes = QLabel("______________________________INFORMAÇÕES PESSOAIS________________________________",self.central_widget)
        self.linhainfpes.move(80,linha)
        self.linhainfpes.setStyleSheet('color: blue; font-size:14px')
        self.linhainfpes.adjustSize()

        # Layout principale
        layout = QVBoxLayout(self.central_widget)
        self.tabela = QTableWidget()
        layout.addWidget(self.tabela)
        self.tabela.setStyleSheet("background-color: lightblue; color: black")
        # Criar Botão para Alternar Visibilidade
        self.botao_toggle = QPushButton("Voltar")
        self.botao_toggle.clicked.connect(self.ocultar_itens)
        self.botao_toggle.setStyleSheet("background-color: green; color: white;")
        self.botao_toggle.setFixedSize(80, 30)
        layout.addWidget(self.botao_toggle)
        # self.tabela.setStyleSheet("QTableWidget { background-color: lightblue; color: black; }")  # Define a cor do texto para azul
        self.ocultar_itens()

    def carregar_tabela_consulta(self):
        vsql = "SELECT T_NOME, T_CPF, T_RG FROM tb_pessoa order by T_NOME"
        dados = banco.consultar(vsql)
        self.tabela.setRowCount(len(dados))
        self.tabela.setColumnCount(5)  # ID, Nome, Idade, Ações
        self.tabela.setColumnWidth(0, 510)   # Coluna 0 com 50 pixels
        self.tabela.setColumnWidth(1, 100)  # Coluna 1 com 150 pixels
        self.tabela.setColumnWidth(2, 100)  # Coluna 2 com 100 pixels
        self.tabela.setColumnWidth(3, 16)  # Coluna 2 com 100 pixels
        self.tabela.setColumnWidth(4, 16)  # Coluna 2 com 100 pixels
        self.tabela.setHorizontalHeaderLabels(["Nome", "CPF", "RG", "", ""])
        for linha_idx, linha in enumerate(dados):
            for col_idx, valor in enumerate(linha):
                self.tabela.setItem(linha_idx, col_idx, QTableWidgetItem(str(valor)))

            # Botão Editar
            botao_editar = QPushButton("")
            icone_editar = QIcon("edicao.png")  # Substitua com o caminho do seu ícone
            botao_editar.setIcon(icone_editar)
            botao_editar.setIconSize(QSize(32, 32))  # Tamanho do ícone
            # botao_editar.setStyleSheet("background-color: green; color black;")
            botao_editar.clicked.connect(lambda _, row=linha[1]: self.editar_registro(row))
            self.tabela.setCellWidget(linha_idx, 3, botao_editar)
            # Botão Excluir
            botao_excluir = QPushButton("")
            icone_excluir = QIcon("trash-can-red.jpg")  # Substitua com o caminho do seu ícone
            botao_excluir.setIcon(icone_excluir)
            botao_excluir.setIconSize(QSize(32, 32))  # Tamanho do ícone
            #botao_excluir.setStyleSheet("background-color: red; color white;")
            botao_excluir.clicked.connect(lambda _, row=linha[1]: self.excluir_registro(row))
            self.tabela.setCellWidget(linha_idx, 4, botao_excluir)
    def editar_registro(self, cpf):
        # QMessageBox.information(self, "Editar", f"Editar formulário de {id_registro}")
        vsql = "SELECT * FROM tb_pessoa WHERE T_CPF = "+ str(cpf)
        resultado = banco.consultar(vsql)
        print("Resultado ...................")
        print(resultado)
        self.lenome.setText(resultado[0][0])
        self.lerg.setText(resultado[0][1])
        self.lecpf.setText(resultado[0][2])
        self.lemae.setText(resultado[0][3])
        self.lecpfmae.setText(resultado[0][4])
        self.lepai.setText(resultado[0][5])
        self.lecpfpai.setText(resultado[0][6])
        id_bairro=resultado[0][7]
        self.lenis.setText(resultado[0][8])
        self.lefone.setText(resultado[0][9])
        self.lecep.setText(resultado[0][10])
        self.combo_grau.setCurrentText(resultado[0][11])
        self.leescola.setText(resultado[0][12])
        self.combo_escola_ano.setCurrentText(resultado[0][13])
        self.combo_trabalha.setCurrentText(resultado[0][14])
        self.lerenda.setText(resultado[0][15])
        self.combo_recbeneficio.setCurrentText(resultado[0][16])
        nomebeneficio=resultado[0][17]
        print(nomebeneficio)
        if nomebeneficio is not None:
            print("Nao nulo")
            if nomebeneficio in ["BPC","Bolsa Família", "Aponsentadoria"]:
                self.combo_nomebeneficio.setCurrentText(nomebeneficio)
                self.combo_nomebeneficio.setVisible(True)
                self.lnomebenefinicio.setVisible(True)
                print("Na lista")
            else:
                self.combo_nomebeneficio.setCurrentText("Outros")
                self.leoutrobeneficio.setText(nomebeneficio)
                self.loutrobeneficio.setVisible(True)
                self.leoutrobeneficio.setVisible(True)
                print("outro")

        if id_bairro == None:
            self.combo_zona.setCurrentIndex(-1)
        else:
            vsql="SELECT T_BAIRRO, N_ZONA FROM tb_bairro WHERE N_ID = "+ str(id_bairro)
            resultado = banco.consultar(vsql)
            vbairro=[row[0] for row in resultado]
            vzona=[row[1] for row in resultado]
            vsql="SELECT T_ZONA FROM tb_zona WHERE N_ID = " + '"' +  str(vzona[0]) + '"'
            vzona=[row[0] for row in banco.consultar(vsql)]
            self.combo_zona.setCurrentText(vzona[0])
            self.combo_bairro.setCurrentText(vbairro[0])

        self.modificar()
    def excluir_registro(self, cpf):
        """Exclui um registro do banco de dados"""
        resposta = QMessageBox.question(self, "Excluir", f"Tem certeza que deseja excluir o {cpf}?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if resposta == QMessageBox.StandardButton.Yes:
            vsql = "DELETE FROM tb_pessoa WHERE T_CPF = "+ str(cpf)
            banco.atualizar(vsql)
            self.carregar_tabela_consulta()  # Recarregar os dados após a exclusão
    def inserir(self):
        self.ocultar_itens()
        self.limpar_dados()
        self.lecpf.setReadOnly(False)
        self.lecpf.setStyleSheet('background: white; color: black; font-size:18px;')
        self.mostrar_formulario()
    def modificar(self):
        self.ocultar_itens_consulta()
        self.mostrar_formulario()
        self.lecpf.setStyleSheet('background: lightgray; color: black; font-size:18px;')
        self.lecpf.setReadOnly(True)
        self.botao1.setVisible(False)
        self.botao2.setVisible(False)
        self.botao3.setVisible(True)
        self.botao4.setVisible(True)
    def mostrar_formulario(self):
        self.botao1.setVisible(True)
        self.botao2.setVisible(True)
        self.linhaiden.setVisible(True)
        self.lnome.setVisible(True)
        self.lenome.setVisible(True)
        self.lrg.setVisible(True)
        self.lerg.setVisible(True)
        self.lcpf.setVisible(True)
        self.lfone.setVisible(True)
        self.lcep.setVisible(True)
        self.lnis.setVisible(True)
        self.l_end.setVisible(True)
        self.l_zona.setVisible(True)
        self.combo_zona.setVisible(True)
        self.l_bairro.setVisible(True)
        self.combo_bairro.setVisible(True)
        self.lmae.setVisible(True)
        self.lcpfmae.setVisible(True)
        self.lpai.setVisible(True)
        self.lcpfpai.setVisible(True)
        self.lecpf.setVisible(True)
        self.lefone.setVisible(True)
        self.lecep.setVisible(True)
        self.lenis.setVisible(True)
        self.lemae.setVisible(True)
        self.lecpfmae.setVisible(True)
        self.lepai.setVisible(True)
        self.lecpfpai.setVisible(True)
        self.linhaescolaridade.setVisible(True)
        self.lgrau.setVisible(True)
        self.combo_grau.setVisible(True)
        self.lescola.setVisible(True)
        self.leescola.setVisible(True)
        self.lescola_ano.setVisible(True)
        self.combo_escola_ano.setVisible(True)
        self.linhaerenda.setVisible(True)
        self.lrecbenefinicio.setVisible(True)
        self.combo_recbeneficio.setVisible(True)
        self.linhainfpes.setVisible(True)
        self.lrenda.setVisible(True)
        self.lerenda.setVisible(True)
        self.ltrabalha.setVisible(True)
        self.combo_trabalha.setVisible(True)
    def consultar(self):
        self.carregar_tabela_consulta()
        self.tabela.setVisible(True)
        self.botao_toggle.setVisible(True)
    def ocultar_itens_consulta(self):
        self.botao_toggle.setVisible(False)
        self.tabela.setVisible(False)
    def ocultar_itens(self):
        self.botao_toggle.setVisible(False)
        self.linhaiden.setVisible(False)
        self.tabela.setVisible(False)
        self.botao1.setVisible(False)
        self.botao2.setVisible(False)
        self.botao3.setVisible(False)
        self.botao4.setVisible(False)
        self.lnome.setVisible(False)
        self.lenome.setVisible(False)
        self.lrg.setVisible(False)
        self.lerg.setVisible(False)
        self.lcpf.setVisible(False)
        self.lcep.setVisible(False)
        self.lfone.setVisible(False)
        self.lnis.setVisible(False)
        self.lcpf.setVisible(False)
        self.l_end.setVisible(False)
        self.l_zona.setVisible(False)
        self.combo_zona.setVisible(False)
        self.l_bairro.setVisible(False)
        self.combo_bairro.setVisible(False)
        self.lmae.setVisible(False)
        self.lcpfmae.setVisible(False)
        self.lpai.setVisible(False)
        self.lcpfpai.setVisible(False)
        self.lecpf.setVisible(False)
        self.lecep.setVisible(False)
        self.lefone.setVisible(False)
        self.lenis.setVisible(False)
        self.lemae.setVisible(False)
        self.lecpfmae.setVisible(False)
        self.lepai.setVisible(False)
        self.lecpfpai.setVisible(False)
        self.linhaescolaridade.setVisible(False)
        self.lgrau.setVisible(False)
        self.combo_grau.setVisible(False)
        self.lescola.setVisible(False)
        self.leescola.setVisible(False)
        self.lescola_ano.setVisible(False)
        self.combo_escola_ano.setVisible(False)
        self.linhaerenda.setVisible(False)
        self.lrecbenefinicio.setVisible(False)
        self.combo_recbeneficio.setVisible(False)
        self.linhainfpes.setVisible(False)
        self.lrenda.setVisible(False)
        self.lerenda.setVisible(False)
        self.ltrabalha.setVisible(False)
        self.combo_trabalha.setVisible(False)
        self.lnomebenefinicio.setVisible(False)
        self.combo_nomebeneficio.setVisible(False)
        self.loutrobeneficio.setVisible(False)
        self.leoutrobeneficio.setVisible(False)
    def carregar_dados(self):
                vnome=self.lenome.text()
                vrg=self.lerg.text()
                vcpf=self.lecpf.text().replace("-", "").replace(".", "")
                vmae=self.lemae.text()
                vcpfmae=self.lecpfmae.text().replace("-", "").replace(".", "")
                vpai=self.lepai.text()
                vcpfpai=self.lecpfpai.text().replace("-", "").replace(".", "")
                vbairro=self.combo_bairro.currentText()
                vnis=self.lenis.text().replace("-", "").replace(".", "")
                vfone=self.lefone.text().replace("(","").replace(")","").replace("-","")
                vcep=self.lecep.text().replace("-","")
                vgrau_ensino=self.combo_grau.currentText()
                vescola=self.leescola.text()
                vserieano=self.combo_escola_ano.currentText()
                vsql="SELECT N_ID FROM tb_bairro WHERE T_BAIRRO = "+ '"' + vbairro + '"'
                vbairro=[row[0] for row in banco.consultar(vsql)]
    def inserir_registro(self):
        vnome=self.lenome.text()
        vrg=self.lerg.text()
        vcpf=self.lecpf.text().replace("-", "").replace(".", "")
        vmae=self.lemae.text()
        vcpfmae=self.lecpfmae.text().replace("-", "").replace(".", "")
        vpai=self.lepai.text()
        vcpfpai=self.lecpfpai.text().replace("-", "").replace(".", "")
        vbairro=self.combo_bairro.currentText()
        vnis=self.lenis.text().replace("-", "").replace(".", "")
        vfone=self.lefone.text().replace("(","").replace(")","").replace("-","")
        vcep=self.lecep.text().replace("-","")
        vgrau_ensino=self.combo_grau.currentText()
        vescola=self.leescola.text()
        vserieano=self.combo_escola_ano.currentText()
        vtrabalha=self.combo_trabalha.currentText()
        vrenda=self.lerenda.text().replace(".", "").replace(",", "")
        vrecbeneficio=self.combo_recbeneficio.currentText()
        if self.combo_nomebeneficio.currentText() == "Outros":
            vnomebeneficio=self.leoutrobeneficio.text()
        else:
            vnomebeneficio=self.combo_nomebeneficio.currentText()
        vsql="SELECT N_ID FROM tb_bairro WHERE T_BAIRRO = "+ '"' + vbairro + '"'
        vbairro=[row[0] for row in banco.consultar(vsql)]
        vcpf=self.lecpf.text().replace("-", "").replace(".", "")
        if not self.cpf_valido(vcpf):
            QMessageBox.critical(self, "Erro Crítico","CPF INVÁLIDO !!!", QMessageBox.StandardButton.Ok)
        elif self.cpf_existe(vcpf):
            QMessageBox.critical(self, "Erro Crítico","CPF JÁ CADASTRADO !!!", QMessageBox.StandardButton.Ok)
        elif len(vbairro) == 0:
            QMessageBox.critical(self, "Erro Crítico","Selecione o endereço !!!", QMessageBox.StandardButton.Ok)
        elif not self.cpf_valido(vnis):
            QMessageBox.critical(self, "Erro Crítico","NIS INVÁLIDO !!!", QMessageBox.StandardButton.Ok)
        elif self.combo_nomebeneficio.currentText() == "Outros" and len(vnomebeneficio) == 0:
            QMessageBox.critical(self, "Erro Crítico","Nome de Benefício deve ser definido !!!", QMessageBox.StandardButton.Ok)
        else:
            vsql="INSERT INTO tb_pessoa (T_NOME, T_RG, T_CPF, T_MAE, T_CPFMAE, T_PAI, T_CPFPAI, N_BAIRRO, T_NIS, T_FONE, T_CEP, T_GRAU_ENSINO, T_ESCOLA, T_SERIE_ANO, T_TRABALHA, T_RENDA, T_RECBENEFICIO, T_NOMEBENEFICIO) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(vnome, vrg, vcpf, vmae, vcpfmae, vpai, vcpfpai, vbairro[0], vnis, vfone, vcep, vgrau_ensino, vescola, vserieano, vtrabalha, vrenda, vrecbeneficio, vnomebeneficio)
            print(vsql)
            banco.atualizar(vsql)
            self.limpar_dados()
    def limpar_dados(self):
        self.combo_zona.setCurrentIndex(-1)
        self.lenome.clear()
        self.lerg.clear()
        self.lecpf.clear()
        self.lemae.clear()
        self.lecpfmae.clear()
        self.lepai.clear()
        self.lecpfpai.clear()
        self.lenis.clear()
        self.lefone.clear()
        self.lefone.setText("55(92)")
        self.lecep.clear()
        self.combo_grau.setCurrentIndex(0)
        self.leescola.clear()
        self.combo_escola_ano.setCurrentIndex(0)
        self.lerenda.clear()
        self.leoutrobeneficio.clear()
        self.combo_trabalha.setCurrentIndex(-1)
        self.combo_recbeneficio.setCurrentIndex(-1)
        self.combo_nomebeneficio.setCurrentIndex(-1)
    def atualizar_dados(self):
        vnome=self.lenome.text()
        vrg=self.lerg.text()
        vcpf=self.lecpf.text().replace("-", "").replace(".", "")
        vmae=self.lemae.text()
        vcpfmae=self.lecpfmae.text().replace("-", "").replace(".", "")
        vpai=self.lepai.text()
        vcpfpai=self.lecpfpai.text().replace("-", "").replace(".", "")
        vbairro=self.combo_bairro.currentText()
        vnis=self.lenis.text().replace("-", "").replace(".", "")
        vfone=self.lefone.text().replace("(","").replace(")","").replace("-","")
        vcep=self.lecep.text().replace("-","")
        vgrau_ensino=self.combo_grau.currentText()
        vescola=self.leescola.text()
        vserieano=self.combo_escola_ano.currentText()
        vtrabalha=self.combo_trabalha.currentText()
        vrenda=self.lerenda.text().replace(".", "").replace(",", "")
        vrecbeneficio=self.combo_recbeneficio.currentText()
        if self.combo_nomebeneficio.currentText() == "Outros":
            vnomebeneficio=self.leoutrobeneficio.text()
        else:
            vnomebeneficio=self.combo_nomebeneficio.currentText()
        vsql="SELECT N_ID FROM tb_bairro WHERE T_BAIRRO = "+ '"' + vbairro + '"'
        vbairro=[row[0] for row in banco.consultar(vsql)]
        if not self.cpf_valido(vcpf):
            QMessageBox.critical(self, "Erro Crítico","CPF INVÁLIDO !!!", QMessageBox.StandardButton.Ok)
        elif len(vbairro) == 0:
            QMessageBox.critical(self, "Erro Crítico","Selecione o endereço !!!", QMessageBox.StandardButton.Ok)
        elif not self.cpf_valido(vnis):
            QMessageBox.critical(self, "Erro Crítico","NIS INVÁLIDO !!!", QMessageBox.StandardButton.Ok)
        elif self.combo_nomebeneficio.currentText() == "Outros" and len(vnomebeneficio) == 0:
            QMessageBox.critical(self, "Erro Crítico","Nome de Benefício deve ser definido !!!", QMessageBox.StandardButton.Ok)
        else:
            vsql= "UPDATE tb_pessoa SET T_NOME='"+vnome+"',T_RG='"+vrg+"',T_CPF='"+vcpf+"',T_MAE='"+vmae+"',T_CPFMAE='"+vcpfmae+"',T_PAI='"+vpai+"',T_CPFPAI='"+vcpfpai+"',N_BAIRRO="+str(vbairro[0])+",T_NIS='"+vnis+"',T_FONE='"+vfone+"',T_CEP='"+vcep+"',T_GRAU_ENSINO='"+vgrau_ensino+"',T_ESCOLA='"+vescola+"',T_SERIE_ANO='"+vserieano+"',T_TRABALHA='"+vtrabalha+"',T_RENDA='"+vrenda+"',T_RECBENEFICIO='"+vrecbeneficio+"',T_NOMEBENEFICIO='"+vnomebeneficio+"' WHERE T_CPF="+vcpf
            print(vsql)
            banco.atualizar(vsql)
            self.consultar()
    def cpf_valido(self, cpf: str) -> bool:
        """Valida um número de CPF (Cadastro de Pessoa Física) do Brasil."""

        # Remover caracteres não numéricos
        cpf = re.sub(r"\D", "", cpf)

        # Verificar se tem exatamente 11 dígitos
        if len(cpf) != 11:
            return False

        # Verificar se todos os dígitos são iguais (ex: "111.111.111-11")
        if cpf == cpf[0] * 11:
            return False

        # Função para calcular o dígito verificador
        #def calcular_digito(cpf_parcial, peso_inicial):
        #    soma = sum(int(digito) * peso for digito, peso in zip(cpf_parcial, range(peso_inicial, 1, -1)))
        #    resto = soma % 11
        #    return "0" if resto < 2 else str(11 - resto)

        # Validar o primeiro dígito verificador
        #primeiro_digito = calcular_digito(cpf[:9], 10)
        #if cpf[9] != primeiro_digito:
        #    return False

        # Validar o segundo dígito verificador
        #segundo_digito = calcular_digito(cpf[:10], 11)
        #if cpf[10] != segundo_digito:
        #    return False

        return True
    def mostrar_mensagem(self, texto):
        mensagem = QMessageBox.critical(self)
        mensagem.setWindowTitle("Erro")
        # mensagem.setStyleSheet('background: lightgray; color: black; font-size:18px;')
        mensagem.setText(texto)
        mensagem.setIcon(QMessageBox.Icon.Information)
        mensagem.setStandardButtons(QMessageBox.StandardButton.Ok)
        mensagem.exec()
    def cpf_existe(self, cpf):
        """Verifica se o CPF já existe no banco de dados."""
        vsql = "SELECT T_CPF FROM tb_pessoa WHERE T_CPF = "+ str(cpf)
        #print(vsql)
        resultado = banco.consultar(vsql)
        #print(resultado)
        if len(resultado) == 0:
            return False
        else:
            return True
    def carregar_zonas(self):
        vsql="SELECT T_ZONA FROM tb_zona ORDER BY T_ZONA"
        zonas=[row[0] for row in banco.consultar(vsql)]
        self.combo_zona.addItems(zonas)
        self.atualizar_bairros()  # Atualizar bairros da primeira zona carregada
    def atualizar_bairros(self):
        zona_selecionada = self.combo_zona.currentText()
        if zona_selecionada == "":
            self.combo_bairro.setCurrentIndex(-1)
        else:
            vsql="SELECT N_ID FROM tb_zona WHERE T_ZONA = " + '"' + str(zona_selecionada)+ '"'
            #print(vsql)
            zona_id=[row[0] for row in banco.consultar(vsql)]
            #print(zona_id)
            vsql="SELECT T_BAIRRO FROM tb_bairro WHERE N_ZONA = "+ str(zona_id[0])
            bairros = [row[0] for row in banco.consultar(vsql)]
            self.combo_bairro.clear()
            self.combo_bairro.addItems(bairros)
    def verificar_beneficio(self):
        """Mostra o campo de texto se a opção 'Outra opção' for escolhida."""
        if self.combo_recbeneficio.currentText() == "SIM":
            self.lnomebenefinicio.setVisible(True)
            self.combo_nomebeneficio.setVisible(True)
            self.loutrobeneficio.setVisible(False)
            self.leoutrobeneficio.setVisible(False)
            self.combo_nomebeneficio.setCurrentIndex(1)
        else:
            self.lnomebenefinicio.setVisible(False)
            self.combo_nomebeneficio.setVisible(False)
            self.loutrobeneficio.setVisible(False)
            self.leoutrobeneficio.setVisible(False)
            self.leoutrobeneficio.clear()
    def verificar_nomedobeneficio(self):
        """Mostra o campo de texto se a opção 'Outra opção' for escolhida."""
        if self.combo_nomebeneficio.currentText() == "Outros":
            self.loutrobeneficio.setVisible(True)
            self.leoutrobeneficio.setVisible(True)
        else:
            self.loutrobeneficio.setVisible(False)
            self.leoutrobeneficio.setVisible(False)
    def mostrar_mensagem_sobre(self):
        mensagem = QMessageBox(self)
        mensagem.setWindowTitle("Sobre")
        # mensagem.setStyleSheet('background: lightgray; color: black; font-size:18px;')
        mensagem.setText("""
Controle de Formulários
ONG Amazonia Viva
Versão: 1.0.0
Autor: Marcelo Ferreira
            """)
        mensagem.setIcon(QMessageBox.Icon.Information)
        mensagem.setStandardButtons(QMessageBox.StandardButton.Ok)
        mensagem.exec()

app = QApplication(sys.argv)
janela = MinhaJanela()
janela.show()
app.exec()
