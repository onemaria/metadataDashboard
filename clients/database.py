from requests import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import CrossRefJournal, Base


DATABASE_URL = "postgresql://postgres:password@localhost:5432/mydatabase"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def insert_journal(db: Session, journal_data: dict):
    init_db()
    dois_by_issued_year = journal_data["breakdowns"].get("dois-by-issued-year", [])

    count_current_dois = 0
    count_backfile_dois = 0

    if len(dois_by_issued_year) > 0:
        count_current_dois = dois_by_issued_year[0][1]
    if len(dois_by_issued_year) > 1:
        count_backfile_dois = dois_by_issued_year[1][1]

    journal = CrossRefJournal(
        title=journal_data["title"],
        publisher=journal_data["publisher"],
        total_dois=journal_data["counts"]["total-dois"],
        current_dois=journal_data["counts"]["current-dois"],
        backfile_dois=journal_data["counts"]["backfile-dois"],
        issn=journal_data["ISSN"],
        issn_type=[issn["value"] for issn in journal_data["issn-type"]],
        last_status_check_time=journal_data["last-status-check-time"],
        count_current_dois=count_current_dois,
        count_backfile_dois=count_backfile_dois,
    )

    db.add(journal)
    db.commit()
    db.refresh(journal)
    return journal


def init_db():
    Base.metadata.create_all(bind=engine)
