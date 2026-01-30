
WITH orders AS (
    SELECT * FROM {{ ref('stg_orders') }}
),

users AS (
    SELECT * FROM {{ ref('stg_users') }}
)

SELECT 
    u.user_id,
    COUNT(*) AS total_orders
FROM orders o
JOIN users u
    ON o.user_id = u.user_id
GROUP BY u.user_id
ORDER BY total_orders DESC
