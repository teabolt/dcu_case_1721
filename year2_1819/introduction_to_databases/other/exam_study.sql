/* USE world71; */

/* SELECT Name FROM City WHERE Population > 1000000 OR Population < 100000 ORDER BY Name;


(SELECT Name FROM City WHERE Population > 1000000)
union
(SELECT Name FROM City WHERE Population < 100000);

*/

/* Cartesian Product */
/* SELECT * FROM City JOIN Country; */

/* Theta Join */
/* SELECT * FROM City JOIN Country ON Country.Population < City.Population; */

/* Equijoin */
/*
SELECT * FROM City JOIN Country ON Country.Code = City.CountryCode
*/

/* Natural join ? */

/* Full Outer Join ? */

/* Left outer */
/* SELECT * FROM City JOIN Country ON City.Population = Country.Population; */
/* UPDATE Country SET Code = NULL
WHERE Code = "ABW"; */

/* Updates */


/* INSERT INTO City (CountryCode) VALUES ('ZZA'); */
/* UPDATE City SET Name = 'ZZALand', Population = 10 WHERE ID = 4094; */

/*
DELETE FROM City WHERE ID='4095';
*/

/*
SELECT * FROM City
WHERE CountryCode = 'ZZA';
*/


/* Set operations */

/*
SELECT * FROM Country;
SELECT * FROM City;
*/

/* Union */

/* Difference / Intersection */

/*
SELECT DISTINCT Name FROM Country co
WHERE 
NOT EXISTS (SELECT Name FROM City ci WHERE co.Name = ci.Name);
*/

/* Joins */

/*
SELECT co.*, ci.* FROM Country co JOIN (SELECT Name, CountryCode AS Code, District, Population FROM City) ci;
*/

/* Subqueries */

/*
SELECT Name, (Population-(SELECT AVG(Population) FROM Country)) AS PopulationDiff FROM Country co
WHERE Name IN (SELECT Name FROM City ci);
*/

/* Group By */

/*
SELECT Continent, SUM(Population) AS TotalPopulation FROM Country 
GROUP BY Continent HAVING TotalPopulation > 1000000000;
*/

/* Aggregate functions */

/*
SELECT COUNT(IndepYear) AS Independences FROM Country;

SELECT COUNT(DISTINCT IndepYear) AS AcrossTimesIndeps FROM Country;


SELECT COUNT(Code) AS CountryNo FROM Country;

SELECT COUNT(*) AS RowNo FROM Country;

SELECT MAX(Name) AS Highest FROM Country;
*/

/* WHERE */

/*
SELECT * FROM Country WHERE Population != 1000;
*/

/*
SELECT * FROM Country WHERE Population NOT BETWEEN 1000000 AND 10000000;
*/

/*
SELECT * FROM Country WHERE Name IN ('Aruba', 'United States');
*/

/*
SELECT * FROM Country WHERE Name LIKE '%a_a%';
*/

/*
SELECT * FROM Country WHERE IndepYear IS NOT NULL;
*/

/*
SELECT DISTINCT * FROM Country;
*/



/* Papers */



USE world71;

/* a */
SELECT Continent, AVG(LifeExpectancy) AS avgLife FROM Country GROUP BY Continent
HAVING Continent <> 'Antarctica' ORDER BY avgLife DESC;

/* b */
SELECT Name, LifeExpectancy, Continent FROM Country
WHERE LifeExpectancy <= 60
ORDER BY Name ASC, LifeExpectancy DESC;

/* c */
/*
SELECT Name, HeadOfState, 
AVG((SELECT Population FROM City WHERE CountryCode = co.Code AND Population > 1000000)) AS avgCityPopulation 
FROM Country co WHERE Continent = 'Europe'
ORDER BY Name;
*/

SELECT co.Name, co.HeadOfState, AVG(ci.Population) AS avgBigCityPopulation
FROM Country co JOIN City ci ON co.Code = ci.CountryCode AND ci.Population > 1000000
GROUP BY co.Name
ORDER BY Name;

/* without small cities excluded */
SELECT co.Name, co.HeadOfState, AVG(ci.Population) AS avgCityPopulation
FROM Country co JOIN City ci ON co.Code = ci.CountryCode
GROUP BY co.Name
ORDER BY Name;


/* d */

SELECT co.Name, ci.District, (SELECT AVG(Population) FROM City WHERE District = ci.District)
AS avgDistrictPopulation
FROM Country co JOIN City ci ON co.Code = ci.CountryCode
WHERE co.LifeExpectancy < 60
GROUP BY ci.District
ORDER BY co.Name;


/* 2018 January */

/* b */

USE classicmodels71;


SELECT orderNumber, SUM(quantityOrdered) AS totalQuantityOrdered FROM orderdetails
GROUP BY orderNumber HAVING totalQuantityOrdered < (SELECT AVG(quantityOrdered) AS averageTotalQuantity FROM orderdetails);

/* e */

SELECT * FROM orders WHERE orderDate BETWEEN '2003-01-01' AND '2003-01-31';

/* 2017 */

/* c */

SELECT orderNumber FROM orderdetails
GROUP BY orderNumber HAVING SUM(quantityOrdered) < 100;