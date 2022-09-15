#!/usr/bin/python3
"""the `8-model_state_fetch_first` module
prints the first State object from the database `hbtn_0e_6_usa`
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_result = session.query(State).first()
    if first_result:
        print("{}: {}".format(first_result.id, first_result.name))
    else:
        print("Nothing")

    session.close()
