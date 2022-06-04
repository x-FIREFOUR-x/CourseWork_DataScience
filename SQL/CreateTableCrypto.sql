USE Cryptocurrency


	--EXTRACT

EXEC Procedure_ReadData  'coinAave' , 'coin_Aave.csv'
EXEC Procedure_ReadData  'coinBinanceCoin' ,'coin_BinanceCoin.csv' 
EXEC Procedure_ReadData  'coinBitcoin' ,'coin_Bitcoin.csv' 
EXEC Procedure_ReadData  'coinCardano' ,'coin_Cardano.csv' 
EXEC Procedure_ReadData  'coinChainLink' ,'coin_ChainLink.csv' 
EXEC Procedure_ReadData  'coinCosmos' ,'coin_Cosmos.csv' 
EXEC Procedure_ReadData  'coinCryptocomCoin' ,'coin_CryptocomCoin.csv' 
EXEC Procedure_ReadData  'coinDogecoin' ,'coin_Dogecoin.csv' 
EXEC Procedure_ReadData  'coinEOS' ,'coin_EOS.csv' 
EXEC Procedure_ReadData  'coinEthereum' ,'coin_Ethereum.csv' 
EXEC Procedure_ReadData  'coinIota' ,'coin_Iota.csv' 
EXEC Procedure_ReadData  'coinLitecoin' ,'coin_Litecoin.csv' 
EXEC Procedure_ReadData  'coinMonero' ,'coin_Monero.csv' 
EXEC Procedure_ReadData  'coinNEM' ,'coin_NEM.csv' 
EXEC Procedure_ReadData  'coinPolkadot' ,'coin_Polkadot.csv' 
EXEC Procedure_ReadData  'coinSolana' ,'coin_Solana.csv' 
EXEC Procedure_ReadData  'coinStellar' ,'coin_Stellar.csv' 
EXEC Procedure_ReadData  'coinTether' ,'coin_Tether.csv' 
EXEC Procedure_ReadData  'coinTron' ,'coin_Tron.csv' 
EXEC Procedure_ReadData  'coinUniswap' ,'coin_Uniswap.csv' 
EXEC Procedure_ReadData  'coinUSDCoin' ,'coin_USDCoin.csv' 
EXEC Procedure_ReadData  'coinWrappedBitcoin' ,'coin_WrappedBitcoin.csv' 
EXEC Procedure_ReadData  'coinXRP' ,'coin_XRP.csv' 



	--TRANSFORM

EXEC Procedure_TransformData  'coinAave' 
EXEC Procedure_TransformData  'coinBinanceCoin'  
EXEC Procedure_TransformData  'coinBitcoin'  
EXEC Procedure_TransformData  'coinCardano' 
EXEC Procedure_TransformData  'coinChainLink'  
EXEC Procedure_TransformData  'coinCosmos'  
EXEC Procedure_TransformData  'coinCryptocomCoin'  
EXEC Procedure_TransformData  'coinDogecoin'  
EXEC Procedure_TransformData  'coinEOS'  
EXEC Procedure_TransformData  'coinEthereum' 
EXEC Procedure_TransformData  'coinIota' 
EXEC Procedure_TransformData  'coinLitecoin'  
EXEC Procedure_TransformData  'coinMonero'  
EXEC Procedure_TransformData  'coinNEM'  
EXEC Procedure_TransformData  'coinPolkadot'  
EXEC Procedure_TransformData  'coinSolana'  
EXEC Procedure_TransformData  'coinStellar' 
EXEC Procedure_TransformData  'coinTether'  
EXEC Procedure_TransformData  'coinTron' 
EXEC Procedure_TransformData  'coinUniswap' 
EXEC Procedure_TransformData  'coinUSDCoin' 
EXEC Procedure_TransformData  'coinWrappedBitcoin' 
EXEC Procedure_TransformData  'coinXRP' 



	--LOAD

Create Table Cryptocurrency
(
	[Id] [int] IDENTITY(1,1) PRIMARY KEY,
    [Name] nvarchar(20) NOT NULL,
    [Symbol] nvarchar(10) NOT NULL,
    [Date] date NOT NULL,
    [High] float NOT NULL,
    [Low] float NOT NULL,
    [Open] float NOT NULL,
    [Close] float NOT NULL,
    [Volume] float NOT NULL,
    [Marketcap] float NOT NULL
)


INSERT INTO Cryptocurrency SELECT * FROM coinAave
INSERT INTO Cryptocurrency SELECT * FROM coinBinanceCoin
INSERT INTO Cryptocurrency SELECT * FROM coinBitcoin
INSERT INTO Cryptocurrency SELECT * FROM coinCardano
INSERT INTO Cryptocurrency SELECT * FROM coinChainLink
INSERT INTO Cryptocurrency SELECT * FROM coinCosmos
INSERT INTO Cryptocurrency SELECT * FROM coinCryptocomCoin
INSERT INTO Cryptocurrency SELECT * FROM coinDogecoin
INSERT INTO Cryptocurrency SELECT * FROM coinEOS
INSERT INTO Cryptocurrency SELECT * FROM coinEthereum
INSERT INTO Cryptocurrency SELECT * FROM coinIota
INSERT INTO Cryptocurrency SELECT * FROM coinLitecoin
INSERT INTO Cryptocurrency SELECT * FROM coinMonero
INSERT INTO Cryptocurrency SELECT * FROM coinNEM
INSERT INTO Cryptocurrency SELECT * FROM coinPolkadot
INSERT INTO Cryptocurrency SELECT * FROM coinSolana
INSERT INTO Cryptocurrency SELECT * FROM coinStellar
INSERT INTO Cryptocurrency SELECT * FROM coinTether
INSERT INTO Cryptocurrency SELECT * FROM coinTron
INSERT INTO Cryptocurrency SELECT * FROM coinUniswap
INSERT INTO Cryptocurrency SELECT * FROM coinUSDCoin
INSERT INTO Cryptocurrency SELECT * FROM coinWrappedBitcoin
INSERT INTO Cryptocurrency SELECT * FROM coinXRP


/*
SELECT * FROM coinAave
SELECT * FROM coinBinanceCoin
SELECT * FROM coinBitcoin
SELECT * FROM coinCardano
SELECT * FROM coinChainLink
SELECT * FROM coinCosmos
SELECT * FROM coinCryptocomCoin
SELECT * FROM coinDogecoin
SELECT * FROM coinEOS
SELECT * FROM coinEthereum
SELECT * FROM coinIota
SELECT * FROM coinLitecoin
SELECT * FROM coinMonero
SELECT * FROM coinNEM
SELECT * FROM coinPolkadot
SELECT * FROM coinSolana
SELECT * FROM coinStellar
SELECT * FROM coinTether
SELECT * FROM coinTron
SELECT * FROM coinUniswap
SELECT * FROM coinUSDCoin
SELECT * FROM coinWrappedBitcoin
SELECT * FROM coinXRP
*/


DROP TABLE coinAave
DROP TABLE coinBinanceCoin
DROP TABLE coinBitcoin
DROP TABLE coinCardano
DROP TABLE coinChainLink
DROP TABLE coinCosmos
DROP TABLE coinCryptocomCoin
DROP TABLE coinDogecoin
DROP TABLE coinEOS
DROP TABLE coinEthereum
DROP TABLE coinIota
DROP TABLE coinLitecoin
DROP TABLE coinMonero
DROP TABLE coinNEM
DROP TABLE coinPolkadot
DROP TABLE coinSolana
DROP TABLE coinStellar
DROP TABLE coinTether
DROP TABLE coinTron
DROP TABLE coinUniswap
DROP TABLE coinUSDCoin
DROP TABLE coinWrappedBitcoin
DROP TABLE coinXRP


SELECT * FROM Cryptocurrency
ORDER BY Name

SELECT [Name] FROM Cryptocurrency
GROUP BY [Name] 
ORDER BY Name

--DROP TABLE Cryptocurrency