CREATE TABLE IF NOT EXISTS refined.fct_posts AS
WITH uniao_plataformas AS (
    SELECT * FROM trusted.instagram_posts
    UNION ALL
    SELECT * FROM trusted.tiktok_posts
)
SELECT 
    *,
 
    ROUND(
        CAST(((likes + comments + shares + saves) / NULLIF(views, 0)) * 100 AS NUMERIC), 
        2
    ) AS engagement_rate
FROM uniao_plataformas;


--Esta tabela une as duas redes sociais em um modelo único
