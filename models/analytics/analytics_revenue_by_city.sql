
WITH completed_orders AS (
    SELECT *
    FROM {{ ref('int_completed_orders') }}
)

SELECT 
    city,
    SUM(amount) AS revenue
FROM completed_orders
GROUP BY city
ORDER BY revenue DESC
