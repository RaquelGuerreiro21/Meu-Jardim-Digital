import sqlite3
from tkinter import Tk, Label, Entry, Button, messagebox

# Caminho do banco de dados
db_path = "C:/Users/Raquel/OneDrive/Documents/Meu Jardim Digital/eden/eden.sdb"

def inserir_dados_tkinter():
    """Insere os dados preenchidos na tabela 'plantas'."""
    nome_cientifico = entry_nome_cientifico.get()
    nome_popular = entry_nome_popular.get()
    data_plantio = entry_data_plantio.get()
    especie = entry_especie.get()
    necessidades = entry_necessidades.get()
    notas = entry_notas.get()

    if not all([nome_cientifico, nome_popular, data_plantio, especie, necessidades, notas]):
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        consulta = """
        INSERT INTO plantas (nome_cientifico, nome_popular, data_plantio, especie, necessidades, notas)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(consulta, (nome_cientifico, nome_popular, data_plantio, especie, necessidades, notas))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
        limpar_campos()
    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Erro ao inserir os dados: {e}")

def limpar_campos():
    """Limpa os campos de entrada."""
    entry_nome_cientifico.delete(0, 'end')
    entry_nome_popular.delete(0, 'end')
    entry_data_plantio.delete(0, 'end')
    entry_especie.delete(0, 'end')
    entry_necessidades.delete(0, 'end')
    entry_notas.delete(0, 'end')

# Interface gráfica
app = Tk()
app.title("Cadastro de Plantas")

# Labels e campos de entrada
Label(app, text="Nome Científico:").grid(row=0, column=0, padx=10, pady=5)
entry_nome_cientifico = Entry(app, width=30)
entry_nome_cientifico.grid(row=0, column=1, padx=10, pady=5)

Label(app, text="Nome Popular:").grid(row=1, column=0, padx=10, pady=5)
entry_nome_popular = Entry(app, width=30)
entry_nome_popular.grid(row=1, column=1, padx=10, pady=5)

Label(app, text="Data de Plantio (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=5)
entry_data_plantio = Entry(app, width=30)
entry_data_plantio.grid(row=2, column=1, padx=10, pady=5)

Label(app, text="Espécie:").grid(row=3, column=0, padx=10, pady=5)
entry_especie = Entry(app, width=30)
entry_especie.grid(row=3, column=1, padx=10, pady=5)

Label(app, text="Necessidades:").grid(row=4, column=0, padx=10, pady=5)
entry_necessidades = Entry(app, width=30)
entry_necessidades.grid(row=4, column=1, padx=10, pady=5)

Label(app, text="Notas:").grid(row=5, column=0, padx=10, pady=5)
entry_notas = Entry(app, width=30)
entry_notas.grid(row=5, column=1, padx=10, pady=5)

# Botões
Button(app, text="Salvar", command=inserir_dados_tkinter).grid(row=6, column=0, columnspan=2, pady=10)

# Executar aplicação
app.mainloop()
