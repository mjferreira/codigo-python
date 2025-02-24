from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout

app = QApplication([])
window = QWidget()

line_edit = QLineEdit()

layout = QVBoxLayout()
layout.addWidget(line_edit)
window.setLayout(layout)
line_edit.setText("Digite aqui seu texto")

window.show()
app.exec()
