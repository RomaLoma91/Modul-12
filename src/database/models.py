from db import Base
from enum import Enum

from sqlalchemy import Column, Integer, String, func, DateTime, Date
from sqlalchemy.sql.schema import ForeignKey

from sqlalchemy.orm import relationship

class ContactType(Enum):
    EMAIL = "email"
    PHONE = "phone"

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(55), nullable=False)
    last_name = Column(String(55), nullable=False)
    birthday = Column("birthday", Date)
    email = Column(String(50), nullable=False, unique=True)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    phones = relationship("Phone", backref="contacts")

def __init__(self, first_name, last_name, birthday, contact_type, contact_value):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.contact_type = contact_type
        self.contact_value = contact_value
