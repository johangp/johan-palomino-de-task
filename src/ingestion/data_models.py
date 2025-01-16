from dataclasses import asdict, dataclass


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


@dataclass
class RawList:
    list_id: int
    results_id: str
    list_name: str
    display_name: str
    updated: str
    list_image: str
    created_at: float

    def dict(self):
        return asdict(self)