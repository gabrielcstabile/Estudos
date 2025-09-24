-- Exercício 1: Criar um relatório para todos os clientes de 1996 e seus clientes

SELECT *
FROM orders AS o
INNER JOIN customers AS c ON o.customer_id = c.customer_id
WHERE EXTRACT(YEAR FROM o.order_date) = 1996

-- Uma forma alternativa de executar esse SELECT utilizando o DATE_PART:
SELECT * 
FROM orders AS o
INNER JOIN customers AS c ON o.customer_id = c.customer_id
WHERE DATE_PART('YEAR', o.order_date) = 1996

-- Exercício 2: 
