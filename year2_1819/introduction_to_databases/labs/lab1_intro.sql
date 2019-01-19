USE sakila;

/* Q1 */
SELECT * FROM sakila.actor WHERE first_name = "michael";

USE world71;

/* Q2 */
SELECT * FROM city where country_id = 15;

/* Q3*/
SELECT city, city_id FROM city where country_id = 15;

USE classicmodels71;
/* Q4 */
SELECT productName, quantityInStock FROM products where productLine="Motorcycles";

/* 'SELECT *' and 'WHERE' workings */ 