import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QVBoxLayout,
    QWidget, QPushButton, QComboBox
)

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabela de Parentesco")
        self.setGeometry(100, 100, 600, 400)

        self.unique_options = ["Esposo(a)", "Pai", "Mãe"]
        self.repeatable_options = [
            "AVô(á)", "Filho(a)", "Enteado(a)", "Cunhado(a)",
            "Genro", "Sogro(a)", "Nora", "Tio(a)", "Sobrinho(a)", "Primo(a)"
        ]

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Nome", "Parentesco", "Local"])
        
        self.add_button = QPushButton("Adicionar")
        self.add_button.clicked.connect(self.add_row)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.add_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Armazenar opções únicas escolhidas
        self.chosen_unique_options = []

    def add_row(self):
        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)

        # Criar QComboBox para a coluna de parentesco
        combo_box = QComboBox()
        available_options = self.get_available_options()
        combo_box.addItems(available_options)

        combo_box.currentTextChanged.connect(self.update_options)

        # Adicionar o QComboBox à tabela
        self.table_widget.setCellWidget(row_position, 1, combo_box)

    def get_available_options(self):
        options = self.unique_options.copy()
        options = list(set(options) - set(self.chosen_unique_options))
        return options + self.repeatable_options

    def update_options(self):
        current_combo_box = self.sender()
        chosen_option = current_combo_box.currentText()

        if chosen_option in self.unique_options:
            if chosen_option not in self.chosen_unique_options:
                self.chosen_unique_options.append(chosen_option)

        # Atualizar todos os QComboBox na tabela
        self.update_all_combo_boxes()

    def update_all_combo_boxes(self):
        for row in range(self.table_widget.rowCount()):
            combo_box = self.table_widget.cellWidget(row, 1)
            if combo_box:
                available_options = self.get_available_options()
                combo_box.clear()
                combo_box.addItems(available_options)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())