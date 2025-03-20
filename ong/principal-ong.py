from PyQt6.QtWidgets import QApplication
import formularioimp, sys

app = QApplication(sys.argv)
janela = formularioimp.MinhaJanela()
janela.show()
app.exec()