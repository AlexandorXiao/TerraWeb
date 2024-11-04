from sqlalchemy import create_engine, Column, Integer, BigInteger, String, Boolean, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://username:password@localhost/dbname"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    minecraft_nick = Column(String(32), unique=True)
    discord_id = Column(BigInteger, unique=True)
    email = Column(String(255), unique=True)
    premium = Column(Boolean, default=False)


Base.metadata.create_all(engine)
