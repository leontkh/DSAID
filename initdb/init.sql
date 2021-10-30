\c postgres_db

CREATE TABLE salespeople (
salesperson_id serial PRIMARY KEY,
name VARCHAR (50)
);

CREATE TABLE cars (
car_serial_no VARCHAR(50) PRIMARY KEY,
manufacturer VARCHAR(20),
model_name VARCHAR(15),
weight INTEGER,
price INTEGER
);

CREATE TABLE customers (
customer_id serial PRIMARY KEY,
customer_name VARCHAR (50),
customer_phone VARCHAR (15)
);

CREATE TABLE sales (
sale_id serial PRIMARY KEY,
sale_date DATE,
sale_time TIME,
salesperson_id INTEGER,
car_serial_no VARCHAR(50) UNIQUE,
customer_id INTEGER,
	CONSTRAINT fk_salespeople
		FOREIGN KEY(salesperson_id)
			REFERENCES salespeople(salesperson_id),
	CONSTRAINT fk_cars
		FOREIGN KEY(car_serial_no)
			REFERENCES cars(car_serial_no),
	CONSTRAINT fk_customers
		FOREIGN KEY(customer_id)
			REFERENCES customers(customer_id)
);