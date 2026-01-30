WITH orders AS (
    SELECT * FROM {{ ref('stg_orders') }}
),

users AS (
    SELECT * FROM {{ ref('stg_users') }}
),

payments AS (
    SELECT * FROM {{ ref('stg_payments') }}
)

SELECT
    o.order_id,
    o.order_date,
    o.amount,
    o.status AS order_status,
    u.user_id,
    u.city,
    p.payment_method,
    p.payment_status

FROM orders o
JOIN users u
    ON o.user_id = u.user_id

JOIN payments p
    ON o.order_id = p.order_id

WHERE o.status = 'refunded'
  AND p.payment_status = 'failed'
