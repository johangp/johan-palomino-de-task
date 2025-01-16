from dataclasses import dataclass, asdict


@dataclass
class RawResults:
    results_id: str
    status: str
    copyright: str
    num_results: int
    bestsellers_date: str
    published_date: str
    published_date_description: str
    previous_published_date: str
    next_published_date: str
    created_at: float


    def dict(self):
        return asdict(self)
