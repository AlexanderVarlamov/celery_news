"""
version 
@author varlamov.a
@email varlamov.a@rt.ru
@date 27.11.2023
@time 10:50
"""
from sqlalchemy import Column, BigInteger, TIMESTAMP, JSON, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class NewsLinks(Base):
    __tablename__ = "newslinks"

    id = Column(BigInteger, primary_key=True)
    dt = Column(TIMESTAMP, nullable=False)
    links = Column(JSON, nullable=False)


class RssSources(Base):
    __tablename__ = "rss_sources"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rss = Column(String, nullable=False)
    description = Column(String, nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)

    # def get_news(self):
    #     get_news(self.name, self.rss)

