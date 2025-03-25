import tkinter as tk
from tkinter import messagebox
import sqlite3

def formatar_moeda(valor):
    """Formata o valor como moeda brasileira (R$)"""
    try:
        valor = float(valor)
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except:
        return "R$ 0,00"

def validar_entrada(entrada):
    """Valida a entrada para aceitar apenas números e ponto decimal"""
    if entrada == "":
        return True
    try:
        # Remove formatação existente para validação
        valor = entrada.replace("R$", "").replace(".", "").replace(",", ".")
        float(valor)
        return True
    except ValueError:
        return False

def on_focus_out(event):
    """Formata o valor quando o campo perde o foco"""
    entrada = event.widget.get()
    if entrada:
        # Remove formatação existente
        valor = entrada.replace("R$", "").replace(".", "").replace(",", ".")
        try:
            valor_float = float(valor)
            event.widget.delete(0, tk.END)
            event.widget.insert(0, formatar_moeda(str(valor_float)))
        except ValueError:
            event.widget.delete(0, tk.END)
            event.widget.insert(0, "R$ 0,00")

def salvar_no_banco():
    """Salva o valor no banco de dados SQLite"""
    valor = entrada_valor.get()
    try:
        # Remove formatação e converte para float
        valor_float = float(valor.replace("R$", "").replace(".", "").replace(",", "."))
        
        # Conecta ao banco de dados
        conn = sqlite3.connect('financas.db')
        cursor = conn.cursor()
        
        # Cria a tabela se não existir
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            valor REAL NOT NULL,
            data TEXT DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Insere o valor
        cursor.execute("INSERT INTO transacoes (valor) VALUES (?)", (valor_float,))
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Sucesso", "Valor salvo com sucesso!")
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido!")

def recuperar_do_banco():
    """Recupera o último valor salvo no banco de dados"""
    try:
        conn = sqlite3.connect('financas.db')
        cursor = conn.cursor()
        cursor.execute("SELECT valor FROM transacoes ORDER BY id DESC LIMIT 1")
        resultado = cursor.fetchone()
        conn.close()
        
        if resultado:
            entrada_valor.delete(0, tk.END)
            entrada_valor.insert(0, formatar_moeda(str(resultado[0])))
            messagebox.showinfo("Recuperado", f"Último valor recuperado: {formatar_moeda(str(resultado[0]))}")
        else:
            messagebox.showinfo("Info", "Nenhum valor encontrado no banco de dados.")
    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Erro ao acessar banco de dados: {e}")

# Configuração da interface
root = tk.Tk()
root.title("Entrada de Valores Monetários")

tk.Label(root, text="Valor (R$):").pack(pady=5)

# Registra a função de validação
validacao = root.register(validar_entrada)

entrada_valor = tk.Entry(root, validate="key", validatecommand=(validacao, "%P"))
entrada_valor.pack(pady=5)
entrada_valor.bind("<FocusOut>", on_focus_out)

tk.Button(root, text="Salvar", command=salvar_no_banco).pack(pady=5)
tk.Button(root, text="Recuperar Último", command=recuperar_do_banco).pack(pady=5)

root.mainloop()