SELECT COUNT(DISTINCT Country.Name) AS Number_Of_English_French_Countries
FROM Country INNER JOIN CountryLanguage ON Country.Code = CountryLanguage.CountryCode
WHERE CountryLanguage.Language = "English" OR CountryLanguage.Language = "French" AND CountryLanguage.IsOfficial = TRUE