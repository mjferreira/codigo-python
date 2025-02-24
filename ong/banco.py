import sqlite3
from sqlite3 import Error
import os

pastaApp=os.path.dirname(__file__)
caminho=pastaApp+"/ong.db"
print(caminho)
########## Criar Conexão
def ConexaoBanco():
#    caminho="/home/marcelo/programacao/codigo-python/ong/ong.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

def criarTabela(conexao,sql):
    vcon=ConexaoBanco()
    try:
        c=vcon.cursor()
        c.execute(sql)
    except Error as ex:
        print(ex)
    finally:
        print("Tabela criada")
    vcon.close()

def atualizar(sql):
    try:
        vcon=ConexaoBanco()
        c=vcon.cursor()
        c.execute(sql)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)

def consultar(sql):
    vcon=ConexaoBanco()
    c=vcon.cursor()
    c.execute(sql)
    resultado=c.fetchall()
    vcon.close()
    return resultado


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
#vcon=ConexaoBanco()
#criarTabela(vcon,vsql)
#vcon.close()

# inserir(vcon,vsql)
# deletar(vcon,vsql)
# atualizar(vcon,vsql)
