from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QLabel, QButtonGroup


class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Seleção com QRadioButton")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Escolha uma opção:")

        # Criar os botões de opção
        self.radio1 = QRadioButton("Opção 1")
        self.radio2 = QRadioButton("Opção 2")
        self.radio3 = QRadioButton("Opção 3")

        # Criar um grupo para os botões (garante que apenas um seja selecionado)
        self.grupo = QButtonGroup(self)
        self.grupo.addButton(self.radio1)
        self.grupo.addButton(self.radio2)
        self.grupo.addButton(self.radio3)

        # Conectar os botões para atualizar o rótulo
        self.radio1.toggled.connect(self.atualizar_label)
        self.radio2.toggled.connect(self.atualizar_label)
        self.radio3.toggled.connect(self.atualizar_label)

        # Adicionar widgets ao layout
        layout.addWidget(self.label)
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.radio3)

        self.setLayout(layout)

    def atualizar_label(self):
        # Verifica qual botão está selecionado e atualiza o rótulo
        botao_selecionado = self.grupo.checkedButton()
        if botao_selecionado:
            self.label.setText(f"Selecionado: {botao_selecionado.text()}")

if __name__ == "__main__":
    app = QApplication([])
    janela = JanelaPrincipal()
    janela.show()
    app.exec()
