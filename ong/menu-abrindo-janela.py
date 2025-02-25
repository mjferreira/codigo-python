import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtGui import QAction

def mostrar()

class MeuApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Exemplo de Menu no PyQt6")
        self.setGeometry(100, 100, 600, 400)

        # Criando a barra de menu
        barra_menu = self.menuBar()
        menu_arquivo = barra_menu.addMenu("Arquivo")

        # Criando uma ação para o menu
        acao_sobre = QAction("Sobre", self)
        acao_sobre.triggered.connect(self.mostrar_mensagem)
        menu_arquivo.addAction(acao_sobre)

        # Criando ação para sair
        acao_sair = QAction("Sair", self)
        acao_sair.triggered.connect(self.close)
        menu_arquivo.addAction(acao_sair)

    def mostrar_mensagem(self):
        QMessageBox.information(self, "Sobre", "Este é um exemplo de menu com PyQt6.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MeuApp()
    janela.show()
    sys.exit(app.exec())
