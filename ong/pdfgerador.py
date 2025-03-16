import sys
import subprocess
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
)
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors

class PDFGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.largura_pagina, self.altura_pagina = A4

    def mp(self, mm):
        return mm/0.352777

    def centralizar_texto(self, pdf, texto, y, fonte="Helvetica-Bold", tamanho=16):
        """ Centraliza um texto horizontalmente no PDF """
        pdf.setFont(fonte, tamanho)

        # Calcula a posição X centralizada
        largura_texto = pdf.stringWidth(texto, fonte, tamanho)
        x = (self.largura_pagina - largura_texto) / 2

        # Desenha o texto na posição centralizada
        pdf.drawString(x, y, texto)

    def create_pdf(self):
        c = canvas.Canvas(self.filename, pagesize=A4)
        #Largura: 210 mm (milímetros) ou aproximadamente 8,27 polegadas.
        #Altura: 297 mm (milímetros) ou aproximadamente 11,69 polegadas.
        altura_coluna = 1 * 28.35  # Convertendo cm para pontos (1 cm = 28.35 pontos)
        
        # Desenhando o retângulo
        c.setFillColor(colors.lightblue)  # Cor de fundo cinza claro
        c.rect(self.mp(20), self.altura_pagina-self.mp(30), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo

        # Título
        c.setFillColor(colors.black)  # Cor de fundo cinza claro
        c.setFont("Helvetica-Bold", 14)\
        # Centraliza um título na parte superior
        self.centralizar_texto(c, "FICHA DE INSCRIÇÃO", self.altura_pagina-self.mp(25), tamanho=16)

        # Adicionar marca d'água
        c.saveState()
        c.setFont("Helvetica", 50)
        c.setFillColorRGB(0.7, 0.7, 0.7)  # Cor cinza
        c.drawCentredString(4 * inch, 5 * inch, "ONG Amazônia Viva")  # Adicione a marca d'água no centro
        c.restoreState()

        # Definindo as coordenadas da borda
        x1, y1 = self.mp(20), self.mp(20)  # Ponto inferior esquerdo
        x2, y2 = self.largura_pagina-x1, self.altura_pagina-y1  # Ponto superior direito
        
        # Desenhar a borda externa (linha dupla)
        c.setStrokeColorRGB(0, 0, 0)  # Cor da linha (preto)
        c.setLineWidth(2)  # Largura da linha
        c.rect(x1, y1, x2 - x1, y2 - y1, stroke=1, fill=0)  # Retângulo externo


        
        # Linhas de preenchimento
        c.setFont("Helvetica", 12)
        c.drawString(50, 700, "NOME:")
        c.line(100, 698, 500, 698)  # Linha para preenchimento

        c.drawString(50, 670, "CPF:")
        c.line(100, 668, 200, 668)  # Linha para preenchimento

        c.drawString(50, 640, "MATRÍCULA:")
        c.line(100, 638, 200, 638)  # Linha para preenchimento

        c.drawString(50, 610, "ENDEREÇO:")
        c.line(100, 608, 500, 608)  # Linha para preenchimento

        c.drawString(50, 580, "CIDADE:")
        c.line(100, 578, 200, 578)  # Linha para preenchimento

        c.drawString(50, 550, "ESTADO:")
        c.line(100, 548, 200, 548)  # Linha para preenchimento

        c.drawString(50, 520, "CEP:")
        c.line(100, 518, 200, 518)  # Linha para preenchimento

        c.drawString(50, 490, "TELEFONE:")
        c.line(100, 488, 200, 488)  # Linha para preenchimento

        # Instruções adicionais
        c.setFont("Helvetica", 10)
        c.drawString(50, 450, "INSTRUÇÕES:")
        c.drawString(50, 430, "1. Preencha todos os campos.")
        c.drawString(50, 415, "2. Entregue o formulário na secretaria.")
        c.save()

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gerador de PDF")
        self.setGeometry(100, 100, 300, 200)

        self.button_generate = QPushButton("Gerar PDF e Imprimir")
        self.button_generate.clicked.connect(self.generate_pdf)

        layout = QVBoxLayout()
        layout.addWidget(self.button_generate)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def generate_pdf(self):
        filename = "output.pdf"
        pdf_generator = PDFGenerator(filename)
        pdf_generator.create_pdf()

        # Abrir o PDF gerado
        self.open_pdf(filename)

    def open_pdf(self, filename):
        try:
            # Tenta abrir o PDF com o visualizador padrão
            subprocess.run(['xdg-open', filename])
        except Exception as e:
            print(f"Erro ao abrir o PDF: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())