import json
from sqlalchemy import create_engine, Column, Integer, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy.sql.sqltypes import DATETIME
from app.consts import *

Base = declarative_base()

DATABASE_URL_ENGINE = ""

if DEBUG == True:
    DATABASE_URL_ENGINE = DATABASE_LOCAL
else:
    DATABASE_URL_ENGINE = DATABASE_URL


class Order(Base):
    __tablename__ = "order"
    id = Column('id', Integer, primary_key=True, autoincrement=True) 
    cod_transaction = Column('cod_transaction', String, unique=True)
    date = Column('date', String)
    total_order = Column('total_order', DECIMAL)
    total_cashback = Column('total_cashback', DECIMAL)
    customer = Column('customer', String)
    
    def return_dict(self):
        return json.dumps( {
            "id":self.id,
            "cod_transaction":self.cod_transaction ,
            "date":str(self.date),
            "total_order":float(self.total_order),
            "total_cashback":float(self.total_cashback),
            "customer":self.customer 
        })
        
    
engine = create_engine(DATABASE_URL_ENGINE)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


