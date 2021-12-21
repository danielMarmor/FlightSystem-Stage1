from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db_config import Base


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    address = Column(String(200), nullable=False)
    phone_number = Column(String(20), unique=True, nullable=False)
    credit_card_number = Column(String(24), unique=True, nullable=False)
    user_id = Column(BigInteger, ForeignKey('users.id'), unique=True, nullable=False)

    def __str__(self):
        return f'<Customer> id:{self.id}, first_name:{self.first_name}, last_name:{self.last_name}' \
               f'address:{self.address} phone_number:{self.phone_number} credit_card_number:' \
               f'{self.credit_card_number} user_id:{self.user_id}'

    def __repr__(self):
        return f'<Customer> id:{self.id}, first_name:{self.first_name}, last_name:{self.last_name}' \
               f'address:{self.address} phone_number:{self.phone_number} credit_card_number:' \
               f'{self.credit_card_number} user_id:{self.user_id}'
