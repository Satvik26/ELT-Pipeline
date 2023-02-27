USE sys;
CREATE TABLE IF NOT EXISTS Orders (
OrderId int,
OrderStatus varchar(30),
LastUpdated timestamp
);

INSERT INTO sys.Orders VALUES
(1,'Backordered','2020-06-01 12:00:00'),
(1,'Shipped','2020-06-09 12:00:25'),
(2,'Shipped','2020-07-11 3:05:00'),
(1,'Shipped','2020-06-09 11:50:00'),
(3,'Shipped','2020-07-12 12:00:00');


SELECT * FROM sys.Orders;

SELECT *
FROM sys.Orders 
WHERE LastUpdated > (SELECT MAX(LastUpdated) FROM warehouse.Orders);