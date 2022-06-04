USE Cryptocurrency

DROP PROCEDURE Procedure_ReadData

CREATE PROCEDURE Procedure_ReadData
	@TableName NVARCHAR(128),
	@FileName NVARCHAR(250)
AS 
BEGIN 
	SET NOCOUNT ON;
	DECLARE @SqlCreate NVARCHAR(MAX);
	DECLARE @SqlInsert NVARCHAR(MAX);

	DECLARE @Path varchar(100);
	SET @Path = 'D:\project c++\4Semestr\CourseWork\data\CryptocurrencyHistoricalPrices\' ;

	SET @SqlCreate = 
		N'Create Table' + QUOTENAME(@TableName) + 
		N'(
			[SNo] int,
			[Name] nvarchar(20),
			[Symbol] nvarchar(10),
			[Date] nvarchar(30),
			[High] float,
			[Low] float,
			[Open] float,
			[Close] float,
			[Volume] float,
			[Marketcap] float
		)'


	SET @SqlInsert = 
		N'BULK INSERT' + QUOTENAME(@TableName) +
		N'FROM' + QUOTENAME(@Path + @FileName) +
		N'WITH
		(
				FORMAT = ''CSV'',
				FIELDTERMINATOR = '','',
				ROWTERMINATOR = ''0x0a'',
				FIRSTROW = 2
		)'
	


		EXECUTE sp_executesql @SqlCreate
		EXECUTE sp_executesql @SqlInsert

END


