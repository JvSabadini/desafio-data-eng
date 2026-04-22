import os
import pandas as pd
from sqlalchemy import create_engine, text

DATABASE_URI = 'postgresql+psycopg2://retize_user:retize_password@localhost:5432/retize_db'
engine = create_engine(DATABASE_URI)

def carregar_raw():
    print("--- Preparando banco e limpando dados antigos ---")
    
    with engine.connect() as conexao:
        conexao.execute(text("DROP SCHEMA IF EXISTS raw CASCADE;"))
        conexao.execute(text("DROP SCHEMA IF EXISTS trusted CASCADE;"))
        conexao.execute(text("DROP SCHEMA IF EXISTS refined CASCADE;"))
        
        conexao.execute(text("CREATE SCHEMA raw;"))
        conexao.execute(text("CREATE SCHEMA trusted;"))
        conexao.execute(text("CREATE SCHEMA refined;"))
        conexao.commit()

    print("--- Iniciando carga na camada RAW ---")
    arquivos = {
        'instagram_comments.csv': 'instagram_comments',
        'instagram_media.csv': 'instagram_media',
        'instagram_media_insights.csv': 'instagram_media_insights',
        'tiktok_comments.csv': 'tiktok_comments',
        'tiktok_posts.csv': 'tiktok_posts'
    }

    for arquivo, tabela in arquivos.items():
        caminho = os.path.join('data', arquivo)
        if os.path.exists(caminho):
            print(f"Lendo {arquivo}...")
            df = pd.read_csv(caminho)
            df.to_sql(tabela, engine, schema='raw', if_exists='replace', index=False)
            print(f"OK: Tabela raw.{tabela} criada.")
        else:
            print(f"Erro: Arquivo {caminho} não encontrado. Verifique a pasta 'data'.")

if __name__ == "__main__":
    carregar_raw()
    print("Carga da camada RAW finalizada com sucesso!")
