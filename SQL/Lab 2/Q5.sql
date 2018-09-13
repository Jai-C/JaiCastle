SELECT Name
FROM Country INNER JOIN CountryLanguage ON Country.Code = CountryLanguage.CountryCode
WHERE Language = "French" AND IsOfficial = TRUE