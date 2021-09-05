import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, BigInteger, Text, DateTime, Boolean, Float
from sqlalchemy import Sequence
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()


class UserDB(Base):
    __tablename__ = 'Users'
    Uuid = Column(String,
                primary_key=True)
    EncryptedKey = Column(String)
    Username     = Column(String)
    Hash         = Column(String)
    FirstName    = Column(String)
    LastName     = Column(String)
    PhoneNumber  = Column(String)
    Email        = Column(String)
    SwVersion    = Column(String)

    # def update(self, transaction:InvestmentTransactionItem):
    #     self.Ticker = transaction.ticker
    #     self.Name = transaction.name
    #     self.UUID = transaction.uuid
    #     self.Date = transaction.date
    #     self.Account = transaction.account     
    #     self.Transaction = transaction.transaction 
    #     self.Category = transaction.category    
    #     self.ExpenseRatio = transaction.expenseratio
    #     self.Shares = transaction.shares      
    #     self.PricePerShare = transaction.pricepershare        
    #     self.Total = transaction.total       

    def __repr__(self):
        return ""

class PasswordDB(Base):
    __tablename__ = 'Passwords'
    UniqueID = Column(String,
                primary_key=True)
    UserUuid    = Column(String)
    Application = Column(String)
    Username    = Column(String)
    Email       = Column(String)
    Description = Column(String)
    Website     = Column(String)
    Category    = Column(String)
    Passphrase  = Column(String)

    # def update(self, transaction:CryptoTransactionItem):
    #     self.Ticker             = transaction.ticker
    #     self.Name               = transaction.name              
    #     self.UUID               = transaction.uuid              
    #     self.Date               = transaction.date              
    #     self.Account            = transaction.account            
    #     self.Transaction        = transaction.transaction             
    #     self.QuoteCurrency      = transaction.quotecurrency     
    #     self.QuotePrice         = transaction.quoteprice        
    #     self.Shares             = transaction.shares            
    #     self.QuotePricePerShare = transaction.quotepricepershare
    #     self.Fee                = transaction.fee              
    #     self.FeeCurrency        = transaction.feecurrency       
    #     self.TotalPrice         = transaction.totalprice        
    #     self.TotalPriceUsd      = transaction.totalpriceusd     
    