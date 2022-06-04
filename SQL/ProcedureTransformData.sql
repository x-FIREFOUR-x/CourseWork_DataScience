USE Cryptocurrency

DROP PROCEDURE Procedure_TransformData

CREATE PROCEDURE Procedure_TransformData
	@TableName NVARCHAR(128)
AS 
BEGIN 
	SET NOCOUNT ON;
	DECLARE @Sql1 NVARCHAR(MAX);
	DECLARE @Sql2 NVARCHAR(MAX);
	DECLARE @Sql3 NVARCHAR(MAX);


	SET @Sql1 = 
		N'UPDATE' + QUOTENAME(@TableName) +
		N'SET [Date] = (SELECT TOP(1) * FROM string_split([Date], '' '') )'

	SET @Sql2 =
		N'ALTER TABLE' + QUOTENAME(@TableName) + N'ALTER COLUMN [Date] date NOT NULL'

	SET @Sql3 =
		N'ALTER TABLE' + QUOTENAME(@TableName) + N'DROP COLUMN [SNo]'


		EXECUTE sp_executesql @Sql1
		EXECUTE sp_executesql @Sql2
		EXECUTE sp_executesql @Sql3

END


