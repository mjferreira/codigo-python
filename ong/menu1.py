import banco, sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout, QLabel

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Seleção de Bairro e Zona")
        self.setGeometry(100, 100, 350, 200)

        # Layout principal
        layout = QVBoxLayout()

        # Rótulo para a zona
        self.label_zona = QLabel("Selecione a Zona:")
        layout.addWidget(self.label_zona)

        # ComboBox para zonas
        self.combo_zona = QComboBox()
        self.combo_zona.currentIndexChanged.connect(self.atualizar_bairros)
        layout.addWidget(self.combo_zona)

        # Rótulo para o bairro
        self.label_bairro = QLabel("Selecione o Bairro:")
        layout.addWidget(self.label_bairro)

        # ComboBox para bairros
        self.combo_bairro = QComboBox()
        layout.addWidget(self.combo_bairro)

        # Carregar dados do banco
        self.carregar_zonas()

        # Configura o layout
        self.setLayout(layout)

    def carregar_zonas(self):
        vsql="SELECT T_ZONA FROM tb_zona ORDER BY T_ZONA"
        zonas=[row[0] for row in banco.consultar(vsql)]
        print(zonas)
        self.combo_zona.addItems(zonas)
        self.atualizar_bairros()  # Atualizar bairros da primeira zona carregada

    def atualizar_bairros(self):
        zona_selecionada = self.combo_zona.currentText()
        #cursor.execute("SELECT N_ID FROM tb_zona WHERE T_ZONA = ?", (zona_selecionada,))
        #vsql="SELECT N_ID FROM tb_zona WHERE T_ZONA = ?", (zona_selecionada,))
        vsql="SELECT N_ID FROM tb_zona WHERE T_ZONA = " + '"' + str(zona_selecionada)+ '"'
        print(vsql)
        zona_id=[row[0] for row in banco.consultar(vsql)]
        print(zona_id)
        vsql="SELECT T_BAIRRO FROM tb_bairro WHERE N_ZONA = "+ str(zona_id[0])
        bairros = [row[0] for row in banco.consultar(vsql)]
        print(bairros)
        self.combo_bairro.clear()
        self.combo_bairro.addItems(bairros)

if __name__ == "__main__":
    app = QApplication([])

    janela = JanelaPrincipal()
    janela.show()

    app.exec()
