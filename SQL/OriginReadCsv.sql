USE Cryptocurrency

--DROP TABLE coinAave

Create Table coinAave
(
    [SNo] int,
    [Name] nvarchar(20),
    [Symbol] nvarchar(10),
    [Date] nvarchar(30),
    [High] float,
    [Low] float,
    [Open] float,
    [Close] float,
    [Volume] float,
    [Marketcap] float,
)


BULK INSERT dbo.coinAave
FROM 'D:\project c++\4Semestr\CourseWork\data\CryptocurrencyHistoricalPrices\coin_Aave.csv'
WITH
(
        FORMAT = 'CSV',
		FIELDTERMINATOR = ',',
		ROWTERMINATOR = '0x0a',
		FIRSTROW = 2
)

UPDATE coinAave
SET [Date] =( SELECT TOP(1) * FROM string_split([Date], ' '))

ALTER TABLE coinAave ALTER COLUMN [Date] date NOT NULL

ALTER TABLE coinAave DROP COLUMN [SNo]

SELECT * FROM dbo.coinAave

