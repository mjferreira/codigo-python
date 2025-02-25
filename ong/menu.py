import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QHBoxLayout
from PyQt6.QtGui import QAction
class MeuApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Exemplo de Menu no PyQt6")
        self.setGeometry(100, 100, 600, 400)

        # Criando um widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Criando um label para exibir mensagens
        self.label_mensagem = QLabel("Selecione uma opção do menu.", self.central_widget)
        self.label_mensagem.move(20, 20)

        # Criando um campo de entrada e botão (inicialmente ocultos)
        self.entrada_texto = QLineEdit(self.central_widget)
        self.entrada_texto.setPlaceholderText("Digite algo...")
        self.entrada_texto.move(150, 100)
        self.entrada_texto.setVisible(False)

        self.botao_acao = QPushButton("Confirmar", self.central_widget)
        self.botao_acao.move(150, 140)
        self.botao_acao.setFixedSize(100, 30)
        self.botao_acao.setVisible(False)
        self.botao_acao.clicked.connect(self.desativar_componentes)

        # Criando a barra de menu
        barra_menu = self.menuBar()
        menu_arquivo = barra_menu.addMenu("Arquivo")

        # Criando uma ação para o menu
        acao_sobre = QAction("Sobre", self)
        acao_sobre.triggered.connect(self.mostrar_mensagem)
        menu_arquivo.addAction(acao_sobre)

        # Criando ação para ativar entrada e botão
        acao_ativar = QAction("Ativar Entrada", self)
        acao_ativar.triggered.connect(self.ativar_componentes)
        menu_arquivo.addAction(acao_ativar)

        # Criando ação para sair
        acao_sair = QAction("Sair", self)
        acao_sair.triggered.connect(self.close)
        menu_arquivo.addAction(acao_sair)

    def mostrar_mensagem(self):
        self.label_mensagem.setText("Este é um exemplo de menu com PyQt6.")

    def ativar_componentes(self):
        self.entrada_texto.setVisible(True)
        self.botao_acao.setVisible(True)

    def desativar_componentes(self):
        self.entrada_texto.setVisible(False)
        self.botao_acao.setVisible(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MeuApp()
    janela.show()
    sys.exit(app.exec())
