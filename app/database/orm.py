from sqlalchemy import create_engine, Column, Integer, ForeignKey, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import session, sessionmaker, relationship

Base = declarative_base()

class Order(Base):
    __tablename__ = "order"
    id = Column('id', Integer, primary_key=True) 
    cod_transaction = Column('cod_transaction', String, unique=True)
    date = Column('date', DateTime)
    total_order = Column('total_order', DECIMAL)
    total_cashback = Column('total_cashback', DECIMAL)
    customer = Column('customer', String)

engine = create_engine("sqlite:///order.db", echo=True)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)



session = Session()

session.commit()
session.close()