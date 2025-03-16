from PyQt6.QtWidgets import QVBoxLayout, QWidget, QPushButton, QLineEdit, QHBoxLayout, QMessageBox, QTableWidget
from PyQt6.QtWidgets import QTableWidgetItem, QComboBox, QSizePolicy, QDialog, QTextEdit
#from PyQt6.QtGui import QAction, QIcon, QTextCursor
#from PyQt6.QtCore import QSize

class TableWindow(QDialog):
    def __init__(self, parent=None, data=None):
        super().__init__(parent)

        self.setWindowTitle("Composição Familiar")
        self.resize(720, 400)
        # Criando a tabela
        self.tabela_composicao = QTableWidget(0, 3)  # Inicia com 0 linhas e 3 colunas
        self.tabela_composicao.setHorizontalHeaderLabels(["Nome", "Parentesco", "Escola/Local de Trabalho"])
        self.tabela_composicao.setColumnWidth(0, 200)
        self.tabela_composicao.setColumnWidth(1, 100)
        self.tabela_composicao.setColumnWidth(2, 395)


        self.botao_add = QPushButton("Adicionar")
        self.botao_add.clicked.connect(self.adiciona_composicao)
        self.botao_remove = QPushButton("Remover")
        self.botao_remove.clicked.connect(self.remove_composicao)
        self.btn_ok = QPushButton("OK")
        self.btn_ok.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.tabela_composicao)
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.botao_add)
        btn_layout.addWidget(self.botao_remove)
        layout.addLayout(btn_layout)
        layout.addWidget(self.btn_ok)
        self.setLayout(layout)

        # Preencher tabela com dados existentes
        if data:
            self.load_data(data)

    def adiciona_composicao(self, nome="", parentesco="Filho(a)", local=""):
        """Adiciona uma nova linha com valores opcionais"""
        row_position = self.tabela_composicao.rowCount()
        self.tabela_composicao.insertRow(row_position)
        self.tabela_composicao.setItem(row_position, 0, QTableWidgetItem(nome))
        self.tabela_composicao.setItem(row_position, 2, QTableWidgetItem(local))
        combo = QComboBox()
        combo.addItems(["Esposo(a)","Pai", "Mãe", "Filho(a)", "Avô(ó)","Sobrinho(a)","Enteado(a)","Tio(a)", "Gênro", "Nora", "Primo(a)"])
        combo.setCurrentText(parentesco)
        self.tabela_composicao.setCellWidget(row_position, 1, combo)

    def remove_composicao(self):
        """Remove a linha selecionada"""
        selected = self.tabela_composicao.currentRow()
        if selected >= 0:
            self.tabela_composicao.removeRow(selected)


    def get_data(self):
        data = []
        for row in range(self.tabela_composicao.rowCount()):
            nome_item = self.tabela_composicao.item(row, 0)
            # parentesco_item = self.tabela_composicao.item(row, 1)
            vparentesco_widget = self.tabela_composicao.cellWidget(row, 1)  # Obtém o QComboBox
            parentesco_item = vparentesco_widget.currentText() if vparentesco_widget else ""
            local_item = self.tabela_composicao.item(row,2)
            data.append((nome_item.text(), parentesco_item, local_item.text()))
        return data

    def load_data(self, data):
        """ Preenche a tabela com os dados passados """
        for nome, parentesco, local in data:
            row_count = self.tabela_composicao.rowCount()
            self.tabela_composicao.insertRow(row_count)
            self.tabela_composicao.setItem(row_count, 0, QTableWidgetItem(nome))
            # self.tabela_composicao.setItem(row_count, 1, QTableWidgetItem(parentesco))
            self.tabela_composicao.setItem(row_count, 2, QTableWidgetItem(local))
            combo = QComboBox()
            combo.addItems(["Esposo(a)","Pai", "Mãe", "Filho(a)", "Avô(ó)","Sobrinho(a)","Enteado(a)","Tio(a)"])
            combo.setCurrentText(parentesco)
            self.tabela_composicao.setCellWidget(row_count, 1, combo)