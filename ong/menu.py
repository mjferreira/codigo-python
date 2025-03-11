import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget, QComboBox
)


class TabelaWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabela de Parentesco")
        self.resize(500, 300)

        # Criar widget principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Criar tabela com 3 colunas
        self.tabela = QTableWidget(5, 3)  # 5 linhas, 3 colunas
        self.tabela.setHorizontalHeaderLabels(["Nome", "Idade", "Parentesco"])

        # Lista de opções do ComboBox
        self.opcoes_unicas = ["Esposo", "Pai", "Mãe"]  # Essas opções podem ser escolhidas apenas uma vez
        self.opcoes_repetidas = ["Vô", "Vó", "Filho", "Enteado", "Cunhado", "Genro", "Sogro", "Nora"]  # Podem se repetir

        # Adicionar combobox na terceira coluna
        for row in range(self.tabela.rowCount()):
            self.adicionar_combobox(row)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.tabela)
        self.central_widget.setLayout(layout)

    def adicionar_combobox(self, row):
        """ Adiciona um QComboBox na terceira coluna de cada linha """
        combobox = QComboBox()
        combobox.addItems(["Nenhum"] + self.opcoes_unicas + self.opcoes_repetidas)  # Adiciona "Nenhum" como padrão
        combobox.currentIndexChanged.connect(lambda: self.atualizar_opcoes())
        self.tabela.setCellWidget(row, 2, combobox)

    def atualizar_opcoes(self):
        """ Remove das opções os itens únicos já selecionados em outras linhas """
        selecionados = set()

        # Percorre todas as linhas para capturar seleções de opções únicas
        for row in range(self.tabela.rowCount()):
            combobox = self.tabela.cellWidget(row, 2)
            if combobox:
                opcao = combobox.currentText()
                if opcao in self.opcoes_unicas:
                    selecionados.add(opcao)

        # Atualiza cada combobox removendo opções já escolhidas
        for row in range(self.tabela.rowCount()):
            combobox = self.tabela.cellWidget(row, 2)
            if combobox:
                opcao_atual = combobox.currentText()

                # 🔴 Desativar o sinal antes de modificar o combobox para evitar loop infinito
                combobox.blockSignals(True)
                combobox.clear()
                combobox.addItem("Nenhum")

                # Adiciona opções únicas apenas se não estiverem selecionadas em outra linha
                for opcao in self.opcoes_unicas:
                    if opcao not in selecionados or opcao == opcao_atual:
                        combobox.addItem(opcao)

                # Adiciona opções repetidas sempre disponíveis
                for opcao in self.opcoes_repetidas:
                    combobox.addItem(opcao)

                combobox.setCurrentText(opcao_atual)  # Mantém a opção selecionada
                
                # 🟢 Reativar o sinal após modificar o combobox
                combobox.blockSignals(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TabelaWidget()
    window.show()
    sys.exit(app.exec())
