from PyQt6.QtWidgets import (QApplication, QMainWindow, QScrollArea, QWidget, 
                            QLabel, QLineEdit, QPushButton)

class AbsoluteScrollForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulário com Scroll Absoluto")
        
        # Criar QScrollArea como widget central
        scroll_area = QScrollArea()
        self.setCentralWidget(scroll_area)
        scroll_area.setWidgetResizable(True)
        
        # Widget de conteúdo que terá posicionamento absoluto
        content_widget = QWidget()
        scroll_area.setWidget(content_widget)
        content_widget.setMinimumSize(800, 1200)  # Tamanho maior que a janela
        
        # Adicionar widgets com posicionamento absoluto
        label1 = QLabel("Nome:", content_widget)
        label1.move(20, 20)
        
        input1 = QLineEdit(content_widget)
        input1.move(120, 20)
        input1.resize(200, 25)
        
        label2 = QLabel("Endereço:", content_widget)
        label2.move(20, 60)
        
        input2 = QLineEdit(content_widget)
        input2.move(120, 60)
        input2.resize(300, 25)
        
        # Adicionar mais widgets em posições específicas...
        button = QPushButton("Enviar", content_widget)
        button.move(20, 500)
        button.resize(100, 30)

app = QApplication([])
window = AbsoluteScrollForm()
window.resize(400, 300)
window.show()
app.exec()