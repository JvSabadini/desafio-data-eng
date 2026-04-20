import os
from sqlalchemy import create_engine, text


DATABASE_URI = 'postgresql+psycopg2://retize_user:retize_password@localhost:5432/retize_db'
engine = create_engine(DATABASE_URI)

def executar_pasta_sql(nome_da_pasta):
    """Lê e executa todos os arquivos .sql de uma pasta específica."""
    print(f"\n--- Iniciando transformações na pasta: {nome_da_pasta} ---")
    
    if not os.path.exists(nome_da_pasta):
        print(f"Erro: A pasta '{nome_da_pasta}' não existe!")
        return
    arquivos = sorted([f for f in os.listdir(nome_da_pasta) if f.endswith('.sql')])
    
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(nome_da_pasta, arquivo)
        print(f"Executando: {arquivo}...")
        
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                query_sql = f.read()
            
            with engine.connect() as conexao:
                conexao.execute(text(query_sql))
                conexao.commit()
            print(f"Sucesso: {arquivo}!")
            
        except Exception as e:
            print(f"Erro ao rodar {arquivo}: {e}")

if __name__ == "__main__":

    executar_pasta_sql('sql/trusted')
    executar_pasta_sql('sql/refined')
    
    print("\n Todas as transformações foram concluídas com sucesso!")