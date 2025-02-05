from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.orm import declarative_base


class authConfiguration(BaseModel):
        server_url: str
        realm: str
        client_id: str
        client_secret: str
        authorization_url: str
        token_url: str


Base = declarative_base()

class CrossRefJournal(Base):
    __tablename__ = 'crossref_journals'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    publisher = Column(String)
    total_dois = Column(Integer)
    current_dois = Column(Integer)
    backfile_dois = Column(Integer)
    issn = Column(ARRAY(String))
    issn_type = Column(ARRAY(String))
    last_status_check_time = Column(Integer)
    count_current_dois = Column(Integer)
    count_backfile_dois = Column(Integer)