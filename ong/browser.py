import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QMessageBox
import banco

class TabelaDados(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Browser de Tabela de Dados")
        self.setGeometry(100, 100, 800, 600)
        # self.setStyleSheet("background-color: lightgray; color black;")
        # Widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        # Layout principal
        layout = QVBoxLayout(self.central_widget)
        # Criar a tabela
        self.tabela = QTableWidget()
        layout.addWidget(self.tabela)
        self.tabela.setStyleSheet("background-color: blue;")
        # self.tabela.setStyleSheet("QTableWidget { background-color: lightblue; color: black; }")  # Define a cor do texto para azul

        self.carregar_dados()

    def carregar_dados(self):

        vsql = "SELECT N_ID, T_NOME, T_CPF FROM tb_pessoa order by T_NOME"
        dados = banco.consultar(vsql)

        self.tabela.setRowCount(len(dados))
        self.tabela.setColumnCount(5)  # ID, Nome, Idade, Ações
        self.tabela.setColumnWidth(0, 10)   # Coluna 0 com 50 pixels
        self.tabela.setColumnWidth(1, 400)  # Coluna 1 com 150 pixels
        self.tabela.setColumnWidth(2, 100)  # Coluna 2 com 100 pixels
        self.tabela.setHorizontalHeaderLabels(["ID", "Nome", "CPF", "Ações", ""])

        for linha_idx, linha in enumerate(dados):
            for col_idx, valor in enumerate(linha):
                self.tabela.setItem(linha_idx, col_idx, QTableWidgetItem(str(valor)))

            # Botão Editar
            botao_editar = QPushButton("Editar")
            botao_editar.setStyleSheet("background-color: green; color white;")
            botao_editar.clicked.connect(lambda _, row=linha[0]: self.editar_registro(row))
            self.tabela.setCellWidget(linha_idx, 3, botao_editar)

            # Botão Excluir
            botao_excluir = QPushButton("Excluir")
            botao_excluir.setStyleSheet("background-color: red; color white;")
            botao_excluir.clicked.connect(lambda _, row=linha[0]: self.excluir_registro(row))
            self.tabela.setCellWidget(linha_idx, 4, botao_excluir)

    def editar_registro(self, id_registro):
        """Simula edição de um registro"""
        QMessageBox.information(self, "Editar", f"Editar formulário de {id_registro}")

    def excluir_registro(self, id_registro):
        """Exclui um registro do banco de dados"""
        resposta = QMessageBox.question(self, "Excluir", f"Tem certeza que deseja excluir o {id_registro}?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if resposta == QMessageBox.StandardButton.Yes:
            vsql = "DELETE FROM tb_pessoa WHERE N_ID = "+ str(id_registro)
            banco.atualizar(vsql)
            self.carregar_dados()  # Recarregar os dados após a exclusão

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = TabelaDados()
    janela.show()
    sys.exit(app.exec())
