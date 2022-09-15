#!/usr/bin/python3
"""the `13-model_state_delete_a` module
deletes all `State` objects with a name containing
the letter `a` from the database `hbtn_0e_6_usa`
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.like("%a%")).all()
    for state in states_with_a:
        session.delete(state)
    session.commit()
    session.close()
