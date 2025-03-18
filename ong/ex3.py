from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Nome do arquivo de saída
arquivo_pdf = "exemplo_quebra_pagina.pdf"

# Criando o documento PDF
c = canvas.Canvas(arquivo_pdf, pagesize=A4)

# Definição de texto para a primeira página
c.drawString(100, 750, "Este é um texto na primeira página.")

# Forçando a quebra de página
c.showPage()

# Definição de texto para a segunda página
c.drawString(100, 750, "Este é um texto na segunda página.")

# Salvando o PDF
c.save()

print(f"PDF '{arquivo_pdf}' criado com sucesso!")
