from database.models.core.main import db
from database.models.core.service_object import ServiceObject
from sqlalchemy import Column, Enum, Text, ForeignKey, Integer, DateTime, text, Boolean, String, UUID
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

class User(ServiceObject, db.Model):
    __tablename__ = "users"

    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)