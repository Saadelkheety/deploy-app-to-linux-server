from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_imageattach.entity import Image, image_attachment
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine("postgresql://catalog:catalog@localhost/catalog")
Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(25000), nullable=False)
    email = Column(String(25000), nullable=False)
    picture = Column(String(25000))


class Main_Category(Base):
    __tablename__ = 'maincategory'
    id = Column(Integer, primary_key=True)
    name = Column(String(2000), nullable=False)

    @property
    def serialize(self):
        # Return object data in easily serializeable format
        return {
            'name': self.name,
            'id': self.id,
        }


class Sub_Category(Base):
    __tablename__ = 'subcategory'
    id = Column(Integer, primary_key=True)
    name = Column(String(2000), nullable=False)
    description = Column(String(2500), nullable=False)
    main_id = Column(Integer, ForeignKey('maincategory.id'), nullable=False)
    maincategory = relationship(Main_Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    picture = image_attachment('ItemPicture')

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'main_id': self.main_id,
        }


class ItemPicture(Base, Image):
    __tablename__ = 'item_picture'
    item_id = Column(Integer, ForeignKey('subcategory.id'), primary_key=True)
    subcategory = relationship('Sub_Category')
