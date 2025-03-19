from reportlab.pdfgen import canvas

def criar_pdf_com_linhas():
    nome_pdf = "linhas_exemplo.pdf"
    pdf = canvas.Canvas(nome_pdf)

    # Linha horizontal
    pdf.line(50, 750, 550, 750)

    # Linha vertical
    pdf.line(300, 700, 300, 500)  # De (300,700) até (300,500)

    # Linha diagonal
    pdf.line(100, 400, 500, 200)  # De (100,400) até (500,200)

    # Adicionando textos explicativos
    pdf.drawString(50, 760, "Linha Horizontal")
    pdf.drawString(310, 710, "Linha Vertical")
    pdf.drawString(150, 410, "Linha Diagonal")

    # Salvar PDF
    pdf.save()
    print(f"PDF '{nome_pdf}' gerado com sucesso!")

# Criar PDF com diferentes tipos de linhas
criar_pdf_com_linhas()
