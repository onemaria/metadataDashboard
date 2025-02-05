from pydantic import BaseModel
from typing import List

class CrossRefJournalBase(BaseModel):
    title: str
    publisher: str
    total_dois: int
    current_dois: int
    backfile_dois: int
    issn: List[str]
    issn_type: List[str]
    last_status_check_time: int
    count_current_dois: int
    count_backfile_dois: int

class CrossRefJournalResponse(CrossRefJournalBase):
    id: int
    class Config:
        orm_mode = True





