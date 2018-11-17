from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import *

def addbasics():
    name = Main_Category(name="Landmarks")
    session.add(name)
    session.commit()

    name = Main_Category(name="Restaurants")
    session.add(name)
    session.commit()

    name = Main_Category(name="Cafes")
    session.add(name)
    session.commit()

    name = Main_Category(name="Coworking space")
    session.add(name)
    session.commit()

    name = Main_Category(name="Cinemas")
    session.add(name)
    session.commit()

    name = Main_Category(name="Parks")
    session.add(name)
    session.commit()

    name = Main_Category(name="Stores")
    session.add(name)
    session.commit()

    name = Main_Category(name="Markets")
    session.add(name)
    session.commit()

    name = Main_Category(name="Clubs")
    session.add(name)
    session.commit()

    name = Main_Category(name="Others")
    session.add(name)
    session.commit()

    print ("added!")
