import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QAction  # Importar QAction corretamente

class MinhaJanela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Janela com Menu")
        self.setGeometry(100, 100, 500, 400)

        # Criar a barra de menus
        menu_bar = self.menuBar()

        # Criar um menu "Arquivo"
        menu_arquivo = menu_bar.addMenu("Arquivo")

        # Criar ações para o menu
        acao_abrir = QAction("Abrir", self)
        acao_salvar = QAction("Salvar", self)
        acao_sair = QAction("Sair", self)

        # Adicionar ações ao menu
        menu_arquivo.addAction(acao_abrir)
        menu_arquivo.addAction(acao_salvar)
        menu_arquivo.addSeparator()
        menu_arquivo.addAction(acao_sair)

        # Conectar a ação "Sair" para fechar a janela
        acao_sair.triggered.connect(self.close)

app = QApplication(sys.argv)
janela = MinhaJanela()
janela.show()
sys.exit(app.exec())
