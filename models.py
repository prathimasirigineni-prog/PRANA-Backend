
from sqlalchemy import Column, Integer, String, Date, Text, Boolean
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), nullable=False)
    date_of_birth = Column(Date, nullable=True)
    sex = Column(String(30), nullable=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    pin_code = Column(String(10), nullable=True)
    address = Column(Text, nullable=True)
    blood_group = Column(String(10), nullable=True)
    phone = Column(String(20), nullable=True)


class MedicalProfile(Base):
    __tablename__ = "medical_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    past_medical_history = Column(Text, nullable=True)
    existing_conditions = Column(Text, nullable=True)
    allergies = Column(Text, nullable=True)
    current_medications = Column(Text, nullable=True)
    emergency_contact_name = Column(String(150), nullable=True)
    emergency_contact_phone = Column(String(20), nullable=True)


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    latitude = Column(String(30), nullable=True)
    longitude = Column(String(30), nullable=True)
    sharing_enabled = Column(Boolean, default=False)
