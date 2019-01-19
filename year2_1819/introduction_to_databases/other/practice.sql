/* USE classicmodels71; */

/* SELECT 
	concat(contactFirstName, contactLastName) AS name, 
	concat_ws(" ", addressLine1, addressLine2) AS address 
FROM customers;
*/

/* SELECT * FROM employees
WHERE jobTitle LIKE '%Manager%';
*/

/*
SELECT * FROM orders
WHERE datediff(requiredDate, orderDate) <= 7;
*/

/*
SELECT 
    p.productCode, p.productName, p.quantityInStock, SUM(od.quantityOrdered) AS totalOrders
FROM
    products p
        JOIN
    orderdetails od ON p.productCode = od.productCode
GROUP BY p.productCode
HAVING totalOrders >= p.quantityInStock;
*/

/*
USE world71;
*/

/*
SELECT * FROM Country
WHERE Name <> LocalName;
*/

/*
SELECT * FROM City;
SELECT * FROM CountryLanguage;
*/

/* Countries */

USE world71;

SELECT * FROM Country
WHERE Name LIKE 'Philippines%';

SELECT * FROM City
WHERE CountryCode='PHL';

SELECT District, COUNT(Name) FROM City
WHERE CountryCode='LBY' GROUP BY District;

SELECT City.Name, City.Population, Country.Population, (City.Population*100)/(Country.Population) AS percentPopulation
FROM City 
JOIN Country 
ON City.CountryCode = Country.Code
WHERE District='Kaunas';

SELECT * FROM CountryLanguage
WHERE CountryCode='PHL';


SELECT * FROM Country
JOIN City ON Country.Code = City.CountryCode
JOIN CountryLanguage ON Country.Code = CountryLanguage.CountryCode
WHERE Country.Name IN ('Bulgaria', 'Lithuania', 'Philippines') OR 
Country.Name LIKE 'Libya%';