SELECT COUNT(Name) AS NUMBER_OF_ENGLISH_SPEAKING
FROM Country INNER JOIN CountryLanguage ON Country.Code = CountryLanguage.CountryCode
WHERE Language = "English"