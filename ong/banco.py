import sqlite3
from sqlite3 import Error
import os, sys
import pyzipper

# Configurações
zip_filename = "banco.zip"  # Nome do arquivo ZIP
db_filename = "ong.db"           # Nome do banco de dados
zip_password = b"@0m0z9n10V1v0!"      # Senha do ZIP (deve estar em bytes)

BASE_DIR = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
caminho = os.path.join(BASE_DIR, "ong.db")

########## Criar Conexão
def ConexaoBanco():
#    caminho="/home/marcelo/programacao/codigo-python/ong/ong.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

def criarTabela(sql):
    extrair_banco()
    vcon=ConexaoBanco()
    try:
        c=vcon.cursor()
        c.execute(sql)
    except Error as ex:
        print(ex)
    finally:
        print("Tabela criada")
    vcon.close()
    compactar_banco()

def atualizar(sql):
    try:
        extrair_banco()
        vcon=ConexaoBanco()
        c=vcon.cursor()
        c.execute(sql)
        vcon.commit()
        vcon.close()
        compactar_banco()
    except Error as ex:
        print(ex)

def consultar(sql):
    extrair_banco()
    vcon=ConexaoBanco()
    c=vcon.cursor()
    c.execute(sql)
    resultado=c.fetchall()
    vcon.close()
    compactar_banco()
    return resultado


# 1️⃣ Descompactar o banco de dados com senha
def extrair_banco():
    if os.path.exists(db_filename):  # Remove o banco antigo, se existir
        os.remove(db_filename)
    
    with pyzipper.AESZipFile(zip_filename, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
        zipf.extract(db_filename, pwd=zip_password)  # Extrai com senha AES-256
#        print(f"Banco de dados '{db_filename}' extraído com sucesso!")

# 3️⃣ Compactar o banco de volta no ZIP com senha forte (AES-256)
def compactar_banco():
    with pyzipper.AESZipFile(zip_filename, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
        zipf.setpassword(zip_password)  # Define a senha AES-256
        zipf.write(db_filename)  # Adiciona o banco ao ZIP
#        print(f"Banco de dados '{db_filename}' compactado novamente com criptografia forte!")

    os.remove(db_filename)  # Remover o banco descompactado por segurança




#vsql= """INSERT INTO tb_pessoa1
#          (T_NOME, [N_RG], [N_CPF], T_MAE, [N_CPF-MAE], T_PAI, [N_CPF-PAI])
#           VALUES('teste',123456,12345678901,'Maria',123,'teste',123)
#      """

# vsql="DELETE FROM tb_pessoa1 WHERE N_ID=1"
# vsql= "UPDATE tb_pessoa1 SET T_NOME='Marcelo',N_CPF=12345678901,T_PAI='Manoel Valdenor' WHERE N_ID=2"

# vsql= "SELECT * FROM tb_pessoa1 WHERE N_ID=6"

# vsql="""CREATE TABLE tb_pessoa (
#            N_ID        INTEGER      PRIMARY KEY AUTOINCREMENT,
#            T_NOME      TEXT (60),
#            T_RG        TEXT (15),
#            T_CPF       TEXT (11),
#            T_MAE       TEXT (60),
#            T_CPFMAE   TEXT (11),
#            T_PAI       TEXT (60),
#            T_CPFPAI   TEXT (11)
#        );"""

#criarTabela(vsql)
#vcon.close()

# inserir(vsql)
# atualizar(vsql)
