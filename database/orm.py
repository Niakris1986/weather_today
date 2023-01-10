from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import database_config
from .models import Base, User, WeatherReport

engine = create_engine(database_config.url, echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def add_user(tg_id):
    session = Session()
    user = session.query(User).filter(User.tg_id == tg_id).first()
    if user is None:
        new_user = User(tg_id=tg_id)
        session.add(new_user)
        session.commit()


def set_user_city(tg_id, city):
    session = Session()
    user = session.query(User).filter(User.tg_id == tg_id).first()
    user.city = city
    session.commit()


def get_user_city(tg_id):
    session = Session()
    user = session.query(User).filter(User.tg_id == tg_id).first()
    return user.city
