from datetime import datetime
from sqlalchemy import Column, BigInteger, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db_config import Base


class AirlineCompany(Base):
    __tablename__ = 'airine_companies'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)
    user_id = Column(BigInteger, unique=True, nullable=False)

    def __str__(self):
        return f'<AirlineCompany> id:{self.id} name:{self.name} country_id:{self.country_id}' \
               f'user_id:{self.user_id}'

    def __repr__(self):
        return f'<AirlineCompany> id:{self.id} name:{self.name} country_id:{self.country_id}' \
               f'user_id:{self.user_id}'
