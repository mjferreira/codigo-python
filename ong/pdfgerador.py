import sys, os
import subprocess
import configparser
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
)
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors

caminho_pdf = "/home/marcelo/Downloads/"
pastaApp=os.path.dirname(__file__)
# Criar um objeto ConfigParser
config = configparser.ConfigParser()
# Ler o arquivo de configuração
config.read('config.ini')
nome_fantasia = config['configuracao']['nome_fantasia']
empresa = config['configuracao']['empresa']
end_empresa = config['configuracao']['end_empresa']
cnpj_empresa = config['configuracao']['cnpj_empresa']
email_empresa = config['configuracao']['email_empresa']
fone_empresa = config['configuracao']['fone_empresa']

class PDFGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.largura_pagina, self.altura_pagina = A4

    def mp(self, mm):
        return mm/0.352777

    def cabecalho(self, pdf):
        pdf.drawImage(pastaApp+"/logo.png",self.mp(101), self.altura_pagina-self.mp(11),self.mp(8),self.mp(8))
        self.centralizar_texto(pdf, nome_fantasia, self.altura_pagina-self.mp(15), tamanho=8)   

    def corpo(self, pdf):
       # Definindo as coordenadas da borda
        x1, y1 = self.mp(20), self.mp(20)  # Ponto inferior esquerdo
        x2, y2 = self.largura_pagina-x1, self.altura_pagina-y1  # Ponto superior direito
        # Desenhar a borda externa (linha dupla)
        pdf.setStrokeColorRGB(0, 0, 0)  # Cor da linha (preto)
        pdf.setLineWidth(1)  # Largura da linha
        pdf.rect(x1, y1, x2 - x1, y2 - y1, stroke=1, fill=0)  # Retângulo externo
        #Largura: 210 mm (milímetros) ou aproximadamente 8,27 polegadas.
        #Altura: 297 mm (milímetros) ou aproximadamente 11,69 polegadas.
        altura_coluna = 0.8 * 28.35  # Convertendo cm para pontos (1 cm = 28.35 pontos)
        
        pdf.setLineWidth(1)  # Largura da linha
        linha=25
        # Desenhando o retângulo
        pdf.setFillColor(colors.lightgrey)  # Cor de fundo cinza claro
        pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        self.centralizar_texto(pdf, "FICHA DE INSCRIÇÃO", self.altura_pagina-self.mp(linha-2), tamanho=12)

        linha+=8
        pdf.setFillColor(colors.white)  
        pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        pdf.setFont("Helvetica", 10)
        pdf.drawString(self.mp(22), self.altura_pagina-self.mp(linha-1), "Data de Requerimento:")

        linha+=8
        pdf.setFillColor(colors.lightgrey)  # Cor de fundo cinza claro
        pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black)  # Cor de fundo cinza claro
        self.centralizar_texto(pdf, "IDENTIFICAÇÃO", self.altura_pagina-self.mp(linha-2), tamanho=12)  

        linha+=8
        pdf.setFillColor(colors.white)  
        pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        pdf.setFont("Helvetica", 10)
        pdf.drawString(self.mp(22), self.altura_pagina-self.mp(linha-1), "NOME:")

        linha+=8
        pdf.setFillColor(colors.white)  
        pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.mp(55), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        pdf.setFont("Helvetica", 10)
        pdf.drawString(self.mp(22), self.altura_pagina-self.mp(linha-1), "RG:")

        pdf.setFillColor(colors.white)  
        pdf.rect(self.mp(75), self.altura_pagina-self.mp(linha), self.mp(55), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        pdf.setFont("Helvetica", 10)
        pdf.drawString(self.mp(77), self.altura_pagina-self.mp(linha-1), "CPF:")

        pdf.setFillColor(colors.white)  
        pdf.rect(self.mp(130), self.altura_pagina-self.mp(linha), self.mp(60), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        pdf.setFont("Helvetica", 10)
        pdf.drawString(self.mp(132), self.altura_pagina-self.mp(linha-1), "FONE:")       


        # Linhas de preenchimento
        # cpdf.setFont("Helvetica", 12)
        # pdf.drawString(50, 700, "NOME:")
        # pdf.line(100, 698, 500, 698)  # Linha para preenchimento


    def rodape(self, pdf):
        self.centralizar_texto(pdf, empresa+" - CNPJ:"+cnpj_empresa, self.mp(15), tamanho=8)   
        self.centralizar_texto(pdf, end_empresa, self.mp(10), tamanho=8)  
        self.centralizar_texto(pdf, "Telefone: "+fone_empresa+" E-mail:"+email_empresa, self.mp(5), tamanho=8) 

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
        self.cabecalho(c)
        self.corpo(c)
        self.rodape(c) 
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
        filename = caminho_pdf+"output.pdf"
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