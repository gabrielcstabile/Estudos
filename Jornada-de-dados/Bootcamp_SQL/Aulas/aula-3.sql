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

-- Exercício 2: Criar um relatório que mostra o número de funcionários e clientes de cada cidade que tem funcionários
SELECT e.city AS cidade, 
       COUNT(DISTINCT e.employee_id) AS numero_de_funcionarios, 
       COUNT(DISTINCT c.customer_id) AS numero_de_clientes
FROM employees e 
LEFT JOIN customers c ON e.city = c.city
GROUP BY e.city
ORDER BY cidade;

-- Criar um relatório que mostra o número de funcionários e clientes de cada cidade que tem clientes
SELECT c.city AS cidade, 
       COUNT(DISTINCT c.customer_id) AS numero_de_clientes, 
       COUNT(DISTINCT e.employee_id) AS numero_de_funcionarios
FROM employees e 
RIGHT JOIN customers c ON e.city = c.city
GROUP BY c.city
ORDER BY cidade

-- Criar um relatório que mostra o número de funcionários e clientes de cada cidade
SELECT
	COALESCE(e.city, c.city) AS cidade,
	COUNT(DISTINCT e.employee_id) AS numero_de_funcionarios,
	COUNT(DISTINCT c.customer_id) AS numero_de_clientes
FROM employees e 
FULL JOIN customers c ON e.city = c.city
GROUP BY e.city, c.city
ORDER BY cidade


