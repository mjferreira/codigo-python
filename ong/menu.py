import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QPushButton, QVBoxLayout, QWidget

class MinhaJanela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo de Visibilidade da Tabela")
        self.setGeometry(100, 100, 500, 300)

        # Criar widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Criar layout
        layout = QVBoxLayout(self.central_widget)

        # Criar Tabela
        self.tabela = QTableWidget(3, 3)  # 3 linhas, 3 colunas
        self.tabela.setHorizontalHeaderLabels(["ID", "Nome", "Status"])
        layout.addWidget(self.tabela)

        # Criar Botão para Alternar Visibilidade
        self.botao_toggle = QPushButton("Ocultar Tabela")
        self.botao_toggle.clicked.connect(self.alternar_visibilidade)
        layout.addWidget(self.botao_toggle)

    def alternar_visibilidade(self):
        if self.tabela.isVisible():
            self.tabela.setVisible(False)
            self.botao_toggle.setText("Mostrar Tabela")
        else:
            self.tabela.setVisible(True)
            self.botao_toggle.setText("Ocultar Tabela")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec())
