CREATE OR REPLACE VIEW trusted.instagram_posts AS
SELECT 
    m.id AS post_id,
    m.username AS account_name,
    'Instagram' AS platform,
    CAST(m.timestamp AS TIMESTAMP) AS created_at,
    m.media_product_type AS content_type,
    CAST(COALESCE(i.likes, m.like_count, 0) AS NUMERIC) AS likes,
    CAST(COALESCE(i.comments, m.comments_count, 0) AS NUMERIC) AS comments,
    CAST(COALESCE(i.shares, 0) AS NUMERIC) AS shares,
    CAST(COALESCE(i.views, 0) AS NUMERIC) AS views,
    CAST(COALESCE(i.reach, 0) AS NUMERIC) AS reach,
    CAST(COALESCE(i.saved, 0) AS NUMERIC) AS saves
FROM raw.instagram_media m
LEFT JOIN raw.instagram_media_insights i ON m.id = i.id
WHERE CAST(m.timestamp AS DATE) BETWEEN '2025-03-01' AND '2026-03-31';