import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key = True)
    username = Column(String(250), nullable = False)
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250), nullable = False, unique = True)

class Follower(Base):
    __tablename__ = 'follower'
    ID = Column(Integer, primary_key = True)
    user_from_id = Column(Integer, ForeignKey('user.ID'))
    user_to_id = Column(Integer, ForeignKey('user.ID'))
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    ID = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.ID'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    ID = Column(Integer, primary_key = True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.ID'))
    post_id = Column(Integer, ForeignKey('post.ID'))
    user = relationship(User)
    post = relationship(Post)

class Media(Base):
    __tablename__ = 'media'
    ID = Column(Integer, primary_key = True)
    media_type = Column(Integer)
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.ID'))
    post = relationship(Post)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e