from datetime import datetime
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from db_config import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    user_role = Column(Integer, ForeignKey('user_roles.id'), nullable=False)

    def __str__(self):
        return f'<User> id:{self.id} username=:{self.username} password:{self.password}' \
               f'email:{self.email} user_role:{self.user_role}, image:{len(self.image)}'

    def __repr__(self):
        return f'<User> id:{self.id} username=:{self.username} password:{self.password}' \
               f'email:{self.email} user_role:{self.user_role}'

