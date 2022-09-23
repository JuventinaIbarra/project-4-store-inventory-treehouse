from sqlalchemy import create_engine, Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///inventory.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    product_name = Column('Name', String)
    price_of_product = Column('Price', Integer)
    product_quantity = Column('Quantity', Integer)
    date_updated = Column('Updated', Date)

    def __repr__(self):
        return f'<Name: {self.product_name} Price: {self.price_of_product} Quantity: {self.product_quantity} Updated: {self.date_updated}>'
