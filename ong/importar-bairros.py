import sys
import sqlite3

# Caminho do arquivo texto (CSV)
arquivo_texto = sys.argv[1]

# Nome do banco de dados SQLite
banco_de_dados = 'ong.db'

# Conectando ao banco de dados SQLite (ou criando se não existir)
conn = sqlite3.connect(banco_de_dados)
cursor = conn.cursor()

# Função para importar dados do arquivo de texto para a tabela SQLite
def importar_dados(arquivo):
    with open(arquivo, 'r') as file:
        # Lê cada linha do arquivo
        for linha in file:
            # Supondo que os dados sejam separados por vírgula (formato CSV)
            dados = linha.strip().split(',')  # Separar os dados por vírgula
            # Inserir os dados na tabela
            cursor.execute('''
            INSERT INTO tb_bairro (N_ZONA, T_BAIRRO)
            VALUES (?, ?)
            ''', (dados[0], dados[1]))  # Insira os valores na tabela

    # Commit das alterações
    conn.commit()

# Chamar a função para importar os dados
importar_dados(arquivo_texto)

# Fechar a conexão com o banco de dados
conn.close()

print("Dados importados com sucesso!")
