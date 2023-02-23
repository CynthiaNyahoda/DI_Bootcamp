CREATE TABLE product_orders (
  order_id INTEGER PRIMARY KEY,
  order_date DATE,
  customer_name VARCHAR(255),
  total_price DECIMAL
);

CREATE TABLE items (
  item_id INTEGER PRIMARY KEY,
  order_id INTEGER,
  item_name VARCHAR(255),
  price DECIMAL,
  FOREIGN KEY (order_id) REFERENCES product_orders(order_id)
);
