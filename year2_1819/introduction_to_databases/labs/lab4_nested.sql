USE classicmodels71;

/* Q1 */

SELECT 
    *,
    buyPrice - (SELECT 
            avg(buyPrice) AS avgPrice
        FROM
            products) AS avgDifference
FROM
    products
WHERE
    buyPrice > (SELECT 
            avg(buyPrice) AS avgPrice
        FROM
            products)
ORDER BY avgDifference DESC;



/* Q2 */
SELECT 
    *, (MSRP - buyPrice) AS profit
FROM
    products
WHERE
    MSRP - buyPrice > (SELECT 
            AVG(MSRP - buyPrice) AS avgProfit
        FROM
            products)
ORDER BY profit * quantityInStock;


/* Q3 */

/* Assuming that 'credit limit greater than any customer living in Austria' means that the credit limit 
must be greater when you compare it to all of the Australian's credit limits (not just one) */

SELECT 
    customerNumber,
    customerName,
    contactLastName,
    contactFirstName,
    phone,
    addressLine1,
    addressLine2,
    city,
    state,
    postalCode,
    country AS customerCountry,
    salesRepEmployeeNumber,
    creditLimit
FROM
    customers
WHERE
    creditLimit > ALL (SELECT 
            creditLimit
        FROM
            customers
        WHERE
            country = 'Austria')
        AND (SELECT 
            COUNT(DISTINCT salesRepEmployeeNumber)
        FROM
            customers
        GROUP BY country
        HAVING country = customerCountry) > 1
ORDER BY creditLimit;



/* Q4 */

SELECT 
    customerNumber, country, SUM(creditLimit) AS creditTotal
FROM
    customers
GROUP BY country
HAVING creditTotal > SOME (SELECT 
        creditLimit
    FROM
        customers
    WHERE
        country = 'Austria');

/* with min and max */
SELECT 
    c.*
FROM
    customers c
WHERE
    (SELECT 
            MIN(creditLimit) AS lowestCredit
        FROM
            customers
        WHERE
            country = c.country) > (SELECT 
            MAX(creditLimit) AS highestCredit
        FROM
            customers
        WHERE
            country = 'Austria')
ORDER BY customerNumber;
