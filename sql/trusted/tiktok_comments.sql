CREATE OR REPLACE VIEW trusted.tiktok_comments AS
SELECT 
    comment_id,
    post_id,
    'TikTok' AS platform,
    CAST(comment_timestamp AS TIMESTAMP) AS created_at,
    LOWER(predicted_sentiment) AS sentiment
FROM raw.tiktok_comments;