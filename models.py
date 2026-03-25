from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID, LargeBinary, text, Interval
from sqlalchemy.types import Enum
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=True)
    password = Column(String, nullable=True)
    created_at_dt = Column(DateTime, nullable=True, server_default=text("now()"))


class Satellites(Base):
    __tablename__ = "satellites"

    id = Column(Integer, primary_key=True, autoincrement=True)
    norad_id = Column(Integer, nullable=True)
    name = Column(String, nullable=True)
    tle_line1 = Column(String, nullable=True)
    tle_line2 = Column(String, nullable=True)
    created_at_dt = Column(DateTime, nullable=True, server_default=text("now()"))


class GroundStations(Base):
    __tablename__ = "ground_stations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=True)
    name = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    created_at_dt = Column(DateTime, nullable=True, server_default=text("now()"))


class ConjunctionAlerts(Base):
    __tablename__ = "conjunction_alerts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    satellite_a_id = Column(Integer, nullable=True)
    satellite_b_id = Column(Integer, nullable=True)
    miss_km = Column(Float, nullable=True)
    approach_dt = Column(DateTime, nullable=True, server_default=text("now()"))
    created_at_dt = Column(DateTime, nullable=True, server_default=text("now()"))


class UserWatchlist(Base):
    __tablename__ = "user_watchlist"

    user_id = Column(Integer, primary_key=True)
    satellite_id = Column(Integer, primary_key=True)
    created_at_dt = Column(DateTime, nullable=True, server_default=text("now()"))


