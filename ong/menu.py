import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QLineEdit

class Janela(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo de QComboBox com Campo Condicional")
        self.setGeometry(100, 100, 350, 200)

        layout = QVBoxLayout()

        # Rótulo e ComboBox
        self.label = QLabel("Escolha uma opção:")
        layout.addWidget(self.label)

        self.combo = QComboBox()
        self.combo.addItems(["Opção 1", "Opção 2", "Outra opção"])
        self.combo.currentIndexChanged.connect(self.verificar_opcao)
        layout.addWidget(self.combo)

        # Campo de entrada (inicialmente oculto)
        self.label_extra = QLabel("Digite sua opção:")
        self.label_extra.setVisible(False)  # Escondido no início
        layout.addWidget(self.label_extra)

        self.campo_extra = QLineEdit()
        self.campo_extra.setVisible(False)  # Escondido no início
        layout.addWidget(self.campo_extra)

        self.setLayout(layout)

    def verificar_opcao(self):
        """Mostra o campo de texto se a opção 'Outra opção' for escolhida."""
        if self.combo.currentText() == "Outra opção":
            self.label_extra.setVisible(True)
            self.campo_extra.setVisible(True)
        else:
            self.label_extra.setVisible(False)
            self.campo_extra.setVisible(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    sys.exit(app.exec())
