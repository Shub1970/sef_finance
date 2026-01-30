
WITH completed_orders AS (
    SELECT *
    FROM {{ ref('int_completed_orders') }}
)

SELECT 
    order_date AS date,
    SUM(amount) AS revenue
FROM completed_orders
GROUP BY order_date 
ORDER BY order_date ASC
