USE world71;

/* Q1 */

/* Need to fix to use the JOIN keyword explicitly */

SELECT 
    Name, Population
FROM
    City c,
    CountryLanguage l
WHERE
    c.CountryCode = l.CountryCode
        AND Language = 'English'
        AND isOfficial = 'T';

/* Q2 */

SELECT 
    ci.Name, ci.Population,
	ci.Population/co.Population*100 AS percentPopulation,
	co.Name, co.Population
FROM
    City ci JOIN Country co 
	ON ci.CountryCode = co.Code
ORDER BY percentPopulation DESC;


USE classicmodels71;

/* Q3 */ 

/* assume that 'full details of all orders' does not include the product codes, lines, etc,
as I have to get the total payment for each order, summing the payments for each product */
/* assume that 'order payment' is derived from multiplying unit price by quantity, and is not gotten from the 'payments' table*/

SELECT *, customerNumber AS customer FROM (
SELECT 
	c.customerNumber, c.customerName, 
	o.orderNumber, o.orderDate, o.requiredDate, o.shippedDate, o.status, o.comments,
	SUM(od.quantityOrdered*od.priceEach) AS orderPayment
FROM customers c
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
GROUP BY o.orderNumber
) details
WHERE (SELECT MIN(orderPayment) FROM details WHERE customerNumber=customer) > 
(SELECT MAX(orderPayment) FROM details WHERE customerName = 'Signal Gift Stores');


/* no */

/* Join the customers, orders, and payments tables */

SELECT c.customerName, c.customerNumber, o.*, p.amount AS amount FROM customers c
JOIN orders o USING (customerNumber)
JOIN payments p USING (customerNumber)
WHERE amount > 
(SELECT MAX(ps.amount) AS signalAmount FROM customers cs JOIN payments ps USING (customerNumber)
WHERE customerName = 'Signal Gift Stores');

/* solution has LEFT JOIN */

/* Q4 */

SELECT customerNumber, customerName, contactLastName, contactFirstName 
FROM customers
WHERE customerNumber NOT IN (SELECT customerNumber FROM orders);

/* Or check if: orderNumber is NULL*/