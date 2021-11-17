from sqlalchemy import create_engine, Column, Integer, ForeignKey, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker
import json

from sqlalchemy.sql.sqltypes import DATETIME

Base = declarative_base()

class Order(Base):
    __tablename__ = "order"
    id = Column('id', Integer, primary_key=True, autoincrement=True) 
    cod_transaction = Column('cod_transaction', String, unique=True)
    date = Column('date', DATETIME)
    total_order = Column('total_order', DECIMAL)
    total_cashback = Column('total_cashback', DECIMAL)
    customer = Column('customer', String)
    
    def return_dict(self):
        value = {
            "id":self.id,
            "cod_transaction":self.cod_transaction ,
            "date":str(self.date),
            "total_order":float(self.total_order),
            "total_cashback":float(self.total_cashback),
            "customer":self.customer 
        }
        return value
    
engine = create_engine("sqlite:///order.db", echo=True)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
