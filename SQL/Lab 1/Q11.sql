SELECT MAX(City.Population), City.Name
FROM Country INNER JOIN City ON Country.Code = City.CountryCode
WHERE Country.Code = "CAN"
GROUP BY City.Name