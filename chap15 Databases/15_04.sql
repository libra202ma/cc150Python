/*

What are the different types of joins? Please explain how they differ and why certain types are better in certain situations.

*/

JOIN
NATURAL Join
LEFT JOIN
RIGHT JOIN
OUTER JOIN
INNER JOIN


-- referenced answer

/*

JOIN is used to combine the results of two tables. To perform a JOIN, each of the tables must have at least one field that will be used to find matching records from the other table. The join type defines which records will go into the result set.

Let's take for example two tables: one table lists the 'regular' beverages, and another lists the calorie-free beverages. Each table has two fields: the beverage name and its product code. The 'code' field will be used to perform the record matching.

Regular Beverages:

| Name      | Code      |
|-----------+-----------|
| Budweiser | BUDWEISER |
| Coco-Cola | COCACOLA  |
| Pepsi     | PEPSI     |

Calorie-Free Beverages:

| Name           | Code     |
|----------------+----------|
| Diet Coca-Cola | COCACOLA |
| Presca         | FRESCA   |
| Diet Pepsi     | PEPSI    |
| Pepsi Light    | PEPSI    |
| Purified Water | WATER    |

If we wanted to join Beverages with Calorie-Free Beverages, we would have many options. There are discussed below.

- INNER JOIN: The result would contain only the data where the criteria match. In our example, we would get three records, one with a COCOCOLA code and two with PEPSI code.

- OUTER JOIN: An OUTER JOIN will always contain the results of INNER JOIN, but it may also contain some records that have no matching record in the other table. OUTER JOINs are divided into the following subtypes:

  - LEFT OUTER JOIN, or simply LEFT JOIN: The result will contain all records from the left table. If no matching records were found in the right table, then its fields will contain the NULL values. In our example, we would get four records. In addition to INNER JOIN results, BUDWEISER would be listed, because it was in the left table.

  - RIGHT OUTER JOIN, or simply RIGHT JOIN: This type of join is the opposite of LEFT JOIN. It will contain every record from the right table, the missing fields from the left table will be NULL. Note that if we have two tables, A and B, then we say that the statement A LEFT JOIN B is equivalent to the statement B RIGHT JOIN A. In our example, we will get five records. In addition to INNER JOIN results, FRESCA and WATER records will be listed.

  - FULL OUTER JOIN: This type of join combines the results of the LEFT AND RIGHT JOINS. All records from both tables will be included in the result set, regardless of whether or not a matching record exists in the other table. If no matching record was found, then the corresponding result fields will have a NULL value. In our example, we will get six records.


*/
