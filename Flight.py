from datetime import datetime
from sqlalchemy import Column, BigInteger, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db_config import Base


class Flight(Base):
    __tablename__ = 'flights'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    airline_company_id = Column(BigInteger, nullable=False)
    origin_country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)
    destination_country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)
    departure_time = Column(DateTime, nullable=False)
    landing_time = Column(DateTime, nullable=False)
    remaining_tickets = Column(Integer, nullable=False)

    def __str__(self):
        return f'<Flight>: id:{self.id} airline_company_id:{self.airline_company_id} origin_country_id:' \
               f'{self.origin_country_id} destination_country_id:{self.destination_country_id} ' \
               f'departure_time:{self.departure_time} landing_time:{self.landing_time} ' \
               f'remaining_tickets:{self.remaining_tickets}'

    def __repr__(self):
        return f'<Flight>: id:{self.id} airline_company_id:{self.airline_company_id} origin_country_id:' \
               f'{self.origin_country_id} destination_country_id:{self.destination_country_id} ' \
               f'departure_time:{self.departure_time} landing_time:{self.landing_time} ' \
               f'remaining_tickets:{self.remaining_tickets}'
