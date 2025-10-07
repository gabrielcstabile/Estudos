-- Calcule:
-- Quantos produtos únicos tem  dentro do mesmo pedido?
-- Quantidade de peças vendidas por pedido?
-- Qual é o valor total vendido por produto?

SELECT
	distinct order_id,
	COUNT (order_id) OVER (PARTITION BY order_id) AS total_unique_products,
	SUM (quantity) OVER (PARTITION BY order_id) AS total_product_sales,
	SUM (unit_pricE * quantity) OVER (PARTITION BY order_id) AS total_sales
FROM order_details
ORDER BY order_id
	
	