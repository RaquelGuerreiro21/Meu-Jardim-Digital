import sqlite3

# Caminho do banco de dados
db_path = "C:/Users/Raquel/OneDrive/Documents/Meu Jardim Digital/eden/eden.sdb"

def conectar_banco():
    """Conecta ao banco de dados e retorna a conexão."""
    try:
        conn = sqlite3.connect(db_path)
        print("Conexão estabelecida com sucesso!")
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None

def inserir_dados(tabela, dados):
    """
    Insere dados na tabela especificada.
    - tabela: Nome da tabela.
    - dados: Dicionário com colunas e valores.
    """
    conn = conectar_banco()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        # Preparar consulta SQL dinâmica
        colunas = ', '.join(dados.keys())
        valores = ', '.join(['?'] * len(dados))
        consulta = f"INSERT INTO {tabela} ({colunas}) VALUES ({valores})"
        
        # Executar consulta
        cursor.execute(consulta, list(dados.values()))
        conn.commit()
        print(f"Dados inseridos na tabela '{tabela}' com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        conn.close()

# Exemplo de inserção na tabela 'plantas'
dados_plantas = {
    "nome_cientifico": "Ficus lyrata",
    "nome_popular": "Figueira-lira",
    "data_plantio": "2024-11-17",
    "especie": "Moraceae",
    "necessidades": "Luz indireta, rega moderada",
    "notas": "Pode crescer até 2m em ambiente interno"
}

inserir_dados("plantas", dados_plantas)
