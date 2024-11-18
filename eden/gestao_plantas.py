import sqlite3
from tkinter import Tk, Label, Entry, Button, messagebox, Toplevel, ttk

# Caminho do banco de dados
db_path = "C:/Users/Raquel/OneDrive/Documents/Meu Jardim Digital/eden/eden.sdb"

def conectar_banco():
    """Conecta ao banco de dados e retorna a conexão."""
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco: {e}")
        return None

def carregar_dados():
    """Carrega os dados da tabela 'plantas' para exibir na interface."""
    conn = conectar_banco()
    if not conn:
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM plantas")
        dados = cursor.fetchall()
        conn.close()
        return dados
    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Erro ao carregar os dados: {e}")
        return []

def atualizar_tabela(tree):
    """Atualiza os dados exibidos na tabela."""
    for item in tree.get_children():
        tree.delete(item)  # Remove todos os itens existentes

    dados = carregar_dados()
    for linha in dados:
        tree.insert("", "end", values=linha)

def abrir_tela_inserir(tree):
    """Abre a tela para inserir novos dados."""

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
            conn = conectar_banco()
            cursor = conn.cursor()
            consulta = """
            INSERT INTO plantas (nome_cientifico, nome_popular, data_plantio, especie, necessidades, notas)
            VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(consulta, (nome_cientifico, nome_popular, data_plantio, especie, necessidades, notas))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
            atualizar_tabela(tree)  # Atualiza a tabela principal
            janela_inserir.destroy()  # Fecha a janela de inserção
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Erro ao inserir os dados: {e}")

    # Janela para inserir dados
    janela_inserir = Toplevel()
    janela_inserir.title("Inserir Novo Registro")

    # Labels e campos de entrada
    Label(janela_inserir, text="Nome Científico:").grid(row=0, column=0, padx=10, pady=5)
    entry_nome_cientifico = Entry(janela_inserir, width=30)
    entry_nome_cientifico.grid(row=0, column=1, padx=10, pady=5)

    Label(janela_inserir, text="Nome Popular:").grid(row=1, column=0, padx=10, pady=5)
    entry_nome_popular = Entry(janela_inserir, width=30)
    entry_nome_popular.grid(row=1, column=1, padx=10, pady=5)

    Label(janela_inserir, text="Data de Plantio (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=5)
    entry_data_plantio = Entry(janela_inserir, width=30)
    entry_data_plantio.grid(row=2, column=1, padx=10, pady=5)

    Label(janela_inserir, text="Espécie:").grid(row=3, column=0, padx=10, pady=5)
    entry_especie = Entry(janela_inserir, width=30)
    entry_especie.grid(row=3, column=1, padx=10, pady=5)

    Label(janela_inserir, text="Necessidades:").grid(row=4, column=0, padx=10, pady=5)
    entry_necessidades = Entry(janela_inserir, width=30)
    entry_necessidades.grid(row=4, column=1, padx=10, pady=5)

    Label(janela_inserir, text="Notas:").grid(row=5, column=0, padx=10, pady=5)
    entry_notas = Entry(janela_inserir, width=30)
    entry_notas.grid(row=5, column=1, padx=10, pady=5)

    # Botão para salvar
    Button(janela_inserir, text="Salvar", command=inserir_dados_tkinter).grid(row=6, column=0, columnspan=2, pady=10)

def criar_interface():
    """Cria a interface principal."""
    app = Tk()
    app.title("Gestão de Plantas")

    # Tabela para exibir os dados
    tree = ttk.Treeview(app, columns=("ID", "Nome Científico", "Nome Popular", "Data de Plantio", "Espécie", "Necessidades", "Notas"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome Científico", text="Nome Científico")
    tree.heading("Nome Popular", text="Nome Popular")
    tree.heading("Data de Plantio", text="Data de Plantio")
    tree.heading("Espécie", text="Espécie")
    tree.heading("Necessidades", text="Necessidades")
    tree.heading("Notas", text="Notas")
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    # Botão para inserir novos dados
    Button(app, text="Inserir Dados", command=lambda: abrir_tela_inserir(tree)).pack(pady=10)

    # Atualizar tabela ao abrir
    atualizar_tabela(tree)

    app.mainloop()

# Executar a interface
criar_interface()
