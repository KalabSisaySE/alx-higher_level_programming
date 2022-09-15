#!/usr/bin/python3
"""the `12-model_state_update_id_2` module
changes the name of a `State` object from
the database `hbtn_0e_6_usa`
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

    id_2 = session.query(State).filter_by(id=2).first()
    id_2.name = "New Mexico"
    session.commit()
    session.close()
