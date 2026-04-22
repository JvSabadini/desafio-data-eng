README 
Desafio Engenharia de Dados - Retize
Pipeline de dados para consolidação de métricas do Instagram e TikTok, estruturado em arquitetura de medalhão.

Arquitetura de Dados
Camada Raw: Dados brutos carregados via Python (Pandas).
Camada Trusted: Padronização de colunas e correção de formatos
Camada Refined: Tabelas analíticas unificadas com cálculo de taxa de engajamento.

Tecnologias
Python 3.11 (Pandas, SQLAlchemy, Psycopg2)

Outras instalações
SQL-TOOLS
SQLTools PostgreSQL/Cockroach Driver

PostgreSQL (Docker)

SQL (Transformações e Consultas)

Como Executar
Subir o banco de dados: docker-compose up -d

Instalar dependências: pip install -r requirements.txt

Executar ingestão: python src/ingestion_raw.py

Executar transformações: python src/run_transformations.py

Lógica de Engajamento
A métrica foi calculada na tabela refined.fct_posts seguindo a fórmula:
((Likes + Comentários + Shares + Saves) / Visualizações) * 100

Consultas de Negócio
As respostas para as perguntas de negócio (melhor dia, pior plataforma, top conteúdos e formatos) estão disponíveis na pasta sql/queries/. Todos os scripts utilizam as tabelas finais da camada Refined para garantir a integridade dos resultados.
