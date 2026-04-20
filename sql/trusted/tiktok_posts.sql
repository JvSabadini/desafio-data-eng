CREATE OR REPLACE VIEW trusted.tiktok_posts AS
SELECT 
    item_id AS post_id,
    business_username AS account_name,
    'TikTok' AS platform,
    
    -- Aqui está a mágica: convertendo o BIGINT (Unix Timestamp) para TIMESTAMP
    to_timestamp(create_time) AS created_at,
    
    'VIDEO' AS content_type, 
    
    -- Tratando métricas
    CAST(COALESCE(likes, 0) AS NUMERIC) AS likes,
    CAST(COALESCE(comments, 0) AS NUMERIC) AS comments,
    CAST(COALESCE(shares, 0) AS NUMERIC) AS shares,
    CAST(COALESCE(video_views, 0) AS NUMERIC) AS views,
    CAST(COALESCE(reach, 0) AS NUMERIC) AS reach,
    CAST(COALESCE(favorites, 0) AS NUMERIC) AS saves

FROM raw.tiktok_posts
WHERE CAST(to_timestamp(create_time) AS DATE) BETWEEN '2025-03-01' AND '2026-03-31';