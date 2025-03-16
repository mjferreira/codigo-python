from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch

def criar_relatorio():
    """Cria um relatório PDF formatado"""
    
    nome_pdf = "relatorio.pdf"
    pdf = canvas.Canvas(nome_pdf, pagesize=A4)
    pdf.setTitle("Relatório de Usuários")

    # Definir fontes e título
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(200, 800, "Relatório de Usuários")

    # Linha divisória
    pdf.setStrokeColor(colors.black)
    pdf.line(50, 790, 550, 790)

    # Dados fictícios
    usuarios = [
        {"id": 1, "nome": "Carlos Silva", "idade": 30, "email": "carlos@email.com"},
        {"id": 2, "nome": "Ana Souza", "idade": 25, "email": "ana@email.com"},
        {"id": 3, "nome": "Marcos Lima", "idade": 40, "email": "marcos@email.com"},
    ]

    # Cabeçalhos
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, 750, "ID")
    pdf.drawString(100, 750, "Nome")
    pdf.drawString(250, 750, "Idade")
    pdf.drawString(300, 750, "Email")

    # Linha divisória
    pdf.line(50, 740, 550, 740)

    # Adicionar os dados na tabela
    pdf.setFont("Helvetica", 12)
    y = 720
    for usuario in usuarios:
        pdf.drawString(50, y, str(usuario["id"]))
        pdf.drawString(100, y, usuario["nome"])
        pdf.drawString(250, y, str(usuario["idade"]))
        pdf.drawString(300, y, usuario["email"])
        y -= 20  # Pular linha

    # Salvar o PDF
    pdf.save()
    print(f"Relatório gerado: {nome_pdf}")

# Executar a função
criar_relatorio()
