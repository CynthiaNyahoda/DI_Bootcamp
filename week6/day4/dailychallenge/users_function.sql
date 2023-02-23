CREATE FUNCTION get_total_price_for_user_order(user_id INTEGER, order_id INTEGER) RETURNS DECIMAL
BEGIN
  DECLARE total_price DECIMAL DEFAULT 0;
  SELECT SUM(price) INTO total_price 
  FROM items 
  INNER JOIN product_orders ON items.order_id = product_orders.order_id 
  WHERE items.order_id = order_id AND product_orders.customer_id = user_id;
  RETURN total_price;
END;
