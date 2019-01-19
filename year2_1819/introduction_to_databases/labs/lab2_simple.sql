USE worldl71;

/* Q1 */
SELECT * FROM CountryLanguage;

/* Q2 */
SELECT Name, Continent, Region, Population, LocalName FROM Country;

USE sakila;

/* Q3 */
SELECT title, description, release_year, rental_rate FROM film WHERE release_year=2006;

/* Q4 */
SELECT customer_id, inventory_id FROM rental WHERE staff_id=1;


USE classicmodels71;

/* Q5 */
SELECT 
    productName,
    productLine,
    productScale,
    productVendor,
    productDescription,
    quantityInStock,
    buyPrice,
    MSRP
FROM
    products
WHERE
    5000 < quantityInStock
        AND MSRP > buyPrice * 2
ORDER BY productName ASC;

/* Q6 */
SELECT 
    customerNumber,
    checkNumber,
    paymentDate,
    SUM(amount) AS total
FROM
    payments
GROUP BY customerNumber
HAVING 30000 < total
ORDER BY total DESC;