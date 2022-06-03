USE Cryptocurrency

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



Create Table Crypto
(
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


INSERT INTO Crypto SELECT * FROM coinAave
INSERT INTO Crypto SELECT * FROM coinBinanceCoin
INSERT INTO Crypto SELECT * FROM coinBitcoin
INSERT INTO Crypto SELECT * FROM coinCardano
INSERT INTO Crypto SELECT * FROM coinChainLink
INSERT INTO Crypto SELECT * FROM coinCosmos
INSERT INTO Crypto SELECT * FROM coinCryptocomCoin
INSERT INTO Crypto SELECT * FROM coinDogecoin
INSERT INTO Crypto SELECT * FROM coinEOS
INSERT INTO Crypto SELECT * FROM coinEthereum
INSERT INTO Crypto SELECT * FROM coinIota
INSERT INTO Crypto SELECT * FROM coinLitecoin
INSERT INTO Crypto SELECT * FROM coinMonero
INSERT INTO Crypto SELECT * FROM coinNEM
INSERT INTO Crypto SELECT * FROM coinPolkadot
INSERT INTO Crypto SELECT * FROM coinSolana
INSERT INTO Crypto SELECT * FROM coinStellar
INSERT INTO Crypto SELECT * FROM coinTether
INSERT INTO Crypto SELECT * FROM coinTron
INSERT INTO Crypto SELECT * FROM coinUniswap
INSERT INTO Crypto SELECT * FROM coinUSDCoin
INSERT INTO Crypto SELECT * FROM coinWrappedBitcoin
INSERT INTO Crypto SELECT * FROM coinXRP


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


SELECT * FROM Crypto
ORDER BY Name

SELECT [Name] FROM Crypto
GROUP BY [Name] 
ORDER BY Name

--DROP TABLE Crypto