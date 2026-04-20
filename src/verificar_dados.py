import pandas as pd
from sqlalchemy import create_engine

DATABASE_URI = 'postgresql+psycopg2://retize_user:retize_password@localhost:5432/retize_db'
engine = create_engine(DATABASE_URI)

# Podes mudar a query para o que quiseres testar
query = "SELECT * FROM refined.fct_posts LIMIT 10;"

df = pd.read_sql(query, engine)
print(df)