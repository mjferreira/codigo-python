from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def create_pdf_with_table(filename):
    c = canvas.Canvas(filename, pagesize=A4)

    # Definir as dimensões da tabela
    x = 100  # Posição x da tabela
    y = 700  # Posição y da tabela
    col_width = 150  # Largura de cada coluna
    row_height = 30   # Altura de cada linha

    # Desenhar cabeçalho da tabela
    headers = ["Coluna 1", "Coluna 2", "Coluna 3"]
    for i in range(len(headers)):
        c.rect(x + i * col_width, y, col_width, row_height)  # Moldura da célula
        c.drawString(x + i * col_width + 10, y + 7, headers[i])  # Texto do cabeçalho

    # Desenhar uma linha de dados
    data = ["Dado 1", "Dado 2", "Dado 3"]
    for i in range(len(data)):
        c.rect(x + i * col_width, y - row_height, col_width, row_height)  # Moldura da célula
        c.drawString(x + i * col_width + 10, y - row_height + 7, data[i])  # Texto da célula

    # Finalizar o PDF
    c.save()

if __name__ == "__main__":
    create_pdf_with_table("table_with_borders.pdf")