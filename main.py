from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uvicorn

SAMPLE_METADATA = [
    {"doi": "10.1234/example1", "title": "Research Paper 1", "citations": 15, "date": "2022-01-15", "authors": ["Author A", "Author B"], "affiliation": "University X"},
    {"doi": "10.1234/example2", "title": "Research Paper 2", "citations": 25, "date": "2021-05-10", "authors": ["Author C"], "affiliation": "University Y"},
    {"doi": "10.1234/example3", "title": "Research Paper 3", "citations": 5, "date": "2023-03-22", "authors": ["Author D", "Author E"], "affiliation": "Institute Z"},
]

app = FastAPI(title="Metadata Dashboard")

class MetadataQuery(BaseModel):
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    min_citations: Optional[int] = 0

@app.get("/citations/trends", summary="Get citation trends")
def get_citation_trends(
    start_date: Optional[datetime] = Query(None, description="Start date for the query in YYYY-MM-DD format"),
    end_date: Optional[datetime] = Query(None, description="End date for the query in YYYY-MM-DD format"),
    min_citations: Optional[int] = Query(0, description="Minimum number of citations")
):
    filtered_metadata = [
        entry for entry in SAMPLE_METADATA
        if (start_date is None or datetime.strptime(entry["date"], "%Y-%m-%d") >= start_date) and
           (end_date is None or datetime.strptime(entry["date"], "%Y-%m-%d") <= end_date) and
           (entry["citations"] >= min_citations)
    ]
    return {"data": filtered_metadata, "count": len(filtered_metadata)}

@app.get("/metadata/gaps", summary="Identify metadata gaps")
def identify_metadata_gaps():
    gaps = [
        {
            "doi": entry["doi"],
            "missing_fields": [
                field for field in ["doi", "title", "citations", "date", "authors", "affiliation"] if not entry.get(field)
            ]
        }
        for entry in SAMPLE_METADATA if any(not entry.get(field) for field in ["doi", "title", "citations", "date", "authors", "affiliation"])
    ]
    return {"data": gaps, "count": len(gaps)}

@app.get("/journals/{journal_id}/stats", summary="Get journal-specific stats")
def get_journal_stats(journal_id: str):
    return {"message": f"Statistics for journal {journal_id} are not implemented yet."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
