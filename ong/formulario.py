import re
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QHBoxLayout, QMessageBox, QTableWidget
from PyQt6.QtWidgets import QTableWidgetItem, QComboBox, QSizePolicy, QDialog, QTextEdit
from PyQt6.QtGui import QAction, QIcon, QTextCursor
from PyQt6.QtCore import QSize
import banco
import observacao
import composicao

class MinhaJanela(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.resize(600,500)
        self.setGeometry(500, 100, 720, 850)
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
        self.denfir_formulario()
        self.definir_tabela_consulta()
        self.ocultar_itens()
    def denfir_formulario(self):
        self.botao1 = QPushButton("Gravar", self.central_widget)
        self.botao1.setFixedSize(80, 30)
        self.botao1.move(630,780)
        self.botao1.setStyleSheet('background-color:red;color:white')
        self.botao1.clicked.connect(self.inserir_registro)

        self.botao2 = QPushButton("Voltar", self.central_widget)
        self.botao2.setFixedSize(80,30)
        self.botao2.move(400,780)
        self.botao2.setStyleSheet('background-color:green;color:white')
        self.botao2.clicked.connect(self.ocultar_itens)

        self.botao3 = QPushButton("Atualizar", self.central_widget)
        self.botao3.setFixedSize(80, 30)
        self.botao3.move(630,780)
        self.botao3.setStyleSheet('background-color:red;color:white')
        self.botao3.clicked.connect(self.atualizar_dados)

        self.botao4 = QPushButton("Voltar Consulta", self.central_widget)
        self.botao4.setFixedSize(120,30)
        self.botao4.move(400,780)
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

        self.lnomebenefinicio = QLabel("Qual Benefício:",self.central_widget)
        self.lnomebenefinicio.move(300,linha)
        self.lnomebenefinicio.setStyleSheet('color: black; font-size:16px')
        self.lnomebenefinicio.adjustSize()
        self.combo_nomebeneficio = QComboBox(self.central_widget)
        self.combo_nomebeneficio.setGeometry(450,linha,200,25)
        self.combo_nomebeneficio.addItems(["BPC","Bolsa Família", "Aponsentadoria", "Outros"])
        self.combo_nomebeneficio.currentIndexChanged.connect(self.verificar_nomedobeneficio)

        linha=linha+30
        self.loutrobeneficio = QLabel("Nome Benefício:",self.central_widget)
        self.loutrobeneficio.move(300,linha)
        self.loutrobeneficio.setStyleSheet('color: red; font-size:16px')
        self.loutrobeneficio.adjustSize()
        self.leoutrobeneficio = QLineEdit("", self.central_widget)
        self.leoutrobeneficio.setGeometry(450,linha,200,25)
        self.leoutrobeneficio.setStyleSheet('background: white; color: black; font-size:18px;')

        linha=linha+25
        self.linhainfpes = QLabel("_____________________________INFORMAÇÕES PESSOAIS_______________________________",self.central_widget)
        self.linhainfpes.move(80,linha)
        self.linhainfpes.setStyleSheet('color: blue; font-size:14px')
        self.linhainfpes.adjustSize()

        linha=linha+30
        self.lmedicacao = QLabel("Faz uso de Medicação:",self.central_widget)
        self.lmedicacao.move(10,linha)
        self.lmedicacao.setStyleSheet('color: black; font-size:16px')
        self.lmedicacao.adjustSize()
        self.combo_medicacao = QComboBox(self.central_widget)
        self.combo_medicacao.setGeometry(200,linha,60,25)
        self.combo_medicacao.addItems(["SIM","NÃO"])
        self.combo_medicacao.currentIndexChanged.connect(self.verificar_nomemedicacao)

        self.lnomemedicacao = QLabel("Nome Medicação:",self.central_widget)
        self.lnomemedicacao.move(300,linha)
        self.lnomemedicacao.setStyleSheet('color: red; font-size:16px')
        self.lnomemedicacao.adjustSize()
        self.lenomemedicacao = QLineEdit("", self.central_widget)
        self.lenomemedicacao.setGeometry(450,linha,200,25)
        self.lenomemedicacao.setStyleSheet('background: white; color: black; font-size:18px;')

        linha=linha+25
        self.linhacompo = QLabel("______________________________COMPOSIÇÃO FAMILIAR________________________________",self.central_widget)
        self.linhacompo.move(80,linha)
        self.linhacompo.setStyleSheet('color: blue; font-size:14px')
        self.linhacompo.adjustSize()

        linha=linha+25
        # Criando a tabela
        self.btn_composicao = QPushButton("Adicionar Composicao Familiar",self.central_widget)
        self.btn_composicao.setGeometry(10,linha,700,20)
        self.btn_composicao.clicked.connect(self.abrir_composicao)

        linha=linha+30
        self.linhamoradia = QLabel("______________________________SITUAÇÃO DE MORADIAS_______________________________",self.central_widget)
        self.linhamoradia.move(80,linha)
        self.linhamoradia.setStyleSheet('color: blue; font-size:14px')
        self.linhamoradia.adjustSize()

        linha=linha+30
        self.lmoradia = QLabel("Moradia:",self.central_widget)
        self.lmoradia.move(10,linha)
        self.lmoradia.setStyleSheet('color: black; font-size:16px')
        self.lmoradia.adjustSize()
        self.combo_moradia = QComboBox(self.central_widget)
        self.combo_moradia.setGeometry(120,linha,135,25)
        self.combo_moradia.addItems(["Própria","Alugada", "Cedida"])
        self.combo_moradia.currentIndexChanged.connect(self.verificar_moradia)

        self.lvalor_aluguel = QLabel("Valor do aluguel:",self.central_widget)
        self.lvalor_aluguel.move(300,linha)
        self.lvalor_aluguel.setStyleSheet('color: red; font-size:16px')
        self.lvalor_aluguel.adjustSize()
        self.levalor_aluguel = QLineEdit("", self.central_widget)
        self.levalor_aluguel.setGeometry(450,linha,90,25)
        self.levalor_aluguel.setStyleSheet('background: white; color: black; font-size:18px;')
        self.levalor_aluguel.setInputMask("99.999,00")  # Apenas números e "-" fixo

        linha=linha+30
        self.lparedes = QLabel("Paredes:",self.central_widget)
        self.lparedes.move(10,linha)
        self.lparedes.setStyleSheet('color: black; font-size:16px')
        self.lparedes.adjustSize()
        self.combo_paredes = QComboBox(self.central_widget)
        self.combo_paredes.setGeometry(120,linha,135,25)
        self.combo_paredes.addItems(["Alvenaria","Madeira", "Outros"])
        self.combo_paredes.currentIndexChanged.connect(self.verificar_paredes)

        self.lparede_outro = QLabel("Tipo de Parede:",self.central_widget)
        self.lparede_outro.move(300,linha)
        self.lparede_outro.setStyleSheet('color: red; font-size:16px')
        self.lparede_outro.adjustSize()
        self.leparede_outro = QLineEdit("", self.central_widget)
        self.leparede_outro.setGeometry(450,linha,150,25)
        self.leparede_outro.setStyleSheet('background: white; color: black; font-size:18px;')

        linha=linha+30
        self.ltelhado = QLabel("Telhado:",self.central_widget)
        self.ltelhado.move(10,linha)
        self.ltelhado.setStyleSheet('color: black; font-size:16px')
        self.ltelhado.adjustSize()
        self.combo_telhado = QComboBox(self.central_widget)
        self.combo_telhado.setGeometry(120,linha,135,25)
        self.combo_telhado.addItems(["Brasilit","Galvanizada", "Barro", "Outros"])
        self.combo_telhado.currentIndexChanged.connect(self.verificar_telhado)

        self.ltelhado_outro = QLabel("Tipo de Telhado:",self.central_widget)
        self.ltelhado_outro.move(300,linha)
        self.ltelhado_outro.setStyleSheet('color: red; font-size:16px')
        self.ltelhado_outro.adjustSize()
        self.letelhado_outro = QLineEdit("", self.central_widget)
        self.letelhado_outro.setGeometry(450,linha,150,25)
        self.letelhado_outro.setStyleSheet('background: white; color: black; font-size:18px;')       

        linha=linha+30
        self.lpiso = QLabel("Piso:",self.central_widget)
        self.lpiso.move(10,linha)
        self.lpiso.setStyleSheet('color: black; font-size:16px')
        self.lpiso.adjustSize()
        self.combo_piso = QComboBox(self.central_widget)
        self.combo_piso.setGeometry(120,linha,135,25)
        self.combo_piso.addItems(["Batido","Cerâmica", "Porcelanato", "Outros"])
        self.combo_piso.currentIndexChanged.connect(self.verificar_piso)

        self.lpiso_outro = QLabel("Tipo de piso:",self.central_widget)
        self.lpiso_outro.move(300,linha)
        self.lpiso_outro.setStyleSheet('color: red; font-size:16px')
        self.lpiso_outro.adjustSize()
        self.lepiso_outro = QLineEdit("", self.central_widget)
        self.lepiso_outro.setGeometry(450,linha,150,25)
        self.lepiso_outro.setStyleSheet('background: white; color: black; font-size:18px;')

        linha=linha+30
        self.linhaobservacao = QLabel("___________________________________OBSERVAÇOES___________________________________",self.central_widget)
        self.linhaobservacao.move(80,linha)
        self.linhaobservacao.setStyleSheet('color: blue; font-size:14px')
        self.linhaobservacao.adjustSize()    

        linha=linha+30
        # Criando a tabela
        self.btn_observacao = QPushButton("Observações - Profissional Entrevistador",self.central_widget)
        self.btn_observacao.setGeometry(10,linha,700,20)
        self.btn_observacao.clicked.connect(self.abrir_observacao)
    def definir_tabela_consulta(self):
        # Layout principale
        layout = QVBoxLayout(self.central_widget)
        # Campo de busca
        self.search_box = QLineEdit(self)
        self.search_box.setPlaceholderText("Digite para filtrar...")
        self.search_box.textChanged.connect(self.filter_table)  # Conecta ao método de filtro
        layout.addWidget(self.search_box)

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
    def carregar_tabela_consulta(self):
        vsql = "SELECT T_NOME, T_CPF, T_NIS FROM tb_pessoa order by T_NOME"
        dados = banco.consultar(vsql)
        self.tabela.setRowCount(len(dados))
        self.tabela.setColumnCount(5)  # ID, Nome, Idade, Ações
        self.tabela.setColumnWidth(0, 300)   # Coluna 0 com 50 pixels
        self.tabela.setColumnWidth(1, 105)  # Coluna 1 com 150 pixels
        self.tabela.setColumnWidth(2, 105)  # Coluna 2 com 100 pixels
        self.tabela.setColumnWidth(3, 60)  # Coluna 2 com 100 pixels
        self.tabela.setColumnWidth(4, 60)  # Coluna 2 com 100 pixels
        self.tabela.setHorizontalHeaderLabels(["Nome", "CPF", "NIS", "Edita", "Remove", "Imprimir"])
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
        medicacao=resultado[0][18]
        self.lenomemedicacao.setText(resultado[0][19])
        moradia=resultado[0][20]
        aluguel=resultado[0][21]
        paredes=resultado[0][22]
        telhado=resultado[0][23]
        piso=resultado[0][24]
        self.data_observacao=resultado[0][25]
        
        self.combo_medicacao.setCurrentText(medicacao)
        if len(nomebeneficio) != 0:
            if nomebeneficio in ["BPC","Bolsa Família", "Aponsentadoria"]:
                self.combo_nomebeneficio.setCurrentText(nomebeneficio)
                self.combo_nomebeneficio.setVisible(True)
                self.lnomebenefinicio.setVisible(True)
            else:
                self.combo_nomebeneficio.setCurrentText("Outros")
                self.leoutrobeneficio.setText(nomebeneficio)
                self.combo_nomebeneficio.setVisible(True)
                self.lnomebenefinicio.setVisible(True)
                self.loutrobeneficio.setVisible(True)
                self.leoutrobeneficio.setVisible(True)
        if medicacao == "SIM":
            self.lnomemedicacao.setVisible(True)
            self.lenomemedicacao.setVisible(True)
        elif len(medicacao) == 0:
            self.combo_medicacao.setCurrentIndex(-1)

        self.combo_moradia.setCurrentText(moradia)
        if moradia != "Alugada":
            self.levalor_aluguel.setText("")
            self.lvalor_aluguel.setVisible(False)
            self.levalor_aluguel.setVisible(False)
        else:
            self.levalor_aluguel.setText(aluguel)
            self.lvalor_aluguel.setVisible(True)
            self.levalor_aluguel.setVisible(True)

        if paredes not in ["Alvenaria", "Madeira"]:
            self.combo_paredes.setCurrentText("Outros")
            self.leparede_outro.setText(paredes)
            self.lparede_outro.setVisible(True)
            self.leparede_outro.setVisible(True)
        else:
            self.combo_paredes.setCurrentText(paredes)
            self.lparede_outro.setVisible(False)
            self.leparede_outro.setVisible(False)

        if telhado not in ["Brasilit","Galvanizada", "Barro"]:
            self.combo_telhado.setCurrentText("Outros")
            self.letelhado_outro.setText(telhado)
            self.ltelhado_outro.setVisible(True)
            self.letelhado_outro.setVisible(True)
        else:
            self.combo_telhado.setCurrentText(paredes)
            self.ltelhado_outro.setVisible(False)
            self.letelhado_outro.setVisible(False)
     
        if piso not in ["Batido","Cerâmica", "Porcelanato"]:
            self.combo_piso.setCurrentText("Outros")
            self.lepiso_outro.setText(piso)
            self.lpiso_outro.setVisible(True)
            self.lepiso_outro.setVisible(True)
        else:
            self.combo_piso.setCurrentText(piso)
            self.lpiso_outro.setVisible(False)
            self.lepiso_outro.setVisible(False)            

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
        self.carregar_composicao()
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
        self.lmedicacao.setVisible(True)
        self.combo_medicacao.setVisible(True)
        self.linhacompo.setVisible(True)
        self.btn_composicao.setVisible(True)
        self.btn_observacao.setVisible(True)
        self.linhamoradia.setVisible(True)
        self.lmoradia.setVisible(True)
        self.combo_moradia.setVisible(True)
        self.lparedes.setVisible(True)
        self.combo_paredes.setVisible(True)
        self.combo_telhado.setVisible(True)
        self.ltelhado.setVisible(True)  
        self.lpiso.setVisible(True)
        self.combo_piso.setVisible(True)   
        self.linhaobservacao.setVisible(True) 
    def consultar(self):
        self.ocultar_itens()
        self.carregar_tabela_consulta()
        self.tabela.setVisible(True)
        self.botao_toggle.setVisible(True)
        self.search_box.setVisible(True)
    def ocultar_itens_consulta(self):
        self.botao_toggle.setVisible(False)
        self.tabela.setVisible(False)
        self.search_box.setVisible(False)
    def ocultar_itens(self):
        self.botao_toggle.setVisible(False)
        self.linhaiden.setVisible(False)
        self.tabela.setVisible(False)
        self.search_box.setVisible(False)
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
        self.lmedicacao.setVisible(False)
        self.combo_medicacao.setVisible(False)
        self.lnomemedicacao.setVisible(False)
        self.lenomemedicacao.setVisible(False)
        self.linhacompo.setVisible(False)
        self.btn_composicao.setVisible(False)
        self.linhamoradia.setVisible(False)
        self.lmoradia.setVisible(False)
        self.combo_moradia.setVisible(False)
        self.lvalor_aluguel.setVisible(False)
        self.levalor_aluguel.setVisible(False)
        self.lparedes.setVisible(False)
        self.combo_paredes.setVisible(False)
        self.leparede_outro.setVisible(False)
        self.lparede_outro.setVisible(False)
        self.letelhado_outro.setVisible(False)
        self.ltelhado_outro.setVisible(False)
        self.combo_telhado.setVisible(False)
        self.ltelhado.setVisible(False)
        self.lpiso.setVisible(False)
        self.combo_piso.setVisible(False)
        self.lpiso_outro.setVisible(False)
        self.lepiso_outro.setVisible(False)
        self.btn_observacao.setVisible(False)
        self.linhaobservacao.setVisible(False)
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
        if vrecbeneficio == "SIM":
            if self.combo_nomebeneficio.currentText() == "Outros":
                vnomebeneficio=self.leoutrobeneficio.text()
            else:
                vnomebeneficio=self.combo_nomebeneficio.currentText()
        else:
            vnomebeneficio=""
        vmedicacao=self.combo_medicacao.currentText()
        vnomemedicacao=self.lenomemedicacao.text()
        vmoradia=self.combo_moradia.currentText()
        if vmoradia != "Alugada":
            valuguel=""
        else:
            valuguel=self.levalor_aluguel.text().replace(".", "").replace(",", "")
        vparedes=self.combo_paredes.currentText()
        if vparedes == "Outros":
            vparedes=self.leparede_outro.text()
        vtelhado=self.combo_telhado.currentText()
        if vtelhado == "Outros":
            vtelhado=self.letelhado_outro.text() 
        vpiso=self.combo_piso.currentText()
        if vpiso == "Outros":
            vpiso=self.lepiso_outro.text()
        vobs=self.data_observacao
        vsql="SELECT N_ID FROM tb_bairro WHERE T_BAIRRO = "+ '"' + vbairro + '"'
        vbairro=[row[0] for row in banco.consultar(vsql)]
        # vcpf=self.lecpf.text().replace("-", "").replace(".", "")
        if not self.cpf_valido(vcpf):
            QMessageBox.critical(self, "Erro Crítico","CPF INVÁLIDO !!!", QMessageBox.StandardButton.Ok)
        elif self.cpf_existe(vcpf):
            QMessageBox.critical(self, "Erro Crítico","CPF JÁ CADASTRADO !!!", QMessageBox.StandardButton.Ok)
        elif len(vbairro) == 0:
            QMessageBox.critical(self, "Erro Crítico","Selecione o endereço !!!", QMessageBox.StandardButton.Ok)
        elif not self.cpf_valido(vnis):
            QMessageBox.critical(self, "Erro Crítico","NIS INVÁLIDO !!!", QMessageBox.StandardButton.Ok)
        elif self.combo_recbeneficio.currentText() == "SIM" and self.combo_nomebeneficio.currentText() == "Outros" and len(vnomebeneficio) == 0:
            QMessageBox.critical(self, "Erro Crítico","Nome de Benefício deve ser definido !!!", QMessageBox.StandardButton.Ok)
        elif self.combo_medicacao.currentText() == "SIM" and len(vnomemedicacao) == 0:
            QMessageBox.critical(self, "Erro Crítico","Nome da Medicação deve ser informada !!!", QMessageBox.StandardButton.Ok)
        elif self.combo_moradia.currentText() == "Alugada" and len(valuguel) == 0:
            QMessageBox.critical(self, "Erro Crítico","Valor do aluguel deve ser informado !!!", QMessageBox.StandardButton.Ok)
        elif self.combo_paredes.currentText() == "Outros" and len(vparedes) == 0:
            QMessageBox.critical(self, "Erro Crítico","Tipo de  Parede deve ser informada !!!", QMessageBox.StandardButton.Ok)
        elif self.combo_telhado.currentText() == "Outros" and len(vtelhado) == 0:
            QMessageBox.critical(self, "Erro Crítico","Tipo de  Telhaod deve ser informado !!!", QMessageBox.StandardButton.Ok)
        elif self.combo_piso.currentText() == "Outros" and len(vpiso) == 0:
            QMessageBox.critical(self, "Erro Crítico","Tipo de Piso deve ser informado!!!", QMessageBox.StandardButton.Ok)
        else:
            vsql="INSERT INTO tb_pessoa (T_NOME, T_RG, T_CPF, T_MAE, T_CPFMAE, T_PAI, T_CPFPAI, N_BAIRRO, T_NIS, T_FONE, T_CEP, T_GRAU_ENSINO, T_ESCOLA, T_SERIE_ANO, T_TRABALHA, T_RENDA, T_RECBENEFICIO, T_NOMEBENEFICIO, T_MEDICACAO, T_NOMEMEDICACAO, T_MORADIA, T_VALOR_ALUGUEL, T_PAREDES, T_TELHADO, T_PISO, T_OBS) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', %s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(vnome, vrg, vcpf, vmae, vcpfmae, vpai, vcpfpai, vbairro[0], vnis, vfone, vcep, vgrau_ensino, vescola, vserieano, vtrabalha, vrenda, vrecbeneficio, vnomebeneficio, vmedicacao, vnomemedicacao, vmoradia, valuguel, vparedes, vtelhado, vpiso, vobs)
            print(vsql)
            banco.atualizar(vsql)
            self.gravar_composicao()
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
        self.combo_trabalha.setCurrentIndex(1)
        self.combo_recbeneficio.setCurrentIndex(1)
        self.combo_nomebeneficio.setCurrentIndex(-1)
        self.combo_medicacao.setCurrentIndex(1)
        self.lenomemedicacao.clear()
        self.combo_moradia.setCurrentIndex(1)
        self.levalor_aluguel.clear()
        self.combo_paredes.setCurrentIndex(1)
        self.leparede_outro.clear()
        self.combo_telhado.setCurrentIndex(1)
        self.letelhado_outro.clear()
        self.combo_piso.setCurrentIndex(1)
        self.lepiso_outro.clear()
        self.data_composicao=[]
        self.data_observacao=""
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
        if vrecbeneficio == "SIM":
            if self.combo_nomebeneficio.currentText() == "Outros":
                vnomebeneficio=self.leoutrobeneficio.text()
            else:
                vnomebeneficio=self.combo_nomebeneficio.currentText()
        else:
            vnomebeneficio=""
        vmedicacao=self.combo_medicacao.currentText()
        vnomemedicacao=self.lenomemedicacao.text()
        vmoradia=self.combo_moradia.currentText()
        if vmoradia != "Alugada":
            valuguel=""
        else:
            valuguel=self.levalor_aluguel.text().replace(".", "").replace(",", "")
        print("Valor do alguel...")
        print(valuguel)   
        vparedes=self.combo_paredes.currentText()
        if vparedes == "Outros":
            vparedes=self.leparede_outro.text()
        vtelhado=self.combo_telhado.currentText()
        if vtelhado == "Outros":
            vtelhado=self.letelhado_outro.text() 
        vpiso=self.combo_piso.currentText()
        if vpiso == "Outros":
            vpiso=self.lepiso_outro.text()
        vobs=self.data_observacao
        print(vobs)
        vsql="SELECT N_ID FROM tb_bairro WHERE T_BAIRRO = "+ '"' + vbairro + '"'
        vbairro=[row[0] for row in banco.consultar(vsql)]
        if not self.cpf_valido(vcpf):
            QMessageBox.critical(self, "Erro Crítico","CPF INVÁLIDO !!!", QMessageBox.StandardButton.Ok)
        elif len(vbairro) == 0:
            QMessageBox.critical(self, "Erro Crítico","Selecione o endereço !!!", QMessageBox.StandardButton.Ok)
        elif not self.cpf_valido(vnis):
            QMessageBox.critical(self, "Erro Crítico","NIS INVÁLIDO !!!", QMessageBox.StandardButton.Ok)
        elif self.combo_recbeneficio.currentText() == "SIM" and self.combo_nomebeneficio.currentText() == "Outros" and len(vnomebeneficio) == 0:
            QMessageBox.critical(self, "Erro Crítico","Nome de Benefício deve ser definido !!!", QMessageBox.StandardButton.Ok)
        elif self.combo_medicacao.currentText() == "SIM" and len(vnomemedicacao) == 0:
            QMessageBox.critical(self, "Erro Crítico","Nome da Medicação deve ser informada !!!", QMessageBox.StandardButton.Ok)
        elif self.combo_moradia.currentText() == "Alugada" and len(valuguel) == 0:
            QMessageBox.critical(self, "Erro Crítico","Valor do aluguel deve ser informado !!!", QMessageBox.StandardButton.Ok)
        elif self.combo_paredes.currentText() == "Outros" and len(vparedes) == 0:
            QMessageBox.critical(self, "Erro Crítico","Tipo de  Parede deve ser informada !!!", QMessageBox.StandardButton.Ok)
        elif self.combo_telhado.currentText() == "Outros" and len(vtelhado) == 0:
            QMessageBox.critical(self, "Erro Crítico","Tipo de  Telhaod deve ser informado !!!", QMessageBox.StandardButton.Ok)
        elif self.combo_piso.currentText() == "Outros" and len(vpiso) == 0:
            QMessageBox.critical(self, "Erro Crítico","Tipo de Piso deve ser informado!!!", QMessageBox.StandardButton.Ok)            
        else:
            print(vsql)
            vsql= "UPDATE tb_pessoa SET T_NOME='"+vnome+"',T_RG='"+vrg+"',T_CPF='"+vcpf+"',T_MAE='"+vmae+"',T_CPFMAE='"+vcpfmae+"',T_PAI='"+vpai+"',T_CPFPAI='"+vcpfpai+"',N_BAIRRO="+str(vbairro[0])+",T_NIS='"+vnis+"',T_FONE='"+vfone+"',T_CEP='"+vcep+"',T_GRAU_ENSINO='"+vgrau_ensino+"',T_ESCOLA='"+vescola+"',T_SERIE_ANO='"+vserieano+"',T_TRABALHA='"+vtrabalha+"',T_RENDA='"+vrenda+"',T_RECBENEFICIO='"+vrecbeneficio+"',T_NOMEBENEFICIO='"+vnomebeneficio+"',T_MEDICACAO='"+vmedicacao+"',T_NOMEMEDICACAO='"+vnomemedicacao+"',T_MORADIA='"+vmoradia+"',T_VALOR_ALUGUEL='"+valuguel+"',T_PAREDES='"+vparedes+"',T_TELHADO='"+vtelhado+"',T_PISO='"+vpiso+"',T_OBS='"+vobs+"' WHERE T_CPF="+vcpf
            banco.atualizar(vsql)
            self.gravar_composicao()
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
    def verificar_nomemedicacao(self):
        """Mostra o campo de texto se a opção 'Outra opção' for escolhida."""
        if self.combo_medicacao.currentText() == "SIM":
            self.lnomemedicacao.setVisible(True)
            self.lenomemedicacao.setVisible(True)
        else:
            self.lnomemedicacao.setVisible(False)
            self.lenomemedicacao.setVisible(False)
    def verificar_moradia(self):
        """Mostra o campo de valor do aluguel se ALGUADA."""
        if self.combo_moradia.currentText() == "Alugada":
            self.lvalor_aluguel.setVisible(True)
            self.levalor_aluguel.setVisible(True)
        else:
            self.lvalor_aluguel.setVisible(False)
            self.levalor_aluguel.setVisible(False)
    def verificar_paredes(self):
        """Mostra o campo de tipo de parede se OUTROS."""
        if self.combo_paredes.currentText() == "Outros":
            self.lparede_outro.setVisible(True)
            self.leparede_outro.setVisible(True)
        else:
            self.lparede_outro.setVisible(False)
            self.leparede_outro.setVisible(False)
    def verificar_telhado(self):
        """Mostra o campo de tipo de telhado se OUTROS."""
        if self.combo_telhado.currentText() == "Outros":
            self.ltelhado_outro.setVisible(True)
            self.letelhado_outro.setVisible(True)
        else:
            self.ltelhado_outro.setVisible(False)
            self.letelhado_outro.setVisible(False)
    def verificar_piso(self):
        """Mostra o campo de tipo de piso se OUTROS."""
        if self.combo_piso.currentText() == "Outros":
            self.lpiso_outro.setVisible(True)
            self.lepiso_outro.setVisible(True)
        else:
            self.lpiso_outro.setVisible(False)
            self.lepiso_outro.setVisible(False)
    def filter_table(self):
        filtro = self.search_box.text().lower()
        for row in range(self.tabela.rowCount()):
            row_visible = False
            for col in range(self.tabela.columnCount()):
                item = self.tabela.item(row, col)
                if item and filtro in item.text().lower():
                    row_visible = True
                    break  # Se um dos campos da linha corresponde, mantemos a linha visível
            self.tabela.setRowHidden(row, not row_visible)
    def mostrar_mensagem_sobre(self):
        mensagem = QMessageBox(self)
        mensagem.setWindowTitle("Sobre")
        with open(".sobre", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        mensagem.setText(conteudo)
        mensagem.setIcon(QMessageBox.Icon.Information)
        mensagem.setStandardButtons(QMessageBox.StandardButton.Ok)
        mensagem.exec()
    def abrir_composicao(self):
        comp1 = composicao.TableWindow(self, self.data_composicao)  # Passa os dados existentes
        if comp1.exec():
            self.data_composicao = comp1.get_data()  # Atualiza os dados
            print(self.data_composicao)
    def abrir_observacao(self):
        obs1 = observacao.ObservacaoWindow(self, self.data_observacao)  # Passa os dados existentes
        if obs1.exec():
            self.data_observacao = obs1.get_text()  # Atualiza os dados
            print(self.data_observacao)
    def gravar_composicao(self):
        """Salva os dados da tabela no banco de dados"""
        # Limpa os dados antes de salvar para evitar duplicação
        vcpf=self.lecpf.text().replace("-", "").replace(".", "")
        vsql="DELETE FROM tb_composicao WHERE T_CPF = "+"'"+vcpf+"'"
        print(vsql)
        banco.atualizar(vsql)
        for row in self.data_composicao:
            vnome = row[0]
            vlocal = row[2]
            vparentesco = row[1]
            vsql="INSERT INTO tb_composicao (T_CPF, T_NOME, T_PARENTESCO, T_ESCOLA_TRABALHO) VALUES ("+"'"+vcpf+"'"+","+"'"+vnome+"'"+","+"'"+vparentesco+"'"+","+"'"+vlocal+"'"+")"
            print(vsql)
            banco.atualizar(vsql)
    def carregar_composicao(self):
        """Carrega os dados do banco de dados para a tabela"""
        vcpf=self.lecpf.text().replace("-", "").replace(".", "")
        vsql="SELECT T_NOME, T_PARENTESCO, T_ESCOLA_TRABALHO  FROM tb_composicao WHERE T_CPF ="+str(vcpf)
        print(vsql)
        rows = banco.consultar(vsql)
        print(rows)
        self.data_composicao = []
        # Adiciona os dados à tabela
        for row in rows:
            self.data_composicao.append((row[0], row[1], row[2]))
