from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from db_config import Base


class Administrator(Base):
    __tablename__ = 'administrators'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    user_id = Column(BigInteger, ForeignKey('users.id'), unique=True, nullable=False)

    def __str__(self):
        return f'<Administrator> id:{self.id}, first_name:{self.first_name}, last_name:{self.last_name}' \
               f' user_id:{self.user_id}'

    def __repr__(self):
        return f'<Administrator> id:{self.id}, first_name:{self.first_name}, last_name:{self.last_name}' \
               f' user_id:{self.user_id}'

