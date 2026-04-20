
CREATE TABLE IF NOT EXISTS refined.fct_comments AS
SELECT * FROM trusted.instagram_comments
UNION ALL
SELECT * FROM trusted.tiktok_comments;


--Unifica todos os comentários e seus sentimentos já classificados.
