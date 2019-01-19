USE classicmodels71;

/* Q1 */


/* a */
SELECT productCode, productLine, productName, productVendor, MSRP 
FROM products
ORDER BY MSRP desc;

/* b */
SELECT c.contactLastName, c.city, c.phone, COUNT(o.orderNumber) AS ordersPlaced FROM customers c JOIN orders o ON c.customerNumber = o.customerNumber
GROUP BY c.customerNumber
HAVING ordersPlaced >= 5
ORDER BY ordersPlaced DESC

/* c */
SELECT 
    p.productName, p.productVendor, u.unitsOrdered
FROM
    products p
JOIN
(SELECT 
    productCode, SUM(quantityOrdered) AS unitsOrdered
FROM
    orderdetails
GROUP BY productCode) u
ON p.productCode = u.productCode
ORDER BY u.unitsOrdered DESC;

/* d */
SELECT 
    p.productName, p.productVendor, u.unitsOrdered
FROM
    products p
JOIN
(SELECT 
    productCode, SUM(quantityOrdered) AS unitsOrdered
FROM
    orderdetails
GROUP BY productCode) u
ON p.productCode = u.productCode
WHERE unitsOrdered > 1000
ORDER BY u.unitsOrdered DESC;


/* Q2 */

/* a */
INSERT INTO City (Name, CountryCode, District, Population)
VALUES ('Castlegregory', 'IRL', 'Munster', '205');

SELECT * FROM City
WHERE CountryCode='IRL'
AND District='Munster'
AND Population >= 205;

/* b */
SELECT co.Name, ci.Name, co.Population 
FROM Country co
JOIN (SELECT CountryCode, Name FROM City) ci
ON co.Code = ci.CountryCode
WHERE co.Population > 10000000
ORDER BY co.Population DESC, co.Name ASC, ci.Name ASC;

/* c */
SELECT COUNT(Name) AS countriesOver10Mil FROM Country
WHERE Population > 10000000;

/* d */

SELECT co.Code, co.Name, cl.languagesSpoken FROM Country co 
JOIN (SELECT CountryCode , COUNT(Language) AS languagesSpoken FROM CountryLanguage GROUP BY CountryCode) cl
ON co.Code = cl.CountryCode
WHERE Code = SOME 
(SELECT CountryCode FROM City
WHERE Population >= 8000000 GROUP BY CountryCode)
ORDER BY languagesSpoken;