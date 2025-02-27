from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize

class MinhaJanela(QWidget):
    def __init__(self):
        super().__init__()

        # Definir título da janela
        self.setWindowTitle("Exemplo de Botão com Ícone")

        # Criar o botão e definir o ícone
        botao_ok = QPushButton(self)
        icone = QIcon("trash-can-red.jpg")  # Substitua com o caminho do seu ícone
        botao_ok.setIcon(icone)
        botao_ok.setIconSize(QSize(32, 32))  # Tamanho do ícone
        botao_ok.setText("")  # Remove o texto para mostrar apenas o ícone

        # Exibir a janela
        self.show()

# Inicializar a aplicação
app = QApplication([])

# Criar e exibir a janela
janela = MinhaJanela()

# Iniciar o loop de eventos da aplicação
app.exec()
