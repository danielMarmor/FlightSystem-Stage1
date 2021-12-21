from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from db_config import Base


class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    flight_id = Column(BigInteger, ForeignKey('flights.id'), nullable=False)
    customer_id = Column(BigInteger, ForeignKey('customers.id'), nullable=False)

    __table_args__ = (UniqueConstraint('flight_id', 'customer_id', name='un_flight_customer'), )

    def __str__(self):
        return f'<Ticket> id:{self.id}, flight_id:{self.flight_id}, customer_id:{self.customer_id}'

    def __repr__(self):
        return f'<Ticket> id:{self.id}, flight_id:{self.flight_id}, customer_id:{self.customer_id}'
