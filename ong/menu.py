import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QHBoxLayout, QComboBox
)

class EditableTable(QWidget):
    def __init__(self):
        super().__init__()

        # Configuração da Janela
        self.setWindowTitle("Tabela Interativa")
        self.setGeometry(100, 100, 500, 300)

        # Layout principal
        layout = QVBoxLayout(self)

        # Criando a tabela
        self.table = QTableWidget(0, 3)  # Inicia com 0 linhas e 3 colunas
        self.table.setHorizontalHeaderLabels(["Nome", "Parentesco", "Local"])
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 120)
        self.table.setColumnWidth(2, 150)
        layout.addWidget(self.table)

        # Botões de controle
        button_layout = QHBoxLayout()

        self.btn_add = QPushButton("Adicionar Linha")
        self.btn_add.clicked.connect(self.add_row)
        button_layout.addWidget(self.btn_add)

        self.btn_remove = QPushButton("Remover Linha")
        self.btn_remove.clicked.connect(self.remove_row)
        button_layout.addWidget(self.btn_remove)

        self.btn_save = QPushButton("Salvar no Banco")
        self.btn_save.clicked.connect(self.save_to_db)
        button_layout.addWidget(self.btn_save)

        layout.addLayout(button_layout)

        # Criar banco de dados e carregar dados
        self.create_database()
        self.load_data()

    def create_database(self):
        """Cria a tabela no banco de dados SQLite se não existir"""
        conn = sqlite3.connect("familia.db")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS parentesco (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT,
                            parentesco TEXT,
                            local TEXT)''')
        conn.commit()
        conn.close()

    def load_data(self):
        """Carrega os dados do banco de dados para a tabela"""
        conn = sqlite3.connect("familia.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nome, parentesco, local FROM parentesco")
        rows = cursor.fetchall()
        conn.close()

        # Adiciona os dados à tabela
        for row in rows:
            self.add_row(row[0], row[1], row[2])

    def add_row(self, nome="", parentesco="Pai", local=""):
        """Adiciona uma nova linha com valores opcionais"""
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        self.table.setItem(row_position, 0, QTableWidgetItem(nome))
        self.table.setItem(row_position, 2, QTableWidgetItem(local))

        combo = QComboBox()
        combo.addItems(["Pai", "Mãe", "Filho", "Avô", "Avó", "Sobrinho"])
        combo.setCurrentText(parentesco)
        self.table.setCellWidget(row_position, 1, combo)

    def remove_row(self):
        """Remove a linha selecionada"""
        selected = self.table.currentRow()
        if selected >= 0:
            self.table.removeRow(selected)

    def save_to_db(self):
        """Salva os dados da tabela no banco de dados"""
        conn = sqlite3.connect("familia.db")
        cursor = conn.cursor()

        # Limpa os dados antes de salvar para evitar duplicação
        cursor.execute("DELETE FROM parentesco")

        for row in range(self.table.rowCount()):
            nome = self.table.item(row, 0).text() if self.table.item(row, 0) else ""
            local = self.table.item(row, 2).text() if self.table.item(row, 2) else ""
            parentesco_widget = self.table.cellWidget(row, 1)  # Obtém o QComboBox
            parentesco = parentesco_widget.currentText() if parentesco_widget else ""

            cursor.execute("INSERT INTO parentesco (nome, parentesco, local) VALUES (?, ?, ?)",
                           (nome, parentesco, local))

        conn.commit()
        conn.close()
        print("Dados salvos com sucesso!")

# Executando a aplicação
app = QApplication([])
window = EditableTable()
window.show()
app.exec()
