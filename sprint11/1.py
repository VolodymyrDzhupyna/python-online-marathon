from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///sprint11/q1.db")
Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    grade = Column(Integer)
    salesperson_id = Column(Integer)

    def __init__(self, name, city, grade, salesperson_id):
        self.name = name
        self.city = city
        self.grade = grade
        self.salesperson_id = salesperson_id
    
    def __repr__(self):
        return f"{self.id} {self.name} {self.city} {self.grade} {self.salesperson_id}"

Session = sessionmaker(bind=engine)
session = Session()

query = session.query(Customer).filter(Customer.grade > 200).order_by(Customer.id)
clients = query.all()

number_records = query.count()


def get_info():
    print("Connected to SQLite")
    print("Total rows are:  ", number_records)
    print("Printing each row")
    for client in clients:
        print(f"Id: ", client.id)
        print("Name: ", client.name)
        print("City: ", client.city)
        print("Grade: ", client.grade)
        print("Seller: ", client.salesperson_id, end="\n\n\n")
    print("The SQLite connection is closed")


if __name__ == "__main__":
    get_info()
