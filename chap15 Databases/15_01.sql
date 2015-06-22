/*

Write a SQL query to get a list of tenants who are renting more than one apartment.

*/

SELECT TenantID, TenantName
FROM (
     SELECT TenantID, TenantName, AptID, count(TenantID) as Aptcnt
     FROM AptTenants NATURAL JOIN Tenants
     GROUP BY TenantID
     )
WHERE Aptcnt > 1;


-- Referenced answer

SELECT TenantName
FROM Tenants
INNER JOIN
      (
      SELECT TenantID
      FROM AptTenants
      GROUP BY TenantID
      HAVING cout(*) > 1
      ) C
ON Tenants.TenantID = C.TenantID
