import sqlite3
import pyzipper
import os

# Configurações
zip_filename = "banco.zip"  # Nome do arquivo ZIP
db_filename = "ong.db"           # Nome do banco de dados
zip_password = b"@0m0z9n10V1v0!"      # Senha do ZIP (deve estar em bytes)

# 1️⃣ Descompactar o banco de dados com senha
def extrair_banco():
    if os.path.exists(db_filename):  # Remove o banco antigo, se existir
        os.remove(db_filename)
    
    with pyzipper.AESZipFile(zip_filename, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
        zipf.extract(db_filename, pwd=zip_password)  # Extrai com senha AES-256
        print(f"Banco de dados '{db_filename}' extraído com sucesso!")

# 2️⃣ Acessar e manipular o banco de dados
def acessar_banco():
    conn = sqlite3.connect(db_filename)  # Conectar ao SQLite
    cursor = conn.cursor()

    # Criar uma tabela de exemplo (se não existir)
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT)")
    
    # Inserir um usuário
    cursor.execute("INSERT INTO usuarios (nome) VALUES ('João')")
    conn.commit()
    
    # Ler os dados
    cursor.execute("SELECT * FROM tb_pessoa")
    print("Usuários cadastrados:", cursor.fetchall())

    conn.close()

# 3️⃣ Compactar o banco de volta no ZIP com senha forte (AES-256)
def compactar_banco():
    with pyzipper.AESZipFile(zip_filename, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
        zipf.setpassword(zip_password)  # Define a senha AES-256
        zipf.write(db_filename)  # Adiciona o banco ao ZIP
        print(f"Banco de dados '{db_filename}' compactado novamente com criptografia forte!")

    os.remove(db_filename)  # Remover o banco descompactado por segurança

# 🚀 Executar as funções

compactar_banco()
extrair_banco()
acessar_banco()
compactar_banco()
