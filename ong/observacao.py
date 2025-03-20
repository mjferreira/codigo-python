from PyQt6.QtGui import QTextCursor
from PyQt6.QtWidgets import QDialog, QTextEdit, QPushButton, QVBoxLayout
import textwrap

class ObservacaoWindow(QDialog):
    def __init__(self, parent=None, texto_atual=""):
        super().__init__(parent)
        self.setWindowTitle("Observação")
        self.resize(400, 200)
        
        self.text_edit = QTextEdit()
        self.text_edit.setPlainText(texto_atual)
        self.text_edit.setPlaceholderText("Digite sua observação aqui...")

        self.btn_ok = QPushButton("OK")
        self.btn_ok.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.btn_ok)
        self.setLayout(layout)

        # Conecta a função ao evento de mudança de texto
        self.text_edit.textChanged.connect(self.limitar_texto)

    def get_text(self):
        """ Retorna o texto digitado, já limitado a 400 caracteres """
        text =  self.text_edit.toPlainText()[:400]
        formatted_text = textwrap.fill(text, width=80)
        return formatted_text
        

    def limitar_texto(self):
        """ Impede que o usuário digite mais de 400 caracteres """
        texto = self.text_edit.toPlainText()
        if len(texto) > 400:
            # Trunca o texto para 400 caracteres
            self.text_edit.blockSignals(True)  # Evita loop infinito de eventos
            self.text_edit.setPlainText(texto[:400])
            self.text_edit.blockSignals(False)

            # Move o cursor para o final do texto
            self.text_edit.moveCursor(QTextCursor.MoveOperation.End)