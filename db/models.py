from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
db = SQLAlchemy()

sqlalchemy_url = "postgresql://smartodds:Test123@localhost:5432/smartodds"

# TODO: This needs to be moved to better home and import the session here
def get_session():
    engine = create_engine(sqlalchemy_url, echo=True)
    Session = sessionmaker(engine)
    sess = Session()
    return sess

class Tennis(Model,Base):
    """
    Table type: Transactional
    Tennis data
    """
    __tablename__ = "tennis_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    atp = Column(Integer, nullable=True)
    location = Column(String, nullable=True)
    tournament = Column(String, nullable=True)


