/* Division Example */

/* Get all Customers who ordered at least once from all of the following product lines: Vintage Cars, Motorcycles, Classic Cars
'Collectioner' customer statistics, market research */

/* R */
/*
SELECT c.customerNumber, p.productLine FROM customers c 
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
JOIN products p ON od.productCode = p.productCode ORDER BY customerNumber;
*/

/* S */
/*
SELECT productLine FROM productlines 
WHERE productLine IN ('Vintage Cars', 'Motorcycles', 'Classic Cars');
*/

/* T1 (C) */
/*
SELECT c.customerNumber FROM customers c 
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
JOIN products p ON od.productCode = p.productCode ORDER BY customerNumber;
*/

/* S * T1 cross AND difference */
SELECT r.customerNumber FROM 
(SELECT productLine FROM productlines 
WHERE productLine IN ('Vintage Cars', 'Motorcycles', 'Classic Cars')) s 
JOIN (SELECT c.customerNumber FROM customers c 
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
JOIN products p ON od.productCode = p.productCode) r
WHERE concat(s.productLine, r.customerNumber) NOT EXISTS 
(SELECT concat(c.customerNumber, p.productLine) FROM customers c 
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
JOIN products p ON od.productCode = p.productCode ORDER BY customerNumber);