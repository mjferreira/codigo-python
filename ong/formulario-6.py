import sys, re
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QHBoxLayout, QMessageBox, QTableWidget
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import QSize
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

        self.botao1 = QPushButton("Gravar", self.central_widget)
        self.botao1.setFixedSize(80, 30)
        self.botao1.move(400,400)
        self.botao1.setVisible(False)
        self.botao1.setStyleSheet('background-color:red;color:white')
        self.botao1.clicked.connect(self.inserir_registro)

        self.botao2 = QPushButton("Voltar", self.central_widget)
        self.botao2.setFixedSize(80,30)
        self.botao2.move(10,400)
        self.botao2.setVisible(False)
        self.botao2.setStyleSheet('background-color:green;color:white')
        self.botao2.clicked.connect(self.ocultar_itens)

        self.botao3 = QPushButton("Atualizar", self.central_widget)
        self.botao3.setFixedSize(80, 30)
        self.botao3.move(400,400)
        self.botao3.setStyleSheet('background-color:red;color:white')
        self.botao3.setVisible(True)
        self.botao3.clicked.connect(self.modificarDados)

        self.botao4 = QPushButton("Voltar Consulta", self.central_widget)
        self.botao4.setFixedSize(120,30)
        self.botao4.move(10,400)
        self.botao4.setVisible(False)
        self.botao4.setStyleSheet('background-color:green;color:white')
        self.botao4.clicked.connect(self.consultar)

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
        self.lerg.setInputMask("99999999999")
        self.lerg.setVisible(False)

        self.lcpf = QLabel("CPF:",self.central_widget)
        self.lcpf.move(10,70)
        self.lcpf.setStyleSheet('color: black; font-size:16px')
        self.lecpf = QLineEdit("",self.central_widget)
        self.lecpf.setStyleSheet('background: white; color: black; font-size:18px;')
        self.lecpf.setGeometry(80,70,150,25)
        self.lecpf.setInputMask("999.999.999-99")  # Apenas números e "-" fixo


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
        self.lecpfmae.setInputMask("999.999.999-99")  # Apenas números e "-" fixo


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
        self.lecpfpai.setInputMask("999.999.999-99")  # Apenas números e "-" fixo


        # Layout principal
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

    def carregar_dados(self):
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
        self.lenome.setText(resultado[0][0])
        self.lerg.setText(resultado[0][1])
        self.lecpf.setText(resultado[0][2])
        self.lemae.setText(resultado[0][3])
        self.lecpfmae.setText(resultado[0][4])
        self.lepai.setText(resultado[0][5])
        self.lecpfpai.setText(resultado[0][6])
        self.modificar()

    def excluir_registro(self, cpf):
        """Exclui um registro do banco de dados"""
        resposta = QMessageBox.question(self, "Excluir", f"Tem certeza que deseja excluir o {cpf}?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if resposta == QMessageBox.StandardButton.Yes:
            vsql = "DELETE FROM tb_pessoa WHERE T_CPF = "+ str(cpf)
            banco.atualizar(vsql)
            self.carregar_dados()  # Recarregar os dados após a exclusão

    def inserir(self):
        self.ocultar_itens()
        self.limpar_dados()
        self.lecpf.setReadOnly(False)
        self.lecpf.setStyleSheet('background: white; color: black; font-size:18px;')
        self.mostrar_formulario()

    def modificar(self):
        self.ocultar_itens()
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

    def consultar(self):
        self.carregar_dados()
        self.tabela.setVisible(True)
        self.botao_toggle.setVisible(True)

    def ocultar_itens(self):
        self.botao_toggle.setVisible(False)
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
        self.lmae.setVisible(False)
        self.lcpfmae.setVisible(False)
        self.lpai.setVisible(False)
        self.lcpfpai.setVisible(False)
        self.lecpf.setVisible(False)
        self.lemae.setVisible(False)
        self.lecpfmae.setVisible(False)
        self.lepai.setVisible(False)
        self.lecpfpai.setVisible(False)

    def inserir_registro(self):
        vnome=self.lenome.text()
        vrg=self.lerg.text()
        vcpf=self.lecpf.text().replace("-", "").replace(".", "")
        vmae=self.lemae.text()
        vcpfmae=self.lecpfmae.text().replace("-", "").replace(".", "")
        vpai=self.lepai.text()
        vcpfpai=self.lecpfpai.text().replace("-", "").replace(".", "")

        if self.cpf_existe(vcpf):
            QMessageBox.critical(self, "Erro Crítico","CPF JÁ CADASTRADO !!!", QMessageBox.StandardButton.Ok)
#        elif not self.cpf_valido(vcpf):
#            QMessageBox.critical(self, "Erro Crítico","CPF INVÁLIDO !!!", QMessageBox.StandardButton.Ok)
        else:
            vsql="INSERT INTO tb_pessoa (T_NOME, T_RG, T_CPF, T_MAE, T_CPFMAE, T_PAI, T_CPFPAI) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(vnome, vrg, vcpf, vmae, vcpfmae, vpai, vcpfpai)
            banco.atualizar(vsql)
            self.limpar_dados()

    def limpar_dados(self):
        self.lenome.clear()
        self.lerg.clear()
        self.lecpf.clear()
        self.lemae.clear()
        self.lecpfmae.clear()
        self.lepai.clear()
        self.lecpfpai.clear()

    def modificarDados(self):
        vnome=self.lenome.text()
        vrg=self.lerg.text()
        vcpf=self.lecpf.text().replace("-", "").replace(".", "")
        vmae=self.lemae.text()
        vcpfmae=self.lecpfmae.text().replace("-", "").replace(".", "")
        vpai=self.lepai.text()
        vcpfpai=self.lecpfpai.text().replace("-", "").replace(".", "")
        vsql= "UPDATE tb_pessoa SET T_NOME='"+vnome+"',T_RG='"+vrg+"',T_CPF='"+vcpf+"',T_MAE='"+vmae+"',T_CPFMAE='"+vcpfmae+"',T_PAI='"+vpai+"',T_CPFPAI='"+vcpfpai+"' WHERE T_CPF="+vcpf
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
        def calcular_digito(cpf_parcial, peso_inicial):
            soma = sum(int(digito) * peso for digito, peso in zip(cpf_parcial, range(peso_inicial, 1, -1)))
            resto = soma % 11
            return "0" if resto < 2 else str(11 - resto)

        # Validar o primeiro dígito verificador
        primeiro_digito = calcular_digito(cpf[:9], 10)
        if cpf[9] != primeiro_digito:
            return False

        # Validar o segundo dígito verificador
        segundo_digito = calcular_digito(cpf[:10], 11)
        if cpf[10] != segundo_digito:
            return False

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
        print(vsql)
        resultado = banco.consultar(vsql)
        print(resultado)
        if len(resultado) == 0:
            return False
        else:
            return True

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
