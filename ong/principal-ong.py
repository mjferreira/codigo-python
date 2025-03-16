from PyQt6.QtWidgets import QApplication
import formulario, sys

app = QApplication(sys.argv)
janela = formulario.MinhaJanela()
janela.show()
app.exec()