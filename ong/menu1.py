import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog,
    QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox
)

class TableWindow(QDialog):
    def __init__(self, parent=None, data=None):
        super().__init__(parent)
        self.setWindowTitle("Tabela de Dados")
        self.resize(400, 300)

        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(["Nome", "Idade"])

        self.btn_add = QPushButton("Adicionar Linha")
        self.btn_remove = QPushButton("Remover Linha")
        self.btn_ok = QPushButton("OK")

        self.btn_add.clicked.connect(self.add_row)
        self.btn_remove.clicked.connect(self.remove_row)
        self.btn_ok.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_remove)
        layout.addLayout(btn_layout)
        layout.addWidget(self.btn_ok)
        self.setLayout(layout)

        # Preencher tabela com dados existentes
        if data:
            self.load_data(data)

    def add_row(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)

    def remove_row(self):
        selected = self.table.currentRow()
        if selected >= 0:
            self.table.removeRow(selected)

    def get_data(self):
        data = []
        for row in range(self.table.rowCount()):
            nome_item = self.table.item(row, 0)
            idade_item = self.table.item(row, 1)
            if nome_item and idade_item:
                data.append((nome_item.text(), idade_item.text()))
        return data

    def load_data(self, data):
        """ Preenche a tabela com os dados passados """
        for nome, idade in data:
            row_count = self.table.rowCount()
            self.table.insertRow(row_count)
            self.table.setItem(row_count, 0, QTableWidgetItem(nome))
            self.table.setItem(row_count, 1, QTableWidgetItem(idade))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
        self.resize(300, 200)

        self.btn_open_table = QPushButton("Abrir Tabela")
        self.btn_save_db = QPushButton("Salvar no Banco")

        self.btn_open_table.clicked.connect(self.open_table)
        self.btn_save_db.clicked.connect(self.save_to_db)

        layout = QVBoxLayout()
        layout.addWidget(self.btn_open_table)
        layout.addWidget(self.btn_save_db)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.data = []
        self.init_db()

    def open_table(self):
        dialog = TableWindow(self, self.data)  # Passa os dados existentes
        if dialog.exec():
            self.data = dialog.get_data()  # Atualiza os dados

    def save_to_db(self):
        if not self.data:
            QMessageBox.warning(self, "Aviso", "Nenhum dado para salvar!")
            return
        conn = sqlite3.connect("dados.db")
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", self.data)
        conn.commit()
        conn.close()
        QMessageBox.information(self, "Sucesso", "Dados salvos no banco!")
        self.data = []

    def init_db(self):
        conn = sqlite3.connect("dados.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                idade INTEGER
            )
        """)
        conn.commit()
        conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
