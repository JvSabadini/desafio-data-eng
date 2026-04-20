CREATE OR REPLACE VIEW trusted.instagram_comments AS
SELECT 
    comment_id,
    post_id,
    'Instagram' AS platform,
    CAST(comment_timestamp AS TIMESTAMP) AS created_at,
    LOWER(predicted_sentiment) AS sentiment
FROM raw.instagram_comments;