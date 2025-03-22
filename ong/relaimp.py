import sys, os
import subprocess
import banco
import configparser
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
)
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors

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
caminho_pdf = config['ambiente']['caminho_pdf']
caminho_icones = config['ambiente']['caminho_icones']
altura_coluna = 0.7 * 28.35  # Convertendo cm para pontos (1 cm = 28.35 pontos)
incremento = 7

class PDFGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.largura_pagina, self.altura_pagina = A4

    def mp(self, mm):
        return mm/0.352777

    def cabecalho(self, pdf):
        pdf.drawImage(caminho_icones+"/logo.png",self.mp(100), self.altura_pagina-self.mp(15),self.mp(10),self.mp(10))
        self.imprimir_texto(pdf, nome_fantasia, self.altura_pagina-self.mp(20), tamanho=8, posicao=0)   

    def pagina1_vazia(self, pdf):
       # Definindo as coordenadas da borda
        x1, y1 = self.mp(20), self.mp(30)  # Ponto inferior esquerdo
        x2, y2 = self.largura_pagina-x1, self.altura_pagina-y1  # Ponto superior direito
        # Desenhar a borda externa (linha dupla)
        pdf.setStrokeColorRGB(0, 0, 0)  # Cor da linha (preto)
        pdf.setLineWidth(1)  # Largura da linha
        pdf.rect(x1, y1, x2 - x1, y2 - y1, stroke=1, fill=0)  # Retângulo externo
        #Largura: 210 mm (milímetros) ou aproximadamente 8,27 polegadas.
        #Altura: 297 mm (milímetros) ou aproximadamente 11,69 polegadas.
   
        pdf.setLineWidth(1)  # Largura da linha
        
        linha=30+incremento      
        self.imprimir_linha_tabela(pdf, "FICHA DE INSCRIÇÃO", linha, fonte="Helvetica-Bold", tamanho=12, posicao=0, fundo=colors.lightgrey)
        # Desenhando o retângulo
        # pdf.setFillColor(colors.lightgrey)  # Cor de fundo cinza claro
        #pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        #pdf.setFillColor(colors.black) 
        #self.imprimir_texto(pdf, "FICHA DE INSCRIÇÃO", self.altura_pagina-self.mp(linha-2), tamanho=12, posicao=0)
        
        linha+=incremento
        self.imprimir_linha_tabela(pdf, "Data de Requerimento:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.largura_pagina-(2*self.mp(20)), fundo=colors.white)
        #pdf.setFillColor(colors.white)  
        #pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        #pdf.setFillColor(colors.black) 
        #self.imprimir_texto(pdf, "Data de Requerimento:", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(22))
            
        linha+=incremento
        #pdf.setFillColor(colors.lightgrey)  # Cor de fundo cinza claro
        #pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        #pdf.setFillColor(colors.black)  # Cor de fundo cinza claro
        #self.imprimir_texto(pdf, "IDENTIFICAÇÃO", self.altura_pagina-self.mp(linha-2), tamanho=12, posicao=0)  
        # self.imprimir_texto(pdf, "IDENTIFICAÇÃO", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(22))
        self.imprimir_linha_tabela(pdf, "IDENTIFICAÇÃO", linha, fonte="Helvetica-Bold", tamanho=12, posicao=0, fundo=colors.lightgrey)
        
        linha+=incremento
        #pdf.setFillColor(colors.white)  
        #pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        #pdf.setFillColor(colors.black) 
        #self.imprimir_texto(pdf, "NOME:", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(22))
        self.imprimir_linha_tabela(pdf, "NOME:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.largura_pagina-(2*self.mp(20)), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "RG:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(55), fundo=colors.white)
        self.imprimir_linha_tabela(pdf, "CPF:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(75), largura_coluna = self.mp(55), fundo=colors.white)
        self.imprimir_linha_tabela(pdf, "FONE:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(130), largura_coluna = self.mp(60), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "ENDEREÇO:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        
        linha+=incremento
        self.imprimir_linha_tabela(pdf, "BAIRRO:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(110), fundo=colors.white)
        self.imprimir_linha_tabela(pdf, "CEP:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(130), largura_coluna = self.mp(60), fundo=colors.white)
  
        linha+=incremento
        self.imprimir_linha_tabela(pdf, "MÃE:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(110), fundo=colors.white)
        self.imprimir_linha_tabela(pdf, "CPF:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(130), largura_coluna = self.mp(60), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "PAI:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(110), fundo=colors.white)
        self.imprimir_linha_tabela(pdf, "CPF:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(130), largura_coluna = self.mp(60), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "NIS:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "ESCOLARIDADE", linha, fonte="Helvetica-Bold", tamanho=12, posicao=0, fundo=colors.lightgrey)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "GRAU DE ENSINO: (   ) ANALFABELTO   (   ) ENS. FUNDA  (   ) ENS. MÉDIO  (   ) ENS. SUPERIOR", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "EM CASAO DE ESTUDANTE:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "ESCOLA:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "SÉRIE/ANO:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "RENDA", linha, fonte="Helvetica-Bold", tamanho=12, posicao=0, fundo=colors.lightgrey)
 
        linha+=incremento
        self.imprimir_linha_tabela(pdf, "TRABALHA: (   ) SIM  (   ) NÃO", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(105), fundo=colors.white)
        self.imprimir_linha_tabela(pdf, "RENDA FAMILIAR: R$", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(105), largura_coluna = self.mp(85), fundo=colors.white)
       
        linha+=incremento
        self.imprimir_linha_tabela(pdf, "RECEBE BENEFÍCIO: (   ) SIM  (   ) NÃO", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        
        linha+=incremento
        self.imprimir_linha_tabela(pdf, "SE SIM, QUAL: (   ) BPC  (   ) BOLSA FAMÍLIA  (   ) APOSENTADORIA", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
 
        linha+=incremento
        self.imprimir_linha_tabela(pdf, "OUTROS:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
 
        linha+=incremento
        self.imprimir_linha_tabela(pdf, "INFORMAÇÕES PESSOAIS", linha, fonte="Helvetica-Bold", tamanho=12, posicao=0, fundo=colors.lightgrey)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "FAZ USO DE MEDICAÇÃO: (   ) SIM  (   ) NÃO    SE, SIM, QUAL:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

        linha+=2*incremento
        self.imprimir_linha_tabela(pdf, "COMPOSIÇÃO FAMILIAR", linha, fonte="Helvetica-Bold", tamanho=12, posicao=0, fundo=colors.lightgrey)
   
        linha+=incremento
        self.imprimir_linha_tabela(pdf, "Nome:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(70), fundo=colors.white)
        self.imprimir_linha_tabela(pdf, "Parentesco:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(90), largura_coluna = self.mp(25), fundo=colors.white)
        self.imprimir_linha_tabela(pdf, "Estuda/Trabalha - Local:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(115), largura_coluna = self.mp(75), fundo=colors.white)

        for i in range(7):
            linha+=incremento
            self.imprimir_linha_tabela(pdf, "", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(70), fundo=colors.white)
            self.imprimir_linha_tabela(pdf, "", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(90), largura_coluna = self.mp(25), fundo=colors.white)
            self.imprimir_linha_tabela(pdf, "", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(115), largura_coluna = self.mp(75), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "SITUAÇÃO DE MORADIAS", linha, fonte="Helvetica-Bold", tamanho=12, posicao=0, fundo=colors.lightgrey)
     
        linha+=incremento
        self.imprimir_linha_tabela(pdf, "CASA: (   )PRÓPRIA  (   )ALUGADA  (   )CEDIDA", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

    def pagina2_vazia(self,pdf):
        x1, y1 = self.mp(20), self.mp(141)  # Ponto inferior esquerdo
        x2, y2 = self.largura_pagina-x1, self.altura_pagina-self.mp(30) # Ponto superior direito
        # Desenhar a borda externa (linha dupla)
        pdf.setStrokeColorRGB(0, 0, 0)  # Cor da linha (preto)
        pdf.setLineWidth(1)  # Largura da linha
        pdf.rect(x1, y1, x2 - x1, y2 - y1, stroke=1, fill=0)  # Retângulo externo

        linha=30+incremento
        self.imprimir_linha_tabela(pdf, "SE ALUGUEL, QUANTO: R$", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        
        linha+=incremento
        self.imprimir_linha_tabela(pdf, "PAREDES: (   )ALVENÁRIA  (   )MADEIRA                   OUTROS:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "TELHADO: (   )BRASILIT  (   )GALVANIZADA  (   )BARRO     OUTROS:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "PISO: (   )BATIDO  (   )CERÂMICA  (   )PORCELANATO       OUTROS:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

        linha+=2*incremento
        self.imprimir_linha_tabela(pdf, "OBSERVAÇÕES PROFISSIONAL ENTREVISTADOR", linha, fonte="Helvetica-Bold", tamanho=12, posicao=0, fundo=colors.lightgrey)
        
        for i in range(12):
            linha+=incremento
            self.imprimir_linha_tabela(pdf, "", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

        self.imprimir_texto(pdf, "___________________________________________", self.mp(105), tamanho=8, posicao=0)  
        self.imprimir_texto(pdf, "Assinatura e Carimbo", self.mp(100), tamanho=8, posicao=0)  


    def pagina1(self, pdf, resultado, resultado_composicao):
       # Definindo as coordenadas da borda
        x1, y1 = self.mp(20), self.mp(30)  # Ponto inferior esquerdo
        x2, y2 = self.largura_pagina-x1, self.altura_pagina-y1  # Ponto superior direito
        # Desenhar a borda externa (linha dupla)
        pdf.setStrokeColorRGB(0, 0, 0)  # Cor da linha (preto)
        pdf.setLineWidth(1)  # Largura da linha
        pdf.rect(x1, y1, x2 - x1, y2 - y1, stroke=1, fill=0)  # Retângulo externo
        #Largura: 210 mm (milímetros) ou aproximadamente 8,27 polegadas.
        #Altura: 297 mm (milímetros) ou aproximadamente 11,69 polegadas.
   
        pdf.setLineWidth(1)  # Largura da linha
     
        linha=30+incremento      
        self.imprimir_linha_tabela(pdf, "FICHA DE INSCRIÇÃO", linha, fonte="Helvetica-Bold", tamanho=12, posicao=0, fundo=colors.lightgrey)
        # Desenhando o retângulo
        # pdf.setFillColor(colors.lightgrey)  # Cor de fundo cinza claro
        #pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        #pdf.setFillColor(colors.black) 
        #self.imprimir_texto(pdf, "FICHA DE INSCRIÇÃO", self.altura_pagina-self.mp(linha-2), tamanho=12, posicao=0)
        
        linha+=incremento
        self.imprimir_linha_tabela(pdf, "Data de Requerimento: "+resultado[0][27], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.largura_pagina-(2*self.mp(20)), fundo=colors.white)
        #pdf.setFillColor(colors.white)  
        #pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        #pdf.setFillColor(colors.black) 
        #self.imprimir_texto(pdf, "Data de Requerimento:", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(22))
            
        linha+=incremento
        #pdf.setFillColor(colors.lightgrey)  # Cor de fundo cinza claro
        #pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        #pdf.setFillColor(colors.black)  # Cor de fundo cinza claro
        #self.imprimir_texto(pdf, "IDENTIFICAÇÃO", self.altura_pagina-self.mp(linha-2), tamanho=12, posicao=0)  
        # self.imprimir_texto(pdf, "IDENTIFICAÇÃO", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(22))
        self.imprimir_linha_tabela(pdf, "IDENTIFICAÇÃO", linha, fonte="Helvetica-Bold", tamanho=12, posicao=0, fundo=colors.lightgrey)
        
        linha+=incremento
        #pdf.setFillColor(colors.white)  
        #pdf.rect(self.mp(20), self.altura_pagina-self.mp(linha), self.largura_pagina-(2*self.mp(20)), altura_coluna, fill=1)  # Preencher o retângulo
        #pdf.setFillColor(colors.black) 
        #self.imprimir_texto(pdf, "NOME:", self.altura_pagina-self.mp(linha-2), fonte="Helvetica", tamanho=10, posicao=self.mp(22))
        self.imprimir_linha_tabela(pdf, "NOME: "+resultado[0][0], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.largura_pagina-(2*self.mp(20)), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "RG: "+resultado[0][1], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(55), fundo=colors.white)
        self.imprimir_linha_tabela(pdf, "CPF: "+resultado[0][2], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(75), largura_coluna = self.mp(55), fundo=colors.white)
        self.imprimir_linha_tabela(pdf, "FONE: "+resultado[0][9], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(130), largura_coluna = self.mp(60), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "ENDEREÇO: "+resultado[0][26], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        
        id_bairro=resultado[0][7]
        vsql="SELECT T_BAIRRO, N_ZONA FROM tb_bairro WHERE N_ID = "+ str(id_bairro)
        res_temp = banco.consultar(vsql)
        vbairro=[row[0] for row in res_temp]
        
        linha+=incremento
        self.imprimir_linha_tabela(pdf, "BAIRRO: "+vbairro[0], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(110), fundo=colors.white)
        self.imprimir_linha_tabela(pdf, "CEP: "+resultado[0][10], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(130), largura_coluna = self.mp(60), fundo=colors.white)
  
        linha+=incremento
        self.imprimir_linha_tabela(pdf, "MÃE: "+resultado[0][3], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(110), fundo=colors.white)
        self.imprimir_linha_tabela(pdf, "CPF: "+resultado[0][4], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(130), largura_coluna = self.mp(60), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "PAI: "+resultado[0][5], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(110), fundo=colors.white)
        self.imprimir_linha_tabela(pdf, "CPF: "+resultado[0][6], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(130), largura_coluna = self.mp(60), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "NIS: "+resultado[0][8], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "ESCOLARIDADE", linha, fonte="Helvetica-Bold", tamanho=12, posicao=0, fundo=colors.lightgrey)

        linha+=incremento
        if resultado[0][11] == "Analfabeto":
            self.imprimir_linha_tabela(pdf, "GRAU DE ENSINO: ( X ) ANALFABELTO   (   ) ENS. FUNDA  (   ) ENS. MÉDIO  (   ) ENS. SUPERIOR", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        elif resultado[0][11] == "Fundamental":
            self.imprimir_linha_tabela(pdf, "GRAU DE ENSINO: (   ) ANALFABELTO   ( X ) ENS. FUNDA  (   ) ENS. MÉDIO  (   ) ENS. SUPERIOR", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        elif resultado[0][11] == "Médio":
            self.imprimir_linha_tabela(pdf, "GRAU DE ENSINO: (   ) ANALFABELTO   (   ) ENS. FUNDA  ( X ) ENS. MÉDIO  (   ) ENS. SUPERIOR", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        elif resultado[0][11] == "Superior":
            self.imprimir_linha_tabela(pdf, "GRAU DE ENSINO: (   ) ANALFABELTO   (   ) ENS. FUNDA  (   ) ENS. MÉDIO  ( X ) ENS. SUPERIOR", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "EM CASAO DE ESTUDANTE:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "ESCOLA: "+resultado[0][12], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "SÉRIE/ANO: "+resultado[0][13], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "RENDA", linha, fonte="Helvetica-Bold", tamanho=12, posicao=0, fundo=colors.lightgrey)
 
        linha+=incremento
        if resultado[0][14] == "SIM":
            self.imprimir_linha_tabela(pdf, "TRABALHA: ( X ) SIM  (   ) NÃO", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(105), fundo=colors.white)
        else:
            self.imprimir_linha_tabela(pdf, "TRABALHA: (   ) SIM  ( X ) NÃO", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(105), fundo=colors.white)
            
        self.imprimir_linha_tabela(pdf, "RENDA FAMILIAR: R$ "+resultado[0][15], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(105), largura_coluna = self.mp(85), fundo=colors.white)
        
       
        linha+=incremento
        if resultado[0][16] == "SIM":
            self.imprimir_linha_tabela(pdf, "RECEBE BENEFÍCIO: ( X ) SIM  (   ) NÃO", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        else:    
            self.imprimir_linha_tabela(pdf, "RECEBE BENEFÍCIO: (   ) SIM  ( X ) NÃO", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)          

        linha+=incremento
        if resultado[0][16] == "NÃO": 
            self.imprimir_linha_tabela(pdf, "SE SIM, QUAL: (   ) BPC  (   ) BOLSA FAMÍLIA  (   ) APOSENTADORIA", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white) 
            linha+=incremento
            self.imprimir_linha_tabela(pdf, "OUTROS:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        elif resultado[0][17] == "BPC": 
            self.imprimir_linha_tabela(pdf, "SE SIM, QUAL: ( X ) BPC  (   ) BOLSA FAMÍLIA  (   ) APOSENTADORIA", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white) 
            linha+=incremento
            self.imprimir_linha_tabela(pdf, "OUTROS:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)           
        elif resultado[0][17] == "Bolsa Família":
            self.imprimir_linha_tabela(pdf, "SE SIM, QUAL: (   ) BPC  ( X ) BOLSA FAMÍLIA  (   ) APOSENTADORIA", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white) 
            linha+=incremento
            self.imprimir_linha_tabela(pdf, "OUTROS:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        elif resultado[0][17] == "Aponsentadoria":
            self.imprimir_linha_tabela(pdf, "SE SIM, QUAL: (   ) BPC  (   ) BOLSA FAMÍLIA  ( X ) APOSENTADORIA", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white) 
            linha+=incremento
            self.imprimir_linha_tabela(pdf, "OUTROS:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        else:
            self.imprimir_linha_tabela(pdf, "SE SIM, QUAL: (   ) BPC  (   ) BOLSA FAMÍLIA  (   ) APOSENTADORIA", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white) 
            linha+=incremento
            self.imprimir_linha_tabela(pdf, "OUTROS: "+resultado[0][17], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
 
        
 
        linha+=incremento
        self.imprimir_linha_tabela(pdf, "INFORMAÇÕES PESSOAIS", linha, fonte="Helvetica-Bold", tamanho=12, posicao=0, fundo=colors.lightgrey)

        linha+=incremento
        if resultado[0][18] == "NÃO":
            self.imprimir_linha_tabela(pdf, "FAZ USO DE MEDICAÇÃO: (   ) SIM  ( X ) NÃO    SE, SIM, QUAL:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        else:    
            self.imprimir_linha_tabela(pdf, "FAZ USO DE MEDICAÇÃO: ( X ) SIM  (   ) NÃO    SE, SIM, QUAL: "+resultado[0][19], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

        linha+=2*incremento
        self.imprimir_linha_tabela(pdf, "COMPOSIÇÃO FAMILIAR", linha, fonte="Helvetica-Bold", tamanho=12, posicao=0, fundo=colors.lightgrey)
   
        linha+=incremento
        self.imprimir_linha_tabela(pdf, "Nome:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(70), fundo=colors.white)
        self.imprimir_linha_tabela(pdf, "Parentesco:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(90), largura_coluna = self.mp(25), fundo=colors.white)
        self.imprimir_linha_tabela(pdf, "Estuda/Trabalha - Local:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(115), largura_coluna = self.mp(75), fundo=colors.white)

        vsql="SELECT T_NOME, T_PARENTESCO, T_ESCOLA_TRABALHO  FROM tb_composicao WHERE T_CPF ="+resultado[0][2]
        rows = banco.consultar(vsql)
        print(rows)
        # Adiciona os dados à tabela
        intervalo=7
        for row in rows:
            linha+=incremento
            self.imprimir_linha_tabela(pdf, row[0], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(70), fundo=colors.white)
            self.imprimir_linha_tabela(pdf, row[1], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(90), largura_coluna = self.mp(25), fundo=colors.white)
            self.imprimir_linha_tabela(pdf, row[2], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(115), largura_coluna = self.mp(75), fundo=colors.white)
            intervalo-=1
            if intervalo == 0:
                break
        
        for i in range(intervalo):
            linha+=incremento
            self.imprimir_linha_tabela(pdf, "", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(75), fundo=colors.white)
            self.imprimir_linha_tabela(pdf, "", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(90), largura_coluna = self.mp(25), fundo=colors.white)
            self.imprimir_linha_tabela(pdf, "", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(115), largura_coluna = self.mp(75), fundo=colors.white)

        linha+=incremento
        self.imprimir_linha_tabela(pdf, "SITUAÇÃO DE MORADIAS", linha, fonte="Helvetica-Bold", tamanho=12, posicao=0, fundo=colors.lightgrey)
     
        linha+=incremento
        if resultado[0][20] == "Própria":
            self.imprimir_linha_tabela(pdf, "CASA: ( X ) PRÓPRIA  (   ) ALUGADA  (   ) CEDIDA", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        elif resultado[0][20] == "Alugada": 
            self.imprimir_linha_tabela(pdf, "CASA: (   ) PRÓPRIA  ( X ) ALUGADA  (   ) CEDIDA", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        else:
            self.imprimir_linha_tabela(pdf, "CASA: (   ) PRÓPRIA  (   ) ALUGADA  ( X ) CEDIDA", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
    

    def pagina2(self,pdf, resultado, resultado_composicao):
        x1, y1 = self.mp(20), self.mp(141)  # Ponto inferior esquerdo
        x2, y2 = self.largura_pagina-x1, self.altura_pagina-self.mp(30) # Ponto superior direito
        # Desenhar a borda externa (linha dupla)
        pdf.setStrokeColorRGB(0, 0, 0)  # Cor da linha (preto)
        pdf.setLineWidth(1)  # Largura da linha
        pdf.rect(x1, y1, x2 - x1, y2 - y1, stroke=1, fill=0)  # Retângulo externo

        linha=30+incremento
        self.imprimir_linha_tabela(pdf, "SE ALUGUEL, QUANTO: R$ "+resultado[0][21], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        
        linha+=incremento
        if resultado[0][22] == "Alvenaria":
            self.imprimir_linha_tabela(pdf, "PAREDES: ( X ) ALVENARIA  (   ) MADEIRA                   OUTROS:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        elif resultado[0][22] == "Madeira":
            self.imprimir_linha_tabela(pdf, "PAREDES: (   ) ALVENARIA  ( X ) MADEIRA                   OUTROS:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        else:
            self.imprimir_linha_tabela(pdf, "PAREDES: (   ) ALVENARIA  (   ) MADEIRA                   OUTROS: "+resultado[0][22], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
  
        linha+=incremento
        if resultado[0][23] == "Brasilit":
            self.imprimir_linha_tabela(pdf, "TELHADO: ( X ) BRASILIT  (   ) GALVANIZADA  (   ) BARRO     OUTROS:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        elif resultado[0][23] == "Galvanizada":
            self.imprimir_linha_tabela(pdf, "TELHADO: (   ) BRASILIT  ( X ) GALVANIZADA  (   ) BARRO     OUTROS:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        elif resultado[0][23] == "Barro":
            self.imprimir_linha_tabela(pdf, "TELHADO: (   ) BRASILIT  (   ) GALVANIZADA  ( X ) BARRO     OUTROS:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        else:
            self.imprimir_linha_tabela(pdf, "TELHADO: (   ) BRASILIT  (   ) GALVANIZADA  (   ) BARRO     OUTROS: "+resultado[0][23], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

        linha+=incremento
        if resultado[0][24] == "Batido":
            self.imprimir_linha_tabela(pdf, "PISO: ( X ) BATIDO  (   ) CERÂMICA  (   ) PORCELANATO       OUTROS:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        elif resultado[0][24] == "Cerâmica":
            self.imprimir_linha_tabela(pdf, "PISO: (   ) BATIDO  ( X ) CERÂMICA  (   ) PORCELANATO       OUTROS:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        elif resultado[0][24] == "Porcelanato":
            self.imprimir_linha_tabela(pdf, "PISO: (   ) BATIDO  (   ) CERÂMICA  ( X ) PORCELANATO       OUTROS:", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)
        else:
            self.imprimir_linha_tabela(pdf, "PISO: (   ) BATIDO  (   ) CERÂMICA  (   ) PORCELANATO       OUTROS: "+resultado[0][24], linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

        linha+=2*incremento
        self.imprimir_linha_tabela(pdf, "OBSERVAÇÕES PROFISSIONAL ENTREVISTADOR", linha, fonte="Helvetica-Bold", tamanho=12, posicao=0, fundo=colors.lightgrey)
        
        linhaobs=linha+incremento

        for i in range(12):
            linha+=incremento
            self.imprimir_linha_tabela(pdf, "", linha, fonte="Helvetica", tamanho=10, posicao=self.mp(20), largura_coluna = self.mp(170), fundo=colors.white)

        x_position = self.mp(22)  # Margem esquerda
        y_position = self.altura_pagina-self.mp(linhaobs)+self.mp(2)  # Posição inicial (de cima para baixo)

        long_text = resultado[0][25]
        # Criando um bloco de texto
        text_object = pdf.beginText(x_position, y_position)
        text_object.setFont("Helvetica", 12)  
        text_object.setLeading(self.mp(7))  # Define o espaçamento entre as linhas (16 pontos)

        # Adiciona o texto ao objeto de texto
        for line in long_text.split("\n"):
            text_object.textLine(line)

        pdf.drawText(text_object)

        self.imprimir_texto(pdf, "___________________________________________", self.mp(105), tamanho=8, posicao=0)  
        self.imprimir_texto(pdf, "Assinatura e Carimbo", self.mp(100), tamanho=8, posicao=0)  


    def rodape(self, pdf):
        self.imprimir_texto(pdf, empresa+" - CNPJ:"+cnpj_empresa, self.mp(15), tamanho=8, posicao=0)   
        self.imprimir_texto(pdf, end_empresa, self.mp(10), tamanho=8, posicao=0)  
        self.imprimir_texto(pdf, "Telefone: "+fone_empresa+" E-mail:"+email_empresa, self.mp(5), tamanho=8, posicao=0) 

    def imprimir_linha_tabela(self, pdf, texto, y, fonte="Helvetica-Bold", tamanho=16, posicao=0, largura_coluna=0, fundo=colors.white):
        """ Centraliza um texto horizontalmente no PDF """
        pdf.setFillColor(fundo)    
        y1 =  self.altura_pagina-self.mp(y)
        y2 =  self.altura_pagina-self.mp(y-2)     
        if posicao == 0:
            # Calcula a posição X centralizada
            largura_texto = pdf.stringWidth(texto, fonte, tamanho)
            largura_coluna = self.largura_pagina-(2*self.mp(20))
            x = (self.largura_pagina - largura_texto) / 2
            posicao = self.mp(20)
        else:
            x = posicao+self.mp(2)
        
        pdf.rect(posicao, y1, largura_coluna, altura_coluna, fill=1)  # Preencher o retângulo                                               
        pdf.setFillColor(colors.black) 
        pdf.setFont(fonte, tamanho)   
        # Desenha o texto na posição centralizada
        pdf.drawString(x, y2, texto)     
       
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

    def create_pdf(self, resultado, resultado_composicao):
        c = canvas.Canvas(self.filename, pagesize=A4)
        self.cabecalho(c)
        self.pagina1(c, resultado, resultado_composicao)
        self.rodape(c)
        c.showPage()
        self.cabecalho(c)
        self.pagina2(c, resultado, resultado_composicao)
        self.rodape(c)
        c.save()