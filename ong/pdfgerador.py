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
altura_coluna = 0.8 * 28.35  # Convertendo cm para pontos (1 cm = 28.35 pontos)


class PDFGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.largura_pagina, self.altura_pagina = A4

    def mp(self, mm):
        return mm/0.352777

    def cabecalho(self, pdf):
        pdf.drawImage(pastaApp+"/logo.png",self.mp(101), self.altura_pagina-self.mp(11),self.mp(8),self.mp(8))
        self.imprimir_texto(pdf, nome_fantasia, self.altura_pagina-self.mp(15), tamanho=8, posicao=0)   

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
   
        pdf.setLineWidth(1)  # Largura da linha
        
        linha=28
        
        #self.imprimir_linha_tabela(pdf, "FICHA DE INSCRIÇÃO", self.altura_pagina-self.mp(linha), fonte="Helvetica-Bold", tamanho=12, posicao=0, fundo=colors.lightgrey)
        # Desenhando o retângulo
        pdf.setFillColor(colors.lightgrey)  # Cor de fundo cinza claro
        pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        self.imprimir_texto(pdf, "FICHA DE INSCRIÇÃO", self.altura_pagina-self.mp(linha-2), tamanho=12, posicao=0)
        
        linha+=8
        # self.imprimir_linha_tabela(pdf, "Data de Requerimento:", self.altura_pagina-self.mp(linha), fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.largura_pagina-(2*self.mp(20)), fundo=colors.white)
        pdf.setFillColor(colors.white)  
        pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        self.imprimir_texto(pdf, "Data de Requerimento:", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(22))
            
        linha+=8
        pdf.setFillColor(colors.lightgrey)  # Cor de fundo cinza claro
        pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black)  # Cor de fundo cinza claro
        self.imprimir_texto(pdf, "IDENTIFICAÇÃO", self.altura_pagina-self.mp(linha-2), tamanho=12, posicao=0)  
        # self.imprimir_texto(pdf, "IDENTIFICAÇÃO", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(22))
        # self.imprimir_linha_tabela(pdf, "IDENTIFICAÇÃO", self.altura_pagina-self.mp(linha-2), fonte="Helvetica-Bold", tamanho=12, posicao=0, fundo=colors.lightgrey)
        
        linha+=8
        pdf.setFillColor(colors.white)  
        pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        self.imprimir_texto(pdf, "NOME:", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(22))

        linha+=8
        pdf.setFillColor(colors.white)  
        pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.mp(55), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        self.imprimir_texto(pdf, "RG:", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(22))

        pdf.setFillColor(colors.white)  
        pdf.rect(self.mp(75), self.altura_pagina-self.mp(linha), self.mp(55), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        self.imprimir_texto(pdf, "CPF:", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(77))

        pdf.setFillColor(colors.white)  
        pdf.rect(self.mp(130), self.altura_pagina-self.mp(linha), self.mp(60), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        self.imprimir_texto(pdf, "FONE:", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(132))

        linha+=8
        pdf.setFillColor(colors.white)  
        pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        self.imprimir_texto(pdf, "ENDEREÇO:", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(22))
        
        
        linha+=8
        pdf.setFillColor(colors.white)  
        pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        self.imprimir_texto(pdf, "BAIRRO:", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(22))
        
        pdf.setFillColor(colors.white)  
        pdf.rect(self.mp(130), self.altura_pagina-self.mp(linha), self.mp(60), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        self.imprimir_texto(pdf, "CEP:", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(132))
        
        linha+=8
        pdf.setFillColor(colors.white)  
        pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        self.imprimir_texto(pdf, "MÃE:", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(22))
        
        pdf.setFillColor(colors.white)  
        pdf.rect(self.mp(130), self.altura_pagina-self.mp(linha), self.mp(60), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        self.imprimir_texto(pdf, "CPF:", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(132))   
        
        linha+=8
        pdf.setFillColor(colors.white)  
        pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        self.imprimir_texto(pdf, "PAI:", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(22))
        
        pdf.setFillColor(colors.white)  
        pdf.rect(self.mp(130), self.altura_pagina-self.mp(linha), self.mp(60), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        self.imprimir_texto(pdf, "CPF:", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(132))
 
        linha+=8
        pdf.setFillColor(colors.white)  
        pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        self.imprimir_texto(pdf, "NIS:", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(22))        
        
        linha+=8
        pdf.setFillColor(colors.lightgrey)  # Cor de fundo cinza claro
        pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black)  # Cor de fundo cinza claro
        self.imprimir_texto(pdf, "ESCOLARIDADE", self.altura_pagina-self.mp(linha-2), tamanho=12, posicao=0)  
        
        linha+=8
        pdf.setFillColor(colors.white)  
        pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        pdf.setFillColor(colors.black) 
        self.imprimir_texto(pdf, "GRAU DE ENSINO: (  ) ANALFABELTO   (  ) ENS. FUNDA  (  ) ENS. MÉDIO  (  ) ENS. SUPERIOR", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(22))  

        # Linhas de preenchimento
        # cpdf.setFont("Helvetica", 12)
        # pdf.drawString(50, 700, "NOME:")
        # pdf.line(100, 698, 500, 698)  # Linha para preenchimento


    def rodape(self, pdf):
        self.imprimir_texto(pdf, empresa+" - CNPJ:"+cnpj_empresa, self.mp(15), tamanho=8, posicao=0)   
        self.imprimir_texto(pdf, end_empresa, self.mp(10), tamanho=8, posicao=0)  
        self.imprimir_texto(pdf, "Telefone: "+fone_empresa+" E-mail:"+email_empresa, self.mp(5), tamanho=8, posicao=0) 

    def imprimir_linha_tabela(self, pdf, texto, y, fonte="Helvetica-Bold", tamanho=16, posicao=0, largura_coluna=0, fundo=colors.white):
        """ Centraliza um texto horizontalmente no PDF """
        pdf.setFillColor(fundo)          
        if posicao == 0:
            # Calcula a posição X centralizada
            largura_texto = pdf.stringWidth(texto, fonte, tamanho)
            largura_coluna = self.largura_pagina-(2*self.mp(20))
            x = (self.largura_pagina - largura_texto) / 2
            posicao = self.mp(20)
        else:
            x = posicao+2
        
        pdf.rect(posicao, y, largura_coluna, altura_coluna, fill=1)  # Preencher o retângulo                                               
        pdf.setFillColor(colors.black) 
        pdf.setFont(fonte, tamanho)   
        # Desenha o texto na posição centralizada
        pdf.drawString(x, y, texto)       
       
    def imprimir_texto(self, pdf, texto, y, fonte="Helvetica-Bold", tamanho=16, posicao=0):
        """ Centraliza um texto horizontalmente no PDF """      
        if posicao == 0:
            # Calcula a posição X centralizada
            largura_texto = pdf.stringWidth(texto, fonte, tamanho)
            x = (self.largura_pagina - largura_texto) / 2
        else:
            x = posicao
        
        pdf.setFont(fonte, tamanho)   
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