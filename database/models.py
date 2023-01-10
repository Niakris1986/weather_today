import sqlalchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, select, Table, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

engine=sqlalchemy.create_engine('sqlite:///db.sqlite')

Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    connection_date = Column(DateTime, default=datetime.now, nullable=False)
    tg_id = Column(BigInteger, nullable=False)
    city = Column(String)
    reports = relationship('WeatherReport', backref='report', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return self.tg_id


class WeatherReport(Base):
    __tablename__ = 'WeatherReports'
    id = Column(Integer, primary_key=True)
    owner = Column(Integer, ForeignKey('Users.id'), nullable=False)
    date = Column(DateTime, default=datetime.now, nullable=False)
    temp = Column(Integer, nullable=False)
    feels_like = Column(Integer, nullable=False)
    wind_speed = Column(Integer, nullable=False)
    pressure_mm = Column(Integer, nullable=False)
    city = Column(String, nullable=False)

    def __repr__(self):
        return self.city