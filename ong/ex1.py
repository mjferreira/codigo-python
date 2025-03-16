from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def criar_pdf():
    """Cria um PDF com exemplos de bordas em tabelas"""
    nome_pdf = "tabela_bordas.pdf"
    doc = SimpleDocTemplate(nome_pdf, pagesize=A4)
    elementos = []

    # Dados da tabela
    dados = [
        ["Tipo de Borda", "Exemplo"],
        ["Sem borda", "Texto 1"],
        ["Borda sólida", "Texto 2"],
        ["Apenas borda externa", "Texto 3"],
        ["Borda personalizada", "Texto 4"],
    ]

    # Criar tabela base
    tabela = Table(dados, colWidths=[200, 200])

    # Estilos de borda
    estilo = TableStyle([
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"),  # Negrito no cabeçalho
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),  # Fundo do cabeçalho
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),  # Cor do texto do cabeçalho
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),  # Centralizar texto
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),  # Alinhar verticalmente
        ("GRID", (0, 1), (-1, 1), 0, colors.white),  # Sem borda (linha 1)
        ("GRID", (0, 2), (-1, 2), 1, colors.black),  # Borda sólida (linha 2)
        ("BOX", (0, 3), (-1, 3), 2, colors.red),  # Apenas borda externa (linha 3)
        ("INNERGRID", (0, 4), (-1, 4), 1, colors.blue),  # Linhas internas em azul (linha 4)
        ("BOX", (0, 4), (-1, 4), 2, colors.green),  # Borda externa em verde (linha 4)
    ])

    tabela.setStyle(estilo)
    elementos.append(tabela)

    # Criar o PDF
    doc.build(elementos)
    print(f"PDF '{nome_pdf}' gerado com sucesso!")

# Gerar o PDF com bordas
criar_pdf()
