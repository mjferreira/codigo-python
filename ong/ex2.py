import sqlite3
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# Conectar ao banco de dados SQLite
db_filename = "banco.db"  # Nome do banco de dados
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

# Criar a tabela se não existir (exemplo)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL,
        nis TEXT NOT NULL
    )
""")

# Inserir dados fictícios (apague essa parte caso já tenha dados no banco)
cursor.executemany("INSERT INTO pessoas (nome, cpf, nis) VALUES (?, ?, ?)", [
    ("João da Silva", "123.456.789-00", "12345678900"),
    ("Maria Souza", "987.654.321-00", "98765432100"),
    ("Carlos Oliveira", "111.222.333-44", "11122233344"),
])
conn.commit()

# Buscar os dados do banco
cursor.execute("SELECT nome, cpf, nis FROM pessoas")
dados = cursor.fetchall()
conn.close()  # Fechar conexão

# Gerar o relatório PDF
pdf_filename = "relatorio_presenca.pdf"

def gerar_relatorio():
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    largura, altura = A4

    # Definir título do relatório
    c.setFont("Helvetica-Bold", 14)
    c.drawString(200, altura - 50, "Relatório de Presença")

    # Cabeçalho da tabela
    x_start = 50
    y_start = altura - 100
    col_widths = [200, 150, 150, 200]  # Largura das colunas

    # Criar cabeçalho
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x_start, y_start, "Nome")
    c.drawString(x_start + col_widths[0], y_start, "CPF")
    c.drawString(x_start + col_widths[0] + col_widths[1], y_start, "NIS")
    c.drawString(x_start + col_widths[0] + col_widths[1] + col_widths[2], y_start, "Assinatura")

    # Linha horizontal abaixo do cabeçalho
    c.setStrokeColor(colors.black)
    c.line(x_start, y_start - 5, x_start + sum(col_widths), y_start - 5)

    # Listar os dados
    c.setFont("Helvetica", 10)
    y = y_start - 20
    for nome, cpf, nis in dados:
        if y < 50:  # Se chegar ao fim da página, cria uma nova
            c.showPage()
            c.setFont("Helvetica", 10)
            y = altura - 50
        
        c.drawString(x_start, y, nome)
        c.drawString(x_start + col_widths[0], y, cpf)
        c.drawString(x_start + col_widths[0] + col_widths[1], y, nis)
        c.line(x_start + col_widths[0] + col_widths[1] + col_widths[2], y + 5, x_start + sum(col_widths), y + 5)  # Linha para assinatura

        y -= 20  # Pular para a próxima linha

    # Salvar e fechar o PDF
    c.save()
    print(f"Relatório gerado: {pdf_filename}")

# Executar a função
gerar_relatorio()
