/*

Write a SQL query to get a list of all buildings and the number of open requests (Requests in which status equals 'open).

*/

SELECT Buildings.BuildingID, Buildings.BuildingName, count(RequestID) as RequestCnt
-- SELECT *
FROM Buildings LEFT JOIN (
     SELECT *
     FROM Apartments NATURAL JOIN Requests
     WHERE Requests.Status = 'Open'
) AS AptRequests
ON Buildings.BuildingID = AptRequests.BuildingID
GROUP BY Buildings.BuildingID;

-- Referenced Answer

SELECT BuildingName, ISNULL(Count, 0) as 'Count'
FROM Builindings
LEFT JOIN
     (
     SELECT Apartments.BuildingID, count(*) as 'Count'
     FROM Requets INNER JOIN Apartments
     ON Requests.AptID = Apartments.AptID
     WHERE Request.Status = 'Open'
     GROUP BY Apartments.BuildingID
     ) ReqCounts
ON ReqCounts.BuildingID = Buildings.BuildingID
