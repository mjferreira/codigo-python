import sqlite3
from sqlite3 import Error
import banco


vcon=ConexaoBanco()

########## Criar tabela
vsql="""CREATE TABLE tb_pessoa2 (
            N_ID        INTEGER      PRIMARY KEY AUTOINCREMENT,
            T_NOME      TEXT (60),
            N_RG        TEXT (15),
            N_CPF       TEXT (11),
            T_MAE       TEXT (60),
            [N_CPF-MAE] TEXT (11),
            T_PAI       TEXT (60),
            [N_CPF-PAI] TEXT (11)
        );"""

criarTabela(vcon,vsql)

vcon.close()
