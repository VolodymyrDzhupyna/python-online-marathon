from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///sprint11/q1.db", echo=False)
print("Connected to SQLite")

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    grade = Column(Integer)
    salesperson_id = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def get_info():
    query = session.query(Customer).filter(Customer.grade > 200).order_by(Customer.id)
    clients = query.all()
    number_records = query.count()
    column_names = Customer.__table__.columns.keys()
    print("Total rows are:  ", number_records)
    print("Printing each row")
    for client in clients:
        for item in column_names:
            if item == "salesperson_id":
                print(f"Seller:  {getattr(client, item)}")
            else:
                print(f"{item.capitalize()}:  {getattr(client, item)}")
        print(end="\n\n")
    print("The SQLite connection is closed")

session.close()


if __name__ == "__main__":
    get_info()
