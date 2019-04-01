from sqlalchemy import Column,Integer,String
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:123456@localhost/flaskdb',
                       encoding="utf8", echo=True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True,autoincrement=True, nullable=False)
    username = Column(String(20), nullable=False)
    password = Column(String(255), nullable=True)


class Novel(Base):
    __tablename__ = 'novel'
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    novel = Column(String(20), nullable=False)
    desc = Column(String(255), nullable=False)
    author = Column(String(50), nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)

