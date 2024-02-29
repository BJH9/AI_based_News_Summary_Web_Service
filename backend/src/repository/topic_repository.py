from sqlalchemy.orm import Session
from fastapi import Depends
from database.connection import get_db

class Topic_repository:
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session
        