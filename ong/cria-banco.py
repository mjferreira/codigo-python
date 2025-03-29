import sqlite3
from sqlite3 import Error
import banco

########## Criar tabela
vsql="""CREATE TABLE tb_pessoa1 (
    T_NOME          TEXT (60),
    T_RG            TEXT (11),
    T_CPF           TEXT (11)  PRIMARY KEY,
    T_MAE           TEXT (60),
    T_CPFMAE        TEXT (11),
    T_PAI           TEXT (60),
    T_CPFPAI        TEXT (11),
    N_BAIRRO        INTEGER    REFERENCES tb_bairro (N_ID),
    T_NIS           TEXT (11),
    T_FONE          TEXT (13),
    T_CEP           TEXT (8),
    T_GRAU_ENSINO   TEXT (15),
    T_ESCOLA        TEXT (60),
    T_SERIE_ANO     TEXT (15),
    T_TRABALHA      TEXT (3),
    T_RENDA         REAL (7),
    T_RECBENEFICIO  TEXT (3),
    T_NOMEBENEFICIO TEXT (20),
    T_MEDICACAO     TEXT (3),
    T_NOMEMEDICACAO TEXT (40),
    T_MORADIA       TEXT (10),
    T_VALOR_ALUGUEL REAL (7),
    T_PAREDES       TEXT (20),
    T_TELHADO       TEXT (20),
    T_PISO          TEXT (20),
    T_OBS           TEXT (400),
    T_ENDE          TEXT (60),
    T_DATA_INS      TEXT (19),
    T_DATA_MOD      TEXT (19) 
);"""

banco.criarTabela(vsql)
