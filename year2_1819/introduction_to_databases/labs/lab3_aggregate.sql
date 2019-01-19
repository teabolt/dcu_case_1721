/* Q1 */
SELECT 
    orderNumber,
    SUM(quantityOrdered) AS totalAmount,
    COUNT(DISTINCT productCode) AS typesNumber
FROM
    orderdetails
GROUP BY orderNumber; 


/* Q2 */
SELECT 
    customerNumber, COUNT(orderNumber) AS ordersShipped
FROM
    orders
WHERE
    status = 'Shipped'
GROUP BY customerNumber
ORDER BY orderDate DESC;


/* Q3 */
SELECT 
    COUNT(orderNumber) AS shippedOrders
FROM
    orders
WHERE
    customerNumber = 350
        AND status = 'Shipped';

/* Q4 */

SELECT 
    customerNumber, COUNT(orderNumber) AS shippedOrders
FROM
    orders
WHERE
    status = 'Shipped'
GROUP BY customerNumber
HAVING shippedOrders > (SELECT 
        COUNT(orderNumber) AS shippedOrders
    FROM
        orders
    WHERE
        customerNumber = 350
            AND status = 'Shipped')
ORDER BY shippedOrders DESC;