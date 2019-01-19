/* Lab 6 solutions (like in lab exam) */

/* Q1 */
USE sakila;

/* A */
SELECT title, release_year, description FROM film
WHERE rating='PG';

/* B */
SELECT f.title, c.name 
FROM film_category fc
JOIN film f ON fc.film_id=f.film_id
JOIN category c ON fc.category_id=c.category_id
WHERE c.name LIKE 'A%'
ORDER BY f.title ASC;


/* Q2 */
USE world71;

/* A */
SELECT 
ci.Name AS cityName, 
ci.Population AS cityPopulation, co.Name AS countryName,
ci.Population/co.Population*100 AS percentPopulation
FROM City ci JOIN Country co ON ci.CountryCode=co.Code
WHERE co.LifeExpectancy BETWEEN 50 AND 70
ORDER BY percentPopulation DESC;

/* B */
SELECT 
    Name, Population, Continent AS countryContinent
FROM
    Country
WHERE
    Population > (SELECT 
            AVG(Population) AS avgPopulation
        FROM
            Country
        GROUP BY Continent
        HAVING Continent=countryContinent)
ORDER BY Name;

/* Can also use WHERE - find average only for a continent (better performance?) */


/* Q3 */

USE classicmodels71;

/* A */

/* ------------- */

/* trying nested query*/

SELECT * FROM productlines;
SELECT * FROM products;
SELECT * FROM orders;
SELECT * FROM orderdetails;

SELECT pl.productLine, pl.textDescription FROM productlines pl;
SELECT productCode, productName, productLine FROM products
WHERE productLine='Motorcycles';
SELECT productCode, SUM(quantityOrdered) FROM orderdetails
WHERE productCode='S10_1678'
GROUP BY productCode;

SELECT pl.productLine, pl.textDescription, 
()
 AS quantity
FROM productlines pl;

SELECT
SUM(())
FROM products
WHERE productLine='Motorcycles'
GROUP BY productLine
 
SELECT SUM(quantityOrdered) AS productQuantity FROM orderdetails od
WHERE productCode=od.productCode
GROUP BY productCode

/* ------------- */

SELECT 
    pl.productLine, pl.textDescription, po.totalLineOrders
FROM
    productlines pl
        JOIN
    (SELECT 
        pr.productLine, SUM(od.totalOrdered) AS totalLineOrders
    FROM
        products pr
    JOIN (SELECT 
        SUM(quantityOrdered) AS totalOrdered, productCode
    FROM
        orderdetails od
    GROUP BY productCode) od ON pr.productCode = od.productCode
    GROUP BY pr.productLine) po ON pl.productLine = po.productLine
ORDER BY totalLineOrders DESC;


/* B */

/* My three parts */
/*
SELECT e.employeeNumber, e.lastName, e.firstName,
m.lastName AS managersLastName, m.firstName AS managersFirstName
FROM employees e
LEFT JOIN employees m ON e.reportsTo = m.employeeNumber;

SELECT salesRepEmployeeNumber, COUNT(customerNumber) AS numberOfCustomers FROM customers GROUP BY salesRepEmployeeNumber;

SELECT c.salesRepEmployeeNumber, SUM(od.quantityOrdered*od.priceEach) AS moneyThroughOrders
FROM customers c, orders o, orderdetails od
WHERE c.customerNumber = o.customerNumber AND o.orderNumber = od.orderNumber
GROUP BY c.salesRepEmployeeNumber;
*/

/* Attempts to join the three parts */
/* 
SELECT emp.lastName, emp.firstName, cus.numberOfCustomers, man.lastName AS managerLastName, man.firstName AS managerFirstName 
FROM 
	employees emp, 
	(SELECT salesRepEmployeeNumber, COUNT(customerNumber) AS numberOfCustomers FROM customers GROUP BY salesRepEmployeeNumber) cus,
	(SELECT m.employeeNumber, m.lastName, m.firstName FROM employees e LEFT JOIN employees m ON e.reportsTo = m.employeeNumber) man
WHERE emp.employeeNumber = cus.salesRepEmployeeNumber;
*/

/* Table with three joins */
/* 
SELECT * FROM orders o
JOIN orderdetails od ON o.orderNumber = od.orderNumber
JOIN customers c ON c.customerNumber = o.customerNumber
JOIN employees e ON e.employeeNumber = c.salesRepEmployeeNumber
LEFT JOIN employees m ON e.reportsTo = m.employeeNumber;
*/

/* final version (don't know how, but it gives the right numbers)
SELECT e.firstName, e.lastName, 
cn.numberOfCustomers, 
m.firstName AS managerFirstName, m.lastName AS managerLastName,
SUM(od.quantityOrdered*od.priceEach) AS moneyThroughOrders 
FROM orders o
JOIN orderdetails od ON o.orderNumber = od.orderNumber
JOIN customers c ON c.customerNumber = o.customerNumber
JOIN employees e ON e.employeeNumber = c.salesRepEmployeeNumber
LEFT JOIN employees m ON e.reportsTo = m.employeeNumber
JOIN (SELECT COUNT(customerNumber) AS numberOfCustomers, salesRepEmployeeNumber FROM customers GROUP BY salesRepEmployeeNumber) cn ON cn.salesRepEmployeeNumber = e.employeeNumber 
GROUP BY e.employeeNumber
ORDER BY moneyThroughOrders DESC
LIMIT 3;