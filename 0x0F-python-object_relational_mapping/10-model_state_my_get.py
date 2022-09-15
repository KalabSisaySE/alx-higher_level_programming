#!/usr/bin/python3
"""the `10-model_state_my_get` module
prints the `State` object with the `name` passed as
argument from the db `hbtn_0e_6_usa`
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

    first_result = session.query(State).filter_by(name=argv[4]).first()
    if first_result:
        print(first_result.id)
    else:
        print("Not found")

    session.close()
